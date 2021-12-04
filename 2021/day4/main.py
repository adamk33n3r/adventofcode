import re

USE_EXAMPLE = False
PRINT_DEBUG = False

def checkBoard(board):
    for row in board:
        rowWin = len([n for n in row if 'x' in n]) == 5
        if rowWin:
            break
    for c in range(5):
        colWin = len([row[c] for row in board if 'x' in row[c]]) == 5
        if colWin:
            break

    return rowWin or colWin

numbers = []
boards = []
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    numbers = file.readline().split(',')
    # spacer
    file.readline()
    board = []
    for line in file:
        line = line.strip()
        if len(line) > 0:
            board.append(re.split(' +', line))
        else:
            boards.append(board)
            board = []
            continue
    boards.append(board)

    def breakFunc():
        for num in numbers:
            for board in boards:
                for row in board:
                    ri = 0
                    for n in row:
                        if n == num:
                            row[ri] += 'x'
                        ri += 1
                if checkBoard(board):
                    return (num, board)
    num, winningBoard = breakFunc()
    score = sum([
        sum([int(n) for n in row if 'x' not in n])
        for row in winningBoard
    ])
    print(int(num) * score)

numbers = []
boards = []
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    numbers = file.readline().split(',')
    # spacer
    file.readline()
    board = []
    for line in file:
        line = line.strip()
        if len(line) > 0:
            board.append(re.split(' +', line))
        else:
            boards.append(board)
            board = []
            continue
    boards.append(board)

    def breakFunc():
        winningBoards = []
        for num in numbers:
            for board in boards:
                for row in board:
                    ri = 0
                    for n in row:
                        if n == num:
                            row[ri] += 'x'
                        ri += 1
                if checkBoard(board):
                    if len(winningBoards) == len(boards) - 1:
                        finalBoard = [b for b in boards if b not in winningBoards][0]
                        if board == finalBoard:
                            return (num, finalBoard)
                    elif board not in winningBoards:
                        winningBoards.append(board)
    num, winningBoard = breakFunc()
    score = sum([
        sum([int(n) for n in row if 'x' not in n])
        for row in winningBoard
    ])
    print(int(num) * score)
