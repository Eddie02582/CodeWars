# Is my friend cheating?

<ul>
    <li>A friend of mine takes a sequence of numbers from 1 to n (where n > 0).</li>
    <li>Within that sequence, he chooses two numbers, a and b.</li>
    <li>He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.</li>
    <li>Given a number n, could you tell me the numbers he excluded from the sequence?</li>
</ul>

The function takes the parameter: n (n is always strictly greater than 0) and returns an array or a string (depending on the language) of the form:

```
[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
```

with all (a, b) which are the possible removed numbers in the sequence 1 to n.</br>

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ...will be sorted in increasing order of the "a".

It happens that there are several possible (a, b). The function returns an empty array (or an empty string) if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).


## Examples:

```
    removNb(26) should return [(15, 21), (21, 15)]
```



## Solution

sol : 依提意 sum-x-y=x*y => y=(sum-x)/(x+1),迴圈從1到n 如果y是整數且小於等於n即符合



``` python
def removNb(n):
    result=[]
    total= n*(n+1)/2

    for x in range(1,n+1):
        y= (total-x)//(x+1)
        if (total-x)%(x+1)==0 and y <=n:
            result.append((x,y))  
    return result
```










