from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt
from state import State
from agents.router import router_node
from agents.content import propose as content_propose
from schemas.profile import load_profile
from tools.validators import run_validations
from tools.workspace import (
    create_workspace, read_file, write_file, make_diff,
    apply_workspace, discard_workspace,
)

CONTENT_FILE = "content/site.json"

def propose_node(state: State) -> dict:
    ws= create_workspace(state["run_id"])          
    current= read_file(ws, CONTENT_FILE)            
    profile= load_profile().model_dump()            
    nuevo= content_propose(state["instruction"], profile, current)
    write_file(ws, CONTENT_FILE, nuevo)
    diff = make_diff(ws, CONTENT_FILE)              
    print(f'[propose] propuesta escrita en: {ws}')
    return {
        "workspace": str(ws), 
        "changed_files": [CONTENT_FILE],
        "diff": diff,   
    }
    
def validate_node(state: State) -> dict:
    '''Corre validaciones deterministas sobre la propuesta en el workspace.'''
    resultado = run_validations(state["workspace"])
    estado = "OK" if resultado["ok"] else "FALLO"
    print(f"[validate] {estado} -> {[c['check'] for c in resultado['checks']]}")
    return {"validation": resultado}
    
def approval_node(state: State) -> dict:
    decision = interrupt({
        "instruccion": state["instruction"],
        "archivos": state["changed_files"],
        "diff": state["diff"],
        "validacion_ok": state.get("validation", {}).get("ok"),
        "validacion": state.get("validation"),
    })
    return {"decision": decision}

def route_decision(state: State) -> str:
    d = str(state.get("decision", "reject")).lower()
    return "apply" if d in ("approve", "aprobar", "si", "yes", "y") else "discard"

def apply_node(state: State) -> dict:
    apply_workspace(state["workspace"], state["changed_files"])
    discard_workspace(state["workspace"])
    print("[apply] cambios aplicados a main")
    return {"status": "aplicado"}

def discard_node(state: State) -> dict:
    discard_workspace(state["workspace"])
    print("[discard] propuesta descartada, main intacto")
    return {"status": "descartado"}



def build_graph():
    builder = StateGraph(State)
    builder.add_node("router", router_node)
    builder.add_node("propose", propose_node)
    builder.add_node("validate", validate_node) 
    builder.add_node("approval", approval_node)
    builder.add_node("apply", apply_node)
    builder.add_node("discard", discard_node)

    builder.add_edge(START, "router")
    builder.add_edge("router", "propose")
    builder.add_edge("propose", "validate")
    builder.add_edge("validate", "approval")
    builder.add_conditional_edges("approval", route_decision, {"apply": "apply", "discard": "discard"})
    builder.add_edge("apply", END)
    builder.add_edge("discard", END)
    return builder



