
'''
You are given two arrays a1 and a2 of strings. Each string is composed with letters 
from a to z. Let x be any string in the first array and y be any string in the second array.

Find max max(abs(length(x) - length(y))
If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

'''

		
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1
	
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1
    
def mxdiflg(a1, a2):
    if not (a1 and a2): return -1
    l1 = list(map(len, a1))
    l2 = list(map(len, a2))
    return max((max(l1)-min(l2)), (max(l2)-min(l1)))
    
	
def mxdiflg4(a1, a2):
    if not a1 or not a2:
        return-1
    max_1,max_2,min_1,min_2=0,0,0,0    
    len_1=len(a1)
    len_2=len(a2)    
    lens=max(len_1,len_2)
    for i in range(lens):
        if (i<len_1):
            if a1[i]>max_1:
                max_1=a1[i]
            elif a1[i] <min_1:
                min_1=a1[i]
        if (i<len_2):
            if a2[i]>max_1:
                max_2=a2[i]
            elif a2[i] <min_1:
                min_2=a2[i]                
    
    return max([max_1-min_2,max_2-min_1])	


	
s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

print mxdiflg3(s1,s2)