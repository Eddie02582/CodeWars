# Playing with digits

Some numbers have funny properties. For example:</br>

```
89 --> 81 + 92 = 89 * 1

695 --> 62 + 93 + 5?= 1390 = 695 * 2

46288 --> 43 + 6?+ 2? + 8? + 8? = 2360688 = 46288 * 51

```
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n. In other words:</br>

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k </br>

If it is the case we will return k, if not return -1.</br>

Note: n, p will always be given as strictly positive integers.</br>

```
digPow(89, 1) should return 1 since 81 + 92 = 89 = 89 * 1
digPow(92, 1) should return -1 since there is no k such as 91 + 22 equals 92 * k
digPow(695, 2) should return 2 since 62 + 93 + 5?= 1390 = 695 * 2
digPow(46288, 3) should return 51 since 43 + 6?+ 2? + 8? + 8? = 2360688 = 46288 * 51

```
## Solution
<sol>

```python 
def dig_pow(n, p):
    # your code
    a=sum(int(x)**(i) for i,x in  enumerate(str(n),p))    
    return  a/n  if a%n ==0 else -1
```
