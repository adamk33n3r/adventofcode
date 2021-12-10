import re
from collections import defaultdict

from map.node import Node as BaseNode
from map.map import Map as BaseMap

USE_EXAMPLE = False
PRINT_DEBUG = False

class Node(BaseNode):
    def __init__(self, map, x: int, y: int, type: str):
        super().__init__(map, x, y, type)

class Map(BaseMap):
    def lowPoints(self):
        lows = []
        for _, node in self.items():
            if all([int(node.type) < int(n.type) for n in node.adj]):
                lows.append(node)
        return lows

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    m = Map()
    y = 0
    for line in file:
        x = 0
        line = line.strip()
        for d in line:
            Node(m, x, y, d)
            x += 1
        y += 1
    # print(sum([1 + int(low.type) for low in m.lowPoints()]))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    m = Map()
    y = 0
    for line in file:
        x = 0
        line = line.strip()
        for d in line:
            Node(m, x, y, d)
            x += 1
        y += 1

    def scan(node, basin):
        if node.type == '9':
            return
        if node not in basin:
            basin.append(node)
        for adj in node.adj:
            if adj in basin:
                continue
            scan(adj, basin)
        return basin

    total = 1
    for m in sorted([len(scan(low, [])) for low in m.lowPoints()], reverse=True)[:3]:
        total *= m
    print(total)
