# Day 11

Today's problem is about monkeys throwing around your stuff! Our input is a list of descriptions of each monkey and the properties it has. We get the items it starts with, which are represented by how much you are worried about them with an integer.

Part 1 asks us to "play" 20 rounds and multiply the top two items that have been inspected by monkeys.

Part 2 was kinda lame, it was purely an efficiency/limitation problem. The numbers would grow too big because it takes away the dividing by 3 of part 1, so you had to find a way to handle that. And I just didn't really have the experience to know what to do. So I had to look up how to do it. At least one possible solution is to find the Least Common Multiple of all of all of the monkey's test values.
```python
LCM = reduce(lambda a, b: a*b, [monkey['test'] for monkey in monkeys], 1)
```
Since the only thing you care about is if the item's worry value is a multiple of the test values, as long as you keep the worry value a multiple of all of them, the math still works.
