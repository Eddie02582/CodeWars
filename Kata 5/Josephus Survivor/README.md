# Josephus Survivor

In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus permutation. </br>

Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements, like this:</br>

```
josephus_survivor(7,3) => means 7 people in a circle;
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!
```




## Solution

sol : 類似<a href="https://github.com/Eddie02582/CodeWars/tree/master/Kata%205/Josephus%20Permutation">Josephus Permutation</a>取出最後一位
``` python
def josephus(n, k):
    items=[ x for x in range(1, n + 1)]
    i, result = 0, []
    while len(items) > 0:
        i = (i + k - 1) % len(items)
        result.append(items.pop(i))
    return result[-1]
``` 

簡化一下
``` python
def josephus_survivor(n, k):	
	items,i=[ x for x in range(1, n + 1)] ,0	
	while len(items) > 1:
		i = (i + k - 1) % len(items)
		items.pop(i)		
	return items[0]
```










