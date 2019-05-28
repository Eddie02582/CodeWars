def minimum_number(numbers):
    sums=sum(numbers)
    while　True　:        
        if all (sums%i for i in range(2,int(sums**0.5)+1,1)):
            return sums-sum(numbers)
        sums=sums+1
 
 
def minimum_number(numbers):
    n=sum(numbers)  
    add=0
    while True:
        if is_prime(n+add):
            return add
        else:
            add += 1    
    return add

def is_prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        return all ( [n%i for i in range(2,int(n**0.5)+1)])