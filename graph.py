from langgraph.graph import StateGraph, START, END
from state import State

def saludo_node(state: State)-> dict:
    '''
        Primer nodo: lee la instrucción del estado y devuelve un saludo.
        
        Un nodo SIEMPRE recibe el estado complet y devuelve un dict SOLO con los campos que quiere agregar o
        cambiar. LangGrpah  se encarga de mezclar ese dict en el estado que sigue viajando por el grafo.
    '''
    
    instruccion = state["instruction"]
    print(f'[saludo_node] recibi la instruccion: {instruccion!r}')
    return {"status": "nodo ejecutado"}

def build_graph():
    '''Construye y compila el grafo.'''
    builder = StateGraph(State)
    
    builder.add_node("saludo", saludo_node)
    builder.add_edge(START, "saludo")
    builder.add_edge("saludo", END)
    return builder.compile()

graph= build_graph()