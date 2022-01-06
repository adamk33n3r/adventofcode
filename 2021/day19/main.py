import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = True
PRINT_DEBUG = False

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    scanners = []
    for line in file:
        if line.startswith('---'):
            scanners.append([])
            continue
        if line == '\n':
            # endScanner
            continue
        x, y, z = map(int, line.strip().split(','))
        scanners[len(scanners)-1].append((x, y, z))
    print(scanners)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    for line in file:
        line = line.strip()
