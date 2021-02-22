import turtle

myPen = turtle.Turtle()
myPen.speed(20)
myPen.shape("arrow")
myPen.penup()
myPen.pencolor("red")
myPen.setposition(0, -180)
myPen.pendown()
myPen.fillcolor("red")
myPen.begin_fill()
myPen.circle(180)
myPen.end_fill()

currentHour = 2
currentMinute = 49
currentSecond = 35

myPen.color("white")
myPen.pensize(7)

for item in range(1, 13):
    myPen.penup()
    myPen.goto(0, 0)
    myPen.setheading(90)
    myPen.right(item * 360 / 12)
    myPen.forward(155)
    myPen.pendown()
    myPen.forward(20)

myPen.pensize(3)

for item in range(1, 61):
    myPen.penup()
    myPen.goto(0, 0)
    myPen.setheading(90)
    myPen.right(item * 360 / 60)
    myPen.forward(170)
    myPen.pendown()
    myPen.forward(10)

myPen.color("green")
myPen.pensize(3)
myPen.penup()
myPen.goto(0, 0)
myPen.setheading(90)
myPen.right((currentHour * 360 / 12) + (currentMinute * 0.5))
myPen.pendown()
myPen.forward(100)

myPen.color("blue")
myPen.pensize(3)
myPen.penup()
myPen.goto(0, 0)
myPen.setheading(90)
myPen.right((currentMinute * 360 / 60) + (currentSecond / 10))
myPen.pendown()
myPen.forward(150)

myPen.color("black")
myPen.pensize(3)
myPen.penup()
myPen.goto(0, 0)
myPen.setheading(90)
myPen.right((currentSecond * 360 / 60))
myPen.pendown()
myPen.forward(100)

input("Enter value to close program")

