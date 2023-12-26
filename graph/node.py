from __future__ import annotations

class Node:
    def __init__(self, name: str, graph: Graph):
        self.graph = graph
        self.connections = set()
        self.name = name
        self.graph.add(self)

    def connect(self, node: str) -> "Node":
        n = self.graph.get(node)
        self.connections.add(n)
        n.connections.add(self)
        return n

    def __str__(self) -> str:
        return '({}: [{}])'.format(self.name, ', '.join([n.name for n in self.connections]))
    def __repr__(self) -> str:
        return self.__str__()
