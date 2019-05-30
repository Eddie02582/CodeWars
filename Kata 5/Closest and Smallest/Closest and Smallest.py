def closest(strng):
    if strng=="":
        return []

    weight= sorted([ [ sum(map(int,n)), i, int(n)]  for i,n in enumerate(strng.split()) ],key= lambda x:(x[0],x[1]))
    delta,position=weight[-1][0],0
    index=len(weight)
    
    for i in range(len(weight)-1):        
        if weight[i+1][0]-weight[i][0] < delta:            
                position=i
                delta=weight[i+1][0]-weight[i][0]
            
    return [weight[position] ,weight[position+1] ]


def closest(strng):
    weight = sorted([ [sum(int(c) for c in n), i, int(n)] for i, n in enumerate(strng.split()) ], key=lambda x: (x[0], x[1]))
    diff = [ abs(a[0] - b[0]) for a, b in zip(weight, weight[1:]) ]
    index=diff.index(min(diff))
    return  [ weight [index ], weight [index+ 1] ] if weight else []