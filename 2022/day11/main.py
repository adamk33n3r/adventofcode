import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    monkeys = []
    while file:
        line = file.readline().strip()
        if not line:
            break
        startingItems = list(map(int, file.readline().strip()[len('Starting items: '):].split(', ')))
        op, arg = re.match('(.) (\d+|old)', file.readline().strip()[len('Operation: new = old '):]).groups()
        test = int(file.readline().strip()[len('Test: divisible by '):])
        t = int(file.readline().strip()[len('If true: throw to monkey '):])
        f = int(file.readline().strip()[len('If false: throw to monkey '):])
        file.readline()

        monkeys.append({
            'items': startingItems,
            'op': op,
            'arg': arg,
            'test': test,
            't': t,
            'f': f,
        })

    def printMonkeys():
        for i, monkey in enumerate(monkeys):
            print(i, monkey['items'])

    rounds = 20
    inspections = [0] * 20
    for i in range(rounds):
        for im, monkey in enumerate(monkeys):
            for item in monkey['items']:
                inspections[im] += 1
                if monkey['arg'] == 'old':
                    arg = item
                else:
                    arg = int(monkey['arg'])
                if monkey['op'] == '*':
                    item *= arg
                else:
                    item += arg
                item //= 3
                if item / monkey['test'] == item // monkey['test']:
                    monkeys[monkey['t']]['items'].append(item)
                else:
                    monkeys[monkey['f']]['items'].append(item)
            monkey['items'] = []
    topTwo = sorted(inspections)[-2:]
    print(topTwo[0] * topTwo[1])

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    monkeys = []
    while file:
        line = file.readline().strip()
        if not line:
            break
        startingItems = list(map(int, file.readline().strip()[len('Starting items: '):].split(', ')))
        op, arg = re.match('(.) (\d+|old)', file.readline().strip()[len('Operation: new = old '):]).groups()
        test = int(file.readline().strip()[len('Test: divisible by '):])
        t = int(file.readline().strip()[len('If true: throw to monkey '):])
        f = int(file.readline().strip()[len('If false: throw to monkey '):])
        file.readline()

        monkeys.append({
            'items': startingItems,
            'op': op,
            'arg': arg,
            'test': test,
            't': t,
            'f': f,
        })

    def printMonkeys():
        for i, monkey in enumerate(monkeys):
            print(i, monkey['items'])

    from functools import reduce
    LCM = reduce(lambda a, b: a*b, [monkey['test'] for monkey in monkeys], 1)

    rounds = 10000
    inspections = [0] * 20
    for i in range(rounds):
        for im, monkey in enumerate(monkeys):
            for item in monkey['items']:
                inspections[im] += 1
                if monkey['arg'] == 'old':
                    arg = item
                else:
                    arg = int(monkey['arg'])
                if monkey['op'] == '*':
                    item *= arg
                else:
                    item += arg
                item %= LCM
                if item % monkey['test'] == 0:
                    monkeys[monkey['t']]['items'].append(item)
                else:
                    monkeys[monkey['f']]['items'].append(item)
            monkey['items'] = []
    topTwo = sorted(inspections)[-2:]
    print(topTwo[0] * topTwo[1])
