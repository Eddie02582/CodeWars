#Sum of Digits  Digital Root
# digital_root(16)
# => 1 + 6
# => 7

# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6

# digital_root(132189)
# => 1 + 3 + 2 + 1 + 8 + 9
# => 24 ...
# => 2 + 4
# => 6

# digital_root(493193)
# => 4 + 9 + 3 + 1 + 9 + 3
# => 29 ...
# => 2 + 9
# => 11 ...
# => 1 + 1
# => 2


def digital_root(n):         
    while(n>10):        
        n=sum[int(digit) for digit in str(n)]    
    return n       
    

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
	
def digital_root(n):   
    while n>9:
        n=sum(map(int,str(n)))
    return n	
	
	
print digital_root(505600016516)