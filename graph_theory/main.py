### Imports
# Standard library

# Third-party libraries

# Local files
from algorithms.breadth_first_search import BFS  # type: ignore
from graph import Graph  # type: ignore

if __name__ == "__main__":
    g = Graph()

    g.add_edge("1", "2")
    g.add_edge("1", "3")
    g.add_edge("1", "4")
    g.add_edge("1", "5")
    g.add_edge("2", "6")
    g.add_edge("2", "7")
    g.add_edge("3", "8")
    g.add_edge("3", "9")
    g.add_edge("4", "7")
    g.add_edge("4", "10")
    g.add_edge("5", "10")
    g.add_edge("5", "11")
    g.add_edge("6", "8")
    g.add_edge("6", "12")
    g.add_edge("7", "12")
    g.add_edge("9", "11")
    g.add_edge("9", "13")
    g.add_edge("10", "11")
    g.add_edge("10", "13")

    BFS_g, level, time = BFS(g, "1")
    print(level)
    # BFS_g.create_adjacency_matrix()
    # print(BFS_g.adjacency_matrix)
    # print_rich.print_adjacency_matrix(BFS_g.adjacency_matrix)
