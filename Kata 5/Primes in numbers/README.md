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

sol:將Factorial decomposition簡化

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

sol:上面dic 拆掉,message 改由在迴圈過程中累加,增加message 的條件當n%x 不是0,表示已無x 因數了,或是n==1,表示最後一筆

``` python
def primeFactors(n):    
    message=""
    x,count=2,0
    while(n!=1):       
        if n%x==0:
            count+=1            
            n=n//x              
        if n%x or n==1:
            if count==1:
               message+="({})".format(x)
            elif count>1:
               message+="({}**{})".format(x,count) 
            count=0
            x+=1  
    return messa
```











