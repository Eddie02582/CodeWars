'''
find different odd or even in series
'''

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)==1 else evens[0]

def find_outlier_1(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
	
	
def find_outlier_2(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]