import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map.loadFromFile(file)
    count = 0
    for y in range(m.height):
        for x in range(m.width):
            node = m[x, y]
            if node.type == '.':
                continue
            if len(list(filter(lambda x: x.type == '@', node.adj2))) < 4:
                count += 1
    print(count)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map.loadFromFile(file)
    prevCount = -1
    count = 0
    while prevCount != count:
        prevCount = count
        for y in range(m.height):
            for x in range(m.width):
                node = m[x, y]
                if node.type == '.':
                    continue
                if len(list(filter(lambda x: x.type == '@', node.adj2))) < 4:
                    node.type = '.'
                    count += 1
    print(count)
