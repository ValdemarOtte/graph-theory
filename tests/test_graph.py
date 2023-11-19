### Imports
# Standard library

# Third-party libraries

# Local files
from graph_theory.graph import Graph


class TestGraph:
    def test_valid_graph(self, simple_graph: Graph, valid_graph: dict):
        assert simple_graph.graph == valid_graph

    def test_valid_vertices(self, simple_graph: Graph, valid_vertices: list):
        assert simple_graph.vertices == valid_vertices

    def test_valid_adjacency_matrix(self, simple_graph: Graph, valid_adjacency_matrix: dict):
        assert simple_graph.adjacency_matrix == valid_adjacency_matrix
