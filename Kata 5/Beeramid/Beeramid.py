def beeramid(bonus, price):
    i = 0
    while bonus > 0:
        i += 1
        bonus -= price * i**2
        if bonus < 0: i -= 1
    return i
	
def beeramid(bonus, price):    
    j=0
    while True: 
        bonus-=price*j*j      
        if bonus < (j+1)**2*price:
            break 
        j+=1 
    return j