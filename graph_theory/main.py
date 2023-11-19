### Imports
# Standard library

# Third-party libraries

# Local files
from mics.print_rich import print_adjacency_matrix
from graph import Graph  # type: ignore

if __name__ == "__main__":
    g = Graph()

    g.add_edge("B", "C", cost=1457)
    g.add_edge("B", "G", cost=1892)
    g.add_edge("B", "N", cost=901)
    g.add_edge("B", "S", cost=1078)
    g.add_edge("B", "T", cost=111)
    g.add_edge("B", "W", cost=1057)
    g.add_edge("B", "Y", cost=1117)

    g.add_edge("C", "G", cost=978)
    g.add_edge("C", "N", cost=1199)
    g.add_edge("C", "S", cost=1430)
    g.add_edge("C", "T", cost=1442)
    g.add_edge("C", "W", cost=750)
    g.add_edge("C", "Y", cost=473)

    g.add_edge("G", "N", cost=1133)
    g.add_edge("G", "S", cost=1197)
    g.add_edge("G", "T", cost=1820)
    g.add_edge("G", "W", cost=837)
    g.add_edge("G", "Y", cost=867)

    g.add_edge("N", "S", cost=267)
    g.add_edge("N", "T", cost=800)
    g.add_edge("N", "W", cost=459)
    g.add_edge("N", "Y", cost=727)

    g.add_edge("S", "T", cost=970)
    g.add_edge("S", "W", cost=681)
    g.add_edge("S", "Y", cost=962)

    g.add_edge("T", "W", cost=988)
    g.add_edge("T", "Y", cost=1080)

    g.add_edge("W", "Y", cost=285)

    g.create_adjacency_matrix()
    print_adjacency_matrix(g.adjacency_matrix)

    """
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
    """
