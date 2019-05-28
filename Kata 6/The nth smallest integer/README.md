# The nth smallest integer

Given a list of integers, return the nth smallest integer in the list. Only distinct elements should be considered when calculating the answer. n will always be positive (n > 0) </br>

If the n<sup>th</sup> small integer doesn't exist, return -1 (C++) / None (Python) / nil (Ruby) / null (JavaScript).

Notes:

<ul>
    <li>"indexing" starts from 1</li>
    <li>huge lists (of 1 million elements) will be tested</li>
</ul>


## Example

```
nth_smallest([1, 3, 4, 5], 7)        ==> None  # n is more than the size of the list
nth_smallest([4, 3, 4, 5], 4)        ==> None  # 4th smallest integer doesn't exist
nth_smallest([45, -10, 4, 5, 4], 4)  ==> 45    # 4th smallest integer is 45
```

## Solution

sol :利用set,再排序,再取出n-1位置

```python 
def nth_smallest(arr, n):
    array= sorted(list(set(arr)))
    if n> len(array):
        return None
    else:
        return array[n-1]       
```
