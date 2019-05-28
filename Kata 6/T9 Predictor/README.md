# The nth smallest integer
## Task :
Given a List [] of n integers , find minimum mumber to be inserted in a list, so that sum of all elements of list should equal the closest prime number .



## Note

<ul>
    <li>List size is at least 2 .</li>
    <li>List's numbers will only positives (n > 0).</li>
    <li>Repeatition of numbers in the list could occur .</li>
    <li>The newer list's sum should equal the closest prime number </li>
</ul>

## Input >> Output Examples

```
1- minimumNumber ({3,1,2}) ==> return (1)
```

##　Explanation:
Since , the sum of the list's elements equal to (6) , the minimum number to be inserted to transform the sum to prime number is (1) , which will make *the sum of the List** equal the closest prime number (7)* .

```
2-  minimumNumber ({2,12,8,4,6}) ==> return (5)
```
## Explanation:
Since , the sum of the list's elements equal to (32) , the minimum number to be inserted to transform the sum to prime number is (5) , which will make *the sum of the List** equal the closest prime number (37)* .


```
3- minimumNumber ({50,39,49,6,17,28}) ==> return (2)
```

## Explanation:
Since , the sum of the list's elements equal to (189) , the minimum number to be inserted to transform the sum to prime number is (2) , which will make *the sum of the List** equal the closest prime number (191)* .



## Solution

sol :while迴圈如果是質數回傳增加的數

```python 
def minimum_number(numbers):
    n=sum(numbers)  
    add=0
    while True:
        if is_prime(n+add):
            return add
        else:
            add += 1    
    return add

def is_prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        return all ( [n%i for i in range(2,int(n**0.5)+1)])
```