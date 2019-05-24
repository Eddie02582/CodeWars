Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.</br>

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)</br>

## Examples :
```
IQ.Test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

IQ.Test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
```

<sol> 判斷奇偶利用除以2餘數判斷
```python
def iq_test(numbers):
    reslut=[ int(i)%2 for i in numbers.split(' ')]
    return array.index(0)+1 if reslut.count(0)==1 else array.index(1)+1     
```  



```python
def iq_test(numbers):
    array=[int(x)%2 for x in numbers.split(' ')]
    return array.index(1)+1 if sum(array)==1 else array.index(0)+1   
```   
