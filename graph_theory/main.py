### Imports
# Standard library

# Third-party libraries

# Local files
from graph import Graph
from mics import print_rich


if __name__ == "__main__":
    g = Graph()
    
    g.add_edge("a", "b")
    g.add_edge("a", "a")
    g.add_edge("a", "c")
    g.add_edge("b", "c")
    g.add_edge("a", "b")

    a = {
        "a": {"a": 2, "b": 2, "c": 1},
        "b": {"a": 2, "b": 0, "c": 1},
        "c": {"a": 1, "b": 1, "c": 0},
    }

    g.create_adjacency_matrix()
    print_rich.print_adjacency_matrix(g.adjacency_matrix)