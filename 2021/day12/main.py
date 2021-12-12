import re
from collections import defaultdict

USE_EXAMPLE = False
PRINT_DEBUG = False

def isSmall(n):
    return (n[0] >= 'a' and n[0] <= 'z') or n == 'start' or n == 'end'

def visit(graph, node, visited, paths):
    visited.append(node)
    if node == 'end':
        paths.append(visited)
        return
    nodes = graph[node]
    for n in nodes:
        if isSmall(n) and n in visited:
            continue
        visit(graph, n, visited[:], paths)
def visit2(graph, node, visited, paths):
    visited.append(node)
    if node == 'end':
        paths.append(visited)
        return
    nodes = graph[node]
    for n in nodes:
        smallVisitedCaves = [cave for cave in visited if isSmall(cave)]
        visitedCount = defaultdict(int)
        visitedCountOthers = defaultdict(int)
        for cave in smallVisitedCaves:
            visitedCount[cave] += 1
            if cave != n:
                visitedCountOthers[cave] += 1
        # we go again
        if isSmall(n) and n != 'start' and n != 'end' and visitedCount[n] <= 1 and not any([n == 2 for n in visitedCountOthers.values()]):
            visit2(graph, n, visited[:], paths)
        elif isSmall(n) and n not in visited:
            visit2(graph, n, visited[:], paths)
        elif not isSmall(n):
            visit2(graph, n, visited[:], paths)

# Part 1
# lol example blew recursion but not the input because I was checking
# the whole string in the isSmall instead of the first character.
# I forgot that the cave names could have more than one character
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    graph = defaultdict(list)
    for line in file:
        fromNode, toNode = line.strip().split('-')
        graph[fromNode].append(toNode)
        graph[toNode].append(fromNode)
    visited = []
    paths = []
    visit(graph, 'start', visited, paths)
    print(len(paths))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    graph = defaultdict(list)
    for line in file:
        fromNode, toNode = line.strip().split('-')
        graph[fromNode].append(toNode)
        graph[toNode].append(fromNode)
    visited = []
    paths = []
    visit2(graph, 'start', visited, paths)
    print(len(paths))
