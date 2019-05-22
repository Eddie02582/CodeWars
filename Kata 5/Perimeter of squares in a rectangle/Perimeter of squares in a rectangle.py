def perimeter(n):
	if n==0:
		return 4
    result=[1,1]
    for i in range(2,n+1):        
       result.append(result[-1]+result[-2])
    return 4*sum(result)
	
def perimeter(n):	
	result=[1,1]
	for i in range(1,n+1):
		if len(result)==1:
			result.append(result[-1])
		else:
			result.append(result[-1]+result[-2])
	return 4*sum(result)
	
########	
def fib(n):
    a, b = 0, 1

    for i in range(n+1):
        if i == 0:
            yield b 
        else:
            a, b = b, a+b
            yield b        

def perimeter(n):   
    return sum(fib(n)) * 4
##############
	
	
if __name__ == '__main__':
	pass