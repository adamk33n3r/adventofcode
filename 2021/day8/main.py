import re
from collections import defaultdict

USE_EXAMPLE = False
PRINT_DEBUG = False

# 0: abcefg
# 1: cf
# 2: acdeg
# 3: acdfg
# 4: bcdf
# 5: abdfg
# 6: abdefg
# 7: acf
# 8: abcdefg
# 9: abcdfg

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    c = 0
    for line in file:
        inputLine, outputLine = line.strip().split(' | ')
        inputs = inputLine.split()
        outputs = outputLine.split()
        for inputSegment in outputs:
            # is 1
            if len(inputSegment) == 2:
                c += 1
            # is 4
            elif len(inputSegment) == 4:
                c += 1
            # is 7
            elif len(inputSegment) == 3:
                c += 1
            # is 8
            elif len(inputSegment) == 7:
                c += 1
    print(c)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    total = 0
    for line in file:
        inputLine, outputLine = line.strip().split(' | ')
        inputs = inputLine.split()
        outputs = outputLine.split()
        mapping = {}
        for inputSegment in inputs:
            inputSet = frozenset(inputSegment)
            # is 1
            if len(inputSegment) == 2:
                mapping[1] = inputSet
                mapping[inputSet] = 1
            # is 4
            elif len(inputSegment) == 4:
                mapping[4] = inputSet
                mapping[inputSet] = 4
            # is 7
            elif len(inputSegment) == 3:
                mapping[7] = inputSet
                mapping[inputSet] = 7
            # is 8
            elif len(inputSegment) == 7:
                mapping[8] = inputSet
                mapping[inputSet] = 8
        cf = ''.join(mapping[1])
        a = list(mapping[7] - mapping[1])[0]
        bd = ''.join(mapping[4] - mapping[1])
        g = ''
        d = ''
        for inputSegment in inputs:
            if len(inputSegment) == 5:
                inputSet = frozenset(inputSegment)
                if a in inputSet and set(bd).issubset(inputSet):
                    res = list(inputSet - set(bd) - set(a) - set(cf))
                    g = res[0]
                    mapping[5] = inputSet
                    mapping[inputSet] = 5
                    break
        # get 3(d)
        for inputSegment in inputs:
            if len(inputSegment) == 5:
                inputSet = frozenset(inputSegment)
                if a in inputSet and cf[0] in inputSet and cf[1] in inputSet and g in inputSet:
                    d = list(inputSet - set(a) - set(cf) - set(g))[0]
                    mapping[3] = inputSet
                    mapping[inputSet] = 3
                    break
        # get 2(e)
        for inputSegment in inputs:
            if len(inputSegment) == 5:
                inputSet = frozenset(inputSegment)
                if mapping[5] != inputSet and mapping[3] != inputSet:
                    mapping[2] = inputSet
                    mapping[inputSet] = 2
                    break
        # get 9
        for inputSegment in inputs:
            if len(inputSegment) == 6:
                inputSet = frozenset(inputSegment)
                if a in inputSet and bd[0] in inputSet and bd[1] in inputSet and cf[0] in inputSet and cf[1] in inputSet and g in inputSet:
                    mapping[9] = inputSet
                    mapping[inputSet] = 9
                    break
        # get 0
        for inputSegment in inputs:
            if len(inputSegment) == 6:
                inputSet = frozenset(inputSegment)
                if d not in inputSegment:
                    mapping[0] = inputSet
                    mapping[inputSet] = 0
                    break

        # get 6(c)
        for inputSegment in inputs:
            if len(inputSegment) == 6:
                inputSet = frozenset(inputSegment)
                if inputSet != mapping[0] and inputSet != mapping[9]:
                    mapping[6] = inputSet
                    mapping[inputSet] = 6
                    break

        s = ''
        for outputSegment in outputs:
            s += str(mapping[frozenset(outputSegment)])

        total += int(s)

    print(total)
