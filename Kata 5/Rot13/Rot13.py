'''
ROT13 is a simple letter substitution cipher 
that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Please note that using "encode" in Python is considered cheating.
'''
# -*- coding: utf-8 -*-



#My sol


def rot13(message):
    en=list('abcdefghijklmnopqrstuvwxyz')  
    result=""
    for letter in  message :
        if letter in en:
            index=en.index(letter)
            result+=en[index-13]
        elif letter.lower() in en:
			index=en.index(letter.lower())
			result+=en[index-13].upper() 
        else:
            result+=letter
    return result	

import string
def rot13(message):
	trans = string.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz', 'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
	return message.translate(trans)	
	
	
from string import maketrans, lowercase, uppercase
#pick lower,Upper translatetable 
#maketrans(intab, outtab) 建立轉換表
def rot13(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)	
	
	
	
def rot13(message):
	return message.encode("rot13")