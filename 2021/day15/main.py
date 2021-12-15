import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    m = Map.loadFromFile(file)
    print(m.dijkstra(m[(0, 0)], m[m.width - 1, m.height - 1]))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    m = Map.loadFromFile(file)
    m2 = Map.loadFromFile(file)
    w, h = m.width, m.height
    for (xp, yp), n in m.items():
        for x in range(5):
            for y in range(5):
                newVal = int(n.type) + 1 * (x+y)
                while newVal > 9:
                    newVal -= 9
                Node(m2, xp + w * x, yp + h * y, newVal)
    print(m2.dijkstra(m2[(0, 0)], m2[m2.width - 1, m2.height - 1]))
