# Sort - one, three, two

Hey You ! </br>
Sort these integers for me ...</br>

By name ...</br>

Do it now !</br>

<ul>
    <li>Range is 0-999</li>
    <li>There may be duplicates</li>
    <li>The array may be empty</li>
</ul>


sol:將Factorial decomposition簡化

``` python
def primeFactors(n):
    dic={}    
    x=2         
    while(n!=1): 
        if n%x==0:
            dic[x]= dic.get(x,0)+1
            n=n//x                
        else:
            x+=1 
    return "".join(["({})".format(key) if dic[key]==1 else "({}**{})".format(key,dic[key]) for key in sorted(dic.keys())])
```

sol:上面dic 拆掉,message 改由在迴圈過程中累加,增加message 的條件當n%x 不是0,表示已無x 因數了,或是n==1,表示最後一筆

``` python
def primeFactors(n):    
    message=""
    x,count=2,0
    while(n!=1):       
        if n%x==0:
            count+=1            
            n=n//x              
        if n%x or n==1:
            if count==1:
               message+="({})".format(x)
            elif count>1:
               message+="({}**{})".format(x,count) 
            count=0
            x+=1  
    return messa
```











