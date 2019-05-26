# Factorial decomposition

The aim of the kata is to decompose n! (factorial n) into its prime factors.</br>

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :</br>
```
 "(p1**n1)(p2**n2)...(pk**nk)"
```
with the p(i) in increasing order and n(i) empty if n(i) is 1.


```
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
```

分析:<a href="https://github.com/Eddie02582/CodeWars/tree/master/Kata%205/Factorial%20decomposition">Factorial decomposition</a> 簡化版

sol:迴圈用一指針由2開始,若整除指針表示含有因數,並利用字典記錄個數,若不整除,指針加1,直到數字變1,表示找完因數

``` python
def primeFactors(n):
    dic={}    
    x=2         
    while(n!=1): 
        if n%x==0:
            dic[x]= dic.get(x,0)+1
            n=n//x                
        else:
            x+=1 
    return "".join(["({})".format(key) if dic[key]==1 else "({}**{})".format(key,dic[key]) for key in sorted(dic.keys())])
```













