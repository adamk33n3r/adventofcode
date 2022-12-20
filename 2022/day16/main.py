import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
import heapq
from map import Map, Node
from typing import Tuple
from itertools import permutations

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Valve:
    def __init__(self, name: str, rate: int, tunnels: list[str], idx, closed = True) -> None:
        self.name = name
        self.rate = rate
        self._tunnels = tunnels
        self.tunnels: list[Valve] = []
        self.idx = idx
        self.closed = closed
        self.costs: dict[Valve, int] = {}
    def __repr__(self):
        return '[%s %s]' % (self.name, self.rate)

memoized = {}
def findMostPressure(valves, valve: Valve, valveState, minutes, elephant):
    if minutes == 0:
        return 0 if not elephant else findMostPressure(valves, valves['AA'], valveState, 26, False)
    memkey = (valve, valveState, minutes, elephant)
    if memkey in memoized:
        return memoized[memkey]

    ans = 0
    # If true, try opening this valve
    if valveState[valve.idx] == False and valve.rate > 0:
        # Scores from the next minute on
        valveScore = (minutes - 1) * valve.rate
        ans = max(ans, valveScore + findMostPressure(valves, valve, tuple([(True if i == valve.idx else s) for i,s in enumerate(valveState)]), minutes-1, elephant))
    
    # Try moving to connected valves
    for adj in valve.tunnels:
        ans = max(ans, findMostPressure(valves, adj, valveState, minutes-1, elephant))

    memoized[memkey] = ans
    return ans

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    valves = {}
    for i, line in enumerate(file):
        line = line.strip()
        # print(line)
        valve, rate, tunnels = re.match('Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line).groups()
        rate = int(rate)
        tunnels = tunnels.split(', ')
        # print(valve, rate, tunnels)
        valves[valve] = Valve(valve, rate, tunnels, i)
    
    for valve in valves.values():
        valve.tunnels = [valves[t] for t in valve._tunnels]

    initialValveState = (False,) * len(valves)
    maxFlow = findMostPressure(valves, valves['AA'], initialValveState, 30, False)
    print(maxFlow)


# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]

    valves = {}
    for i, line in enumerate(file):
        line = line.strip()
        valve, rate, tunnels = re.match('Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line).groups()
        rate = int(rate)
        tunnels = tunnels.split(', ')
        valves[valve] = Valve(valve, rate, tunnels, i)
    
    for valve in valves.values():
        valve.tunnels = [valves[t] for t in valve._tunnels]

    initialValveState = (False,) * len(valves)
    maxFlow = findMostPressure(valves, valves['AA'], initialValveState, 26, True)
    print(maxFlow)
