from langgraph.graph import StateGraph, START, END
from state import State
from agents.router import router_node
from agents.content import propose as content_propose
from schemas.profile import load_profile
from tools.workspace import create_workspace, read_file, write_file

CONTENT_FILE = "content/site.json"

def propose_node(state: State) -> dict:
    '''Crea el workspace aislado y escribe ahi la propuesta del agente.'''
    ws= create_workspace(state["run_id"])          
    current= read_file(ws, CONTENT_FILE)            
    profile= load_profile().model_dump()            
    nuevo= content_propose(state["instruction"], profile, current)
    write_file(ws, CONTENT_FILE, nuevo)              
    print(f'[propose] propuesta escrita en: {ws}')
    return {"workspace": str(ws), "changed_files": [CONTENT_FILE]}

def build_graph():
    builder = StateGraph(State)
    builder.add_node("router", router_node)
    builder.add_node("propose", propose_node)

    builder.add_edge(START, "router")
    builder.add_edge("router", "propose")
    builder.add_edge("propose", END)

    return builder.compile()


graph = build_graph()
