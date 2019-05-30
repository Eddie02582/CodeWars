# Square Matrix Multiplication

Write a function that accepts two square (NxN) matrices (two dimensional arrays), and returns the product of the two. Only square matrices will be given.</br>
Sort these integers for me ...</br>


## Example
```
 A         B          C
|1 2|  x  |3 2|  =  | 5 4|
|3 2|     |1 1|     |11 8|
```

Detailed calculation:
```
C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0] = 1*3 + 2*1 =  5
C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1] = 1*2 + 2*1 =  4
C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0] = 3*3 + 2*1 = 11
C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1] = 3*2 + 2*1 =  8
```


sol:矩陣相乘,每個row x 每個col,最後一個迴圈負責處理元素相乘

``` python
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

```













