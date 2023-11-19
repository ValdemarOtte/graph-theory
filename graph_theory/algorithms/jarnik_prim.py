### Imports
# Standard library
from math import inf
from random import choice

# Third-party libraries
# Local files
from graph_theory.graph import Graph


def jarnik_prim_algoritm(graph: Graph, r: str = "") -> tuple[Graph, float]:
    """
    Jarnik Prim Algoritm for an optimal tree T of G with predecessor function p, and its weight.

    Args:
        graph: The graph which Jarnik Prim algoritm will be used on
        r: The root of the algoritm. Defalut is a empty string

    Returns:
        An optimal tree T of graph and its weigth
    """
    jarnik_prim_graph = Graph()

    uncoloured = graph.vertices
    T_cost = 0.0

    # Pick root if none is giving
    if r == "":
        r = choice(graph.vertices)  # noqa: S311

    jarnik_prim_graph.add_vertex(r)

    uncoloured.remove(r)
    while uncoloured != []:
        min_cost = inf
        for v in jarnik_prim_graph.vertices:
            for u in uncoloured:
                if graph.costs[v][u] < min_cost:
                    min_cost = graph.costs[v][u]
                    uu = u
                    vv = v
        # Step 6
        uncoloured.remove(uu)
        # Step 8
        jarnik_prim_graph.add_edge(vv, uu)
        # Step 9
        T_cost += min_cost

    return jarnik_prim_graph, T_cost
