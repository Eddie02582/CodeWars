# Convert string to camel case
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.</br>

## Example:
```
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
```



## Solution

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

<sol> 與上面相同,用list comprehension
```python	
def to_camel_case(text):
    return ''.join(v.title() if i else v for i,v in enumerate(re.split('[_-]',text)))
```	    
