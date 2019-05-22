def prime(num):
    if num==2:
        return 1
    elif num<2:
        return 0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return 0    
    return 1

def prime_word(array):
    result=[]
    for arr in array:        
        s,n=arr[0],arr[1] 
        print (s,n)
        if any ( prime(n+ord(i)) >0 for i in s):
            result.append(1)
        else:
            result.append(0)       
   
    return result