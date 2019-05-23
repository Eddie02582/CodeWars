def find_it(seq):
    n=0
    for x in seq:
        n^=x      
    return n
    
import operator

def find_it(xs):
    return reduce(operator.xor, xs)