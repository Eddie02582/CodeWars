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
        
        if any ( prime(n+ord(i)) >0 for i in s):
            result.append(1)
        else:
            result.append(0)       
   
    return result
    
def prime_word(array):
    result=[0]*len(array)
    for index,x in enumerate(array):
        word,add=x
        for c in word:
            value=ord(c)+add 
            is_prime=True
            for i in range(2,int(value**0.5)+1):
                if value % i ==0:
                    is_prime=False
            if is_prime==True and c != 1:
                result[index]=1
                break                 
    return result