# Factorial decomposition

The aim of the kata is to decompose n! (factorial n) into its prime factors.

Examples:
```
n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.

n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"

n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
Prime numbers should be in increasing order. When the exponent of a prime is 1 don't put the exponent.
```

Notes
<ul>the function is decomp(n) and should return the decomposition of n! into its prime factors in increasing order of the primes, as a string.</li>
	<lifactorial can be a very big number (4000! has 12674 digits, n will go from 300 to 4000).</li>
	<liIn Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings</li>
	
</ul>




<sol> 第一個迴圈2到n,在依序拆解找出質因數</br>
      第二個迴圈用一指針由2開始,若整除指針表示含有因數,並利用字典記錄個數,若不整除,指針加1,直到數字變1,表示找完因數

``` python
def decomp(n):
    dic={}
    for i in range(2,n+1):
        x,t=2,i         
        while t!=1: 
            if t%x==0:
                dic[x]= dic.get(x,0)+1
                t=t//x                
            else:
                x+=1   
    result=[]
	
    for key in sorted(dic.keys()):
        if dic[key]>1: 
            result.append("%s^%s" %(key,dic[key]))
        else:
            result.append("%s" %(key))     
    return " * ".join(result)
```













