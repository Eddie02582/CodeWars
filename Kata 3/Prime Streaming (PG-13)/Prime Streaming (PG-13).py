class Primes:    
    @staticmethod      
    def is_prime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True      

    @staticmethod
    def stream():
        x=1        
        while True:
            x+=1
            if Primes.is_prime(x):                
                yield x
         
        
        
        
class Primes:    

    @staticmethod
    def stream():
        D = {}           
        q = 2
        while True:
            if q not in D:
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1
            
       
