# optimize
'''
def find_x(n):
    x = 0
    for i in range(n):
        for j in range(2*n):
            x += i+j            	
    return x

'''
'''
  S(2) = 0+0 0+1 0+2 0+3
            1+0 1+1 1+2 1+3

            ────────────2N-1
      S(3) = 0+0 0+1 0+2 0+3 0+4 0+5 │
            1+0 1+1 1+2 1+3 1+4 1+5 │
            2+0 2+1 2+2 2+3 2+4 2+5 │
                                    N-1

      S(n) = Sigma(1 to n-1) * 2n + Sigma(1 to 2n-1) * n
          = n(n-1)/2 * 2n + 2n(2n-1)/2 * n
          = n^2(3n-2)
'''	
def find_x2(n):
	return n**3 + 2*(n**3 - n**2)
    
	

#print find_x(1)
print find_x2(12)
#print find_x(3)
#print find_x(9)
#print find_x(13)
#print find_x(15)