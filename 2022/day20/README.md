# Day 20

Either my brain is broken, or today's was deceptively hard. Or both. It seemed straight forward enough. Take a list of numbers, iterate through them, and move them around the list according to their value with wrapping. So if the third element in the list was `-3`, you would move it back 3 positions, ending up at the second to last position in the list. It's kinda hard to think of it that way because the list is circular so moving an element from index `0` to index `-1` is **not actually** different.
[1,-2,3,4,5]
[-2,1,3,4,5]
[1,3,4,-2,5]
```python
numbers = [Num(int(line.strip()), i) for i, line in enumerate(file)]
numbersCopy = numbers[:]
for i in range(len(numbers)):
    numberToMove = numbersCopy[i]
    curIdx = numbers.index(numberToMove)
    newIdx = ((curIdx + numberToMove.value) % (len(numbers)-1))+1

    # If we are moving this backward, lower the index by 1 and remove the existing number first.
    # Since list.remove removes the first occurrence, it would remove the one we add 
    if newIdx < curIdx:
        newIdx -= 1
        numbers.remove(numberToMove)

    assert 0 <= newIdx <= len(numbers), newIdx

    # Add the number to the new spot
    numbers.insert(newIdx, numberToMove)

    # Remove the old number if it was after
    if newIdx >= curIdx:
        numbers.remove(numberToMove)

zeroIdx = [n.value for n in numbers].index(0)
x = numbers[(zeroIdx + 1000) % len(numbers)].value
y = numbers[(zeroIdx + 2000) % len(numbers)].value
z = numbers[(zeroIdx + 3000) % len(numbers)].value
print(x+y+z)
```
I'm not actually sure why the formula for the new index needed to modulo `len(numbers)-1`. But it did the trick, combined with `newIdx -= 1` if the new index was "before" the original index. I'm guessing it has to do with the start and end of the list being the "same" position? Like, since it's a circular list, moving the first element of the list to the end doesn't actually change anything. So I guess it's like there are `len(numbers)-1` positions? I feel like this is something I was trying to do originally but for some reason kept missing it.

Part 2 was basically just an efficiency thing I think. You had to do the operation 10 times and also multiply each number in the list by `811589153` before running it. The only thing that affects my performance is the 10 times, the big numbers don't mean anything because I'm already using modulo against the length of the list.
