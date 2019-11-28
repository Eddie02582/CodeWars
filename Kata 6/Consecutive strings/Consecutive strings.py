
def longest_consec(strarr, k):
    if k > 0 and len(strarr) >= k:
        return ""
        
    result = ""    
    for index in range(len(strarr) - k + 1):
        s = ''.join(strarr[index:index+k])
        if len(s) > len(result):
            result = s
            
    return result
 
 
def longest_consec(strarr, k):
    if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
        return ""
    lst = [''.join(strarr[i:i+k]) for i in range(len(strarr))]
    return max(lst, key= lambda x: len(x))


