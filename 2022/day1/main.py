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
    print(max(elves))
        

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

    print(sum(sorted(elves)[-3:]))

    mostest = PriorityQueue()
    for elf in elves:
        mostest.put(-elf)
    print(-mostest.get()+-mostest.get()+-mostest.get())
