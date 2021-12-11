import re
from map.map import Map
from map.node import Node
from collections import defaultdict

USE_EXAMPLE = False
PRINT_DEBUG = False

def flash(octo, flashed):
    if octo.type > 9:
        flashed.append(octo)
        octo.type = 0
        for adj in octo.adj2:
            if adj in flashed:
                continue
            adj.type += 1
            flash(adj, flashed)

def step(map):
    # increment each level by 1
    for octo in map.values():
        octo.type += + 1
    
    flashed = []
    # check for flashes
    for octo in map.values():
        flash(octo, flashed)
    return len(flashed)

def buildMap():
    m = Map()
    y = 0
    for line in file:
        line = line.strip()
        x = 0
        for octo in line:
            Node(m, x, y, int(octo))
            x += 1
        y += 1
    return m

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    m = buildMap()
    t = sum([step(m) for i in range(100)])
    print(t)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    m = buildMap()
    flashed = 0
    idx = 0
    while flashed != (10 * 10):
        flashed = step(m)
        idx += 1
    print(idx)
