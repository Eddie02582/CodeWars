def isValidWalk(walk):  
    return len(walk)==10 and walk.count('n')==walk.count('s')and walk.count('w')==walk.count('e'