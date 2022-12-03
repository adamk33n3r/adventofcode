import shutil
import sys
import os
import requests

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('wrong args. need <token> <year> <day#>')
        sys.exit()
    token = sys.argv[1]
    year = sys.argv[2]
    day = sys.argv[3]
    dayPath = os.path.join(year, 'day'+day)
    if os.path.exists(dayPath):
        print('Day already exists. Exiting', file=sys.stderr)
        sys.exit()
    shutil.copytree('.template', dayPath)
    with open(os.path.join(dayPath, 'README.md'), 'w') as file:
        file.write('# Day ' + day + '\n')
    inputData = requests.get('https://adventofcode.com/%s/day/%s/input' % (year, day), cookies={'session': token}).text
    with open(os.path.join(dayPath, 'input.txt'), 'w') as file:
        file.writelines(inputData)
