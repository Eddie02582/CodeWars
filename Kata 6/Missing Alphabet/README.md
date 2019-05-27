# Missing Alphabet
In this Kata you have to create a function,named insertMissingLetters,that takes in a string and outputs the same string processed in a particular way.</br>

The function should insert only after the first occurence of each character of the input string, all the alphabet letters that:</br>

-are NOT in the original string</br>
-come after the letter of the string you are processing</br>

Each added letter should be in uppercase, the letters of the original string will always be in lowercase.</br>

Example:</br>

input: "holly"</br>

missing letters: "a,b,c,d,e,f,g,i,j,k,m,n,p,q,r,s,t,u,v,w,x,z"</br>

output: "hIJKMNPQRSTUVWXZoPQRSTUVWXZlMNPQRSTUVWXZlyZ"</br>

You don't need to validate input, the input string will always contain a certain amount of lowercase letters (min 1 / max 50).</br>

## Solution

<sol>迴圈每個字元,在判斷字元是否在word 內沒有,加入該字元後不在字串裡面的字元
```python
    word=''
    for x in st:
        if x not in word:
            word+=x+"".join([ chr(i).upper() for i in range(ord(x),ord('z')+1) if chr(i) not in st ])  
        else:
            word+=x
    return word
```

```python
def insert_missing_letters(st):
    letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result=""
    for s in st:  
        result=result+s
        if result.count(s) ==1:          
            index=letters.index(s.upper())            
            add=sorted(list(set(letters[index:])-set(list(st.upper()))))
            result+=''.join(add)
```