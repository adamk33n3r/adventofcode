import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    m = Map('.')
    folds = []
    for line in file:
        line = line.strip()
        if line == "":
            break
        x, y = line.split(',')
        Node(m, x, y, '#')
    for line in file:
        match = re.match('fold along ([xy])=(\d+)', line)
        folds.append(match.groups())

    firstFold = True
    for fold in folds:
        val = int(fold[1])
        if fold[0] == 'y':
            for y in range(m.maxY, val, -1):
                for x in range(m.minX, m.maxX + 1):
                    n = m.get((x, y))
                    if not n:
                        continue
                    m[(x, y - (y - val) * 2)] = n
            for y in range(val, m.maxY + 1):
                for x in range(m.minX, m.maxX + 1):
                    if (x, y) in m:
                        del m[(x, y)]
        elif fold[0] == 'x':
            for x in range(m.maxX, val, -1):
                for y in range(m.minY, m.maxY + 1):
                    n = m.get((x, y))
                    if not n:
                        continue
                    m[(x - (x - val) * 2, y)] = n
            for x in range(val, m.maxX + 1):
                for y in range(m.minY, m.maxY + 1):
                    if (x, y) in m:
                        del m[(x, y)]
        # Could prevent having to do this because it's always folding in half.
        # So you could keep track of the previous fold value and use that as
        # your max and then divide it in half to use on the next iteration.
        # But it's not that slow to do this and it makes printing it out easy.
        m.trim()
        if firstFold:
            # Part 1
            print(len(m.values()))
            firstFold = False
    # Part 2
    m.print(' ')
