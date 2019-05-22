def longest_repetition(chars):
    if len(chars)==0:
        return ("",0)
    tempCount=1
    Count=0
    templetter=''
    letter=chars[0]
    for c in chars:
        if c !=templetter:
            templetter=c
            tempCount=1
        else :
            tempCount+=1
        if tempCount>Count:
            Count=tempCount
            letter=templetter        
    return (letter,Count)
	
	
def longest_repetition(chars):
    from itertools import groupby
    return max(((char, len(list(group))) for char, group in groupby(chars)),
               key=lambda char_group: char_group[1], default=("", 0))
			   
def longest_repetition(chars):
    if not chars: return ("", 0)    
    longest = max(re.findall(r"((.)\2*)", chars), key=lambda x: len(x[0]))
    return (longest[1], len(longest[0]))