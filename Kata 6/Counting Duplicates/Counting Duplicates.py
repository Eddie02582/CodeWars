from collections import Counter
def duplicate_count(text): 
    counter=sorted(list(Counter(list(text.lower())).values()))  
    return len(counter)-counter.count(1)
    
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])