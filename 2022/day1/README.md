# Day 1

And we're off! Today we're counting calories (too real). We just step over every line and add the number to a total for an elf, adding it to an array. If the line is empty, we skip to the next elf.
```python
elves = []
elfNum = 0
for line in file:
    line = line.strip()
    if line == '':
        elfNum += 1
    else:
        if len(elves) <= elfNum:
            elves.append(0)
        elves[elfNum] += int(line)
```
Once we have the calories for each elf, we just find the biggest one with a simple
```python
print(max(elves))
```
For part 2, we need to sum up the calories of the top 3 elves. Instead of doing something simple like this...
```python
print(sum(sorted(elves)[-3:]))
```
...I decided to use a `PriorityQueue` because that's where my mind went. The thing with priority queues is that they can only sort from low to high, so I had to negate my values in order to achieve that.
```python
mostest = PriorityQueue()
for elf in elves:
    mostest.put(-elf)
print(-mostest.get()+-mostest.get()+-mostest.get())
```
Cut me some slack, it's the first day and Python-isms haven't come back to me fully yet ;)
