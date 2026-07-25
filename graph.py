from langgraph.graph import StateGraph, START, END
from state import State
from agents.router import router_node


def build_graph():
    builder = StateGraph(State)

    builder.add_node("router", router_node)

    builder.add_edge(START, "router")
    builder.add_edge("router", END)

    return builder.compile()


graph = build_graph()