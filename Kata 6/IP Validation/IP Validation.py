def is_valid_IP(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))
    
import re
def is_valid_IP(strng):
    match=re.match(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",strng)     
    if match:
        return all (str(int(n))==n  and 0<=int(n)<=255 for n in  match[0].split('.'))        
    else:
        return False
       
        

def is_valid_IP(strng):
    lst = strng.split('.')
    passed = 0
    for sect in lst:
        if sect.isdigit():
            if sect[0] != '0':
                if 0 < int(sect) <= 255:
                    passed += 1
    return passed == 4

import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))