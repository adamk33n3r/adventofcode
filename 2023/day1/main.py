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
    acc = 0
    for line in file:
        line = line.strip()
        first, last = None, None
        for c in line:
            if c.isdigit():
                if first is None:
                    first = c
                last = c
        val = int(first + last)
        acc += val
    print(acc)

# Part 2
with open('example2.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    numberWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    acc = 0
    for line in file:
        line = line.strip()
        first, last = None, None
        for idx, c in enumerate(line):
            if c.isdigit():
                # print(c)
                if first is None:
                    first = c
                last = c
                continue
            for jdx, word in enumerate(numberWords, 1):
                # if c == 'n' and word == 'nine':
                #     print(line, idx, c, word, line[idx:idx+len(word)])
                if line[idx:idx+len(word)] == word:
                    # print(word)
                    if first is None:
                        first = str(jdx)
                    last = str(jdx)
                    break
        acc += int(first+last)
    print(acc)

