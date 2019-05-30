def insert_missing_letters(st):
    
    word=''
    for x in st:
        if x not in word:
            word+=x+"".join([ chr(i).upper() for i in range(ord(x),ord('z')+1) if chr(i) not in st ])  
        else:
            word+=x
    return word

def insert_missing_letters(st):
    letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result=""
    for s in st:  
        result=result+s
        if result.count(s) ==1:          
            index=letters.index(s.upper())            
            add=sorted(list(set(letters[index:])-set(list(st.upper()))))
            result+=''.join(add)      
    return result