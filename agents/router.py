import re
import json
from core.llm import get_llm

RULES = [
    (r"\b(arquitectura|reestructur|migra|framework|routing|estructura del sitio)", "architecture", "high"),
    (r"\b(color|estilo|layout|dise|espaciad|tipograf|component)","ui","medium"),
    (r"\b(proyecto|experiencia|certificaci|habilidad|secci)","content","medium"),
    (r"\b(texto|copy|contenido|bio|descripci|redacta|resumen|titular|hero|presentaci)","content","low"),
]

def _rule_based(instruction: str):
    '''Intenta clasificar con reglas. Devuelve None si ninguna coincide'''
    text= instruction.lower()
    for pattern, task_type, complexity in RULES:
        if re.search(pattern, text):
            return {"task_type": task_type, "complexity": complexity, "source": "reglas"}        
    return None

def _llm_based(instruction: str):
    '''Red de seguridad: clasifica con el 20B cuando las reglas no alcanzan.'''
    system = (
        "Clasifica la instruccion para un sistema que edita un portafolio. "
        "Responde SOLO con JSON valido, sin explicaciones ni ```. "
        'Formato: {"task_type": "content|ui|architecture", "complexity": "low|medium|high"}'
    )
    
    resp = get_llm().invoke([
        {"role": "system", "content": system},
        {"role": "user", "content": instruction},
    ])
    try:
        data = json.loads(resp.content.strip("`"))
        return { "task_type": data.get("task_type", "content"),
                "complexity": data.get("complexity", "medium"), "source": "20b"}
    except Exception:
        return {"task_type": "content", "complexity": "medium", "source": "fallback"}
        
def classify(instruction: str) -> dict:
    '''Reglas primero; 20B solo si hace falta.'''
    return _rule_based(instruction) or _llm_based(instruction)

def router_node(state) -> dict:
    '''Nodo del grafo: clasifica y escribe task_type y complexity en el estado.'''
    r = classify(state["instruction"])
    print(f"[router] via {r['source']} -> task_type={r['task_type']} complexity={r['complexity']}")
    return {"task_type": r["task_type"], "complexity": r["complexity"]}