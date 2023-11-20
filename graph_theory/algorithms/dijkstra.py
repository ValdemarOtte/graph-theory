### Imports
# Standard library
from math import inf

# Third-party libraries

# Local files
from graph_theory.graph import Graph

g = Graph()
g.add_edge("A", "B", cost=2)
g.add_edge("A", "C", cost=1)
g.add_edge("B", "D", cost=5)
g.add_edge("B", "E", cost=1)
g.add_edge("C", "E", cost=3)
g.add_edge("C", "F", cost=5)
g.add_edge("D", "G", cost=5)
g.add_edge("E", "G", cost=1)
g.add_edge("F", "G", cost=5)



def dijktra_algoritm(graph: Graph, source: str, sink: str = "") -> tuple[Graph, float]:
    dijktra_g = Graph()
    costs  = {}
    for v in graph.vertices:
        costs[v] = inf

    uncoloured = graph.vertices[:]
    dijktra_g.add_vertex(source)
    costs[source] = 0
    uncoloured.remove(source)

    while uncoloured != [] and [u for u in costs.keys() if costs[u] < inf] != []:

        min_cost = inf
        for v in dijktra_g.vertices:
            for u in uncoloured:
                try:
                    if graph.costs[v][u] < min_cost:
                        min_cost = graph.costs[v][u]
                        uu = u
                        vv = v
                except KeyError:
                    pass
        uncoloured.remove(uu)
        costs[uu] = min_cost + costs[vv]
        dijktra_g.add_edge(vv, uu)

        if uu == sink:
            break
    path = None
    # Create path here

    return dijktra_g, costs, path

"""

dijktra_g, costs = dijktra_algoritm(g, "A")
dijktra_g.create_adjacency_matrix()
print(dijktra_g.adjacency_matrix)

print("\n\n\n")
print(costs)
{'A': {'A': 0, 'C': 1, 'B': 1, 'E': 0, 'G': 0, 'F': 0, 'D': 0}, 'C': {'A': 1, 'C': 0, 'B': 0, 'E': 0, 'G': 0, 'F': 1, 'D': 0}, 'B': {'A': 1, 'C': 0, 'B': 0, 'E': 1, 'G': 0, 'F': 0, 'D': 1}, 'E': {'A': 0, 'C': 0, 'B': 1, 'E': 0, 'G': 1, 'F': 0, 'D': 0}, 'G': {'A': 0, 'C': 0, 'B': 0, 'E': 1, 'G': 0, 'F': 0, 'D': 0}, 'F': {'A': 0, 'C': 1, 'B': 0, 'E': 0, 'G': 0, 'F': 0, 'D': 0}, 'D': {'A': 0, 'C': 0, 'B': 1, 'E': 0, 'G': 0, 'F': 0, 'D': 0}}

{'A': 0, 'B': 2, 'C': 1, 'D': 7, 'E': 3, 'F': 6, 'G': 4

None
"""