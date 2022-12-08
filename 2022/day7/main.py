import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class File:
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = size
    def __str__(self):
        return self.name
    def __repr__(self) -> str:
        return self.__str__()

class Dir:
    def __init__(self, name, parent, contents = None):
        self.name = name
        self.parent = parent
        self.contents = contents if contents is not None else []
    def __str__(self):
        return self.name
    def __repr__(self) -> str:
        return self.__str__()

def getSize(dir: Dir):
    size = 0
    for item in dir.contents:
        if type(item) is File:
            size += item.size
        else:
            size += getSize(item)
    return size

def getSizeLimit(dir: Dir, limit, totalSize = 0):
    for item in dir.contents:
        if type(item) is Dir:
            s = getSize(item)
            if s <= limit:
                totalSize += s
            totalSize = getSizeLimit(item, limit, totalSize)
    return totalSize


def walk(dir: Dir, indent = 0):
    print(' '*indent + dir.name)
    indent += 2
    for item in dir.contents:
        if type(item) is File:
            print(' '*indent + item.name)
        else:
            walk(item, indent)

def parseFileSystem(file):
    root = Dir('/', None)
    curDir = root
    for line in file:
        line = line.strip().split()
        # Is command
        if line[0] == '$':
            cmd = line[1]
            if cmd == 'cd':
                args = line[2]
                if args == '/':
                    curDir = root
                    continue
                elif args == '..':
                    curDir = curDir.parent
                else:
                    curDir = next(filter(lambda d: d.name == args, curDir.contents))
            elif cmd == 'ls':
                continue
        elif line[0] == 'dir':
            curDir.contents.append(Dir(line[1], curDir))
        else:
            curDir.contents.append(File(line[1], curDir, int(line[0])))
    return root

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    root = parseFileSystem(file)
    # walk(root)
    print(getSizeLimit(root, 100000))

def findSpace(dir: Dir, dirToDelete = float('inf')):
    for item in dir.contents:
        if type(item) is Dir:
            s = getSize(item)
            if s >= needToDelete and s < dirToDelete:
                dirToDelete = s
            dirToDelete = findSpace(item, dirToDelete)
    return dirToDelete

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    root = parseFileSystem(file)
    totalSize = getSize(root)
    maxUsedSpace = 70000000 - 30000000
    needToDelete = totalSize - maxUsedSpace
    dirToDelete = findSpace(root)
    print(dirToDelete)
    # walk(root)

