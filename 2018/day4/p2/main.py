from collections import defaultdict
from datetime import datetime
import re

def main():
    schedule = defaultdict(dict)
    with open('input.txt', 'r') as f:
        inputLines = []
        for line in f:
            boxId = line.rstrip('\n')
            matches = re.match(r'\[(\d{4}-\d\d-\d\d) (\d\d:\d\d)\] (.*)', boxId)
            inputLines.append(matches.groups())

        sortedInput = sorted(inputLines, key=lambda v: datetime.strptime('{} {}'.format(v[0], v[1]), "%Y-%m-%d %H:%M"))

        currentGuardNumber = 0
        lastMinute = None
        for _, time, info in sortedInput:
            guardNumberMatch = re.match(r'Guard #(\d+)', info)

            minute = int(time.split(':')[1])

            if guardNumberMatch:
                currentGuardNumber = guardNumberMatch.group(1)
                continue

            elif info == 'falls asleep':
                if minute not in schedule[currentGuardNumber]:
                    schedule[currentGuardNumber][minute] = 0
                schedule[currentGuardNumber][minute] += 1
            elif info == 'wakes up':
                for min in range(int(lastMinute), int(minute)):
                    if min not in schedule[currentGuardNumber]:
                        schedule[currentGuardNumber][min] = 0
                    schedule[currentGuardNumber][min] += 1

            lastMinute = minute

        for guard, sched in schedule.items():
            schedule[guard] = sorted(sched.items(), key=lambda kv: kv[1], reverse=True)[0]
        orderedBySleepiestMinute = sorted(schedule.items(), key=lambda kv: kv[1][1], reverse=True)
        winner = orderedBySleepiestMinute[0]

        print('Guard #{} slept the most during minute {}. Answer: {}'.format(winner[0], winner[1][0], int(winner[0]) * winner[1][0]))

main()
