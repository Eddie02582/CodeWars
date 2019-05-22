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

def f(fc):
    n = 0
    while n+1:
        yield fc(n)
        n += 1

def mixbonacci(pattern, length):
    if not pattern or length<=0:
        return []
    result=[]
    fi,n,j,p,t,te=f(fibonacci),f(padovan),f(jacobsthal),f(Pell),f(Tribonacci),f(Tetranacci)
    fis=[0,1]
    pas=[]
	
    for i in range(length):      
        count=i%len(pattern)    
        if pattern[count]=='fib':
            result.append(fi.next())            
        elif pattern[count]=='pad':
            result.append(n.next())            
        elif pattern[count]=='jac':
            result.append(j.next())          	
        elif pattern[count]=='pel':
            result.append(p.next())          
        elif pattern[count]=='tri':
            result.append(t.next())           
        elif pattern[count]=='tet':
            result.append(te.next())
            
    return result