# Find the odd int
Given an array, find the int that appears an odd number of times.</br>

There will always be only one integer that appears an odd number of times.</br>

## Solution
<sol> 用xor
```python
def find_it(seq):
    n=0
    for x in seq:
        n^=x      
    return n
    
import operator
```	