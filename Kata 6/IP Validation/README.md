Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0..255 (included).</br>

Input to the function is guaranteed to be a single string.</br>

Examples
```
// valid inputs:
1.2.3.4
123.45.67.89

// invalid inputs:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
```

<sol> for 迴圈判斷是數字且範圍在[0,..255],且非0d開頭
```python
def is_valid_IP(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))
```   
<sol> 利用re配對ip,有配到在判斷範圍在[0,..255],且非0d開頭

```python 
import re
def is_valid_IP(strng):
    match=re.match(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",strng)     
    if match:
        return all (str(int(n))==n  and 0<=int(n)<=255 for n in  match[0].split('.'))        
    else:
        return False
```

```python 
import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))
 ```