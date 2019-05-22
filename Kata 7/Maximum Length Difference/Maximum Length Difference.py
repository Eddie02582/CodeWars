
'''
You are given two arrays a1 and a2 of strings. Each string is composed with letters 
from a to z. Let x be any string in the first array and y be any string in the second array.

Find max max(abs(length(x) - length(y))
If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

'''

def mxdiflg(a1, a2):   
    if  not (a1 or a2): 
        return -1
    else:
        return max([ abs(len(i)-len(j)) for i in a1 for j in a2 ])
		
		
def mxdiflg2(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1
	
def mxdiflg3(a1, a2):    
    return -1 if not(a1 and a2) else max(abs(len(x) - len(y)) for x in a1 for y in a2)
	
		
s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

print mxdiflg3(s1,s2)