import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

VARS = {
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

def getValue(var):
    return int(var) if any(map(str.isdigit, var)) else VARS[var]

def debug():
    print(VARS)

def process(modelNumber, instructions):
    global VARS
    VARS = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    inputPos = 0
    c = -1
    for cmd, args in instructions:
        if cmd == 'inp':
            c += 1
            print(c, VARS)
            a = args[0]
            VARS[a] = int(modelNumber[inputPos])
            inputPos += 1
        elif cmd == 'add':
            a, b = args
            VARS[a] = getValue(a) + getValue(b)
        elif cmd == 'mul':
            a, b = args
            VARS[a] = getValue(a) * getValue(b)
        elif cmd == 'div':
            a, b = args
            VARS[a] = getValue(a) // getValue(b)
        elif cmd == 'mod':
            a, b = args
            VARS[a] = getValue(a) % getValue(b)
        elif cmd == 'eql':
            a, b = args
            VARS[a] = int(getValue(a) == getValue(b))
        else:
            print('error unknown command')
        # print(cmd, args, VARS)
        if c == 10:
            print(cmd, args, VARS)
    print(c+1, VARS)
    return VARS
# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    instructions = []
    for line in file:
        line = line.strip()
        cmd, *args = line.split()
        instructions.append((cmd, args))
    valid = False
    pos = -1
              # 7 more
               # is 9
                #
                 # 3 more
                  # is 2 less than idx 8
                   # is 1?
                    # one more than previous
                     #
    #   12345678911111
    #            01234
    n = 99999299587349
    # n = 11111291111111
    # 7th is 7 more than 6th, 1,8 or 2,9
    process(str(n), instructions)
    sys.exit()
    while not valid:
        VARS = process(str(n), instructions)
        if VARS['z'] == 0:
            print('valid', n)
            valid = True
        n -= 1
        if len(str(n)) < 14:
            print('too small')
            break
        # for i in range(pos, 0):
        #     if int(n[pos]) > 1:
        #         l = list(n)
        #         l[i] = str(int(n[i]) - 1)
        #         n = ''.join(l)
        #     else:
        #         l = list(n)
        #         l[pos] = '9'
        #         pos -= 1
        #         l[pos] = str(int(n[pos]) - 1)
        #         n = ''.join(l)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    for line in file:
        line = line.strip()
