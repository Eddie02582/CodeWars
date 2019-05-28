'''
Josephus Survivor
'''

#similar Josephus Permutation
def josephus_survivor(n, k):	
	items,i=[ x for x in range(1, n + 1)] ,0	
	while len(items) > 1:
		i = (i + k - 1) % len(items)
		items.pop(i)		
	return items[0]
	
def josephus_survivor_(n, k):
    return reduce(lambda x, y: (x+k)%y, xrange(0, n+1)) + 1
	
	
def josephus_survivor__(n, k):
    v = 0
    for i in range(1, n + 1): v = (v + k) % i
    return v + 1

