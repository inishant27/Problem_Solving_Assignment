from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
        self.stack = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v):
        self.visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in self.visited:
                self.topological_sort_util(neighbor)
        self.stack.append(v)

    def topological_sort(self):
        keys = list(self.graph.keys())
        for vertex in keys:
            if vertex not in self.visited:
                self.topological_sort_util(vertex)
        return self.stack[::-1]

g = Graph()
print("Enter edges in the format 'u v', or type 'done' to finish:")
while True:
    edge = input().strip()
    if edge == "done":
        break
    u, v = edge.split()
    g.add_edge(u, v)

print("Topological sort order:", g.topological_sort())
