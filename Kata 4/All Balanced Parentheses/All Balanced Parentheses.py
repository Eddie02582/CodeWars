def balanced_parens(n):
    
    res = []
    def dfs(l,r,s):
        if len(s) == 2*n:
            res.append(s)
        if l:
            dfs(l - 1,r, s + "(")
        if r > l:
            dfs(l,r - 1, s + ")") 
        

    dfs(n,n,"")
    return res 