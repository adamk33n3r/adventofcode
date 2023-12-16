import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = True
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def snafuToDecimal(snafu):
    i = 0
    dec = 0
    while i < len(snafu):
        n = 0
        place = 5 ** (len(snafu) - i - 1)
        ch = snafu[i]
        if ch == '-':
            n = -1
        elif ch == '=':
            n = -2
        else:
            n = int(ch)
        dec += place * n

        i += 1
    return dec
def decimalToSnafu(dec):
    snafu = ''
    while dec > 0:
        d = [0, 1, 2, -2, -1][s % 5];
        snafu = "012=-"[dec % 5] + snafu;
        dec -= d;

        dec //= 5
    return snafu

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    s = 0
    s2 = 0
    for line in file:
        line = line.strip()
        dec = snafuToDecimal(line)
        s += dec

        t = 0
        for ch in line:
            b = "=-012".index(ch) - 2
            t += 5 * t + b
        # print(dec)
        # print(t)
        s2 += t
    print(s)
    print(s2)
    #2=-1=0
    print(decimalToSnafu(s))
    print(decimalToSnafu(s2))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    for line in file:
        line = line.strip()
