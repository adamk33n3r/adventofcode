from collections import defaultdict
import re

USE_EXAMPLE = False
PRINT_DEBUG = False

with open('example.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
    reqs = defaultdict(set)
    steps = set()
    for line in f:
        line = line.rstrip('\n')
        matches = re.match(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.', line)
        req, step = matches.groups()
        reqs[step].add(req)
        steps.add(req)
        steps.add(step)

    sortedSteps = sorted(steps)

    print('P1: ', end='')
    done = set()
    while sortedSteps:
        for step in sortedSteps:
            deps = reqs[step]
            if len(deps - done) == 0:
                print(step, end='')
                sortedSteps.remove(step)
                done.add(step)
                break

    print()

    # Part 2

    sortedSteps = sorted(steps)

    def getTime(step):
        baseTimePerStep = 0 if USE_EXAMPLE else 60
        stepVal = ord(step) - ord('A') + 1
        return baseTimePerStep + stepVal

    maxWorkers = 2 if USE_EXAMPLE else 5
    workers = []
    stepsWorked = []
    time = 0
    done = set()
    res = ''
    if PRINT_DEBUG:
        print('Second', *['Work {}'.format(i) for i in range(maxWorkers)], 'Done', sep='\t')
    while sortedSteps:

        # Find completed steps and tick non-completed steps
        deleteIndexes = []
        for i, (worker, step) in enumerate(zip(workers, stepsWorked)):
            worker -= 1
            if worker == 0:
                # print('Step {} is done at time {}'.format(step, time))

                deleteIndexes.append(i)

                sortedSteps.remove(step)
                done.add(step)
                res += step

            workers[i] = worker

        for i in deleteIndexes:
            del workers[i]
            del stepsWorked[i]

        # Check if new steps are available to start
        for step in sortedSteps:
            deps = reqs[step]
            canDoStep = len(deps - done) == 0
            if canDoStep and step not in stepsWorked:
                if len(workers) < maxWorkers:
                    workers.append(getTime(step))
                    stepsWorked.append(step)

        if PRINT_DEBUG:
            print(time, *['{}:{}'.format(stepsWorked[i], workers[i]) if i < len(stepsWorked) else '' for i in range(maxWorkers)], res, sep='\t')
        time += 1

    print('P2:', time - 1)
