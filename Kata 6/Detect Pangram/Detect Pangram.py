import string

def is_pangram(s):
    return len([ x for x in set(s.lower()) if ord(x)>95 and ord(x)<123 ])==26