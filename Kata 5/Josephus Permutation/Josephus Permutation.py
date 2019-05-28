def josephus(items, k):
    i, result = 0, []
    while len(items) > 0:
        i = (i + k - 1) % len(items)
        result.append(items.pop(i))
    return result
	
    
def josephus(items,k):
    reuslt,index=[],0    
    while items:   
        index=(index+k-1)%len(items)     
        reuslt.append(items[index])
        items.pop(index)        
    return reuslt
