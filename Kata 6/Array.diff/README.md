# Arraydiff

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

Note:注意題目沒說array 排序過的

<sol> 簡單利用for 迴圈搭配 not in 

``` python
def array_diff(a, b):
    return [ x for x in a if x not in b]
```

<sol> 簡單利用for 迴圈搭配 all
利用all
``` python
def array_diff(a, b):
    return [ x for x in a if all (x !=y for y in b)]
```

<sol> 利用filter 搭配lambda
利用all
``` python
def array_diff(a, b):
    return filter(lambda i: i not in b, a)
```

** sol ** :若陣列以排序,或不能使用新額外陣列,可以使用下列方法,利用兩個指針p1,p2,當a[p1]<b[p2]時,p1指針往下移動,當a[p1]>b[p2]時,p2指針往下移動

``` python
def array_diff2(a, b):
    #a.sort()
    #b.sort()
    p1=0
    p2=0
    while(p2<len(b) and p1<len(a)):
        if(a[p1]==b[p2]):
            a.remove(a[p1])
        elif a[p1]<b[p2]:
            p1+=1
        elif a[p1]>b[p2]:
            p2+=1
    return a  
``` 











