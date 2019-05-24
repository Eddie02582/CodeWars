# Highest Rank Number in an Array
Write a method highestRank(arr) (or highest-rank in clojure) which returns the number which is most frequent in the given input array (or ISeq). If there is a tie for most frequent number, return the largest number of which is most frequent.</br>

Example:
```
var arr = new int[] { 12, 10, 8, 12, 7, 6, 4, 10, 12 };
Kata.HighestRank(arr) //=> returns 12

arr = new int[] { 12, 10, 8, 12, 7, 6, 4, 10, 12, 10 };
Kata.HighestRank(arr) //=> returns 12

var arr = new int[] { 12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10 };
Kata.HighestRank(arr) //=> returns 3
```

<sol> 排序 以(arr.count(x),x)排序方式,先排arr.count(x)在排x
```python
def highest_rank(arr):
    return sorted(arr,key=lambda x: (arr.count(x),x))[-1]
```	

<sol> 利用counter 得到每個數字的個數字典{num:count,...},再透過.items轉成turple,依照 key=operator.itemgetter,依照0,1順序取出最大值</br>
ex:arr=[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]</br>
   Counter(arr)===> Counter({3: 4, 10: 3, 12: 2, 8: 2, 2: 1, 4: 1})</br>
   Counter(arr).items()==>dict_items([(12, 2), (10, 3), (8, 2), (3, 4), (2, 1), (4, 1)])</br>


```python
#for 3.6	
import operator
from collections import Counter
def highest_rank(arr):    
    return max(Counter(arr).items(), key=operator.itemgetter(1,0))[0]	
```	

<sol> #for 2.7	同上items改成iteritems()
```python
import operator
from collections import Counter
def highest_rank(arr):    
    return max(Counter(arr).iteritems(), key=operator.itemgetter(1,0))[0] 
```
   
