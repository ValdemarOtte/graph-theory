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