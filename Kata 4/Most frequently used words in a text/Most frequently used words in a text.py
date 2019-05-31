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

from collections import Counter
import re


def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]