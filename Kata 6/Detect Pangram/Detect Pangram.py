import string

def is_pangram(s):
    return len([ x for x in set(s.lower()) if ord('a')<= ord(x)<= ord('z') ])==26  

def is_pangram(s):
    attend=[False]*26
    for x in s.upper():
        if ord('A')<= ord(x)<=ord('Z'):
            attend[ ord(x)-ord('A')]=True
    
    return all (attend) 
 
	
import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
