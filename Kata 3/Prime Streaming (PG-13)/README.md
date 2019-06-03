## Prime Streaming (PG-13)
Create an endless stream of prime numbers - a bit like IntStream.of(2, 3, 5, 7, 11, 13, 17), but infinite. The stream must be able to produce a million primes in a few seconds.


sol :timeout
```python
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
         
```        
 sol :timeout    <a href ="http://code.activestate.com/recipes/117119/">°Ñ¦Òºô§}</a>   
```python        
class Primes:    

    @staticmethod
    def stream():
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        #
        D = {}
        
        # The running integer that's checked for primeness
        q = 2
        
        while True:
            if q not in D:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                # 
                yield q
                D[q * q] = [q]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next 
                # multiples of its witnesses to prepare for larger
                # numbers
                # 
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            
            q += 1
```   

sol
```python        
class Primes:  
    @staticmethod
    def stream():
        yield 2
        D = {}
        q = 3
        while True:
            p = D.pop(q, 0)
            if p:
                x = q + p
                while x in D: x += p
                D[x] = p
            else:
                yield q
                D[q*q] = 2*q
            q += 2
```            
    


















         
            