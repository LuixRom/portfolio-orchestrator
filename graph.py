from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt
from state import State
from agents.router import router_node
from agents.content import propose as content_propose
from schemas.profile import load_profile
from tools.validators import run_validations
from agents.planner import choose_tier
from settings import CONTENT_FILE, MAX_RETRIES
import uuid
from langchain_core.messages import AIMessage
from agents.frontend import propose as frontend_propose
from tools.workspace import (
    create_workspace, read_current, write_file, make_diff,
    apply_workspace, discard_workspace,
)

AGENTES = {
    "content": {"fn": content_propose,  "file": "content/site.json"},
    "ui": {"fn": frontend_propose, "file": "app/page.tsx"},
    "architecture": {"fn": content_propose,  "file": "content/site.json"},  # por ahora
}

CONTENT_FILE = "content/site.json"

def _texto_de_contenido(content) -> str:
    '''Normaliza content de un mensaje (str o lista de content blocks) a str plano.'''
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        partes = []
        for bloque in content:
            if isinstance(bloque, str):
                partes.append(bloque)
            elif isinstance(bloque, dict):
                partes.append(bloque.get("text", ""))
        return "".join(partes)
    return ""

def intake_node(state: State) -> dict:
    '''
        Traduce el ultimo mensaje del chat en nuestra 'instruction'.

        Agent Chat UI (y la pestana Chat de Studio) mandan lo que escribes como
        un mensaje humano; aqui lo leemos y generamos un run_id nuevo por conversacion.
    '''
    msgs = state.get("messages", [])
    if msgs:
        ultimo = msgs[-1]
        contenido = getattr(ultimo, "content", None)
        if contenido is None and isinstance(ultimo, dict):
            contenido = ultimo.get("content", "")
        instruccion = _texto_de_contenido(contenido)
    else:
        instruccion = state.get("instruction", "")
    run_id = state.get("run_id") or uuid.uuid4().hex[:8]
    print(f"[intake] instruccion='{instruccion}' run_id={run_id}")
    return {"instruction": instruccion, "run_id": run_id}

def plan_node(state: State) -> dict:
    '''Elige el tier segun complejidad y reintentos (politica de escalamiento).'''
    tier, motivo = choose_tier(state["task_type"], state["complexity"],
                               state.get("retry_count", 0))
    print(f"[plan] tier={tier} ({motivo})")
    return {"tier": tier}

def propose_node(state: State) -> dict:
    ws = create_workspace(state["run_id"])
    agente = AGENTES.get(state["task_type"], AGENTES["content"])   
    archivo = agente["file"]
    current = read_current(archivo)
    profile = load_profile().model_dump()
    nuevo = agente["fn"](state["instruction"], profile, current, state["tier"])
    write_file(ws, archivo, nuevo)
    diff = make_diff(ws, archivo)
    print(f"[propose] agente={state['task_type']} archivo={archivo} tier={state['tier']} -> {ws}")
    return {"workspace": str(ws), "changed_files": [archivo], "diff": diff}

def after_validate(state: State) -> str:
    '''Decide: si paso -> approval; si fallo y quedan intentos -> retry; si no -> approval.'''
    if state.get("validation", {}).get("ok"):
        return "approval"
    if state.get("retry_count", 0) < MAX_RETRIES:
        return "retry"
    return "approval"

def bump_retry_node(state: State) -> dict:
    '''Incrementa el contador de reintentos (esto dispara la escalada en plan).'''
    n = state.get("retry_count", 0) + 1
    print(f"[retry] reintento #{n}")
    return {"retry_count": n}
    
def validate_node(state: State) -> dict:
    '''Corre validaciones deterministas sobre la propuesta en el workspace.'''
    resultado = run_validations(state["workspace"])
    estado = "OK" if resultado["ok"] else "FALLO"
    print(f"[validate] {estado} -> {[c['check'] for c in resultado['checks']]}")
    return {"validation": resultado}
    
def approval_node(state: State) -> dict:
    '''Pausa con el esquema que Agent Chat UI entiende (botones + diff con formato).'''
    validacion_ok = state.get("validation", {}).get("ok")
    request = {
        "action_request": {
            "action": "Aplicar cambios al portafolio",
            "args": {"archivos": state.get("changed_files", [])},
        },
        "config": {
            "allow_accept": True,     
            "allow_respond": True,    
            "allow_edit": False,
            "allow_ignore": True,     
        },
        "description": (
            f"**Tier usado:** {state.get('tier')}\n\n"
            f"**Validación:** {'ok' if validacion_ok else ' falló'}\n\n"
            f"```diff\n{state.get('diff', '')}\n```"
        ),
    }
    response = interrupt([request])

    decision = response
    if isinstance(decision, list) and decision: 
        decision = decision[0]
    if isinstance(decision, dict):                    # es un HumanResponse -> saca el 'type'
        decision = decision.get("type", "ignore")
    return {"decision": str(decision)}



def route_decision(state: State) -> str:
    d = str(state.get("decision", "")).lower()
    return "apply" if d in ("accept", "approve", "aprobar", "si", "yes", "y") else "discard"

def apply_node(state: State) -> dict:
    apply_workspace(state["workspace"], state["changed_files"])
    discard_workspace(state["workspace"])
    print("[apply] cambios aplicados a main")
    return {"status": "aplicado",
            "messages": [AIMessage(content=" Cambios aplicados a tu portafolio.")]}

def discard_node(state: State) -> dict:
    discard_workspace(state["workspace"])
    print("[discard] propuesta descartada, main intacto")
    return {"status": "descartado",
            "messages": [AIMessage(content=" Propuesta descartada. Tu portafolio no cambió.")]}

def build_graph():
    builder = StateGraph(State)
    builder.add_node("intake", intake_node)
    builder.add_node("router", router_node)
    builder.add_node("plan", plan_node)
    builder.add_node("propose", propose_node)
    builder.add_node("validate", validate_node) 
    builder.add_node("bump_retry", bump_retry_node) 
    builder.add_node("approval", approval_node)
    builder.add_node("apply", apply_node)
    builder.add_node("discard", discard_node)

    builder.add_edge(START, "intake") 
    builder.add_edge("intake", "router")
    builder.add_edge("router", "plan")
    builder.add_edge("plan", "propose")
    builder.add_edge("propose", "validate")
    builder.add_conditional_edges("validate", after_validate, {"approval": "approval", "retry": "bump_retry"})
    builder.add_edge("bump_retry", "plan")
    builder.add_conditional_edges("approval", route_decision, {"apply": "apply", "discard": "discard"})
    builder.add_edge("apply", END)
    builder.add_edge("discard", END)
    return builder

graph = build_graph().compile()

