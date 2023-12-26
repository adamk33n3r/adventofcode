import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from graph import Graph

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def edmondsKarp(graph, source, sink):
    def bfs():
        visited = set()
        queue = deque([(source, float('inf'))])
        visited.add(source)
        while queue:
            current, flow = queue.popleft()
            for neighbor, residualCapacity in graph[current].items():
                if neighbor not in visited and residualCapacity > 0:
                    minFlow = min(flow, residualCapacity)
                    queue.append((neighbor, minFlow))
                    path[neighbor] = current
                    if neighbor == sink:
                        return minFlow
                    visited.add(neighbor)
        return 0

    maxFlow = 0
    while True:
        path = {}
        augmentingFlow = bfs()
        if augmentingFlow == 0:
            break
        maxFlow += augmentingFlow
        current = sink
        while current != source:
            prev = path[current]
            graph[prev][current] -= augmentingFlow
            if current not in graph:
                graph[current] = {}
            graph[current][prev] += augmentingFlow
            current = prev
    return maxFlow

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    graph = Graph()
    for line in file:
        line = line.strip()
        comp, compListStr = line.split(': ')
        compList = compListStr.split()

        for oComp in compList:
            graph.addEdge(comp, oComp)

    start = list(graph.keys())[0]
    for n in graph.keys():
        graph.setAllWeights(1)
        v = edmondsKarp(graph, start, n)
        if v == 3:
            visited = set()
            queue = deque([start])
            visited.add(start)
            while queue:
                current = queue.popleft()
                for neighbor, residualCapacity in graph[current].items():
                    if neighbor not in visited and residualCapacity > 0:
                        queue.append(neighbor)
                        visited.add(neighbor)
            cutA = set([node for node in graph.keys() if node in visited])
            cutB = graph.keys() - cutA
            print(len(cutA) * len(cutB))
            break


    # THIS IS CHEATING

    # import networkx
    # g = networkx.DiGraph()
    # for k, vs in graph.items():
    #     for v in vs:
    #         g.add_edge(k,v,capacity=1.0)
    #         g.add_edge(v,k,capacity=1.0)
    # for y in list(graph.keys()):
    #     if start == y:
    #         continue
    #     cutValue, (L,R) = networkx.minimum_cut(g, start, y)
    #     if cutValue == 3:
    #         print('asdfasdf', cutValue, L, R, len(L), len(R))
    #         break

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    for line in file:
        line = line.strip()
