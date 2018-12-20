from collections import defaultdict
import re

USE_EXAMPLE = False
PRINT_DEBUG = False

def addr(a, b, c, r):
    r[c] = r[a] + r[b]

def addi(a, b, c, r):
    r[c] = r[a] + b

def mulr(a, b, c, r):
    r[c] = r[a] * r[b]

def muli(a, b, c, r):
    r[c] = r[a] * b

def banr(a, b, c, r):
    r[c] = r[a] & r[b]

def bani(a, b, c, r):
    r[c] = r[a] & b

def borr(a, b, c, r):
    r[c] = r[a] | r[b]

def bori(a, b, c, r):
    r[c] = r[a] | b

def setr(a, b, c, r):
    r[c] = r[a]

def seti(a, b, c, r):
    r[c] = a

def gtir(a, b, c, r):
    r[c] = int(a > r[b])

def gtri(a, b, c, r):
    r[c] = int(r[a] > b)

def gtrr(a, b, c, r):
    r[c] = int(r[a] > r[b])

def eqir(a, b, c, r):
    r[c] = int(a == r[b])

def eqri(a, b, c, r):
    r[c] = int(r[a] == b)

def eqrr(a, b, c, r):
    r[c] = int(r[a] == r[b])

p1Ans = 0
with open('example.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
    OPCODES = list(range(0, 16))

    it = iter(f)

    results = defaultdict(list)

    opcodeToFuncName = defaultdict(set)

    while it:
        line = next(it).strip()
        if line == '':
            break
        beforeReg = list(map(int, re.match(r'Before: \[(\d), (\d), (\d), (\d)\]', line).groups()))
        line = next(it).strip()
        opcode, inputA, inputB, output = map(int, line.strip().split())
        line = next(it).strip()
        afterReg = list(map(int, re.match(r'After:  \[(\d), (\d), (\d), (\d)\]', line).groups()))
        line = next(it)

        count = 0

        orig = beforeReg.copy()

        funcs = [
            addr,
            addi,
            mulr,
            muli,
            banr,
            bani,
            borr,
            bori,
            setr,
            seti,
            gtir,
            gtri,
            gtrr,
            eqir,
            eqri,
            eqrr,
        ]

        for func in funcs:
            beforeReg = orig.copy()
            func(inputA, inputB, output, beforeReg)
            if beforeReg == afterReg:
                count += 1
                results[func.__name__].append((opcode, orig.copy(), (inputA, inputB, output), afterReg.copy()))
                opcodeToFuncName[opcode].add(func.__name__)
                if PRINT_DEBUG:
                    print(func.__name__, beforeReg, (inputA, inputB, output), afterReg)

        if count >= 3:
            p1Ans += 1

    print('P1:', p1Ans)

    while True:
        unique = {}
        for op, funcs in opcodeToFuncName.items():
            if len(funcs) == 1:
                unique[op] = funcs

        for op, funcs in unique.items():
            for op2, funcs2 in opcodeToFuncName.items():
                if op != op2:
                    funcs2.difference_update(funcs)

        if len(unique) == len(opcodeToFuncName):
            break

    opcodeToFuncName = {op: funcs.pop() for op, funcs in opcodeToFuncName.items()}

    registers = [0, 0, 0, 0]
    for line in f:
        if line == '\n':
            continue

        opcode, inputA, inputB, output = map(int, line.strip().split())

        globals()[opcodeToFuncName[opcode]](inputA, inputB, output, registers)

    print('P2:', registers[0])
