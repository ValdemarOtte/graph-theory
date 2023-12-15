### Imports
# Standard library

# Third-party libraries

# Local files
from graph_theory.algorithms.dijkstra import dijktra_algoritm
from graph_theory.graph import Graph


class TestJDijkstraAlgoitm:
    def test_valid_dijkstra(
        self,
        dijkstra_graph: Graph,
        dijkstra_valid_predecessor: dict,
        dijkstra_valid_cost: float,
    ):
        # run algorithm and create adjacency matrix
        predecessor, cost = dijktra_algoritm(dijkstra_graph, "A")
        assert predecessor == dijkstra_valid_predecessor
        assert cost == dijkstra_valid_cost
