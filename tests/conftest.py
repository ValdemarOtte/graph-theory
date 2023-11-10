### Imports
# Standard library

# Third-party libraries
import pytest

# Local files
from graph_theory.graph import Graph


@pytest.fixture()
def simple_graph():
    g = Graph()
    
    g.add_edge("a", "b")
    g.add_edge("a", "a")
    g.add_edge("a", "c")
    g.add_edge("b", "c")
    g.add_edge("a", "b")
    
    g.create_adjacency_matrix()
    return g


@pytest.fixture()
def simple_graph_BFS():
    g = Graph()
    
    g.add_edge("1", "2")
    g.add_edge("1", "3")
    g.add_edge("1", "4")
    g.add_edge("1", "5")
    g.add_edge("2", "6")
    g.add_edge("2", "7")
    g.add_edge("3", "8")
    g.add_edge("3", "9")
    g.add_edge("4", "7")
    g.add_edge("4", "10")
    g.add_edge("5", "10")
    g.add_edge("5", "11")
    g.add_edge("6", "8")
    g.add_edge("6", "12")
    g.add_edge("7", "12")
    g.add_edge("9", "11")
    g.add_edge("9", "13")
    g.add_edge("10", "11")
    g.add_edge("10", "13")
    
    g.create_adjacency_matrix()
    return g