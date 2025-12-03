from .map import Map
from .node import Node

class Unit:
    def __init__(self, type: str, node: Node):
        self.type = type
        self.node = node
        self.map = node.map
        self.map.units.append(self)

    def __str__(self):
        return '({}, {}): {}'.format(self.node.x, self.node.y, self.type)
    def __repr__(self):
        return self.__str__()
