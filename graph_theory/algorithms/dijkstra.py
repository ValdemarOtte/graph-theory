### Imports
# Standard library
from math import inf
from random import choice

# Third-party libraries

# Local files
from graph_theory.graph import Graph


def dijktra_algoritm(graph, r):

    uncoloured = graph.vertices
    predecessor = {v : None for v in graph.vertices}
    cost = {v : inf for v in graph.vertices} 
    cost[r] = 0

    while uncoloured != []:
        uncoloured_vertexs_cost = {k:cost[k] for k in uncoloured if k in cost}
        u = min(uncoloured_vertexs_cost, key=uncoloured_vertexs_cost.get)
        uncoloured.remove(u)

        for v in uncoloured:
            try:
                if graph.costs[u][v] + cost[u] < cost[v]:
                    predecessor[v] = u
                    cost[v] = cost[u] + graph.costs[v][u]
            except KeyError:
                continue
    
    return predecessor, cost