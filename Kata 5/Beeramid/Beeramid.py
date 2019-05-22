def square(n):
	return sum( [i*i for i in range(1,n+1)])
    
def beeramid(bonus, price):    
    n=1
    while(True):
        if (price*square(n) > bonus):
            return n-1
        elif (price*square(n)== bonus):
            return n
        n=n+1
    return 0
	
	
def beeramid(bonus, price):
    if bonus<0:
        return 0
    n=0
    while bonus>0 :
        n=n+1
        bonus-=price*n**2	   
    return n-1 if bonus<0 else n
	
def beeramid(bonus, price):
    i = 0
    while bonus > 0:
        i += 1
        bonus -= price * i**2
        if bonus < 0: i -= 1
    return i
	
