from string import maketrans 

## 2.7 include maketrans
def T9(words,seq):

    s='abcdefghijklmnopqrstuvwxyz'
    n='22233344455566677778889999'
    trantab = maketrans(s, n)

    n2='23456789'
    s2='adgjmptw'   
    trantab2 = maketrans(n2, s2)
    result=[word for word in words if word.lower().translate(trantab)==seq]    
    if result:
        return result
    else:        
        return [seq.translate(trantab2)]




##3.6
def T9(words,seq):

    s='abcdefghijklmnopqrstuvwxyz'
    n='22233344455566677778889999'
    trantab = str.maketrans(s, n)

    n2='23456789'
    s2='adgjmptw'   
    trantab2 = str.maketrans(n2, s2)
    result=[word for word in words if word.lower().translate(trantab)==seq]    
    if result:
        return result
    else:        
        return [seq.translate(trantab2)]