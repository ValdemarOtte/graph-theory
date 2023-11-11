### Imports
# Standard library

# Third-party libraries

# Local files
from graph_theory.algorithms.breadth_first_search import BFS
from graph_theory.graph import Graph


class TestBreadthFirstSearch:
    def test_valid_(
        self,
        BFS_graph: Graph,
        BFS_valid_adjacency_matrix: dict,
        BFS_valid_level: dict,
        BFS_valid_time: dict,
    ):
        # run algorithm and create adjacency matrix
        BFS_g, level, time = BFS(BFS_graph, "1")
        BFS_g.create_adjacency_matrix()
        assert BFS_g.adjacency_matrix == BFS_valid_adjacency_matrix
        assert level == BFS_valid_level
        assert time == BFS_valid_time
