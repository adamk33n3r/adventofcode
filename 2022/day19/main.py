import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def canMakeRobot(bp, type: str, resources):
    ore, clay, obsidian, geode = resources
    if type == 'ore':
        return ore >= bp[type]
    elif type == 'clay':
        return ore >= bp[type]
    elif type == 'obsidian':
        return ore >= bp[type][0] and clay >= bp[type][1]
    elif type == 'geode':
        return ore >= bp[type][0] and obsidian >= bp[type][1]

def findBest(bp, time, robots, resources):
    highestOreCost = max(bp['ore'], bp['clay'], bp['obsidian'][0], bp['geode'][0])
    mostGeodes = 0

    memoize = set()
    processQueue = deque([(time, robots, resources)])
    i = 0
    while processQueue:
        i += 1

        if i % 100000 == 0:
            print(time, i)
        time, robots, resources = processQueue.popleft()

        oreRobots, clayRobots, obsidianRobots, geodeRobots = robots
        ore, clay, obsidian, geode = resources

        mostGeodes = max(mostGeodes, geode)

        if time == 0:
            continue


        ###
        # OPTIMIZATIONS
        # Reduce state so we can skip more
        ###

        # We don't need more ore bots than the highest cost
        if oreRobots >= highestOreCost:
            oreRobots = highestOreCost
        # Similarly, we don't need more bots than how much one costs
        # since we can only make 1 at a time anyway.
        if clayRobots >= bp['obsidian'][1]:
            clayRobots = bp['obsidian'][1]
        if obsidianRobots >= bp['geode'][1]:
            obsidianRobots = bp['geode'][1]
        # The exception, of course, is geode bots. We want as many as we can of those.

        # We'll do a similar thing with the resources. We only ever need as many
        # of each resource as we can use in 1 minute. Again, aside from geodes.
        # So we can safely discard resources that we won't need this minute, as
        # well as ones that we'll make back from robots next turn.
        if ore >= highestOreCost + oreRobots:
            ore = highestOreCost + oreRobots
        if clay >= bp['obsidian'][1] + clayRobots:
            clay = bp['obsidian'][1] + clayRobots
        if obsidian >= bp['geode'][1] + obsidianRobots:
            obsidian = bp['geode'][1] + obsidianRobots

        robots = (oreRobots, clayRobots, obsidianRobots, geodeRobots)
        resources = (ore, clay, obsidian, geode)

        # Prevents going down paths we've already gone down
        if (time, robots, resources) in memoize:
            continue
        memoize.add((time, robots, resources))

        # Collect resources
        ore += oreRobots
        clay += clayRobots
        obsidian += obsidianRobots
        geode += geodeRobots

        assert ore>=0 and clay>=0 and obsidian>=0 and geode>=0, (time, robots, resources, highestOreCost)

        if canMakeRobot(bp, 'geode', resources):
            processQueue.append((
                time - 1,
                (oreRobots, clayRobots, obsidianRobots, geodeRobots + 1),
                (ore - bp['geode'][0], clay, obsidian - bp['geode'][1], geode)
            ))
        if canMakeRobot(bp, 'obsidian', resources):
            processQueue.append((
                time - 1,
                (oreRobots, clayRobots, obsidianRobots + 1, geodeRobots),
                (ore - bp['obsidian'][0], clay - bp['obsidian'][1], obsidian, geode)
            ))
        if canMakeRobot(bp, 'clay', resources):
            processQueue.append((
                time - 1,
                (oreRobots, clayRobots + 1, obsidianRobots, geodeRobots),
                (ore - bp['clay'], clay, obsidian, geode)
            ))
        if canMakeRobot(bp, 'ore', resources):
            processQueue.append((
                time - 1,
                (oreRobots + 1, clayRobots, obsidianRobots, geodeRobots),
                (ore - bp['ore'], clay, obsidian, geode)
            ))


        # Do nothing, just collect resources
        processQueue.append((
            time - 1,
            (oreRobots, clayRobots, obsidianRobots, geodeRobots),
            (ore, clay, obsidian, geode)
        ))

    return mostGeodes

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    TIME = 24
    BLUEPRINTS = []
    for line in file:
        costs = line.strip().split(': ')[1].split('. ')
        BLUEPRINTS.append({
            'ore': int(costs[0].split()[-2]),
            'clay': int(costs[1].split()[-2]),
            'obsidian': tuple(map(int, (costs[2].split()[-5], costs[2].split()[-2]))),
            'geode': tuple(map(int, (costs[3].split()[-5], costs[3].split()[-2]))),
        })


    tot = 0
    for id, bp in enumerate(BLUEPRINTS, 1):
        res = findBest(bp, TIME, (1, 0, 0, 0), (0, 0, 0, 0))
        tot += res * id
    print(tot)
    assert tot == 1528

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    TIME = 32
    BLUEPRINTS = []
    for line in file:
        costs = line.strip().split(': ')[1].split('. ')
        BLUEPRINTS.append({
            'ore': int(costs[0].split()[-2]),
            'clay': int(costs[1].split()[-2]),
            'obsidian': tuple(map(int, (costs[2].split()[-5], costs[2].split()[-2]))),
            'geode': tuple(map(int, (costs[3].split()[-5], costs[3].split()[-2]))),
        })
        if len(BLUEPRINTS) == 3:
            break

    tot = 1
    for bp in BLUEPRINTS:
        res = findBest(bp, TIME, (1, 0, 0, 0), (0, 0, 0, 0))
        tot *= res
    print(tot)
    assert tot == 16926
