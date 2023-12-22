import sys
sys.path.append('../..')
import re, heapq
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def isSameDir(cur: Node, prev: Node, next: Node):
    if not prev:
        return False
    return cur.left == prev and cur.right == next or\
           cur.right == prev and cur.left == next or\
           cur.up == prev and cur.down == next or\
           cur.down == prev and cur.up == next

def dijkstra(start: Node, destination: Node, ultra: bool):
    init = [(0, None, 0, start, [start])]
    queue = init[:]
    visited = set()

    while queue:
        dist, prev, count, node, path = heapq.heappop(queue)
        if node == destination and (count >= 4 or not ultra):
            return dist, path
        
        if (node, prev, count) in visited:
            continue

        visited.add((node, prev, count))

        for neighbor in node.adj:
            # No backwards, cheater
            if neighbor == prev:
                continue

            sameDir = isSameDir(node, prev, neighbor)
            c = count + 1 if sameDir else 1
            newdist = dist + int(neighbor.type)

            if c <= 10 and (count >= 4 or sameDir or node == start) if ultra else c <= 3:
                p = path[:] + [neighbor]
                heapq.heappush(queue, (newdist, node, c, neighbor, p))
    return float('inf'), None

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map.loadFromFile(file)
    dest = m[m.width - 1, m.height - 1]
    # print(m)

    dist, path = dijkstra(m[0,0], dest, False)
    print(dist)
    # newMap = Map()
    # for i, n in enumerate(path):
    #     Unit(str(i%10), Node(newMap, n.pos, '.'))
    # print(newMap)

# Part 2
with open('example2.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map.loadFromFile(file)
    dest = m[m.width - 1, m.height - 1]

    dist, path = dijkstra(m[0,0], dest, True)
    print(dist)
