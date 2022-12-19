import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit
from typing import Tuple

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def findPath(end, path: deque[Tuple[int, Node]]):
    visited = set()
    distance = 0
    while path:
        distance, node = path.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return distance
        for adj in node.adj:
            # print(adj)
            # print(ord(adj.type), ord(node.type))
            # print(ord(adj.type) - ord(node.type))
            if ord(adj.type) - ord(node.type) <= 1:
                # print('moving')
                path.append((distance + 1, adj))
    return -1

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map.loadFromFile(file)
    path = deque()
    START: Node = None
    END: Node = None
    for node in m.values():
        if node.type == 'S':
            START = node
            node.type = 'a'
            path.append((0, node))
        elif node.type == 'E':
            END = node
            node.type = 'z'
    # with some modifications, I can use the dijkstra method on the map
    print(m.dijkstra(START, END, lambda t: 1, lambda nbr, n: ord(nbr.type) - ord(n.type) <= 1))
    print(findPath(END, path))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map.loadFromFile(file)
    path = deque()
    START: Node = None
    END: Node = None
    for node in m.values():
        if node.type == 'S':
            START = node
            node.type = 'a'
        elif node.type == 'E':
            END = node
            node.type = 'z'
        if node.type == 'a':
            path.append((0, node))
    # with some modifications, I can use the dijkstra method on the map
    print(m.dijkstra(
        START,
        END, 
        lambda t: 1,
        lambda nbr, n: ord(nbr.type) - ord(n.type) <= 1,
        list(path)
    ))
    print(findPath(END, path))
