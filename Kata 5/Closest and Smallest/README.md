# Closest and Smallest


## Input
<ul>
    <li>a string strng of n positive numbers (n = 0 or n >= 2)</li>
</ul>
Let us call weight of a number the sum of its digits. For example 99 will have "weight" 18, 100 will have "weight" 1.</br>

Two numbers are "close" if the difference of their weights is small.

## Task:

For each number in strng calculate its "weight" and then find two numbers of strng that have:</br>

<ul>
    <li>the smallest difference of weights ie that are the closest</li>
    <li>with the smallest weights</li>
    <li>and with the smallest indices (or ranks, numbered from 0) in strng</li>
</ul>

## Task:
<ul>
    <li>an array of two arrays, each subarray in the following format:</li>
</ul>

```
    [number-weight, index in strng of the corresponding number, original corresponding number instrng]
```

## Examples:

example1
```
strng = "103 123 4444 99 2000"
the weights are 4, 6, 16, 18, 2 (ie 2, 4, 6, 16, 18)

closest should return [[2, 4, 2000], [4, 0, 103]] (or ([2, 4, 2000], [4, 0, 103])
or [{2, 4, 2000}, {4, 0, 103}] or ... depending on the language)
because 2000 and 103 have for weight 2 and 4, ther indexes in strng are 4 and 0.
The smallest difference is 2.
4 (for 103) and 6 (for 123) have a difference of 2 too but they are not 
the smallest ones with a difference of 2 between their weights.
```
example2
```
strng = "80 71 62 53"
All the weights are 8.
closest should return [[8, 0, 80], [8, 1, 71]]
71 and 62 have also:
- the smallest weights (which is 8 for all)
- the smallest difference of weights (which is 0 for all pairs)
- but not the smallest indices in strng.
```

example3
```
strng = "444 2000 445 544"
the weights are 12, 2, 13, 13 (ie 2, 12, 13, 13)

closest should return [[13, 2, 445], [13, 3, 544]] or ([13, 2, 445], [13, 3, 544])
or [{13, 2, 445}, {13, 3, 544}] or ...
444 and 2000 have the smallest weights (12 and 2) but not the smallest difference of weights;
they are not the closest.
Here the smallest difference is 0 and in the result the indexes are in ascending order.
```

example4
```
closest("444 2000 445 644 2001 1002") --> [[3, 4, 2001], [3, 5, 1002]] or ([3, 4, 2001], 
[3, 5, 1002]]) or [{3, 4, 2001}, {3, 5, 1002}] or ...
Here the smallest difference is 0 and in the result the indexes are in ascending order.
```

## Notes :
<ul>
    <li>If n == 0, `closest("") should return [] or ([], []) in Haskell, Clojure, FSharp</li>
</ul>


## Solution

sol :首先建立符合回傳格式的陣列[number-weight, index  original number],接著利用zip找出計算出前後差,找出最小,回傳index,index+1陣列

``` python
def closest(strng):
    weight = sorted([ [sum(int(c) for c in n), i, int(n)] for i, n in enumerate(strng.split()) ], key=lambda x: (x[0], x[1]))
    diff = [ abs(a[0] - b[0]) for a, b in zip(weight, weight[1:]) ]
    index=diff.index(min(diff))
    return  [ weight [index ], weight [index+ 1] ] if weight else []
```

sol :首先建立符合回傳格式的陣列[number-weight, index  original number],接著利用迴圈找出差值最小的位置,回傳位置,位置+1陣列

``` python
def closest(strng):
    if strng=="":
        return []

    weight= sorted([ [ sum(map(int,n)), i, int(n)]  for i,n in enumerate(strng.split()) ],key= lambda x:(x[0],x[1]))
    delta,position=weight[-1][0],0
    index=len(weight)
    
    for i in range(len(weight)-1):        
        if weight[i+1][0]-weight[i][0] < delta:            
                position=i
                delta=weight[i+1][0]-weight[i][0]
            
    return [weight[position] ,weight[position+1] ]
```







