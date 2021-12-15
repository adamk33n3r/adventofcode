import sys
sys.path.append('../..')
import re
from collections import defaultdict, Counter
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    template = file.readline().strip()
    file.readline() # blank
    rules = {}
    for line in file:
        pair, out = re.match('(\w+) -> (\w+)', line).groups()
        rules[pair] = out
    for step in range(10):
        polymer = ''
        for i in range(len(template) - 1):
            polymer = polymer + template[i] + rules[template[i:i+2]]
        polymer += template[-1]
        template = polymer
    c = Counter(template)
    print(max(c.values()) - min(c.values()))

# Part 2
# I needed a hint for this one, I was reminded of the solution
# for the fish reproduction problem we had previously. We can just
# keep track of the count of polymer pairs.
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    template = file.readline().strip()
    file.readline() # blank
    rules = {}
    for line in file:
        pair, out = re.match('(\w+) -> (\w+)', line).groups()
        rules[pair] = out
    # dictionary comprehension for fun :P
    # rules = {pair: out for pair, out in [re.match('(\w+) -> (\w+)', line).groups() for line in file]}

    pairs = Counter([a+b for a, b in zip(template, template[1:])])
    for step in range(40):
        # memoize attempt was not fruitful....
        # wasn't really an issue of processing, but of storage
        # i = 0
        # while i < len(template) - 1:
        #     next = False
        #     for prev, val in sorted(previous.items(), key=lambda x: len(x[0]), reverse=True):
        #         if template[i:i+len(prev)] == prev:
        #             polymer += val
        #             i += len(prev)
        #             next = True
        #             break
        #     if next:
        #         next = False
        #         continue
        #     polymer = polymer + template[i] + rules[template[i:i+2]]
        #     i += 1
        # polymer += template[-1]
        # previous[template] = polymer

        newPairs = Counter()
        for (a, b), count in pairs.items():
            c = rules[a+b]
            newPairs.update({a+c: count, c+b: count})
        pairs = newPairs
    totals = Counter()
    for (a, b), count in pairs.items():
        totals.update({a: count})
    totals.update(template[-1])
    print(max(totals.values()) - min(totals.values()))
