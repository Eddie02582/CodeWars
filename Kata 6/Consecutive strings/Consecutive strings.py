
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result
 
def longest_consec(strarr, k):
    if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
        return ""
    lst = [''.join(strarr[i:i+k]) for i in xrange(len(strarr))]
    return max(lst, key= lambda x: len(x))

def longest_consec(strarr, k):
    if len(strarr)==0 or k > len(strarr) or k <= 0:
        return ""

    len_array=list(map(lambda x:len(x),strarr))   
    temp=0
    array=[]
    for i in range(len(strarr) - k + 1):
        len_sum= sum(len_array[i:i+k])   
        if len_sum >temp:
           temp=len_sum
           array=strarr[i:i+k]
    return "".join(array)  

