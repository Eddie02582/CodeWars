def title_case(title, minor_words=""):
    return " ".join( s.title() if s  not in minor_words.lower().split(' ') or i==0 else s for i,s in enumerate(title.lower().split(' ') ))