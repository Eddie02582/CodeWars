def title_case(title, minor_words=""):
    return " ".join( s.title() if s  not in minor_words.lower().split(' ') or i==0 else s for i,s in enumerate(title.lower().split(' ') ))
    
def title_case(title, minor_words=''):
    words=[ word.lower() for word in minor_words.split(' ')]
    titles=title.split(' ')
    for i,t in enumerate(titles):
        if i!=0 and t.lower()  in words:
            titles[i]=titles[i].lower()
        else:
            titles[i]=titles[i].title()
    return ' '.join(titles)