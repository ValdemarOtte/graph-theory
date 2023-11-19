### Imports
# Standard library

# Third-party libraries

# Local files
from graph_theory.algorithms.jarnik_prim import jarnik_prim_algoritm
from graph_theory.graph import Graph


class TestJarnikPrimAlgoitm:
    def test_valid_Jarnik_Prim(
        self,
        Jarnik_Prim_graph: Graph,
        Jarnik_Prim_valid_adjacency_matrix: dict,
        Jarnik_Prim_valid_cost: float,
    ):
        # run algorithm and create adjacency matrix
        jarnik_prim_g, cost = jarnik_prim_algoritm(Jarnik_Prim_graph, "Y")
        jarnik_prim_g.create_adjacency_matrix()
        assert jarnik_prim_g.adjacency_matrix == Jarnik_Prim_valid_adjacency_matrix
        assert cost == Jarnik_Prim_valid_cost

    def test_valid_Jarnik_Prim_without_root(
        self,
        Jarnik_Prim_graph: Graph,
        Jarnik_Prim_valid_adjacency_matrix: dict,
        Jarnik_Prim_valid_cost: float,
    ):
        # run algorithm without "Y" as root and create adjacency matrix
        jarnik_prim_g, cost = jarnik_prim_algoritm(Jarnik_Prim_graph)
        jarnik_prim_g.create_adjacency_matrix()
        assert jarnik_prim_g.adjacency_matrix == Jarnik_Prim_valid_adjacency_matrix
        assert cost == Jarnik_Prim_valid_cost