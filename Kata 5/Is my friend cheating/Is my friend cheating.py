def removNb(n):
    result=[]
    total= n*(n+1)/2

    for x in range(1,n+1):
        y= (total-x)//(x+1)
        if (total-x)%(x+1)==0 and y <=n:
            result.append((x,y))  
    return result