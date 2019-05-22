# Jumping Number (Special Numbers Series #4)

<a href="https://www.codewars.com/kata/523f5d21c841566fde000009">原文</a>


Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.</br>

It should remove all values from list a, which are present in list b.</br>
```
ArrayDiff(new int[] {1, 2}, new int[] {1}) => new int[] {2}
```
If a value is present in b, all of its occurrences must be removed from the other:

```
ArrayDiff(new int[] {1, 2, 2, 2, 3}, new int[] {2}) => new int[] {1, 3}
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









