### Imports
# Standard library
from pathlib import Path

# Third-party libraries

# Local files
from mics.functions import read_csv
from graph import Graph


def read_graph(path: Path) -> Graph:
    g = Graph()
    graph_data = read_csv(path)
    for v, w, oriented_value, cost in graph_data:

        if oriented_value == "1":
            oriented = True
        oriented = False

        print(v, w, oriented, float(cost))
    return g


def main() -> None:

    g1_path: Path = Path("graph_theory\\data\\graph_1.csv")
    g = read_graph(g1_path)

    pass


if __name__ == "__main__":
    main()