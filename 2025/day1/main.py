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
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    val = 50
    times = 0
    for line in file:
        line = line.strip()
        d = -1 if line[0] == 'L' else 1
        n = int(line[1:])
        val = (val + (d * n)) % 100
        if val == 0:
            times += 1
    print(times)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    val = 50
    times = 0
    for line in file:
        line = line.strip()
        d = -1 if line[0] == 'L' else 1
        n = int(line[1:])
        amt = d * n
        prevVal = val
        val = (val + amt) % 100
        add = abs(amt) // 100
        # print(f'prev: {prevVal} amt: {amt} val: {val}')
        if add > 0:
            times += add
        # Remove the extra 100s
        if amt >= 100:
            amt %= 100
        elif amt <= -100:
            amt %= -100
        if val == 0 or (prevVal != 0 and (((prevVal + amt) > 100) or ((prevVal + amt) < 0))):
            times += 1
    print(times)
