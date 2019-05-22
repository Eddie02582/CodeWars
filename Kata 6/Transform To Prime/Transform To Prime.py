def minimum_number(numbers):
    if numbers == 1: return false
    sums=sum(numbers)
    while(True):
        bZero= all (sums%i >0 for i in range(2,int(sums**0.5)+1,1))
        if bZero:
            return sums-sum(numbers)
        sums=sums+1
		
		
		
def minimum_number(numbers):
    if numbers == 1: return false
    sums=sum(numbers)
    while(True):        
        if all (sums%i for i in range(2,int(sums**0.5)+1,1)):
            return sums-sum(numbers)
        sums=sums+1