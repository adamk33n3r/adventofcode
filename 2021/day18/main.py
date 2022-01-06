import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node
import json

USE_EXAMPLE = True
PRINT_DEBUG = False

def process(data):
    if type(data) == list:
        if type(data[0]) == list:
            process(data[0]) + process(data[1])
    return data

def explode(number):
    pass

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    for line in file:
        line = line.strip()
        # data = json.loads(line)
        # process(data)
        stack = deque()
        pos = 0
        while pos < len(line):
            c = line[pos]
            if len(stack) == 4:
                pos += 1
                nextClose = line[pos:].index(']')
                explodeNumber = line[pos:pos+nextClose]
                print(explodeNumber)

            if c == '[':
                stack.append(c)

            pos += 1

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    for line in file:
        line = line.strip()
