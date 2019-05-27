def solution(n):
    num=int(n)
    if n < num +0.25:
        return num
    elif num +0.25 <=n < num +0.75:    
        return num+0.5      
    else:    
        return num+1  