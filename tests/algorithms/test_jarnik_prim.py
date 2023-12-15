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
        Jarnik_Prim_valid_predecessor: dict,
        Jarnik_Prim_valid_cost: float,
    ):
        """Test if Jarnik Prim algoritm runs without any errors"""
        # run algorithm and create adjacency matrix
        predecessor, cost = jarnik_prim_algoritm(Jarnik_Prim_graph, "Y")
        assert predecessor == Jarnik_Prim_valid_predecessor
        assert cost == Jarnik_Prim_valid_cost

    def test_valid_Jarnik_Prim_without_root(
        self,
        Jarnik_Prim_graph: Graph,
        Jarnik_Prim_valid_predecessor: dict,
        Jarnik_Prim_valid_cost: float,
    ):
        # run algorithm without "Y" as root and create adjacency matrix
        Jarnik_Prim_valid_predecessor, cost = jarnik_prim_algoritm(Jarnik_Prim_graph)
        assert Jarnik_Prim_valid_predecessor == Jarnik_Prim_valid_predecessor
        assert cost == Jarnik_Prim_valid_cost
