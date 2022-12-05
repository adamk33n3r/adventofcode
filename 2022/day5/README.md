# Day 5

What took the longest for me was the parsing/constructing of the data structure I would use to represent the problem. In hindsight, it would have been faster to just hand copy them in.

The solution I came up with is pretty messy
```python
stacks, instructions = file.read().split('\n\n')
stackCount = (len(stacks.split('\n')[0])+1)//4
boxes = [[] for _ in range(stackCount)]
for line in stacks.split('\n')[:-1]:
    seg = 0
    stackNum = 0
    for seg in range(0, stackCount * 4, 4):
        box = line[seg:seg+3]
        if box == '   ':
            box = None
        else:
            box = box[1]
        if box:
            boxes[stackNum].append(box)
        stackNum += 1
```

Once I had the data structure, though, the solution was pretty straight forward.
```python
for ins in instructions:
    if ins == '':
        break
    matches = re.match('move (\d+) from (\d) to (\d)', ins)
    amt, frm, to = [int(g) for g in matches.groups()]
    boxesToMove = [boxes[frm-1].pop(0) for _ in range(amt)]
    boxesToMove.reverse() # for part 1 only
    boxes[to-1] = boxesToMove + boxes[to-1]
```
