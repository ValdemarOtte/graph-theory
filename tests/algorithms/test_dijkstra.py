### Imports
# Standard library

# Third-party libraries

# Local files
from graph_theory.algorithms.dijkstra import dijkstra_algoritm
from graph_theory.graph import Graph


class TestJDijkstraAlgoritm:
    def test_valid_dijkstra(
        self,
        dijkstra_graph: Graph,
        dijkstra_valid_predecessor: dict,
        dijkstra_valid_cost: float,
    ):
        """Test if Dijkstra Algoritm runs without any errors"""
        predecessor, cost = dijkstra_algoritm(dijkstra_graph, "A")
        assert predecessor == dijkstra_valid_predecessor
        assert cost == dijkstra_valid_cost
