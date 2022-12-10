import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Rope(Unit):
    def __init__(self, type: str, node: Node, length: int = 2):
        super().__init__(type, node)
        self.links = [self] + [Unit(str(i+1), node) for i in range(length-1)]
        self.links[-1].type = 'T'

    def move(self, dir: str, dist: int):
        for _ in range(dist):
            # Move Head
            if dir == 'U':
                self.node = self.node.upDefault
            elif dir == 'D':
                self.node = self.node.downDefault
            elif dir == 'L':
                self.node = self.node.leftDefault
            elif dir == 'R':
                self.node = self.node.rightDefault

            # Move Links
            for i, link in enumerate(self.links):
                if link.type == 'H':
                    continue
                prevLink = self.links[i-1]

                # If this link is already touching the previous link, we don't need to move any more
                if abs(prevLink.node.x - link.node.x) <= 1 and abs(prevLink.node.y - link.node.y) <= 1:
                    break

                moveTo = None
                # Check for diagonal first, but only if we are on different x and y
                if link.node.x != prevLink.node.x and link.node.y != prevLink.node.y:
                    for diag in link.node.diagDefault:
                        if abs(prevLink.node.x - diag.x) <= 1 and abs(prevLink.node.y - diag.y) <= 1:
                            moveTo = diag
                            break
                else:
                    for adj in link.node.adjDefault:
                        if abs(prevLink.node.x - adj.x) <= 1 and abs(prevLink.node.y - adj.y) <= 1:
                            moveTo = adj
                            break

                # Alternate logic
                # if abs(prevLink.node.x - link.node.x) >= 2 and abs(prevLink.node.y - link.node.y) >= 2:
                #     moveTo = self.map[prevLink.node.x - 1 if link.node.x < prevLink.node.x else prevLink.node.x + 1, prevLink.node.y - 1 if link.node.y < prevLink.node.y else prevLink.node.y + 1]
                # elif abs(prevLink.node.x - link.node.x) >= 2:
                #     moveTo = self.map[prevLink.node.x - 1 if link.node.x < prevLink.node.x else prevLink.node.x + 1, prevLink.node.y]
                # else:
                #     moveTo = self.map[prevLink.node.x, prevLink.node.y - 1 if link.node.y < prevLink.node.y else prevLink.node.y + 1]

                # Move link to selected node
                link.node = moveTo

            # Mark the tail node as visited
            self.links[-1].node.type = '#'

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    map = Map()
    head = Rope('H', Node(map, (0, 0), 's'))
    for line in file:
        dir, dist = line.strip().split()
        dist = int(dist)
        head.move(dir, dist)

    print(len(list(filter(lambda t: t == '#' or t == 's',[v.type for v in map.values()]))))


# Part 2
with open('example2.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    map = Map()
    head = Rope('H', Node(map, (0, 0), 's'), 10)
    for line in file:
        dir, dist = line.strip().split()
        dist = int(dist)
        head.move(dir, dist)

    print(len(list(filter(lambda t: t == '#' or t == 's',[v.type for v in map.values()]))))
