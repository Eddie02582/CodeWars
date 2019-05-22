'''
solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'''

def Mysolution(args):
	result=[]
	s=""
	for i,x in enumerate(args):    
		if  not s  :
			s+=str(x)		
		elif i is not len(args)-1 :			
			if  args[i] -args[i-1] is  1 and args[i+1] -args[i] is not 1 : 				
				if args[i] -args[i-2] is not 2:
					s+=","+str(x)
				else:
					s+="-"+str(x)
			elif args[i] -args[i-1] is not 1:           
				s+=","+str(x)
		else:
			if args[i] -args[i-2] is  2:
				s+="-"+str(x)
			else:
				s+=","+str(x)            
	return s
	
	
def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)
	
solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])