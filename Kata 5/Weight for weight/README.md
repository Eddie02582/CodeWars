# Weight for weight

My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.</br>

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.</br>

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?</br>

## Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"</br>

When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9), it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

## Notes
<ul>
	<li>it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers</li>
	<li>Don't modify the input</li>
	<li>For C: The result is freed.</li>
</ul>



<sol> 依照題意,照數字總和排序,在照數字排序,先用空白切割數字,再利用sorted or sort()函數排序,用key指定排序方法

``` python
def order_weight2(strng):
	s=strng.split()
	s.sort(key=lambda x: (sum(int(n) for n in x),x))
	return " ".join(s)
```

一行的寫法
利用all
``` python
def order_weight(strng):
	return " ".join(sorted(strng.split(),key=lambda x: (sum(int(n) for n in x),x)))
```












