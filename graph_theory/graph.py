

class Graph():
    """Standard Graph."""

    def __init__(self):
        self.graph = {}
        self.vertices = []
        self.adjacency_matrix = None

    def add_edge(self, u, v, orr=False):
        if u not in self.vertices:
            self.vertices.append(u)
        if v not in self.vertices:
            self.vertices.append(v)

        if not u in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        if orr:
            self.graph[u].append(v)
        else:
            self.graph[u].append(v)
            self.graph[v].append(u)


    def create_adjacency_matrix(self):
        matrix = {}

        for v in self.vertices:
            matrix[str(v)] = {}
            for u in self.vertices:
                matrix[v][u] = 0

        for v in self.graph:
            for u in self.vertices:
                matrix[v][u] = self.graph[v].count(u)
        
        self.adjacency_matrix = matrix

g = Graph()
g.add_edge("a", "b")
g.add_edge("a", "a")
g.add_edge("a", "c")
g.add_edge("b", "c")
g.add_edge("a", "b")

print(g.graph)
print(g.vertices)

a = {
    "a": {"a": 2, "b": 2, "c": 1},
    "b": {"a": 2, "b": 0, "c": 1},
    "c": {"a": 1, "b": 1, "c": 0},
}

g.create_adjacency_matrix()
print(a)
print(g.adjacency_matrix)

#print("  " + " ".join(g.vertices))
    
    #l = Counter(g.graph[vertice])
    #print(l)
#for key in g.graph:
#    print(key)
#print()

