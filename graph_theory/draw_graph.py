### Imports
# Standard library

# Third-party libraries
import matplotlib.pyplot as plt
import networkx as nx

# Local files
from graph_theory.graph import Graph


def draw_graph(graph: Graph):
    G = nx.DiGraph()


    for v in graph.vertices:
        G.add_node(v)

    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        edgelist=graph.edges["not_orr"],
        connectionstyle="arc3, rad = 0.1",
        arrows=False,
    )
    nx.draw(
        G,
        pos,
        with_labels=True,
        edgelist=graph.edges["orr"],
        connectionstyle="arc3, rad = 0.1",
        arrows=True,
    )

    edge_labels = dict(
        [
            (
                (
                    u,
                    v,
                ),
                d["length"],
            )
            for u, v, d in G.edges(data=True)
        ],
    )

    plt.show()
