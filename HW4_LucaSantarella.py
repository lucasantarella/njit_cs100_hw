"""
Luca Santarella
CS 100 2018S Section 009
HW 04, September 24, 2019
"""

import turtle

"""
Exercise 1:
"""
a = 3
b = 4
c = 5

if a < b:
    print("OK")
if c < b:
    print("OK")
if (a + b) == c:
    print("OK")
if (a ** 2 + b ** 2) == c ** 2:
    print("OK")

"""
/ Exercise 1
"""

"""
Exercise 2:
"""
a = 3
b = 4
c = 5

if a < b:
    print("OK")
else:
    print("NOT OK")
if c < b:
    print("OK")
else:
    print("NOT OK")
if (a + b) == c:
    print("OK")
else:
    print("NOT OK")
if (a ** 2 + b ** 2) == c ** 2:
    print("OK")
else:
    print("NOT OK")
"""
/ Exercise 2
"""

"""
Exercise 3:
"""
color = input("what color?")
width = int(input("what line width?"))
length = int(input("what line length?"))
shape = input("line, triangle, or square?")

s = turtle.Screen()
t = turtle.Turtle()

t.penup()
t.speed(90)
t.width(width)
t.color(color)

sides = 0

if shape == 'line':
    sides = 1
elif shape == 'triangle':
    sides = 3
elif shape == 'square':
    sides = 4
else:
    print("Invalid shape.")

if sides > 0:
    ext_angle = 360 / sides

    t.pendown()
    for i in range(sides):
        t.forward(length)
        t.left(ext_angle)

    t.penup()
    t.home()
    s.exitonclick()
