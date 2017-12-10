# CTI-110 
# M5HW1 - Distance Traveled
# Anthony O'Brien
# 10/22/2017

import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.left(90)

for i in (1,2,3,4):
    t.forward(100)
    t.left(90)

t.penup()
t.right(90)
t.forward(100)
t.pendown()

for i in (1,2,3):
    t.forward(100)
    t.left(120)
