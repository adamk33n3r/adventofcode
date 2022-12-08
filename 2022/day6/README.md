# Day 6

Today we're processing a string of characters which are "packets". We're told that the start-of-packet marker is when there are 4 characters in a row that are all different.

For part 1, we're tasked with detecting how many characters need to be processed before we find the first start-of-packet marker.

I step through a range of 4 characters, like a shifting window. I then check each character in that range and if we find a duplicate, we break the loop. If we get through all 4 characters without any dupes, we won't break, and therefore that means we've found our marker!
```python
line = file.read().strip()
for i in range(0, len(line) - 3):
    chrs = []
    for j in line[i:i+4]:
        if j not in chrs:
            chrs.append(j)
        else:
            break
    else:
        print(i+4)
        break
```

For part 2, we're tasked with detecting a start-of-message marker, which is the same as a start of packet marker, but is 14 different characters rather than 4. Same exact process as part 1, just add 10 to the numbers :P
```python
line = file.read().strip()
for i in range(0, len(line) - 13):
    chrs = []
    for j in line[i:i+14]:
        if j not in chrs:
            chrs.append(j)
        else:
            break
    else:
        print(i+14)
        break
```
