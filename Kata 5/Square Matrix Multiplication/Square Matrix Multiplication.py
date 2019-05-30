def matrix_mult(a, b):
    n=len(a)
    result=[]
  
    for row in range(n):
        rows=[]
        for col in range(n):       
            left=a[row]
            right=[b[x][col] for x in range(n)]              
            rows.append(sum([ x*y for x,y in zip(left,right)]))       
            print (row,col)
        result.append(rows)
    return result
  
a=[[1, 2],[3, 2]]
b=[[3, 2],[1, 1]]


def matrix_mult(a, b):
    n=len(a)    
    result=[]
  
    for row in range(n):
        rows=[]
        for col in range(n):
            value=0
            for k in range(n):
                value+=a[row][k]*b[k][col]            
            rows.append(value)       
          
        result.append(rows)
    return result



print (matrix_mult (a,b))
 #3997
