import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = True
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    total = 0
    for line in file:
        bank = line.strip()
        largest: list[tuple[str, str]] = []
        for x in range(len(bank)-1):
            first = bank[x]
            second = None
            for y in range(x+1, len(bank)):
                if second is None or bank[y] > second:
                    second = bank[y]
            if second is not None:
                largest.append((first, second))
        big = sorted(largest, key=lambda x: int(x[0]), reverse=True)[0]
        total += int(big[0]+big[1])
    print(total)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    total = 0
    for line in file:
        line = line.strip()
        bank = [(b, i) for i, b in enumerate(line)]
        sortedBank = sorted(sorted(bank, key=lambda x: x[1], reverse=True), key=lambda x: x[0], reverse=True)
        print(sortedBank)
        twelve = sortedBank[:12]
        print(twelve)
        print(sortedBank[12:])
        resorted = sorted(twelve, key=lambda x: x[1])

        num = int(''.join([b[0] for b in resorted]))
        print(line)
        print(num)
        total += num


        #not 148533858737820

        # largest: list[tuple[str, str]] = []
        # for x in range(len(bank)-1):
        #     first = bank[x]
        #     second = None
        #     for y in range(x+1, len(bank)):
        #         if second is None or bank[y] > second:
        #             second = bank[y]
        #     if second is not None:
        #         largest.append((first, second))
        # big = sorted(largest, key=lambda x: int(x[0]), reverse=True)[0]
        # total += int(big[0]+big[1])
    print(total)
