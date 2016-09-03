# Lesson 3

import turtle

def draw_square(t, size, orientation):
    t.right(orientation)
    for i in range(4):
        t.forward(size)
        t.right(90)

def draw_circle(t, size):
    t.circle(size)

window = turtle.Screen()
window.bgcolor("red")

# turtles = []
# for i in range(36):
#     turtles.append(turtle.Turtle())
#     turtles[i].speed(10)
#     draw_square(turtles[i],100+i*10,i*10)

turtles = []
for i in range(36):
    turtles.append(turtle.Turtle())
    turtles[i].speed(10)
    draw_square(turtles[i],100+i*10,i*10)

window.exitonclick()
