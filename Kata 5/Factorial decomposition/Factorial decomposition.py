def decomp2(n):
    dic={}
    for i in range(2,n+1):
        x,t=2,i         
        while(t!=1 and x<=i): 
            if t%x==0:
                dic[x]= dic.get(x,0)+1
                t=t//x                
            else:
                x+=1   
    result=[]
	
    for key in sorted(dic.keys()):
        if dic[key]>1: 
            result.append("%s^%s" %(key,dic[key]))
        else:
            result.append("%s" %(key))     
    return " * ".join(result)


def decomp(n):
    dic={}
    for i in range(2,n+1):
        x,t=2,i         
        while(t!=1 and x<=i): 
            if t%x==0:
                dic[x]= dic.get(x,0)+1
                t=t//x                
            else:
                x+=1 
    return " * ".join([str(key) if dic[key]==1 else "{}^{}".format(key,dic[key]) for key in sorted(dic.keys())])
    
print (decomp(12))