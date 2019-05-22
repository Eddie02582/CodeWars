'''
arr = [12, 10, 8, 12, 7, 6, 4, 10, 12];
highestRank(arr) //=> returns 12


arr = [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10];
highestRank(arr) //=> returns 3
'''


import operator
def highest_rank(arr):
    # your code here
    dic={}
    for i in arr:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]=dic[i]+1    
    return max(dic.iteritems(), key=operator.itemgetter(1,0))[0]
	
#for 2.7	
import operator
from collections import Counter
def highest_rank(arr):    
    return max(Counter(arr).iteritems(), key=operator.itemgetter(1,0))[0]
	
#for 3.6	
import operator
from collections import Counter
def highest_rank(arr):    
    return max(Counter(arr).items(), key=operator.itemgetter(1,0))[0]	
	
def highest_rank(arr):
    return sorted(arr,key=lambda x: (arr.count(x),x))[-1]