### Imports
# Standard library
from random import choice

# Third-party libraries

# Local files
from graph_theory.graph import Graph


def breadth_first_search(graph: Graph, root: str = "") -> tuple[Graph, dict, dict]:
    """
    Breadth First Search algorithm.
    
    If no root is given, then the algorithm will pick a random root.

    :param (Graph) graph: A connected graph.
    :param (str) root: The root which the search will start from.
    :returns (Graph) grapg: bla
    :returns (dict) level: bla
    :returns (dict) time: bla
    """
    BFS_graph = Graph()
    # Set variables
    index: int = 1
    Q: list = []
    visited: list = []
    time: dict = {}
    level: dict = {}

    # Pick root if none is giving
    if root == "":
        root = choice(graph.vertices)  # noqa: S311

    # Update level, time and visited with root
    Q.append(root)
    time[root] = index
    level[root] = 0
    visited.append(root)

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
