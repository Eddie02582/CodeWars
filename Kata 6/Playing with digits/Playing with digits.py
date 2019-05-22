def dig_pow(n, p):
    # your code
    a=sum(int(x)**(i+p) for i,x in  enumerate(str(n)))
    
    return  a/n  if a%n ==0 else -1