# Day 2
For day2 i did some kinda interesting/funny/unique things. the only map I had was one for scores
```python
scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}
```
to determine winner, i compared scores of each move. if both your moves had the same score, you draw. if you subtract your score from your opponents score, and it's either 1 or -2, you lose. otherwise you win.
```python
def play(opp, me):
    if scores[opp] == scores[me]:
        return 3
    if scores[opp] - scores[me] == 1 or scores[opp] - scores[me] == -2:
        return 0
    else:
        return 6
```
then for part 2 I used the index of a move in a list with some math to determine what your move should be. this could have just been a "win map" but this is more fun :wink:
```python
moves = [ 'A', 'B', 'C' ]
def getMove(opp, end):
    if end == 'X':
        return moves[moves.index(opp) - 1]
    elif end == 'Y':
        return moves[moves.index(opp)]
    elif end == 'Z':
        return moves[(moves.index(opp) + 1) % len(moves)]
```
