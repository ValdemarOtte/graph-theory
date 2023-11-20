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
        dijkstra_valid_adjacency_matrix: dict,
        dijkstra_valid_cost: float,
    ):
        # run algorithm and create adjacency matrix
        dijkstra_g, cost, path = dijktra_algoritm(dijkstra_graph, "A")
        dijkstra_g.create_adjacency_matrix()
        assert dijkstra_g.adjacency_matrix == dijkstra_valid_adjacency_matrix
        assert cost == dijkstra_valid_cost
        assert path == None