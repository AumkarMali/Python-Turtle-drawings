import turtle
import random

draw = turtle.Turtle()
turtle.bgcolor("black")

colors = ["red", "blue", "green", "orange", "yellow", "purple"]

size = 5
draw.speed(17)

for i in range(180):
  draw.pencolor(random.choice(colors))
  draw.forward(size)
  draw.right(59)
  size= size+1

