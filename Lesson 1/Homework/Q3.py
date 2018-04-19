import math
from turtle import*
shape('turtle')
speed(0)
#Arighttriangle
a= float(input('Canh 1?'))
b= float(input('canh 2?'))
forward(a)
left(90)
forward(b)
left(180-math.degrees(math.atan(a/b)))
forward(math.sqrt(a**2+b**2))
n=input('')