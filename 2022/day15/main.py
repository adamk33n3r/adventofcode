import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class Sensor:
    def __init__(self, n: Node, b: Node):
        self.node = n
        self.beacon = b
        self.distance = distance(n.pos, b.pos)

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map()
    sensors: list[Sensor] = []
    beacons = []
    for line in file:
        line = line.strip()
        x1, y1, x2, y2 = map(int, re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line).groups())
        b = Node(m, (x2, y2), 'B')
        sensors.append(Sensor(Node(m, (x1, y1), 'S'), b))
        beacons.append(b)

    beaconPos = [b.pos[:-1] for b in beacons]

    y = 10 if USE_EXAMPLE else 2000000
    s = set()
    for sensor in sensors:
        if distance(sensor.node.pos, (sensor.node.x, y)) <= sensor.distance:
        # if (sensor.node.y + sensor.distance) >= y and sensor.node.y - sensor.distance <= y:
            for x in range(sensor.node.x - sensor.distance, sensor.node.x + sensor.distance + 1):
                if (x, y) not in beaconPos and distance(sensor.node.pos, (x, y)) <= sensor.distance:
                    s.add((x, y))
    print(len(s))

    # SLOW WAY
    # count = 0
    # s = set()
    # r = 1000 if USE_EXAMPLE else 10000000 
    # for x in range(-r, r):
    #     n = m.get((x, y, 0))
    #     if n is not None and (n.type == 'B' or n.type == 'S'):
    #         continue
    #     good = True
    #     for sensor in sensors:
    #         d = distance((x, y), sensor.node.pos)
    #         if d <= sensor.distance:
    #             good = False
    #             break
    #     if not good:
    #         count += 1

    # print(count)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map()
    sensors: list[Sensor] = []
    beacons = []
    for line in file:
        line = line.strip()
        x1, y1, x2, y2 = map(int, re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line).groups())
        b = Node(m, (x2, y2), 'B')
        sensors.append(Sensor(Node(m, (x1, y1), 'S'), b))
        beacons.append(b)

    def findDistress():
        for sensor in sensors:
            # look on the edge of each sensors range
            # there has to only be one "hole", otherwise the problem would be impossible
            for sx, sy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                for x in range(sensor.distance + 1 + 1):
                    y = sensor.distance + 1 - x

                    # calculate position to check
                    x2 = sensor.node.x + x * sx
                    y2 = sensor.node.y + y * sy
                    # skip if out of the range
                    if x2 < 0 or x2 > 4000000 or y2 < 0 or y2 > 4000000:
                        continue

                    good = True
                    # Check if this point is within range of any other sensor
                    # If it's not, then we've found it
                    for sensor2 in sensors:
                        if sensor2 is sensor:
                            continue
                        d = distance((x2, y2), sensor2.node.pos)
                        if d <= sensor2.distance:
                            good = False
                            break
                    if good:
                        return x2, y2
    x, y = findDistress()
    print(x * 4000000 + y)
