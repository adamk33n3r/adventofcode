import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map()
    for line in file:
        line = line.strip()
        rockPath = [list(map(int, g.split(','))) for g in line.split(' -> ')]
        for i in range(len(rockPath) - 1):
            (x1, y1), (x2, y2) = rockPath[i:i+2]
            pos1, pos2 = rockPath[i:i+2]
            diff = (pos2[0] - pos1[0], pos2[1] - pos1[1])
            cs = 1 if diff[0] >= 0 else -1
            rs = 1 if diff[1] >= 0 else -1
            for c in range(0, diff[0] + cs, cs):
                for r in range(0, diff[1] + rs, rs):
                    Node(m, (x1 + c, y1 + r), '#')
    SAND = Node(m, (500, 0), '+')
    AIR = '.'
    restCount = 0
    while True:
        newSand = Unit('o', SAND)
        void = False
        while True:
            if newSand.node.pos[1] >= m.maxY:
                void = True
                break
            if newSand.node.downDefault.type == AIR:
                newSand.node = newSand.node.downDefault
            elif newSand.node.leftDownDefault.type == AIR:
                newSand.node = newSand.node.leftDownDefault
            elif newSand.node.rightDownDefault.type == AIR:
                newSand.node = newSand.node.rightDownDefault
            else:
                restCount += 1
                newSand.node.type = 'S'
                break
        if void:
            break
    print(m)
    print(restCount)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map()
    for line in file:
        line = line.strip()
        rockPath = [list(map(int, g.split(','))) for g in line.split(' -> ')]
        for i in range(len(rockPath) - 1):
            (x1, y1), (x2, y2) = rockPath[i:i+2]
            pos1, pos2 = rockPath[i:i+2]
            diff = (pos2[0] - pos1[0], pos2[1] - pos1[1])
            cs = 1 if diff[0] >= 0 else -1
            rs = 1 if diff[1] >= 0 else -1
            for c in range(0, diff[0] + cs, cs):
                for r in range(0, diff[1] + rs, rs):
                    Node(m, (x1 + c, y1 + r), '#')
    SAND = Node(m, (500, 0), '+')
    AIR = '.'
    restCount = 0
    FLOOR = 2 + m.maxY
    while True:
        newSand = Unit('o', SAND)
        void = False
        while True:
            if newSand.node.pos[1] == FLOOR - 1:
                restCount += 1
                newSand.node.type = 'S'
                break
            if newSand.node.downDefault.type == AIR:
                newSand.node = newSand.node.downDefault
            elif newSand.node.leftDownDefault.type == AIR:
                newSand.node = newSand.node.leftDownDefault
            elif newSand.node.rightDownDefault.type == AIR:
                newSand.node = newSand.node.rightDownDefault
            else:
                restCount += 1
                newSand.node.type = 'S'
                break
        if SAND.type == 'S':
            break
    print(restCount)
