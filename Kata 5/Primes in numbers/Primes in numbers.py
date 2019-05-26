def primeFactors(n):
    dic={}    
    x=2         
    while(n!=1): 
        if n%x==0:
            dic[x]= dic.get(x,0)+1
            n=n//x                
        else:
            x+=1 
    return "".join(["({})".format(key) if dic[key]==1 else "({}**{})".format(key,dic[key]) for key in sorted(dic.keys())])