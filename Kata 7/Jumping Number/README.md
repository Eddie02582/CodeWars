# OddOccurrencesInArray

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
Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>N is an odd integer within the range [1..1,000,000];</li></br>
    <li>each element of array A is an integer within the range [1..1,000,000,000];</li></br>
    <li>all but one of the values in A occur an even number of times.</li></br>
</ul>


