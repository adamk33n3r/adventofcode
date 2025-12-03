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
    m = Map()
    digger = Unit('*', m[0,0])
    for line in file:
        line = line.strip()
        d, n, c = line.split()
        n = int(n)
        for i in range(n):
            if d == 'D':
                digger.node = digger.node.downDefault
            elif d == 'L':
                digger.node = digger.node.leftDefault
            elif d == 'U':
                digger.node = digger.node.upDefault
            elif d == 'R':
                digger.node = digger.node.rightDefault
            digger.node.type = '#'

    # get starting point
    # print(m)
    minNode = m[sorted(m.keys())[0]]
    cur = minNode.downDefault.rightDefault

    Q = deque([cur])
    visited = set()
    while Q:
        node = Q.popleft()
        for neighbor in node.adjDefault:
            if neighbor.type == '#':
                continue
            visited.add(neighbor)
            neighbor.type = '#'
            Q.append(neighbor)

    print(len(m.values()))
    print(len([n for n in m.values() if n.type == '#']))


def area(cmds):
    area = 0
    y = 0
    for cmd in cmds:
        if cmd[0] == 'R':
            area += y*cmd[1]
        elif cmd[0] == 'L':
            area -= y*cmd[1]
        elif cmd[0] == 'U':
            y += cmd[1]
        elif cmd[0] == 'D':
            y -= cmd[1]
        # print(y, area)
    return area

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    cmds = []
    P = 0
    for line in file:
        line = line.strip()
        d, n, c = line.split()

        n = int(c[2:7], 16)
        d = ['R', 'D', 'L', 'U'][int(c[7])]
        cmds.append((d, n))
        P += n
    A = area(cmds)
    print(A + P//2 + 1)

