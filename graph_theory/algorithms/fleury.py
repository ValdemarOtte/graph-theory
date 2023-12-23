### Imports
# Standard library
import copy

# Third-party libraries
# Local files
from graph_theory.graph import Graph

g = Graph()
g.add_edge("A", "C")
g.add_edge("A", "D")
g.add_edge("B", "D")
g.add_edge("B", "E")
g.add_edge("C", "D")
g.add_edge("D", "E")


def fleury(graph, u):
    W = [u]
    x = u
    F = graph.graph
    if F[x] != []:
        a = []
        b = []
        
        print(F[x])


fleury(g, "A")