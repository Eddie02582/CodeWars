# Most frequently used words in a text

Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.</br>


## Assumptions:
<ul>
    <li>A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to handle fancy punctuation.)</li>
    <li>Matches should be case-insensitive, and the words in the result should be lowercased.</li>
    <li>Ties may be broken arbitrarily.</li>
    <li>If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.</li>
</ul>



## Examples:

```
top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
```


## Solution

sol :先轉成小寫在切割非a-z 和 ' ,再利用counter計數排序,接著取出前三項不含只有'的字

``` python
from collections import Counter
import re
def top_3_words(text):
    count_array=sorted( Counter(re.split(r"[^a-z\']",text.lower())).items() ,key= lambda x:(-x[1],x[0]))   
    result=[]
    for x in count_array:
        word=x[0].replace("'","")
        if word.isalpha(): 
            result.append(x[0])
        if len(result)==3:
            return result    
    return result
```

sol :利用re.sub將" ' "取代" "在切跟非a-z ,最後再取出most_common(3)
``` python
from collections import Counter
import re

def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]
```







