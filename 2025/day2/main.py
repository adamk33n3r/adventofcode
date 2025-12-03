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
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    patterns: set[str] = set()
    for line in file:
        productRanges = line.strip().split(',')
        for productRange in productRanges:
            productRange = productRange.split('-')
            start = int(productRange[0])
            end = int(productRange[1])
            for i in range(start, end + 1):
                stri = str(i)
                if len(stri) % 2 == 0:
                    isPattern = stri[:len(stri)//2] == stri[len(stri)//2:]
                    if isPattern:
                        patterns.add(stri)
    # print(sorted(int(p) for p in patterns))
    print(sum(int(p) for p in patterns))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]

    patterns: set[str] = set()
    for line in file:
        productRanges = line.strip().split(',')
        for productRange in productRanges:
            productRange = productRange.split('-')
            start = int(productRange[0])
            end = int(productRange[1])
            for i in range(start, end + 1):
                stri = str(i)
                maxPatternLen = len(stri) // 2
                for pl in range(1, maxPatternLen + 1):
                    # checks that pattern length will fill the whole string
                    if len(stri) % pl != 0:
                        continue
                    test = True
                    tmp = stri
                    times = len(stri) // pl
                    first = tmp[:pl]
                    tmp = tmp[pl:]
                    for t in range(times-1):
                        if first != tmp[:pl]:
                            test = False
                            break
                        tmp = tmp[pl:]
                    if test:
                        patterns.add(stri)
                        break

    # print(sorted(int(p) for p in patterns))
    print(sum(int(p) for p in patterns))
