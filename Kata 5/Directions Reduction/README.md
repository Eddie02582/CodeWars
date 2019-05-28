# Directions Reduction

IOnce upon a time, on a way through the old wild west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction and coming back the opposite direction is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed the desert the smart way.
The directions given to the man are, for example, the following:


The directions given to the man are, for example, the following:

```
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
```

You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

```
["WEST"].
```


## Solution

sol :建立一個新陣列,如果新陣列最後一個與下一個陣列相反,則把新陣列最後一個移除

``` python
def dirReduc(arr):
    opposite={'EAST':'WEST','WEST':'EAST','NORTH':'SOUTH','SOUTH':'NORTH'}
    new_plan = []
    for d in arr:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
```


sol :while 迴圈,離開條件當所有判斷完,如果陣列值i與i+1值相反,則pop出,直到沒有為止</br>
注意:pop i兩次,注意因為當第一次pop(i)時,原i+1會變成i,並重置i </br>
注意:當有相反值時i會回到0,如果當i+1 =len(arr) ,即表示所有相反都刪除完了</br>

``` python
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
    
```







