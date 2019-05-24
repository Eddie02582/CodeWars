# Make the Deadfish swim
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

<ul>
    <li>i increments the value (initially 0)</li>
    <li>d decrements the value</li>
    <li>s squares the value</li>
    <li>o outputs the value into the return array</li>
</ul>


```python
def parse(data):
    values=[]
    value=0
    for x in data:
        if (x=='i'):
            value+=1
        elif (x=='d'):
            value-=1
        elif (x=='s'):
            value*=value
        elif (x=='o'):
            values.append(value)
    return values   
```  

