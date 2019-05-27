def list_squared(m, n):
    result=[]
    for i in range(m,n):
        total=0
        for j in range(1,int(i**0.5)+1):
            if i % j==0:
                p,q=j,i//j
                if p == q:
                    total+=p**2
                else:
                    total+=p**2+q**2
        if total**0.5==int (total**0.5):
            result.append([i,total])
    return result
