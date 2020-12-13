from turtle import *
import numpy as np
#Here n represents the number of cartesian point to represent the edge of the cuboid.
n=8
################################################################################
#x1,x2,x3,x4,x5,x6,x7 and x8 are the values of 8 x-coordinates of the 8 vertices of cuboid. 
x1=0
x1=float(x1)
x2=0
x2=float(x2)
x3=0
x3=float(x3)
x4=0
x4=float(x4) 
x5=-4.5
x5=float(x5)
x6=-4.5
x6=float(x6)
x7=-4.5
x7=float(x7)
x8=-4.5
x8=float(x8)
#Defining a list containing x-coordinates.
obj_x=[x1,x2,x3,x4,x5,x6,x7,x8]
################################################################################
#y1,y2,y3,y4,y5,y6,y7 and y8 are the values of 8 y-coordinates of the 8 vertices of cuboid.
y1=0
y1=float(y1)
y2=4.5
y2=float(y2)
y3=4.5
y3=float(y3)
y4=0
y4=float(y4)
y5=0
y5=float(y5)
y6=4.5
y6=float(y6)
y7=4.5
y7=float(y7)
y8=0
y8=float(y8)
#Defining a list containing y-coordinates.
obj_y=[y1,y2,y3,y4,y5,y6,y7,y8]
################################################################################
#z1,z2,z3,z4,z5,z6,z7 and z8 are the values of 8 z-coordinates of the 8 vertices of cuboid.
z1=0
z1=float(z1)
z2=0
z2=float(z2)
z3=6.2
z3=float(z3)
z4=6.2
z4=float(z4)
z5=0
z5=float(z5)
z6=0
z6=float(z6)
z7=6.2
z7=float(z7)
z8=6.2
z8=float(z8)
#Defining a list containing z-coordinates.
obj_z=[z1,z2,z3,z4,z5,z6,z7,z8]
#################################################################################
#Providing each vertex a capital letter alphabet by making a dictionary object consisting coordinates of each vertex.
obj_dict=[]
k=65
for i in range(0,n,1):
    tup=(chr(k),[obj_x[i],obj_y[i],obj_z[i]])
    obj_dict.append(tup)
    k=k+1
obj_dict=dict(obj_dict)
################################################################################
#Asking the user for the coordinates from where she/he must have been observing the cuboid.
#For the sake of our convenience, let's call this point as OBSERVER point.
obs_x=input("Enter x-coordinate of your location")
obs_x=float(obs_x)
obs_y=input("Enter y-coordinate of your location")
obs_y=float(obs_y)
obs_z=input("Enter z-coordinate of your location")
obs_z=float(obs_z)
obs=[obs_x,obs_y,obs_z]
#################################################################################
#Now entering The coordinates of the point at which observer is looking at.
#For the sake of our convenience, we will call it as FOCUS point.
focus_x=-2.25
focus_x=float(focus_x)
focus_y=2.25
focus_y=float(focus_y)
focus_z=3.1
focus_z=float(focus_z)
focus=[focus_x,focus_y,focus_z]
#################################################################################
#Defining a function: coordinater .
#Coordinator takes three input (three coordinates of a point) and find the point of
#intersection of the line joining
#that point(which is an vertex point) and OBSERVER's point with the plane passing
#through the FOCUS point having its normal vector in the direction of the vector
#pointing from OBSERVER to FOCUS point.
#Let,s call this plane as PROJ_PLANE. 
u=obs[0]
v=obs[1]
w=obs[2]
s=focus[0]
t=focus[1]
p=focus[2]
if (p-w)>=0:
    theta = np.arctan(np.sqrt((s-u)**2+(t-v)**2)/(p-w))
else:
    theta = np.pi + np.arctan(np.sqrt((s-u)**2+(t-v)**2)/(p-w))
if (s-u)>0 and (t-v)>0:
    phi = np.arctan((t-v)/(s-u))
elif (s-u)>0 and (t-v)<0:
    phi = (2*np.pi) + np.arctan((t-v)/(s-u))
elif (s-u)<=0:
    phi = np.pi + np.arctan((t-v)/(s-u))
r = np.sqrt((s-u)**2+(t-v)**2+(p-w)**2)

#Defining matrix
#Here I am using a21,a22,a23 as -cos(theta)cos(phi),-cos(theta)sin(phi),sin(theta) 
# and  a31,a32,a33 as sin(phi),-cos(phi),0 instead of using
# a21,a22,a23 = cos(theta)cos(phi),cos(theta)sin(phi),-sin(theta) and
# a31,a32,a33 = -sin(phi),cos(phi),0 just in order to print a preferred order of
#x,y and z axes.
#It doesn,t change value of any resultant coordinates.

a11,a12,a13 = np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)
a21,a22,a23 = -np.cos(theta)*np.cos(phi),-np.cos(theta)*np.sin(phi),np.sin(theta)
a31,a32,a33 = np.sin(phi),-np.cos(phi),0
    
#We will call these coordinates which came as an output from the
#coordinates as REFL_POINTS.
def coordinater(x1,y1,z1):
    u=obs[0]
    v=obs[1]
    w=obs[2]
    s=focus[0]
    t=focus[1]
    p=focus[2]
    L=-(((s-u)*(x1-s))+((t-v)*(y1-t))+((p-w)*(z1-p)))/((\
        (x1-u)*(s-u))+((t-v)*(y1-v))+((p-w)*(z1-w)))
    x_coordinate=(x1-u)*L+x1
    y_coordinate=(y1-v)*L+y1
    z_coordinate=(z1-w)*L+z1
    return (x_coordinate,y_coordinate,z_coordinate)
#Creatind dictionary object out of these REFL_POINTS.
refl_dict=[]
k=65
for i in range(n):
    coo=coordinater(obj_dict[chr(k)][0],obj_dict[chr(k)][1],\
                    obj_dict[chr(k)][2])
    tup=(chr(k),[coo[0]-s,coo[1]-t,coo[2]-p])
    refl_dict.append(tup)
    k=k+1
refl_dict=dict(refl_dict)
#################################################################################

#x_coordinate of image
img_x=[]
k=65
for i in range(n):
    c=(refl_dict[chr(k)][0]*a31)+(refl_dict[chr(k)][1]*a32)+\
       (refl_dict[chr(k)][2]*a33)
    tup=(chr(k),c)
    img_x.append(tup)
    k=k+1
final_x=dict(img_x)

#y_coordinate of image
img_y=[]
k=65
for i in range(n):
    c=(refl_dict[chr(k)][0]*a21)+(refl_dict[chr(k)][1]*a22)+\
       (refl_dict[chr(k)][2]*a23)
    tup=(chr(k),c)
    img_y.append(tup)
    k=k+1
final_y=dict(img_y)
#################################################################################
#Plot
hideturtle()
setworldcoordinates(-7,-7,7,7)
def plot_face1(x,y):
    hideturtle()
    k=65
    screensize(200,200)
    speed(0)
    color('red')
    pensize(1)
    pu()
    goto(x[chr(k)],y[chr(k)])
    write(f"{chr(k)} ({x1},{y1},{z1})")
    pd()
    goto(x[chr(k+1)],y[chr(k+1)])
    write(f"{chr(k+1)} ({x2},{y2},{z2})")
    goto(x[chr(k+2)],y[chr(k+2)])
    write(f"{chr(k+2)} ({x3},{y3},{z3})")
    goto(x[chr(k+3)],y[chr(k+3)])
    write(f"{chr(k+3)} ({x4},{y4},{z4})")
    goto(x[chr(k)],y[chr(k)])
    pu()

def plot_face2(x,y):
    hideturtle()
    k=69
    screensize(200,200)
    speed(0)
    color('red')
    pensize(1)
    pu()
    goto(x[chr(k)],y[chr(k)])
    write(f"{chr(k)} ({x5},{y5},{z5})")
    pd()
    goto(x[chr(k+1)],y[chr(k+1)])
    write(f"{chr(k+1)} ({x6},{y6},{z6})")
    goto(x[chr(k+2)],y[chr(k+2)])
    write(f"{chr(k+2)} ({x7},{y7},{z7})")
    goto(x[chr(k+3)],y[chr(k+3)])
    write(f"{chr(k+3)} ({x8},{y8},{z8})")
    goto(x[chr(k)],y[chr(k)])
    pu()    
def plot_rem(x,y):
    hideturtle()
    screensize(200,200)
    speed(0)
    color('red')
    pensize(1)
    for k in range(65,69,1):
        pu()
        goto(x[chr(k)],y[chr(k)])
        pd()
        goto(x[chr(k+4)],y[chr(k+4)])
        pu()
plot_face1(final_x,final_y)
plot_face2(final_x,final_y)
plot_rem(final_x,final_y)
print((refl_dict[chr(65)][0]*a31)+(refl_dict[chr(65)][1]*a32)+(refl_dict[chr(65)][2]*a33))
print((refl_dict[chr(65)][0]*a21)+(refl_dict[chr(65)][1]*a22)+(refl_dict[chr(65)][2]*a23))
print((refl_dict[chr(65)][0]*a11)+(refl_dict[chr(65)][1]*a12)+(refl_dict[chr(65)][2]*a13))
