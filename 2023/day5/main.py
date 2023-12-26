import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def mapValue(map, source):
    for destStart, srcStart, range in map:
        if srcStart <= source < srcStart + range:
            return destStart + (source - srcStart)
    return source

def mapValues(map, sourceRanges):
    mappedValues = []
    for destStart, srcStart, range in map:
        newRanges = []
        while sourceRanges:
            sourceRange = sourceRanges.pop()
            before = (sourceRange[0], min(sourceRange[1], srcStart))
            inside = (max(sourceRange[0], srcStart), min(sourceRange[1], srcStart + range))
            after = (max(sourceRange[0], srcStart + range), sourceRange[1])
            if before[0] < before[1]:
                newRanges.append(before)
            if inside[0] < inside[1]:
                mappedValues.append((destStart + (inside[0] - srcStart), destStart + (inside[1] - srcStart)))
            if after[0] < after[1]:
                newRanges.append(after)
        sourceRanges = newRanges

    # sourceRanges here will be the 1:1 mapped values
    return mappedValues + sourceRanges

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    maps = defaultdict(list)
    nextMap = None
    for line in file:
        line = line.strip()
        if len(line) == 0:
            nextMap = None
            continue
        if line.startswith('seeds:'):
            seedNums = [int(x) for x in line.split(': ')[1].split()]
        elif ':' in line:
            nextMap = line.split()[0]
        elif nextMap is not None:
            maps[nextMap].append([int(x) for x in line.split()])
    locs = []
    print(mapValue(maps['seed-to-soil'], 98))
    print(mapValue(maps['seed-to-soil'], 99))
    print(mapValue(maps['seed-to-soil'], 100))
    for seed in seedNums:
        soil = mapValue(maps['seed-to-soil'], seed)
        fert = mapValue(maps['soil-to-fertilizer'], soil)
        water = mapValue(maps['fertilizer-to-water'], fert)
        light = mapValue(maps['water-to-light'], water)
        temp = mapValue(maps['light-to-temperature'], light)
        humid = mapValue(maps['temperature-to-humidity'], temp)
        loc = mapValue(maps['humidity-to-location'], humid)
        locs.append(loc)
    print(min(locs))

            

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    maps = defaultdict(list)
    nextMap = None
    for line in file:
        line = line.strip()
        if len(line) == 0:
            nextMap = None
            continue
        if line.startswith('seeds:'):
            seedNumRanges = [int(x) for x in line.split(': ')[1].split()]
            seedNums = []
            for i in range(len(seedNumRanges)//2):
                seedNums.append((seedNumRanges[i*2], seedNumRanges[i*2] + seedNumRanges[i*2+1]))
        elif ':' in line:
            nextMap = line.split()[0]
        elif nextMap is not None:
            maps[nextMap].append([int(x) for x in line.split()])
    locs = []
    for seedRange in seedNums:
        soil = mapValues(maps['seed-to-soil'], [seedRange])
        fert = mapValues(maps['soil-to-fertilizer'], soil)
        water = mapValues(maps['fertilizer-to-water'], fert)
        light = mapValues(maps['water-to-light'], water)
        temp = mapValues(maps['light-to-temperature'], light)
        humid = mapValues(maps['temperature-to-humidity'], temp)
        loc = mapValues(maps['humidity-to-location'], humid)
        locs.append(min(loc)[0])
    print(locs)
    print(min(locs))
