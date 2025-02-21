import math

def circle(r):
    return math.pi*r**2

def rectangle (l,w):
    return l*w

def square(a):
    return a**2

shape = ("enter your input: ")
if shape == "circle":
    r = int(input("enter the radius value: "))
    print("area of the circle: ",circle(r))
elif shape =="rectangle":
    l = int(input("enter length: "))
    w = int(input("enter width: "))
    print("area of the rectangle: ",rectangle(l,w))
elif shape == "square":
    a = int(input("enter the value of side: "))
    print("area of the squar: ",square(a))
else:
    print("invalid input")

     

    
