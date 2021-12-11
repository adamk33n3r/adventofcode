import re
from collections import defaultdict, deque

USE_EXAMPLE = False
PRINT_DEBUG = False

openChars = '([{<'
closeChars = ')]}>'
scores = [3, 57, 1197, 25137]

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    total = 0
    for line in file:
        line = line.strip()
        if PRINT_DEBUG:
            print(line)
        openStack = deque()
        for c in line:
            if c in openChars:
                openStack.append(c)
                if PRINT_DEBUG:
                    print('open', c)
            elif c in closeChars:
                if PRINT_DEBUG:
                    print('close', c)
                openChar = openStack.pop()
                idx = closeChars.index(c)
                if openChars[idx] == openChar:
                    print('matched', c, openChar) if PRINT_DEBUG else None
                else:
                    if PRINT_DEBUG:
                        print('not matched', c, openChar)
                    total += scores[idx]
                    break
    print(total)

scores = [1, 2, 3, 4]

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    lineScores = []
    for line in file:
        line = line.strip()
        if PRINT_DEBUG:
            print(line)
        openStack = deque()
        isCorrupt = False
        for c in line:
            if c in openChars:
                openStack.append(c)
                if PRINT_DEBUG:
                    print('open', c)
            elif c in closeChars:
                if PRINT_DEBUG:
                    print('close', c)
                openChar = openStack.pop()
                idx = closeChars.index(c)
                if openChars[idx] == openChar:
                    print('matched', c, openChar) if PRINT_DEBUG else None
                else:
                    if PRINT_DEBUG:
                        print('not matched', c, openChar)
                    total += scores[idx]
                    isCorrupt = True
                    break
        if isCorrupt:
            continue
        if len(openStack) > 0:
            if PRINT_DEBUG:
                print('fixing line', openStack)
            openStack.reverse()
            total = 0
            for c in openStack:
                total *= 5
                total += scores[openChars.index(c)]
            lineScores.append(total)

    lineScores.sort()
    print(lineScores[len(lineScores) // 2])
