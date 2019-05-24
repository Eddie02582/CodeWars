def high(x):    
    word=""
    score=0
    for a in x.split(' '):
        temp=sum(map(lambda y :ord(y)-ord('a')+1,a))
        if temp>score:
            score=temp
            word=a
    return word
    
def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]    
    
    
    
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))