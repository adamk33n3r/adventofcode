import re
from itertools import zip_longest
from collections import defaultdict

USE_EXAMPLE = False
PRINT_DEBUG = False

# Original p1 solution
map = {}
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    for line in file:
        x1, y1, x2, y2 = [int(x) for x in re.match('(\d+),(\d+) -> (\d+),(\d+)', line).groups()]
        # Dont consider diagonals
        if x1 != x2 and y1 != y2:
            continue
        # I think this part just happened to work
        # The real solution for this situation is in part 2
        if x2 - x1 < 0:
            t = x1
            x1 = x2
            x2 = t
        if y2 - y1 < 0:
            t = y1
            y1 = y2
            y2 = t
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x not in map:
                    map[x] = defaultdict(int)
                row = map[x]
                if y not in row:
                    row[y] = 0
                row[y] += 1
    count = 0
    for x, row in map.items():
        for y, val in row.items():
            if val >= 2:
                count += 1
    print(count)

def func(ignoreDiagonals):
    map = {}
    with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
        for line in file:
            x1, y1, x2, y2 = [int(x) for x in re.match('(\d+),(\d+) -> (\d+),(\d+)', line).groups()]
            if ignoreDiagonals and x1 != x2 and y1 != y2:
                continue
            if x2 - x1 < 0:
                xlist = list(range(x1, x2 - 1, -1))
            else:
                xlist = list(range(x1, x2 + 1))
            if y2 - y1 < 0:
                ylist = list(range(y1, y2 - 1, -1))
            else:
                ylist = list(range(y1, y2 + 1))
            if len(xlist) == 1:
                fill = x1
            elif len(ylist) == 1:
                fill = y1
            for x, y in zip_longest(xlist, ylist, fillvalue=fill):
                if x not in map:
                    map[x] = defaultdict(int)
                map[x][y] += 1
        count = 0
        for x, row in map.items():
            for y, val in row.items():
                if val >= 2:
                    count += 1
        if USE_EXAMPLE:
            for y in range(10):
                rowstr = ''
                for x in range(10):
                    val = map[x][y]
                    rowstr += str(val) if val > 0 else '.'
                print(rowstr)
        print(count)

func(True)
func(False)
