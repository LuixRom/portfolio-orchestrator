from typing import TypedDict

class State(TypedDict, total = False):
    '''
        Memoria compartida que viaja por el grafo.
        total=False -> todos los campos son opcionales: cada nodo llena solo lo que produce. Empiezan vacios
        y se van llenando paso a paso.
    '''
    
    instruction: str 
    run_id: str
    
    task_type: str
    complexity: str
    
    tier: str
    changed_files: list
    
    workspace: str
    diff: str
    
    validation: dict
    
    decision: str
    retry_count: int 
    
    status: str
    