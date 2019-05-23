def array_diff(a, b):
    return [ x for x in a if all (x !=y for y in b)]
	
def array_diff(a, b):
    return [ x for x in a if x not in b]
	
def array_diff(a, b):   
    return filter(lambda i: i not in b, a)
    
def array_diff2(a, b):
    a.sort()
    b.sort()
    p1=0
    p2=0
    while(p2<len(b) and p1<len(a)):
        if(a[p1]==b[p2]):
            a.remove(a[p1])
        elif a[p1]<b[p2]:
            p1+=1
        elif a[p1]>b[p2]:
            p2+=1
    return a    
	
