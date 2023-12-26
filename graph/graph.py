from .node import Node
from collections import defaultdict

class Graph(defaultdict):
    def __init__(self):
        super().__init__(dict)
    
    def addEdge(self, node1: str, node2: str, weight: int = 1):
        self[node1][node2] = weight
        self[node2][node1] = weight

    def setAllWeights(self, weight):
        for node1 in self.values():
            for node2 in node1.keys():
                node1[node2] = weight
