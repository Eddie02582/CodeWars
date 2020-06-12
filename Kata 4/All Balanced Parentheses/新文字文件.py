def solution(string,markers):    
    import re
    if  not markers:    
        return string
      
    res  = string.split('\n') 
    if  not markers:    
        return string
        
    express = '[{0}].*'.format(key)
    for i in range(len(res)):        
        res[i] = re.sub(express,"",res[i])
        res[i] = res[i].rstrip()
    
    return "\n".join(res)
    

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", []) )
