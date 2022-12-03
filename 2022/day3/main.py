import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node
from itertools import islice

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    total = 0
    for line in file:
        line = line.strip()
        first = line[:len(line)//2]
        second = line[len(line)//2:]
        dupe = None
        for item in first:
            if item in second:
                dupe = item
                break
        total += LETTERS.index(dupe) + 1
    print(total)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    total = 0
    while True:
        next3lines = [line.strip() for line in list(islice(file, 3))]
        if not next3lines:
            break
        [e1, e2, e3] = next3lines
        dupe = None
        for item in e1:
            if item in e2 and item in e3:
                dupe = item
                break
        total += LETTERS.index(dupe) + 1
    print(total)
        
