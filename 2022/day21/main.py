import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Monkey:
    def __init__(self, name, shout: str) -> None:
        self.name = name
        self.me = False
        self.number = None
        if shout.isdigit():
            self.number = int(shout)
        else:
            # print(shout)
            m1, op, m2 = shout.split(' ')
            self.monkey1 = m1
            self.op = op
            self.monkey2 = m2
    def getNumber(self, monkeys: dict[str, 'Monkey']):
        if self.number is not None:
            return self.number
        n1 = monkeys[self.monkey1].getNumber(monkeys)
        n2 = monkeys[self.monkey2].getNumber(monkeys)
        # if self.name == 'root':
        #     print(n1, n2)
        return eval('%d %s %d' %(n1, self.op, n2))

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    monkeys = {}
    for line in file:
        line = line.strip()
        name, shout = line.split(': ')
        monkeys[name] = Monkey(name, shout)
    ans = monkeys['root'].getNumber(monkeys)
    print(ans)


# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    monkeys = {}
    for line in file:
        line = line.strip()
        name, shout = line.split(': ')
        monkeys[name] = Monkey(name, shout)
    monkeys['root'].op = ','
    n = 3429411069020
    monkeys['humn'].me = True
    monkeys['humn'].number = n
    target = 23622695042414
    prev = None
    left, right = monkeys['root'].getNumber(monkeys)
    while left != right:
        n += 1
        # print(n)
        monkeys['humn'].number = n
        if n == 4:
            break
        left, right = monkeys['root'].getNumber(monkeys)
        if prev is not None:
            # print('cmp:', prev - left)
            if prev > target and left <= target:
                print('passed at:', n)
                break
        prev = left
    print(n)
