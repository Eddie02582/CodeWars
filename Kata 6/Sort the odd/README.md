# Sort the odd

You have an array of numbers.</br>
Your task is to sort ascending odd numbers but even numbers must be on their places.</br>

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.</br>

Example

```
    sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
```


## Solution

sol:先將奇數取出並排序,在取代原陣列奇數位置的值



```python 
def sort_array(source_array):
    odds=sorted([ x for x in source_array if x % 2])    
    for i,x in enumerate(source_array):
        if x % 2:
           source_array[i]= odds.pop(0)           
    return source_array 
```
