def dirReduc(arr):    
    dic={'EAST':'WEST','WEST':'EAST','NORTH':'SOUTH','SOUTH':'NORTH'}
    i=0    
    while i+1<len(arr):
        if arr[i]==dic[arr[i+1]]:
            arr.pop(i)
            arr.pop(i)
            i=0          
        else:
            i+=1            
    return arr
    
    
def dirReduc(arr):
    opposite={'EAST':'WEST','WEST':'EAST','NORTH':'SOUTH','SOUTH':'NORTH'}
    new_plan = []
    for d in arr:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan