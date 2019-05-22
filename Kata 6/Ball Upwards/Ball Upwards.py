def h(v,t):
	return v*(1000/3600)*t-0.5*9.81*t**2

def max_ball(v0):
    a=[h(v0,i*0.1)for i in range(1,101,1)]
    print (a)
    return a.index(max(a))+1
	
	
"""
h = vt-0.5gt^2
let h = 0 [that is, when the ball has returned to the ground]
=> 0 = vt-0.5gt^2
=> 0.5gt^2 = vt
=> 0.5gt = v
=> t = 2v/g - the total time the ball is in the air.
=> t at max height  = v/g
"""

def max_ball(v0):
    return round(10*v0/9.81/3.6)