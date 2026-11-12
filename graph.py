class UndirectedGraph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, source: str, target: str, weight: float):

        if source not in self.adj:
            self.adj[source] = []

        if target not in self.adj:
            self.adj[target] = []

        self.adj[source].append((target, weight))
        self.adj[target].append((source, weight))

    def get_nodes(self):
            return list(self.adj.keys())

class DirectedGraph:

    def __inint__(self):
        self.adj = {}

    def add_edge(self, source: str, target: str, weight: float):
        if source not in self.adj:
            self.adj[source] = []

        if target not in self.adj:
            self.adj[target] = []

        self.adj[source].append((target, weight))

    def get_nodes(self):
        return list(self.adj.keys())
