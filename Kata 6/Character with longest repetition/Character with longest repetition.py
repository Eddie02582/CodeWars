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
	
	
def longest_repetition(chars):
    from itertools import groupby
    return max(((char, len(list(group))) for char, group in groupby(chars)),
               key=lambda char_group: char_group[1], default=("", 0))
			   
def longest_repetition(chars):
    if not chars: return ("", 0)    
    longest = max(re.findall(r"((.)\2*)", chars), key=lambda x: len(x[0]))
    return (longest[1], len(longest[0]))