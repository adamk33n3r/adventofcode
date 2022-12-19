import heapq
from collections import defaultdict
from typing import Callable

from .node import Node

class Map(dict):
    @staticmethod
    def loadFromFile(file, default = '.'):
        m = Map()
        y = 0
        for line in file:
            x = 0
            for v in line.strip():
                Node(m, (x, y), v)
                x += 1
            y += 1
        return m

    def __init__(self, default = '.'):
        super().__init__()
        self.default = default
        # print('in map init')
        self.units = []
        # print('setting units to empty')
        # print(units)
        self.minX = 0
        self.minY = 0
        self.maxX = 0
        self.maxY = 0
        self.minZ = 0
        self.maxZ = 0

    def unitAt(self, node):
        l = [unit for unit in self.units if unit.node == node]
        return l[0] if l else None

    @property
    def width(self):
        return self.maxX - self.minX + 1
    @property
    def height(self):
        return self.maxY - self.minY + 1
    @property
    def depth(self):
        return self.maxZ - self.minZ + 1
    
    # @property
    # def minX(self):
    #     return min(self.keys(), key=lambda kv: kv[0])[0]
    # @property
    # def minY(self):
    #     return min(self.keys(), key=lambda kv: kv[1])[1]
    # @property
    # def maxX(self):
    #     return max(self.keys(), key=lambda kv: kv[0])[0]
    # @property
    # def maxY(self):
    #     return max(self.keys(), key=lambda kv: kv[1])[1]

    def row(self, row: int, slc: slice = None):
        if slc is None:
            slc = slice(None)
        return [self[x, row] for x in range(*slc.indices(self.width))]

    def col(self, col: int, slc: slice = None):
        if slc is None:
            slc = slice(None)
        return [self[col, y] for y in range(*slc.indices(self.height))]


    def dijkstra(self, start: Node, destination: Node, typeTransform: Callable = None, condition: Callable = None, init = None):
        if init is None:
            init = [(0, start)]
        queue = init[:]
        mindist = defaultdict(lambda: float('inf'), { n: 0 for n in init })
        visited = set()

        while queue:
            dist, node = heapq.heappop(queue)
            if node == destination:
                return dist
            
            if node in visited:
                continue

            visited.add(node)

            for neighbor in node.adj:
                newdist = dist + (int(neighbor.type) if typeTransform is None else typeTransform(neighbor.type))

                if condition and condition(neighbor, node) or not condition and newdist < mindist[neighbor]:
                    mindist[neighbor] = newdist
                    heapq.heappush(queue, (newdist, neighbor))
        return float('inf')

    def trim(self):
        minX = self.minX
        minY = self.minY
        minZ = self.minZ
        maxX = self.maxX
        maxY = self.maxY
        maxZ = self.maxZ
        self.minX = float('inf')
        self.minY = float('inf')
        self.minZ = float('inf')
        self.maxX = -float('inf')
        self.maxY = -float('inf')
        self.maxZ = -float('inf')
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                for z in range(minZ, maxZ + 1):
                    node = self.get((x, y, z))
                    if node and node.type != self.default:
                        self.__setbounds((x, y, z))

    def print(self, empty = None):
        tmp = self.default
        if empty is not None:
            self.default = empty
        print(self)
        if tmp:
            self.default = tmp

    def __setbounds(self, key):
        if key[0] < self.minX:
            self.minX = key[0]
        if key[0] > self.maxX:
            self.maxX = key[0]
        if key[1] < self.minY:
            self.minY = key[1]
        if key[1] > self.maxY:
            self.maxY = key[1]
        if key[2] < self.minZ:
            self.minZ = key[2]
        if key[2] > self.maxZ:
            self.maxZ = key[2]

    def __getitem__(self, key):
        if len(key) < 3:
            key += (0,)
        # I think we need to change map to be a multi dimensional list rather
        # than a dict to support slices...
        # if isinstance(key[0], slice):
        #     # print(key)
        #     xSlice = key[0].indices(self.width)
        #     print(xSlice)
        #     for x in range(*xSlice):
        #         print(x)
        #     ySlice = key[1].indices(self.height)
        #     # zSlice = key[3].indices(self.height)
        if key in self:
            return super().__getitem__(key)
        return Node(self, key, self.default)
    
    def __setitem__(self, key, val) -> None:
        self.__setbounds(key)
        return super().__setitem__(key, val)

    def toString(self, z = 0):
        self.trim()
        ret = ''
        for y in range(self.minY, self.maxY + 1):
            for x in range(self.minX, self.maxX + 1):
                node = self.get((x, y, z))
                if x == self.minX:
                    ret += '\n'

                unitNodes = {u.node: u for u in self.units}

                if node in unitNodes:
                    ret += str(unitNodes[node].type)
                else:
                    ret += str(node.type) if node else self.default

        return ret[1:]

    def __str__(self):
        return self.toString()
        # for (x, _), node in sorted(self.items(), lambda kv: kv[1]):
        #     if x == 0:
        #         ret += '\n'

        #     unitNodes = {u.node: u for u in self.units}

        #     if node in unitNodes:
        #         ret += unitNodes[node].type
        #     else:
        #         ret += node.type

        # return ret[1:]
