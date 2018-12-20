from collections import defaultdict, deque
from typing import Dict, Tuple, List

from map.node import Node as BaseNode
from map.map import Map

WALL = '#'
FLOOR = '.'
VERT_DOOR = '|'
HORIZ_DOOR = '-'

USE_EXAMPLE = False
PRINT_DEBUG = False

class Node(BaseNode):
    def __init__(self, map, x: int, y: int, type: str):
        super().__init__(map, x, y, type)
        self.dist = 0

with open('example.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
    m = Map()
    path = f.readline().strip()

    currentNode = Node(m, 0, 0, 'X')
    parentNode = currentNode
    stack = []
    for ch in path:
        if ch in 'NSEW':
            dx, dy = { 'E': (2, 0), 'W': (-2, 0), 'N': (0, -2), 'S': (0, 2) }[ch]
            prevX, prevY, dist = currentNode.x, currentNode.y, currentNode.dist
            dist += 1
            x, y = (prevX + dx, prevY + dy)

            Node(m, prevX + dx // 2, prevY + dy // 2, VERT_DOOR if dy == 0 else HORIZ_DOOR)
            Node(m, prevX + dx // 2 - (1 if dx == 0 else 0), prevY + dy // 2 - (1 if dy == 0 else 0), WALL)
            Node(m, prevX + dx // 2 + (1 if dx == 0 else 0), prevY + dy // 2 + (1 if dy == 0 else 0), WALL)

            n = None
            if (x, y) not in m:
                n = Node(m, x, y, FLOOR)
                n.dist = dist
            else:
                n = m[(x, y)]
                if dist < n.dist:
                    n.dist = dist
            currentNode = n
        elif ch == '(':
            stack.append(parentNode)
            parentNode = currentNode
        elif ch == '|':
            currentNode = parentNode
        elif ch == ')':
            parentNode = stack.pop()

    # maxNode = max([n for n in m.values() if n.type == FLOOR], key=lambda n: n.dist)
    maxNode = max(filter(lambda n: n.type == FLOOR, m.values()), key=lambda n: n.dist)
    print('P1:', maxNode.dist)
    maxNodes = [n for n in m.values() if n.type == FLOOR and n.dist >= 1000]
    print('P2:', len(maxNodes))

    if PRINT_DEBUG:
        print(m)
