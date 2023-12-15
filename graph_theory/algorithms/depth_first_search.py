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
    # Set variables
    index = 1
    Q: list = []
    uncoloured = graph.vertices

    # time: dict = {}
    # level: dict = {}
    predecessor = {v: None for v in graph.vertices}
    time = {v: None for v in graph.vertices}
    level = {v: None for v in graph.vertices}

    # Pick root if none is giving
    if not r:
        choice(graph.vertices)  # noqa: S311

    # Update level, time and visited with root
    Q.append(r)
    # time[r] = index
    # level[r] = 0
    uncoloured.remove(r)

    # Run algorithm while Q is nonemprt
    while Q != []:
        index += 1
        # Consider the head of Q
        x = Q[-1]
        # ?
        uncoloured_neighbour = [v for v in graph.graph[x] if v in uncoloured]
        if len(uncoloured_neighbour) > 0:
            u = uncoloured_neighbour[0]
            predecessor[u] = x
            time[u] = index
            Q.append(u)
            uncoloured.remove(u)
        else:
            level[x] = index
            Q.remove(x)

    return predecessor, time, level
