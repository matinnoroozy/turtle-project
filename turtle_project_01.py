from turtle import *
from random import*
speed(0)
colorlist=["red","green","yellow","purple","white"]
bgcolor("black")
pensize(2)
for j in range(15):
    x=randint(-250 , 250)
    y=randint(-250 , 250)
    penup()
    goto (x,y)
    pendown()
    for i in range(5):
        color(colorlist[i])
        circle(10)
        right(72)
done()
    