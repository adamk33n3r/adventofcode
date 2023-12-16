import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node
from itertools import cycle

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Num:
    def __init__(self, value, idx) -> None:
        self.value = value
        self.idx = idx
    def __repr__(self) -> str:
        return '(%s, %s)' % (self.idx, self.value)

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    numbers = [Num(int(line.strip()), i) for i, line in enumerate(file)]
    numbersCopy = numbers[:]
    for i in range(len(numbers)):
        numberToMove = numbersCopy[i]
        curIdx = numbers.index(numberToMove)
        newIdx = ((curIdx + numberToMove.value) % (len(numbers)-1))+1

        # If we are moving this backward, lower the index by 1 and remove the existing number first.
        # Since list.remove removes the first occurrence, it would remove the one we add 
        if newIdx < curIdx:
            newIdx -= 1
            numbers.remove(numberToMove)

        assert 0 <= newIdx <= len(numbers), newIdx

        # Add the number to the new spot
        numbers.insert(newIdx, numberToMove)

        # Remove the old number if it was after
        if newIdx >= curIdx:
            numbers.remove(numberToMove)

    zeroIdx = [n.value for n in numbers].index(0)
    x = numbers[(zeroIdx + 1000) % len(numbers)].value
    y = numbers[(zeroIdx + 2000) % len(numbers)].value
    z = numbers[(zeroIdx + 3000) % len(numbers)].value
    print(x+y+z)
    assert x+y+z == 8302

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]

    numbers = [Num(int(line.strip()) * 811589153, i) for i, line in enumerate(file)]
    numbersCopy = numbers[:]
    for _ in range(10):
        for i in range(len(numbers)):
            numberToMove = numbersCopy[i]
            curIdx = numbers.index(numberToMove)
            newIdx = ((curIdx + numberToMove.value) % (len(numbers)-1))+1

            # If we are moving this backward, lower the index by 1 and remove the existing number first.
            # Since list.remove removes the first occurrence, it would remove the one we add 
            if newIdx < curIdx:
                newIdx -= 1
                numbers.remove(numberToMove)

            assert 0 <= newIdx <= len(numbers)

            # Add the number to the new spot
            numbers.insert(newIdx, numberToMove)

            # Remove the old number if it was after
            if newIdx >= curIdx:
                numbers.remove(numberToMove)

    zeroIdx = [n.value for n in numbers].index(0)
    x = numbers[(zeroIdx + 1000) % len(numbers)].value
    y = numbers[(zeroIdx + 2000) % len(numbers)].value
    z = numbers[(zeroIdx + 3000) % len(numbers)].value
    print(x+y+z)
    assert x+y+z == 656575624777
