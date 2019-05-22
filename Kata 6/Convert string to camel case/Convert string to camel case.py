import re
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
	
def to_camel_case(text):
    return ''.join(v.title() if i else v for i,v in enumerate(re.split('[_-]',text)))
	
