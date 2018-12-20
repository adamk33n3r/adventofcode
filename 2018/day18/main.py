from collections import defaultdict
import re, time

from map.map import Map as BaseMap
from map.node import Node

USE_EXAMPLE = False
PRINT_DEBUG = False

OPEN = '.'
TREES = '|'
LUMBERYARD = '#'

def process(node):
    if node.type == OPEN:
        if len([node for node in node.adj2 if node.type == TREES]) >= 3:
            # node.type = TREES
            return TREES
    elif node.type == TREES:
        if len([node for node in node.adj2 if node.type == LUMBERYARD]) >= 3:
            # node.type = LUMBERYARD
            return LUMBERYARD
    elif node.type == LUMBERYARD:
        one = len([node for node in node.adj2 if node.type == LUMBERYARD]) >= 1
        two = len([node for node in node.adj2 if node.type == TREES]) >= 1
        if one and two:
            return None
        else:
            # node.type = OPEN
            return OPEN

def calc(m):
    woods = 0
    lumberyards = 0
    for (x, y), node in m.items():
        if node.type == TREES:
            woods += 1
        elif node.type == LUMBERYARD:
            lumberyards += 1
    return woods * lumberyards

with open('example.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
    m = BaseMap()

    y = 0
    for line in f:
        for x, ch in enumerate(line.strip()):
            Node(m, x, y, ch)
        y += 1

    counter = 0
    # print(m)
    # print(0)
    # print()
    # print(len([n for n in m[9, 9].adj2 if n.type == TREES]))
    seen = {}
    ans1 = 0
    while True:
        # Make a copy
        mCopy = BaseMap()
        for (x, y), node in m.items():
            Node(mCopy, x, y, node.type)

        for (x, y), node in mCopy.items():
            res = process(node)
            if res:
                m[(x, y)].type = res

        counter += 1
        if counter == 10:
            ans1 = calc(m)

        key = frozenset([((x, y), node.type) for (x, y), node in m.items()])
        if key in seen:
            t, total = seen[key]
            lengthOfPattern = counter - t
            timeLeft = 1000000000 - t
            pos = timeLeft % lengthOfPattern
            ans2 = list(filter(lambda kv: kv[0] == pos + t, seen.values()))[0][1]
            break
        else:
            seen[key] = (counter, calc(m))

        if PRINT_DEBUG:
            print(m)

    print('P1:', ans1)
    print('P2:', ans2)
