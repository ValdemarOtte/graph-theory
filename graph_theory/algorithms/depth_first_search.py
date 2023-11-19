### Imports
# Standard library
from random import choice

# Third-party libraries
# Local files
from graph_theory.graph import Graph


def DFS(graph: Graph, r: None) -> (Graph, dict, dict):
    """
    Depth-First Search.

    Args:
        graph: A connected graph
        r: The root of the graph which a tree will come from

    Returns:
        BFS_graph: A r-tree
        level: A level dict
        time: A time dict
    """
    BFS_graph = Graph()
    # Set variables
    index = 1
    Q: list = []
    visited: list = []
    # time: dict = {}
    # level: dict = {}

    # Pick root if none is giving
    if not r:
        choice(graph.vertices)  # noqa: S311

    # Update level, time and visited with root
    Q.append(r)
    # time[r] = index
    # level[r] = 0
    visited.append(r)

    # Run algorithm while Q is nonemprt
    while [] != Q:
        # Consider the head of Q
        x = Q[-1]
        # ?
        Q.remove(x)
    return BFS_graph  # , level, time
