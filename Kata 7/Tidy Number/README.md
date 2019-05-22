# Jumping Number (Special Numbers Series #4)

<a href="https://www.codewars.com/kata/5a87449ab1710171300000fd">原文</a>

## Definition
*A Tidy number is a number whose digits are in non-decreasing order.*

## Task
Given a number, *Find if it is Jumping or not .*

Notes
<ul>
    <li>Number passed is always Positive .</li>
    <li>Return the result as a Boolean</li>   
</ul>

## Input >> Output Examples
```
1- tidyNumber (12) ==> return (true)
```
## Explanation:
The number's digits { 1 , 2 } are in non-Decreasing Order (i.e) 1 <= 2 .
```
2- tidyNumber (32) ==> return (false)
```
## Explanation:
The Number's Digits { 3, 2} are not in non-Decreasing Order (i.e) 3 > 2 .
```
3- tidyNumber (1024) ==> return (false)
```
## Explanation:
The Number's Digits {1 , 0, 2, 4} are not in non-Decreasing Order as 0 <= 1 .
```

<sol> 一般解法將數字轉為字串,再將字串轉成數字陣列,前後比較差值是否為1

``` python
def tidyNumber(n):
    #pass  
    arr=list(str(n))
    for i in range (1,len(arr)):
        if int(arr[i])-int(arr[i-1]) <0:
            return False
    return True
```

利用all
``` python
def tidyNumber(n): 
	arr=list(str(n))
	return all (int(arr[i])- int(arr[i-1]) >=0 for i in range (1,len(arr))) 
```



<sol> 判斷排序完的值是否與位排序一樣

``` python
def tidyNumber(n):
    s = list(str(n))
    return s == sorted(set(s))
``` 

``` python
def tidyNumber(n):    
    return str(n) == ''.join(sorted(list(str(n))))
``` 









