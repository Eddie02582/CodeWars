def persistence(n):   
    count=0    
    while n >= 10: 
        count += 1 
        total=1      
        for x in str(n):
            total*=int(x)           
        n=total  
    return count


import operator
import functools
def persistence(n):
    i = 0
    while n>=10:
        n=functools.reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i