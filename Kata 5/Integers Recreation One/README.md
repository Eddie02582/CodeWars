# Integers: Recreation One
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!</br>

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.</br>

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.</br>

## Examples:

```
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
```



## Solution

sol :第一層迴圈由m,n區間,第二層迴圈找出因數,如果是因數就把因數平方相加 </br>



``` python
def list_squared(m, n):
    result=[]
    for i in range(m,n+1):
        total=0
        for j in range(1,int(i**0.5)+1):
            if i % j==0:
                p,q=j,i//j
                if p == q:
                    total+=p**2
                else:
                    total+=p**2+q**2
        if total**0.5==int (total**0.5):
            result.append([i,total])
    return result

```










