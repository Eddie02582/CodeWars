# Convert string to camel case
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).</br>

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.</br>


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

<sol> 
```python	3.6
import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())
```	    


```python	
def is_pangram(s):
    return len([ x for x in set(s.lower()) if ord('a')<= ord(x)<= ord('z') ])==26  
```	

```python	
import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
```	