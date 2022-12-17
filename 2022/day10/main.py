import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    X = 1
    cycles = 1
    total = 0
    for line in file:
        line = line.strip()
        if line == 'noop':
            cycles += 1
            if (cycles - 20) % 40 == 0:
                total += cycles * X
            continue
        cmd, arg = line.split()
        if cmd == 'addx':
            for i in range(2):
                cycles += 1
                if i == 1:
                    X += int(arg)
                if (cycles - 20) % 40 == 0:
                    total += cycles * X
    print(total)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    X = 1
    cycles = 0
    lines = [l.split() for l in file.readlines()]
    pc = 0
    op = 0
    screen = ''
    while pc < len(lines):
        if cycles > 0 and cycles % 40 == 0:
            cycles -= 40
            screen += '\n'
        rng = list(range(X - 1, X + 2))
        if cycles in rng:
            # draw
            screen += '#'
        else:
            screen += ' '

        line = lines[pc]
        if line[0] == 'noop':
            pc += 1
        else:
            cmd, arg = line
            if cmd == 'addx':
                op += 1
                if op == 2:
                    op = 0
                    pc += 1
                    X += int(arg)
        cycles += 1
    print(screen)
    print('EHPZPJGL')
