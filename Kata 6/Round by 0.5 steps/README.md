# Round by 0.5 steps

Round any given number to the closest 0.5 step

```
    solution(4.2) = 4
    solution(4.3) = 4.5
    solution(4.6) = 4.5
    solution(4.8) = 5
```
Round up if number is as close to previous and next 0.5 steps.

```
    solution(4.75) == 5
```


## Solution
<sol>

```python 
def solution(n):
    num=int(n)
    if n < num +0.25:
        return num
    elif num +0.25 <=n < num +0.75:    
        return num+0.5      
    else:    
        return num+1  
```

```python 
def solution(n):
    return round(2 * n) / 2
```
