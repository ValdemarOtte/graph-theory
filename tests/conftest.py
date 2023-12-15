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


@pytest.fixture()
def valid_graph():
    # fmt: off
    valid_graph = {
        "a": ["b", "a", "a", "c", "b"],
        "b": ["a", "c", "a"],
        "c": ["a", "b"]
    }
    # fmt: on
    return valid_graph  # noqa: RET504


@pytest.fixture()
def valid_vertices():
    valid_vertices = ["a", "b", "c"]
    return valid_vertices  # noqa: RET504


@pytest.fixture()
def valid_adjacency_matrix():
    valid_adjacency_matrix = {
        "a": {"a": 2, "b": 2, "c": 1},
        "b": {"a": 2, "b": 0, "c": 1},
        "c": {"a": 1, "b": 1, "c": 0},
    }
    return valid_adjacency_matrix  # noqa: RET504


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
    # fmt: off
    valid_adjacency_matrix = {
        "1": {
            "1": 0, "2": 1, "3": 1, "4": 1, "5": 1, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0,  # noqa: E501
        },
        "2": {
            "1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 1, "7": 1, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0,  # noqa: E501
        },
        "3": {
            "1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 1, "9": 1, "10": 0, "11": 0, "12": 0, "13": 0,  # noqa: E501
        },
        "4": {
            "1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 1, "11": 0, "12": 0, "13": 0,  # noqa: E501
        },
        "5": {
            "1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 1, "12": 0, "13": 0,  # noqa: E501
        },
        "6": {
            "1": 0, "2": 1, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 1, "13": 0,  # noqa: E501
        },
        "7": {
            "1": 0, "2": 1, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0,  # noqa: E501
        },
        "8": {
            "1": 0, "2": 0, "3": 1, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0,  # noqa: E501
        },
        "9": {
            "1": 0, "2": 0, "3": 1, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 1,  # noqa: E501
        },
        "10": {
            "1": 0, "2": 0, "3": 0, "4": 1, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0,  # noqa: E501
        },
        "11": {
            "1": 0, "2": 0, "3": 0, "4": 0, "5": 1, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0,  # noqa: E501
        },
        "12": {
            "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 1, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0,  # noqa: E501
        },
        "13": {
            "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 1, "10": 0, "11": 0, "12": 0, "13": 0,  # noqa: E501
        },
    }
    # fmt: on
    return valid_adjacency_matrix  # noqa: RET504


@pytest.fixture()
def BFS_valid_level():
    # fmt: off
    valid_level = {
        "1": 0, "2": 1, "3": 1, "4": 1, "5": 1, "6": 2, "7": 2, "8": 2, "9": 2, "10": 2, "11": 2, "12": 3, "13": 3,  # noqa: E501
    }
    # fmt: on
    return valid_level  # noqa: RET504


@pytest.fixture()
def BFS_valid_time():
    # fmt: off
    valid_time = {
        "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "11": 11, "12": 12, "13": 13,  # noqa: E501
    }
    # fmt: on
    return valid_time  # noqa: RET504


# --------------------------------------------------
# Variables to test_dijkstra.py
# --------------------------------------------------
@pytest.fixture()
def DFS_valid_predecessor():
    valid_predecessor = {
        "1": None,
        "2": "1",
        "3": "8",
        "4": "10",
        "5": "11",
        "6": "2",
        "7": "4",
        "8": "6",
        "9": "3",
        "10": "5",
        "11": "9",
        "12": "7",
        "13": "10",
    }
    return valid_predecessor  # noqa: RET504


@pytest.fixture()
def DFS_valid_time():
    valid_time = {
        "1": None,
        "2": 2,
        "3": 5,
        "4": 10,
        "5": 8,
        "6": 3,
        "7": 11,
        "8": 4,
        "9": 6,
        "10": 9,
        "11": 7,
        "12": 12,
        "13": 16,
    }
    return valid_time  # noqa: RET504


@pytest.fixture()
def DFS_valid_level():
    valid_level = {
        "1": 26,
        "2": 25,
        "3": 22,
        "4": 15,
        "5": 19,
        "6": 24,
        "7": 14,
        "8": 23,
        "9": 21,
        "10": 18,
        "11": 20,
        "12": 13,
        "13": 17,
    }
    return valid_level  # noqa: RET504


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
def Jarnik_Prim_valid_predecessor():
    Jarnik_Prim_valid_predecessor = {
        "B": "T",
        "C": "Y",
        "G": "W",
        "N": "W",
        "S": "N",
        "T": "N",
        "W": "Y",
        "Y": None,
    }
    return Jarnik_Prim_valid_predecessor  # noqa: RET504


@pytest.fixture()
def Jarnik_Prim_valid_cost():
    return 3232.0


# --------------------------------------------------
# Variables to test_dijkstra.py
# --------------------------------------------------
@pytest.fixture()
def dijkstra_graph():
    g = Graph()
    g.add_edge("A", "B", cost=2)
    g.add_edge("A", "C", cost=1)
    g.add_edge("B", "D", cost=5)
    g.add_edge("B", "E", cost=1)
    g.add_edge("C", "E", cost=3)
    g.add_edge("C", "F", cost=5)
    g.add_edge("D", "G", cost=5)
    g.add_edge("E", "G", cost=1)
    g.add_edge("F", "G", cost=5)
    return g


@pytest.fixture()
def dijkstra_valid_predecessor():
    dijkstra_valid_predecessor = {
        "A": None,
        "B": "A",
        "C": "A",
        "D": "B",
        "E": "B",
        "F": "C",
        "G": "E",
    }
    return dijkstra_valid_predecessor  # noqa: RET504


@pytest.fixture()
def dijkstra_valid_cost():
    costs = {"A": 0, "B": 2, "C": 1, "D": 7, "E": 3, "F": 6, "G": 4}
    return costs
