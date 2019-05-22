def tidyNumber(n):
    #pass  
    arr=list(str(n))
    for i in range (1,len(arr)):
        if int(arr[i])-int(arr[i-1]) <0:
            return False
    return True
	
	
#判斷是否所有後面的值大於前面	
def tidyNumber(n): 
	arr=list(str(n))
	return all (int(arr[i])- int(arr[i-1]) >=0 for i in range (1,len(arr))) 
	
#判斷排序完的值是否與位排序一樣
def tidyNumber(n):
    s = list(str(n))
    return s == sorted(set(s))
	
def tidyNumber(n):    
    return str(n) == ''.join(sorted(list(str(n))))
	