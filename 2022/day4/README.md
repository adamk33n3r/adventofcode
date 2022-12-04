# Day 4

After parsing and processing the input, we mark each elf as either the biggest or smallest range. We then increment a counter if the first section of the biggest elf's assignment is lower or equal to the first section of the smallest elf's assignment AND that the last section of the biggest is greater or equal to the last section of the smallest.
```python
if bigger[0] <= smaller[0] and bigger[-1] >= smaller[-1]:
    # is fully contained
    count += 1
```
For part 2, we do mostly the same thing except we need to check for partial overlap. So the biggest range is either overlapping the first section or the last section of the other.
```python
if bigger[0] <= smaller[-1] and bigger[-1] >= smaller[0]:
    # is partially contained
    count += 1
```
