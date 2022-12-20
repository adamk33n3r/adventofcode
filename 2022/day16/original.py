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
    def __init__(self, name: str, rate: int, tunnels: list[str], closed = True) -> None:
        self.name = name
        self.rate = rate
        self._tunnels = tunnels
        self.tunnels: list[Valve] = []
        self.closed = closed
        self.costs: dict[Valve, int] = {}
    def __repr__(self):
        return '[%s %s]' % (self.name, self.rate)

class Graph:
    def __init__(self) -> None:
        self.valves = {}

def dijsktra(start: Valve, dest: Valve):
    queue = deque([(0, start)])
    mindist = defaultdict(lambda: float('inf'), { start: 0 })
    visited = set()

    while queue:
        # dist, node = heapq.heappop(queue)
        dist, node = queue.popleft()
        if node == dest:
            return dist
        
        if node in visited:
            continue

        visited.add(node)

        for neighbor in node.tunnels:
            newdist = dist + 1

            if newdist < mindist[neighbor]:
                mindist[neighbor] = newdist
                # heapq.heappush(queue, (newdist, neighbor))
                queue.append((newdist, neighbor))
    return float('inf')

memoized = {}
def findMostPressure(valves, valve: Valve, minutes, elephant):
    def processRatePath(ratePath):
        if ratePath in memoized:
            return memoized[ratePath]
        t = minutes
        valveStates = {}
        def tick(timeToUse):
            for v in valveStates:
                vs = valveStates[v]
                valveStates[v] = (vs[0], vs[1]+vs[0]*timeToUse)

        for valve, timeToUse, rate in ratePath:
            t -= timeToUse
            tick(timeToUse)

            valveStates[valve] = (rate, 0)
        tick(t)
        res = sum([v[1] for v in valveStates.values()])
        memoized[ratePath] = res
        return res

    valvesWithRate: list[Valve] = list(filter(lambda v: v.rate > 0 and v.closed == True, valves.values()))
    perms = permutations(valvesWithRate, 7)
    maxFlow = float('-inf')
    for i, permutation in enumerate(perms):
        ratePath = getRates(valve, permutation, minutes)
        totalFlow = processRatePath(ratePath)
        if totalFlow > maxFlow:
            maxFlow = totalFlow
            print('new maxFlow1:', maxFlow)
        if i % 1000000 == 0:
            print(i)

        if elephant:
            eleList = valvesWithRate[:]
            for p in permutation:
                eleList.remove(p)
            perms = permutations(eleList, 7)
            for i, permutation in enumerate(perms):
                ratePath = getRates(valve, permutation, minutes)
                totalFlowEle = processRatePath(ratePath)
                if totalFlow + totalFlowEle > maxFlow:
                    maxFlow = totalFlow + totalFlowEle
                    print('new maxFlow2:', maxFlow)
    return maxFlow

def getRates(start, path, minutes):
    if path in memoized:
        return memoized[path]
    totalTime = 0
    rates = []
    prev = start
    for v in path:
        costToValve = prev.costs[v]
        # Check if moving there and opening would take too long
        if totalTime + costToValve + 1 > minutes:
            continue
        # Cost to move there + open
        totalTime += costToValve + 1
        rates.append((v, costToValve + 1, v.rate))
        prev = v
    memoized[path] = tuple(rates)
    return tuple(rates)


# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    valves = defaultdict()
    for line in file:
        line = line.strip()
        # print(line)
        valve, rate, tunnels = re.match('Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line).groups()
        rate = int(rate)
        tunnels = tunnels.split(', ')
        # print(valve, rate, tunnels)
        valves[valve] = Valve(valve, rate, tunnels)
    
    for valve in valves.values():
        valve.tunnels = [valves[t] for t in valve._tunnels]

    # Build costs from each valve to every other
    for valve in valves.values():
        for valveToFind in valves.values():
            if valve is valveToFind:
                continue

            dist = dijsktra(valve, valveToFind)
            valve.costs[valveToFind] = dist
    # for v in valves.values():
    #     print(v.name, v.costs)


    maxFlow = findMostPressure(valves, valves['AA'], 30, False)
    print(maxFlow)


# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]

    valves = defaultdict()
    for line in file:
        line = line.strip()
        # print(line)
        valve, rate, tunnels = re.match('Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line).groups()
        rate = int(rate)
        tunnels = tunnels.split(', ')
        # print(valve, rate, tunnels)
        valves[valve] = Valve(valve, rate, tunnels)
    
    for valve in valves.values():
        valve.tunnels = [valves[t] for t in valve._tunnels]

    # Build costs from each valve to every other
    for valve in valves.values():
        for valveToFind in valves.values():
            if valve is valveToFind:
                continue

            dist = dijsktra(valve, valveToFind)
            valve.costs[valveToFind] = dist
    # for v in valves.values():
    #     print(v.name, v.costs)


    # maxFlow = findMostPressure(valves, valves['AA'], 26, True)
    # print(maxFlow)
    # 1681 too low
    # 1707 too low
