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
    stacks, instructions = file.read().split('\n\n')
    instructions = instructions.split('\n')
    stackCount = (len(stacks.split('\n')[0])+1)//4
    boxes = [[] for _ in range(stackCount)]
    for line in stacks.split('\n')[:-1]:
        seg = 0
        stackNum = 0
        for seg in range(0, stackCount * 4, 4):
            box = line[seg:seg+3]
            if box == '   ':
                box = None
            else:
                box = box[1]
            if box:
                boxes[stackNum].append(box)
            stackNum += 1
    for ins in instructions:
        if ins == '':
            break
        matches = re.match('move (\d+) from (\d) to (\d)', ins)
        amt, frm, to = [int(g) for g in matches.groups()]
        boxesToMove = [boxes[frm-1].pop(0) for _ in range(amt)]
        boxesToMove.reverse()
        boxes[to-1] = boxesToMove + boxes[to-1]
    print(''.join([box[0] for box in boxes]))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    stacks, instructions = file.read().split('\n\n')
    instructions = instructions.split('\n')
    stackCount = (len(stacks.split('\n')[0])+1)//4
    boxes = [[] for _ in range(stackCount)]
    for line in stacks.split('\n')[:-1]:
        seg = 0
        stackNum = 0
        for seg in range(0, stackCount * 4, 4):
            box = line[seg:seg+3]
            if box == '   ':
                box = None
            else:
                box = box[1]
            if box:
                boxes[stackNum].append(box)
            stackNum += 1
    for ins in instructions:
        if ins == '':
            break
        matches = re.match('move (\d+) from (\d) to (\d)', ins)
        amt, frm, to = [int(g) for g in matches.groups()]
        boxesToMove = [boxes[frm-1].pop(0) for _ in range(amt)]
        boxes[to-1] = boxesToMove + boxes[to-1]
    print(''.join([box[0] for box in boxes]))
