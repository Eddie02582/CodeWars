
def revrot_1(strng, sz):
    if sz <= 0 or strng == "" or sz > len(strng):
        return ""  
    result=""
    for i in range(0, len(strng) // sz):
		part = strng[sz*i:sz*(i + 1)]
		if sum(map(lambda x:int(x),s))%2 ==0 
            result+=part[::-1])
	    else:
            result+=part[1:]+part[0] 
    return result
	
	
def revrot_2(strng, sz):
    if not strng or sz < 1 or sz > len(strng):
        return ""
    res=""
    while len(s) >= n:
        group = sz[:n]
        if sum(map(lambda x:int(x),s)) % 2 == 0:
            res += group[::-1]
        else:
            res += group[1:] + group[0]
        sz = s[n:]
    
    return res