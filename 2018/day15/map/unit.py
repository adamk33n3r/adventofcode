from .map import Map
from .node import Node

class Unit:
    def __init__(self, type: str, node: Node, map: Map):
        self.type = type
        self.node = node
        self.map = map
