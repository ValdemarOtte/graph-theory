### Imports
# Standard library

# Third-party libraries
import pytest

# Local files
from graph_theory.graph import Graph


# --------------------------------------------------
# Variables to test_graph.py
# --------------------------------------------------

@pytest.fixture()
def simple_graph():
    g = Graph()

    g.add_edge("a", "b")
    g.add_edge("a", "a")
    g.add_edge("a", "c")
    g.add_edge("b", "c")
    g.add_edge("a", "b")

    g.create_adjacency_matrix()
    return g

# --------------------------------------------------
# Variables to test_breadth_first_search.py
# --------------------------------------------------
@pytest.fixture()
def BFS_graph():
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

    g.create_adjacency_matrix()
    return g


@pytest.fixture()
def BFS_valid_adjacency_matrix():
    valid_adjacency_matrix = {
        "1": {
            "1": 0,
            "2": 1,
            "3": 1,
            "4": 1,
            "5": 1,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
        "2": {
            "1": 1,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 1,
            "7": 1,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
        "3": {
            "1": 1,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 1,
            "9": 1,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
        "4": {
            "1": 1,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 1,
            "11": 0,
            "12": 0,
            "13": 0,
        },
        "5": {
            "1": 1,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 1,
            "12": 0,
            "13": 0,
        },
        "6": {
            "1": 0,
            "2": 1,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 1,
            "13": 0,
        },
        "7": {
            "1": 0,
            "2": 1,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
        "8": {
            "1": 0,
            "2": 0,
            "3": 1,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
        "9": {
            "1": 0,
            "2": 0,
            "3": 1,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 1,
        },
        "10": {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 1,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
        "11": {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 1,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
        "12": {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 1,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
        "13": {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 1,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    }
    return valid_adjacency_matrix  # noqa: RET504


@pytest.fixture()
def BFS_valid_level():
    valid_level = {
        "1": 0,
        "2": 1,
        "3": 1,
        "4": 1,
        "5": 1,
        "6": 2,
        "7": 2,
        "8": 2,
        "9": 2,
        "10": 2,
        "11": 2,
        "12": 3,
        "13": 3,
    }
    return valid_level  # noqa: RET504


@pytest.fixture()
def BFS_valid_time():
    valid_time = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "11": 11,
        "12": 12,
        "13": 13,
    }
    return valid_time  # noqa: RET504


# --------------------------------------------------
# Variables to test_jarnik_prim.py
# --------------------------------------------------
@pytest.fixture()
def Jarnik_Prim_graph():
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
    return g

@pytest.fixture()
def Jarnik_Prim_valid_adjacency_matrix():
    Jarnik_Prim_valid_adjacency_matrix = {'Y': {'Y': 0, 'W': 1, 'N': 0, 'S': 0, 'C': 1, 'T': 0, 'B': 0, 'G': 0}, 'W': {'Y': 1, 'W': 0, 'N': 1, 'S': 0, 'C': 0, 'T': 0, 'B': 0, 'G': 1}, 'N': {'Y': 0, 'W': 1, 'N': 0, 'S': 1, 'C': 0, 'T': 1, 'B': 0, 'G': 0}, 'S': {'Y': 0, 'W': 0, 'N': 1, 'S': 0, 'C': 0, 'T': 0, 'B': 0, 'G': 0}, 'C': {'Y': 1, 'W': 0, 'N': 0, 'S': 0, 'C': 0, 'T': 0, 'B': 0, 'G': 0}, 'T': {'Y': 0, 'W': 0, 'N': 1, 'S': 0, 'C': 0, 'T': 0, 'B': 1, 'G': 0}, 'B': {'Y': 0, 'W': 0, 'N': 0, 'S': 0, 'C': 0, 'T': 1, 'B': 0, 'G': 0}, 'G': {'Y': 0, 'W': 1, 'N': 0, 'S': 0, 'C': 0, 'T': 0, 'B': 0, 'G': 0}}
    return Jarnik_Prim_valid_adjacency_matrix  # noqa: RET504

@pytest.fixture()
def Jarnik_Prim_valid_cost():
    return 3232.0
