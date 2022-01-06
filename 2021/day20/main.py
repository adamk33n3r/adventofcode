import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = True
PRINT_DEBUG = False

def runAlgo(m: Map, algo: str, unknown: str):
    newMap = Map()
    # precalculate the x range so it's not using the new stuff
    xRange = range(m.minX-1, m.maxX + 2)
    for y in range(m.minY-1, m.maxY + 2):
        for x in xRange:
            str = ''
            for y2 in [-1, 0, 1]:
                for x2 in [-1, 0, 1]:
                    n2 = m.get((x + x2, y + y2, 0), None)
                    if n2:
                        str += n2.type
                    else:
                        str += unknown
            str = '0b' + str.replace('.', '0').replace('#', '1')
            new = algo[int(str, 2)]
            Node(newMap, (x, y), new)
    return newMap

import time
def runAlgoNTimes(m, algo, times):
    for i in range(times):
        # if idx 0 is '.' then "the infinite" will always be dark
        if algo[0] == '.':
            m = runAlgo(m, algo, '.')
        # otherwise, it will toggle between lit and not lit every iteration
        else:
            m = runAlgo(m, algo, algo[len(algo)-1] if i % 2 == 0 else algo[0])
        time.sleep(0.5)
        print(m)
    return m

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    algo = file.readline().strip()
    file.readline()
    m = Map()
    y = 0
    for line in file:
        x = 0
        line = line.strip()
        for c in line:
            Node(m, (x, y), c)
            x += 1
        y += 1

    m = runAlgoNTimes(m, algo, 2)
    print(sum([1 if n.type == '#' else 0 for n in m.values()]))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    algo = file.readline().strip()
    file.readline()
    m = Map()
    y = 0
    for line in file:
        x = 0
        line = line.strip()
        for c in line:
            Node(m, (x, y), c)
            x += 1
        y += 1

    m = runAlgoNTimes(m, algo, 50)
    print(sum([1 if n.type == '#' else 0 for n in m.values()]))
    print(m)
