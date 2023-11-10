### Imports
# Standard library

# Third-party libraries

# Local files


class TestGraph():
    def test_valid_graph(self, simple_graph):
        valid_graph = {
            "a": ["b", "a", "a", "c", "b"],
            "b": ["a", "c", "a"],
            "c": ["a", "b"]
        }
        assert simple_graph.graph == valid_graph

    def test_valid_vertices(self, simple_graph):
        valid_vertices = ["a", "b", "c"]
        assert simple_graph.vertices == valid_vertices
    
    def test_valid_adjacency_matrix(self, simple_graph):
        valid_adjacency_matrix = {
            "a": {"a": 2, "b": 2, "c": 1},
            "b": {"a": 2, "b": 0, "c": 1},
            "c": {"a": 1, "b": 1, "c": 0},
        }
        assert simple_graph.adjacency_matrix == valid_adjacency_matrix