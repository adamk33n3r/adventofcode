import sys
sys.path.append('../..')
import re
from collections import defaultdict
from queue import PriorityQueue

USE_EXAMPLE = False
PRINT_DEBUG = False

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    elves = []
    elfNum = 0
    for line in file:
        line = line.strip()
        if line == '':
            elfNum += 1
        else:
            if len(elves) <= elfNum:
                elves.append(0)
            elves[elfNum] += int(line)
    biggest = float('-inf')
    elfNum = 0
    for i, elf in enumerate(elves):
        if elf > biggest:
            biggest = elf
            elfNum = i
    print(biggest)
        

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    elves = []
    elfNum = 0
    for line in file:
        line = line.strip()
        if line == '':
            elfNum += 1
        else:
            if len(elves) <= elfNum:
                elves.append(0)
            elves[elfNum] += int(line)

    biggest = float('-inf')
    elfNum = 0
    mostest = PriorityQueue()
    for i, elf in enumerate(elves):
        mostest.put((-elf, i))
    print(-mostest.get()[0]+-mostest.get()[0]+-mostest.get()[0])
