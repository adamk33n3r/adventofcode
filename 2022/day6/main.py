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
    line = file.read().strip()
    for i in range(0, len(line) - 3):
        chrs = []
        for j in line[i:i+4]:
            if j not in chrs:
                chrs.append(j)
            else:
                break
        else:
            print(i+4)
            break

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    line = file.read().strip()
    for i in range(0, len(line) - 13):
        chrs = []
        for j in line[i:i+14]:
            if j not in chrs:
                chrs.append(j)
            else:
                break
        else:
            print(i+14)
            break
