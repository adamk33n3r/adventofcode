import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

right = {'>':'v', 'v':'<', '<':'^', '^':'>'}
left = {'>':'^', '^':'<', '<':'v', 'v':'>'}
# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map(' ')
    board, path = file.read().split('\n\n')
    START = None
    for y, line in enumerate(board.split('\n')):
        for x, tile in enumerate(line):
            n = Node(m, (x, y), tile)
            if START is None and tile == '.':
                START = n
    path = path.strip()

    steps = []
    i = 0
    while i < len(path):
        if path[i].isalpha():
            steps.append(path[i])
            i += 1
            continue
        num = ''
        while path[i].isdigit():
            num += path[i]
            i += 1
            if i >= len(path):
                break
        num = int(num)
        steps.append(num)

    facing = '>'
    me = Unit('$', START)
    for stepNum, step in enumerate(steps):
        # print(stepNum, step)
        # print('facing:', facing)
        # print(m)
        # print()
        # input(':> ')
        if type(step) == int:
            for _ in range(step):
                nextNode = None
                if facing == '>':
                    nextNode = me.node.right
                elif facing == '<':
                    nextNode = me.node.left
                elif facing == '^':
                    nextNode = me.node.up
                elif facing == 'v':
                    nextNode = me.node.down
                # WRAP
                if nextNode is None or nextNode.type == ' ':
                    d = 1
                    upDown = True
                    if facing == '>':
                        upDown = False
                        x = m.minX
                        y = me.node.y
                    elif facing == '<':
                        upDown = False
                        d = -1
                        x = m.maxX
                        y = me.node.y
                    elif facing == '^':
                        d = -1
                        x = me.node.x
                        y = m.maxY
                    elif facing == 'v':
                        x = me.node.x
                        y = m.minY
                    while nextNode is None or nextNode.type == ' ':
                        nextNode = m.get((x, y, 0))
                        if upDown:
                            y += d
                        else:
                            x += d
                        # print('x,y:', (x, y), nextNode)
                        # input('%= ')
                if nextNode.type == '#':
                    # is wall
                    break
                me.node.type = facing
                me.node = nextNode
        else:
            if step == 'R':
                facing = right[facing]
            else:
                facing = left[facing]
    # print(m)
    print(sum([(me.node.y+1)*1000,(me.node.x+1)*4, {'>':0,'v':1,'<':2,'^':3}[facing]]))


# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    for line in file:
        line = line.strip()
