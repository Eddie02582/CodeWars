# Character with longest consecutive repetition

For a given string s find the character c with longest consecutive repetition and return a tuple (c, l) (in Haskell Just (Char, Int), in C# Tuple<char?, int>, in Shell a String of comma-separated values c,l, in JavaScript [c,l], in Ruby [c, l], in Groovy [c, l]) where l is the length of the repetition. If there are two or more characters with the same l return the first.</br>

For empty string return ('', 0) (in Haskell Nothing, in C# Tuple<char, int>(null, 0), in Shell ,0, in JavaScript ["",0], in Ruby ["", 0], in Groovy ["", 0]).</br>

## Solution

sol: 利用迴圈判斷如果是相同字元count+=1,如果是不同字元count=1
```python
def longest_repetition(chars):
    max=0
    count=1
    temp=""
    for i in range(0,len(chars)-1):
        if chars[i]==chars[i+1]:
            count+=1
        else:
            count=1
            
        if count>max :
            temp=chars[i]            
            max= count   
    return (temp,max)
```	

sol:  利用groupby
```python	
def longest_repetition(chars):
    from itertools import groupby
    return max(((char, len(list(group))) for char, group in groupby(chars)),
               key=lambda char_group: char_group[1], default=("", 0))
```	    

sol: 利用re 配對,再取出長度最長的        
```python	
import re			   
def longest_repetition(chars):
    if not chars: return ("", 0)    
    longest = max(re.findall(r"((.)\2*)", chars), key=lambda x: len(x[0]))
    return (longest[1], len(longest[0]))
```	