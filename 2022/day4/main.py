import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def sections(elfRange):
    ranges = [int(num) for num in elfRange.split('-')]
    return list(range(ranges[0], ranges[1]+1))

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    count = 0
    for line in file:
        elf1, elf2 = line.strip().split(',')
        s1 = sections(elf1)
        s2 = sections(elf2)
        bigger = s1 if len(s1) > len(s2) else s2
        smaller = s2 if len(s1) > len(s2) else s1
        if bigger[0] <= smaller[0] and bigger[-1] >= smaller[-1]:
            # is fully contained
            count += 1
    print(count)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    count = 0
    for line in file:
        elf1, elf2 = line.strip().split(',')
        s1 = sections(elf1)
        s2 = sections(elf2)
        bigger = s1 if len(s1) > len(s2) else s2
        smaller = s2 if len(s1) > len(s2) else s1
        # if
        if bigger[0] <= smaller[-1] and bigger[-1] >= smaller[0]:
            # is partially contained
            count += 1
    print(count)
