def mix(s1, s2):
    word=sorted(list(set(s1+s2)))
    msgs=[]
    for x in word:
        if  ord('a')<= ord(x)<= ord('z') :   
            s1_count=s1.count(x)
            s2_count=s2.count(x)  
            max_count=max(s1_count,s2_count)  
            if max_count >1:
                if s1_count>s2_count:
                    msgs.append(("1",max_count*x))
                elif s2_count>s1_count:
                    msgs.append(("2",max_count*x))
                elif s1_count==s2_count :
                    msgs.append(("=",max_count*x))  
                     
    msgs.sort(key=lambda x : (-len(x[1]),x[0]))              
    
    return "/".join([ "{0}:{1}".format(msg[0],msg[1]) for msg in msgs])  