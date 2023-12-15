### Imports
# Standard library

# Third-party libraries

# Local files
from graph_theory.algorithms.depth_first_search import DFS
from graph_theory.graph import Graph


class TestDepthFirstSearch:
    def test_valid_(
        self,
        BFS_graph: Graph,
        DFS_valid_predecessor: dict,
        DFS_valid_time: dict,
        DFS_valid_level: dict,
    ):
        # run algorithm and create adjacency matrix
        predecessor, time, level = DFS(BFS_graph, "1")
        assert predecessor == DFS_valid_predecessor
        assert time == DFS_valid_time
        assert level == DFS_valid_level
