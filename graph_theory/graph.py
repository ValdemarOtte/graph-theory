class Graph:
    """Standard Graph."""

    def __init__(self) -> None:
        self.graph: dict = {}
        self.vertices: list = []
        self.adjacency_matrix: dict = {}

    def add_edge(self, u: str, v: str, oriented=False) -> None:
        """
        New edge to the graph.

        Args:
            u: A vertices
            v: A vertices
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

    def create_adjacency_matrix(self) -> None:
        """
        Create the adjacency matrix bases by the edges.
        """
        matrix: dict = {}

        # Create adjacency matrix with all vertices where all values is zero.
        for v in self.vertices:
            matrix[v] = {}
            for u in self.vertices:
                matrix[v][u] = 0

        # Fill the adjacency matrix with number of connections between the vertices.
        for v in self.graph:
            for u in self.vertices:
                matrix[v][u] = self.graph[v].count(u)

        self.adjacency_matrix = matrix
