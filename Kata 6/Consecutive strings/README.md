# Consecutive strings
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.</br>

## Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"</br>

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".</br>

## Note
consecutive strings : follow one after another without an interruption</br>





<sol> 利用迴圈index 0 到 len(strarr) - k ,截取[index:index+k],找出最大長度

```python
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result
```	

<sol> 
```python	
def longest_consec(strarr, k):
    if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
        return ""
    lst = [''.join(strarr[i:i+k]) for i in range(len(strarr))]
    return max(lst, key= lambda x: len(x))
```	    
