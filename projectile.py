import math
gravity=9.81
v0=44
theta=80*(math.pi/180)
print(theta)
distance=0.5
height_b=1
height_p=height_b+distance*math.tan(theta)-(gravity*distance*distance/(2*v0*math.cos(theta)*v0*math.cos(theta)))
print(height_p)