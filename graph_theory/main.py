### Imports
# Standard library
from pathlib import Path

# Third-party libraries

# Local files
from graph_theory.utils.functions import read_csv
from graph_theory.graph import Graph
from graph_theory.draw_graph import draw_graph
from graph_theory.algorithms.jarnik_prim import jarnik_prim_algoritm
from graph_theory.algorithms.breadth_first_search import BFS
from graph_theory.algorithms.dijkstra import dijkstra_algoritm
from graph_theory.algorithms.depth_first_search import DFS


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
    #g, a, b = BFS(g)
    
    draw_graph(g)


if __name__ == "__main__":
    main()