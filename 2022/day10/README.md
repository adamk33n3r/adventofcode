# Day 10

Today was a simple CPU instruction processing problem. We had two instructions, `noop` and `addx`. `noop` takes 1 cycle to complete and `addx` takes 2. After the two cycles it adds the value parameter to the `X` register. So we basically just run the program and look at the results.
```python
X = 1
cycles = 1
total = 0
for line in file:
    line = line.strip()
    if line == 'noop':
        cycles += 1
        if (cycles - 20) % 40 == 0:
            total += cycles * X
        continue
    cmd, arg = line.split()
    if cmd == 'addx':
        for i in range(2):
            cycles += 1
            if i == 1:
                X += int(arg)
            if (cycles - 20) % 40 == 0:
                total += cycles * X
print(total)
```
For part 2, we are supposed to use the value of register `X` to "paint" pixels on a 40x6 screen.
```python
X = 1
cycles = 0
lines = [l.split() for l in file.readlines()]
pc = 0
op = 0
screen = ''
while pc < len(lines):
    if cycles > 0 and cycles % 40 == 0:
        cycles -= 40
        screen += '\n'
    rng = list(range(X - 1, X + 2))
    if cycles in rng:
        # draw
        screen += '#'
    else:
        screen += ' '

    line = lines[pc]
    if line[0] == 'noop':
        pc += 1
    else:
        cmd, arg = line
        if cmd == 'addx':
            op += 1
            if op == 2:
                op = 0
                pc += 1
                X += int(arg)
    cycles += 1
print(screen)
```
The answer is displayed as a sequence of characters, in this case it was `EHPZPJGL`.
