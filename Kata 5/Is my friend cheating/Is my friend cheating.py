def removNb(n):
    # (1+n)*n/2+1=(a+1)(b+1)
    Sum=(1+n)*n/2+1
    result,b=[],n   
    while(b>0):
        a=Sum/b-1
        if (Sum %b ==0 and a <n):               
            result.append((a,b-1))
        b-=1
    return result