### Imports
# Standard library
from pathlib import Path

from graph_theory.draw_graph import draw_graph
from graph_theory.graph import Graph

# Third-party libraries
# Local files
from graph_theory.utils.functions import read_csv
from graph_theory.algorithms.breadth_first_search import breadth_first_search


def read_graph(path: Path) -> Graph:
    """
    Read csv-file with information about a graph.

    :param (Path) path: Path to file which contrains information about the graph.
    :return (Graph): A Graph-object
    """
    g = Graph()
    graph_data = read_csv(path)
    for v, w, oriented_value, cost in graph_data:
        if oriented_value == "1":
            oriented = True
        oriented = False

        g.add_edge(v, w, oriented, float(cost))
    return g


def main() -> None:
    g1_path: Path = Path("graph_theory\\data\\graph_2.csv")
    g = read_graph(g1_path)
    g, level, time = breadth_first_search(g)
    
    print(g)
    print(level)
    print(time)

    #draw_graph(g)


if __name__ == "__main__":
    main()
