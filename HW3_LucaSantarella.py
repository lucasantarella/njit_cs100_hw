"""
Luca Santarella
CS 100 2018S Section 009
HW 03, September 17, 2019
"""

import turtle
import math

screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.penup()
turtle.speed(10)

"""
Exercise 1:
"""

# Draw equilateral triangle in top right of screen
turtle.setposition(100, 100)

turtle.pendown()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.penup()

# Draw equilateral triangle in top right of screen
turtle.setposition(100, 80)

turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.penup()

# Draw pentagon in right side of screen
turtle.setposition(100, -40)

turtle.pendown()
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.right(72)
turtle.penup()

"""
Exercise 2:
"""

# Go to left and draw 4 circles
turtle.setheading(180)
turtle.setposition(-200,160)

turtle.pendown()
turtle.circle(200)
turtle.penup()

turtle.left(90)
turtle.forward(50)
turtle.setheading(180)
turtle.pendown()
turtle.circle(150)
turtle.penup()

turtle.left(90)
turtle.forward(50)
turtle.setheading(180)
turtle.pendown()
turtle.circle(100)
turtle.penup()

turtle.left(90)
turtle.forward(50)
turtle.setheading(180)
turtle.pendown()
turtle.circle(50)
turtle.penup()

"""
NOTE:
To see the outputs of Exercise 3, click on the screen window to dismiss turtles
"""
screen.exitonclick()

print("100 factorial:")
print(math.factorial(100))

print("log_2(1000000):")
print(math.log(1000000, 2))

print("GCD of 63 & 49:")
print(math.gcd(63, 49))