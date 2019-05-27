# Diophantine Equation

In mathematics, a Diophantine equation is a polynomial equation, usually with two or more unknowns, such that only the integer solutions are sought or studied.

In this kata we want to find all integers x, y (x >= 0, y >= 0) solutions of a diophantine equation of the form:

x <sup>2</sup> - 4 * y<sup>2</sup> = n
(where the unknowns are x and y, and n is a given positive number) in decreasing order of the positive xi.

If there is no solution return [] or "[]" or "". (See "RUN SAMPLE TESTS" for examples of returns).

## Examples:

```
solEquaStr(90005) --> "[[45003, 22501], [9003, 4499], [981, 467], [309, 37]]"
solEquaStr(90002) --> "[]"
```

## Hint:

x <sup>2</sup> - 4 * y<sup>2</sup>= (x - 2*y) * (x + 2*y)


## Solution
``` 
(x - 2*y)=p
(x + 2*y)=q
x=(p + q) / 2
y=(q - p) / 2
```
sol :利用迴圈,如果是其因數則會整除,在判斷解出來的x,y是否為整數 </br>



``` python
def sol_equa(n):
    result=[]
    end=int(n**0.5)+1
    for i in range(1,end+1):
        if n % i==0:  
            p , q= i , n//i                       
            if (p + q) % 2 == 0 and (p - q) % 4 == 0:       
                x =  (p + q) // 2
                y =  (q - p) // 4 
                result.append([x,y])            
    
    return result
```










