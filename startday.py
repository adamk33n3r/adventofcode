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
    shutil.copytree('.template', dayPath)
    inputData = requests.get('https://adventofcode.com/%s/day/%s/input' % (year, day), cookies={'session': token}).text
    with open(os.path.join(dayPath, 'input.txt'), 'w') as file:
        file.writelines(inputData)
