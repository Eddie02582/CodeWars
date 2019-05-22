def fibonacci(n):   
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1)+fibonacci(n-2)
    
def padovan(n):   
    if n == 0: return 1
    elif n == 1: return 0
    elif n == 2: return 0
    else: return padovan(n-2)+padovan(n-3)    
  
def jacobsthal(n):   
    if n == 0: return 0
    elif n == 1: return 1 	
    else: return jacobsthal(n-1)+2*jacobsthal(n-2)  
	
def Pell (n):   
    if n == 0: return 0
    elif n == 1: return 1 
    else: return 2*Pell(n-1)+Pell(n-2) 

def Tribonacci (n):   
    if n == 0: return 0
    elif n == 1: return 0 
    elif n == 2: return 1 
    else: return Tribonacci(n-1)+Tribonacci(n-2)+Tribonacci(n-3)
	
def Tetranacci (n):   
    if n == 0 or n == 1 or n==2 : return 0
    elif n == 3: return 1 
    else: return Tetranacci(n-1)+Tetranacci(n-2)+Tetranacci(n-3)+Tetranacci(n-4)

def mixbonacci(pattern, length):
    if not pattern or length<=0:
        return []
    result=[]
    f,n,j,p,t,te=0,0,0,0,0,0   
    for i in range(length):      
        count=i%len(pattern)    
        if pattern[count]=='fib':
            result.append(fibonacci(f))
            f+=1
        elif pattern[count]=='pad':
            result.append(padovan(n))
            n+=1    
        elif pattern[count]=='jac':
            result.append(jacobsthal(j))
            j+=1 			
        elif pattern[count]=='pel':
            result.append(Pell(p))
            p+=1 
        elif pattern[count]=='tri':
            result.append(Tribonacci(t))
            t+=1 
        elif pattern[count]=='tet':
            result.append(Tetranacci(te))
            te+=1 
    return result