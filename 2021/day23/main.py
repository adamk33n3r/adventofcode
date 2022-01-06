import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node, Unit

USE_EXAMPLE = True
PRINT_DEBUG = False

energy = {'A':1,'B':10,'C':100,'D':1000}

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    m = Map(' ')
    y = 0
    for line in file:
        line = line.rstrip()
        x = 0
        for c in line:
            if c == '#' or c == '.' or c == ' ':
                Node(m, (x, y), c)
            else:
                n = Node(m, (x, y), '.')
                Unit(c, n)
            x += 1
        y += 1
    print(m)
    def process(u: Unit):
        u.node
        pass
    for u in m.units:
        process(u)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    for line in file:
        line = line.strip()
