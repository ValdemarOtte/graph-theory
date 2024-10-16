### Imports
# Standard library

# Third-party libraries
import numpy as np

# Local files


class Graph:
    """Standard Graph."""

    def __init__(self) -> None:
        self.graph: dict = {}
        self.vertices: list = []
        self.edges: dict = {"orr": [], "not_orr": []}
        self.costs: dict = {}
        self.adjacency_matrix: dict = {}

    def add_edge(self, v: str, w: str, oriented: bool = False, cost: float = 0.0) -> None:
        """
        New edge to the graph.

        :param (str) v: A vertice
        :param (str) w: A vertice
        :param (bool) oriented: a
        :param (float) cost: a
        """
        if v not in self.vertices:
            self.vertices.append(v)
        if w not in self.vertices:
            self.vertices.append(w)

        if v not in self.graph:
            self.graph[v] = []
        if w not in self.graph:
            self.graph[w] = []

        # If the edge is oriented, then its only from v to w
        # Else then it both ways
        if oriented:
            self.graph[v].append(w)
        else:
            self.graph[v].append(w)
            self.graph[w].append(v)

        if oriented:
            self.edges["orr"].append((v, w))

            if v not in self.costs:
                self.costs[v] = {}
            self.costs[v][w] = cost
        else:
            self.edges["not_orr"].append((v, w))

            if v not in self.costs:
                self.costs[v] = {}
            if w not in self.costs:
                self.costs[w] = {}
            self.costs[v][w] = cost
            self.costs[w][v] = cost

    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.vertices:
            self.vertices.append(vertex)
        if vertex not in self.graph:
            self.graph[vertex] = []

    def create_adjacency_matrix(self) -> None:
        """
        Create the adjacency matrix bases by the edges.
        """
        matrix: dict = {}

        # Create adjacency matrix with all vertices where all values is zero.2
        for w in self.vertices:
            matrix[w] = {}
            for v in self.vertices:
                matrix[w][v] = 0

        # Fill the adjacency matrix with number of connections between the vertices.
        for w in self.graph:
            for v in self.vertices:
                matrix[w][v] = self.graph[w].count(v)

        l = []
        for d in matrix.values():
            l.append([value for value in d.values()])

        self.adjacency_matrix = np.array(l)
