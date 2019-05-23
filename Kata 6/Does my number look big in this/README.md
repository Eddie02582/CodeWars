# Does my number look big in this
A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).</br>

For example, take 153 (3 digits):</br>
```
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
``
and 1634 (4 digits):
```
    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
```

<sol> 切割 _和-,如果i==0,維持原字串,其他轉成title 型式

```python
import re
def to_camel_case(text):
    a=[]
    for i,v in enumerate(re.split('[_-]',text)):
        if i:
            a.append(v.title())
        else:
            a.append(v)    
    
    return ''.join(a)
```	

