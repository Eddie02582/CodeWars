def dig_pow(n, p):
    # your code
    a=sum(int(x)**(i) for i,x in  enumerate(str(n),p))    
    return  a/n  if a%n ==0 else -1
    
    
def dig_pow(n, p):
    number=str(n)
    total=0
    for i,x in enumerate(number,p):
        total+=int(x)**i   
    return -1 if total%n else total/n