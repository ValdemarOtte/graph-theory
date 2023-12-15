### Imports
# Standard library
from math import inf
from random import choice

# Third-party libraries
# Local files
from graph_theory.graph import Graph


def jarnik_prim_algoritm(graph: Graph, r: str = "") -> tuple[dict, float]:
    """
    Jarnik Prim Algoritm for an optimal tree T of G with predecessor function p, and its weight.

    Args:
        graph: The graph which Jarnik Prim algoritm will be used on
        r: The root of the algoritm. Defalut is a empty string

    Returns:
        An optimal tree T of graph and its weigth
    """
    uncoloured = graph.vertices
    predecessor = {v : None for v in graph.vertices}
    cost = {v : inf for v in graph.vertices}
    T_cost = 0.0

    # Pick root if none is giving
    if r == "":
        r = choice(graph.vertices)  # noqa: S311

    cost[r] = 0

    while uncoloured != []:
        uncoloured_vertexs_cost = {k:cost[k] for k in uncoloured if k in cost}
        u = min(uncoloured_vertexs_cost, key=uncoloured_vertexs_cost.get)
        uncoloured.remove(u)
        T_cost += cost[u]

        for v in uncoloured:
            if graph.costs[v][u] < cost[v]:
                predecessor[v] = u
                cost[v] = graph.costs[v][u]
    return predecessor, T_cost


def Jarnik_Prim_graph():
    g = Graph()

    g.add_edge("B", "C", cost=1457)
    g.add_edge("B", "G", cost=1892)
    g.add_edge("B", "N", cost=901)
    g.add_edge("B", "S", cost=1078)
    g.add_edge("B", "T", cost=111)
    g.add_edge("B", "W", cost=1057)
    g.add_edge("B", "Y", cost=1117)

    g.add_edge("C", "G", cost=978)
    g.add_edge("C", "N", cost=1199)
    g.add_edge("C", "S", cost=1430)
    g.add_edge("C", "T", cost=1442)
    g.add_edge("C", "W", cost=750)
    g.add_edge("C", "Y", cost=473)

    g.add_edge("G", "N", cost=1133)
    g.add_edge("G", "S", cost=1197)
    g.add_edge("G", "T", cost=1820)
    g.add_edge("G", "W", cost=837)
    g.add_edge("G", "Y", cost=867)

    g.add_edge("N", "S", cost=267)
    g.add_edge("N", "T", cost=800)
    g.add_edge("N", "W", cost=459)
    g.add_edge("N", "Y", cost=727)

    g.add_edge("S", "T", cost=970)
    g.add_edge("S", "W", cost=681)
    g.add_edge("S", "Y", cost=962)

    g.add_edge("T", "W", cost=988)
    g.add_edge("T", "Y", cost=1080)

    g.add_edge("W", "Y", cost=285)
    return g

g = Jarnik_Prim_graph()
p, t = jarnik_prim_algoritm(g, "Y")
print(p)
print(t)