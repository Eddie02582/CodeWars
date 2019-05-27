def sol_equa(n):
    result=[]
    end=int(n**0.5)+1
    for i in range(1,end+1):
        if n % i==0:  
            p , q= i , n//i                       
            if (p + q) % 2 == 0 and (p - q) % 4 == 0:       
                x =  (p + q) // 2
                y =  (q - p) // 4 
                result.append([x,y])            
    
    return result