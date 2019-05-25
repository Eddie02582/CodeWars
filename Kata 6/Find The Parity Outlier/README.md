# Find The Parity Outlier
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.</br>


## Examples
```
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)



##Solution

sol odds and evens 分別存入odd and even ,回傳長度為1的值
```python
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)==1 else evens[0]
```	

sol: 同上
```python
def find_outlier(integers):    
    odd=[]
    even=[]
    for x in integers:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return  odd [0]if len(odd)==1 else even[0]
```	

sol: 先將陣列值除以2,總和為1的即是odd ,再利用list.index找出值的index,回傳integers[index]
```python	
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
   

```
   
 