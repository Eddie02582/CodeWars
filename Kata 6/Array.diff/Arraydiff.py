def array_diff(a, b):
    return [ x for x in a if all (x !=y for y in b)]
	
def array_diff(a, b):
    return [ x for x in a if x not in b]
	
def array_diff(a, b):   
    return filter(lambda i: i not in b, a)