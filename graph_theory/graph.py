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

    def add_edge(self, u: str, v: str, oriented: bool = False, cost: float = 0.0) -> None:
        """
        New edge to the graph.

        Args:
            u: A vertice
            v: A vertice
            oriented: If the edge is oriented or not
        """
        if u not in self.vertices:
            self.vertices.append(u)
        if v not in self.vertices:
            self.vertices.append(v)

        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        # If the edge is oriented, then its only from u to v
        # Else then it both ways
        if oriented:
            self.graph[u].append(v)
        else:
            self.graph[u].append(v)
            self.graph[v].append(u)

        if oriented:
            self.edges["orr"].append((u, v))

            if u not in self.costs:
                self.costs[u] = {}
            self.costs[u][v] = cost
        else:
            self.edges["not_orr"].append((u, v))

            if u not in self.costs:
                self.costs[u] = {}
            if v not in self.costs:
                self.costs[v] = {}
            self.costs[u][v] = cost
            self.costs[v][u] = cost

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
        for v in self.vertices:
            matrix[v] = {}
            for u in self.vertices:
                matrix[v][u] = 0

        # Fill the adjacency matrix with number of connections between the vertices.
        for v in self.graph:
            for u in self.vertices:
                matrix[v][u] = self.graph[v].count(u)

        l = []
        for d in matrix.values():
            l.append([value for value in d.values()])

        self.adjacency_matrix = np.array(l)
