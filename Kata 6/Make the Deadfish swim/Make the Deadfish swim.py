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