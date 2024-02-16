import turtle
import datetime
import time
window = turtle.Screen()
window.bgcolor("black")

clockpen = turtle.Turtle()
pen = turtle.Turtle()
clockpen.shape("circle")
clockpen.color("white")
clockpen.speed(10)
clockpen.pensize(10)
pen.shape("circle")
pen.color("white")
pen.speed(10)
pen.pensize(10)

clockpen.penup()
radius = 200
clockpen.sety(-200)
clockpen.pendown()
clockpen.circle(radius)
clockpen.penup()
clockpen.home()

def minhand(angle):
    pen.home()
    pen.rt(-90)
    pen.right(angle)
    pen.pendown()
    pen.forward(radius - 35)
    pen.home()

def hrhand(angle):
    pen.home()
    pen.rt(-90)
    pen.right(angle)
    pen.pendown()
    pen.forward(radius - 80)
    pen.home()

for i in range (1, 13):
    clockpen.penup()
    clockpen.forward(radius - 20)
    clockpen.stamp()
    clockpen.home()
    clockpen.rt(30 * i)




turtle.home()
while True:
    pen.clear()
    ttime = datetime.datetime.now()
    min = ttime.minute
    hr = ttime.hour
    minhand(min * 6)
    hrhand(hr * 30)
    time.sleep(60)

window.exitonclick()