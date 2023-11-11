### Imports
# Standard library
from random import choice

# Third-party libraries
# Local files
from graph_theory.graph import Graph


def BFS(graph: Graph, r: None) -> (Graph, dict, dict):
    """
    Breadth-First Search.

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
    time: dict = {}
    level: dict = {}

    # Pick root if none is giving
    if not r:
        choice(graph.vertices)  # noqa: S311

    # Update level, time and visited with root
    Q.append(r)
    time[r] = index
    level[r] = 0
    visited.append(r)

    # Run algorithm while Q is nonemprt
    while [] != Q:
        # Consider the head of Q
        x = Q[0]
        for v in graph.graph[x]:
            if v not in visited:
                # Update index, visited, level, time and Q bases on v
                index += 1
                visited.append(v)
                level[v] = level[x] + 1
                time[v] = index
                Q.append(v)
                BFS_graph.add_edge(x, v)
        Q.remove(x)
    return BFS_graph, level, time
