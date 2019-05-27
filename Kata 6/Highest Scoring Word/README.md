# Highest Rank Number in an ArrayHighest Scoring Word
Given a string of words, you need to find the highest scoring word.</br>

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.</br>

You need to return the highest scoring word as a string.</br>

If two words score the same, return the word that appears earliest in the original string.</br>

All letters will be lowercase and all inputs will be valid.</br>

## Solution

```python
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
```	
