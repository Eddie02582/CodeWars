# The nth smallest integer

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in an array like so: [index1, index2].</br>

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.</br>

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).</br>

Based on: http://oj.leetcode.com/problems/two-sum/</br>


```python 
def two_sum(numbers, target):
    dic={}
    for index,n in enumerate(numbers):
        if target-n in dic:
            return [dic[target-n] ,index]      
        dic[n]=index
    return []
```