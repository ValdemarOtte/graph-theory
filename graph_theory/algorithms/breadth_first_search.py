### Imports
# Standard library
from random import choice

# Third-party libraries

# Local files
from graph_theory.graph import Graph


def BFS(graph: Graph, r: None) -> Graph:
    """"""
    BFS_graph = Graph()
    index = 0
    Q = []
    seen = []
    index += 1
    if not r:
        choice(graph.vertices)
    Q.append(r)
    seen.append(r)
    while Q != []:
        x = Q[0]
        for v in graph.graph[x]:
            if v not in seen:
                index += 1
                seen.append(v)
                Q.append(v)
                BFS_graph.add_edge(x, v)
        Q.remove(x)
    return BFS_graph

