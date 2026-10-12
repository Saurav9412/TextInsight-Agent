from langgraph.graph import StateGraph, START, END
from state import State
from nodes import (
    classification_node,
    entity_extraction_node,
    summarization_node
)

# Intialize the workflow
graph = StateGraph(State)

# Register the nodes
graph.add_node("classification", classification_node)
graph.add_node("entity_extraction", entity_extraction_node)
graph.add_node("summarization", summarization_node)

# Connect the nodes with edges
graph.add_edge(START, "classification")
graph.add_edge("classification", "entity_extraction")
graph.add_edge("entity_extraction", "summarization")
graph.add_edge("summarization", END)

# Compile the graph
app = graph.compile()