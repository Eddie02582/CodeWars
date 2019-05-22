# Jumping Number (Special Numbers Series #4)

<a href="https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed">原文</a>

## Definition
*Jumping number is the number that All adjacent digits in it differ by 1.*

## Task
Given a number, *Find if it is Jumping or not .*

Notes
<ul>
    <li>Number passed is always Positive .</li>
    <li>Return the result as String .</li>
    <li>The difference between ‘9’ and ‘0’ is not considered as 1 .</li>
    <li>All single digit numbers are considered as Jumping numbers.</li>
</ul>

## Input >> Output Examples
```
1- jumpingNumber(9) ==> return "Jumping!!"
```
## Explanation:
It's single-digit number
```
2- jumpingNumber(79) ==> return "Not!!"
```
## Explanation:
Adjacent digits don't differ by 1
```
3- jumpingNumber(23) ==> return "Jumping!!"
```
## Explanation:
Adjacent digits differ by 1
```
4- jumpingNumber(556847) ==> return "Not!!"
```
## Explanation:
Adjacent digits don't differ by 1
```
5- jumpingNumber(4343456) ==> return "Jumping!!"
```
## Explanation:
Adjacent digits differ by 1
```
6- jumpingNumber(89098) ==> return "Not!!"
```
## Explanation:
Adjacent digits don't differ by 1
```
7- jumpingNumber(32) ==> return "Jumping!!"
```

<sol> 一般解法將數字轉為字串,再將字串轉成數字陣列,前後比較差值是否為1

``` python
def jumping_number(number):  
    number=str(number)  
    for i in range(len(number)-1):
        if abs(int(number[i])-int(number[i-1])) is not 1:
            return "Not!!"
    return "Jumping!!"
```

``` python
def jumping_number(number):
    digits = [int(n) for n in list(str(number))]
    for i in range(len(digits)-1):
        if abs(digits[i] - digits[i+1]) != 1:
            return 'Not!!'
    return 'Jumping!!'
```

解法類似
``` python
def jumping_number(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]
```    


<sol> **最好解法** 利用遞迴,由後往前比較,每次傳入n/10遞迴直到數字<10

``` python
def jumping_number(n):
    if n <10:
        return "Jumping!!"
    elif abs (n%10 - (n/10)%10) is not 1:
        return "Not!!"
    else:
        return jumping_number(n/10)
     return "Jumping!!"
``` 










