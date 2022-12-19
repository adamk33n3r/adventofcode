import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cmp(a, b):
    # print('left:', a, 'right:', b)
    la, lb = len(a), len(b)
    for i in range(min(la, lb)):
        a1, b1 = a[i], b[i]
        if type(a1) == int and type(b1) == int:
            if a1 > b1:
                return False
            elif a1 < b1:
                return True
        elif type(a1) == list and type(b1) == list:
            res = cmp(a1, b1)
            if res == False:
                return False
            elif res == True:
                return True
        else:
            if type(a1) == list:
                res = cmp(a1, [b1])
                if res == False:
                    return False
                elif res == True:
                    return True
            else:
                res = cmp([a1], b1)
                if res == False:
                    return False
                elif res == True:
                    return True
    if la < lb:
        return True
    elif lb < la:
        return False
    return None

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    groups = file.read().strip().split('\n\n')
    correct = []
    for i, group in enumerate(groups, 1):
        g1, g2 = group.strip().split('\n')
        g1e, g2e = eval(g1), eval(g2)
        # print()
        # print('new:', i)
        # print(g1e, g2e)
        res = cmp(g1e, g2e)
        # print('in order:', res)
        # print()
        if res:
            correct.append(i)
    # print(correct)
    print(sum(correct))

from functools import cmp_to_key
# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    groups = file.read().strip().split('\n\n')
    groups.append('[[2]]\n[[6]]')
    packets = []
    for i, group in enumerate(groups, 1):
        g1, g2 = group.strip().split('\n')
        g1e, g2e = eval(g1), eval(g2)
        packets.append(g1e)
        packets.append(g2e)
    t = 1
    for i, pkt in enumerate(sorted(packets, key=cmp_to_key(lambda a, b: -1 if cmp(a, b) else 1)), 1):
        if pkt == [[2]] or pkt == [[6]]:
            t *= i
    print(t)
