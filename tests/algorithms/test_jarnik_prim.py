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
        """Test if Jarnik Prim Algoritm runs without any errors."""
        predecessor, cost = jarnik_prim_algoritm(Jarnik_Prim_graph, "Y")
        assert predecessor == Jarnik_Prim_valid_predecessor
        assert cost == Jarnik_Prim_valid_cost

    def test_valid_Jarnik_Prim_without_root(
        self,
        Jarnik_Prim_graph: Graph,
        Jarnik_Prim_valid_predecessor: dict,
        Jarnik_Prim_valid_cost: float,
    ):
        """Test if Jarnik Prim Algoritm runs without any errors when no root is given."""
        Jarnik_Prim_valid_predecessor, cost = jarnik_prim_algoritm(Jarnik_Prim_graph)
        assert Jarnik_Prim_valid_predecessor == Jarnik_Prim_valid_predecessor
        assert cost == Jarnik_Prim_valid_cost
