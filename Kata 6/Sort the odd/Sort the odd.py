def sort_array(source_array):
    length = len(source_array)
    for i in range(length-1):
        j,k=0,1
        while j < length-1-i and  k <  length-i :
            if source_array[j] % 2 and    source_array[k] % 2 :          
                if source_array[j] > source_array[k]:
                    source_array[j], source_array[k] = source_array[k], source_array[j] 
                j,k=k,k+1
            elif not source_array[j] % 2 :
                j,k=j+1,k
            elif not source_array[k] % 2 :
                j,k=j,k+1   
            if j==k:
                k=k+1             
    return  source_array


def sort_array(source_array):
    odds=sorted([ x for x in source_array if x % 2])    
    for i,x in enumerate(source_array):
        if x % 2:
           source_array[i]= odds.pop(0)           
    return source_array

def sort_array(source_array):
    odds=sorted([ x for x in source_array if x % 2])   
    return [ odds.pop(0) if x%2 else x for x in source_array]

