import turtle

s = turtle.Screen()
t = turtle.Turtle()
r = turtle.Turtle()
v = turtle.Turtle()
s.bgcolor("grey")

#R
t.pensize(20)
t.pencolor("black")
t.penup()
t.goto(-200,0)
t.pendown()
t.circle(30,180)
t.left(90)
t.forward(90)
t.backward(45)
t.left(45)
t.forward(60)

#8
t.pencolor("brown")
t.pensize(20)
t.penup()
t.goto(0,100)
t.pendown()
t.left(90)
t.circle(25,360)

t.penup()
t.goto(0,150)
t.pendown()
t.circle(25,360)
t.penup()

#7
r.pencolor("brown")
r.pensize(20)
r.penup()
r.goto(-35,40)
r.pendown()
r.forward(60)
r.right(120)
r.forward(90)

#9
t.pensize(20)
t.pencolor("brown")
t.penup()
t.goto(5,-140)
t.pendown()
t.left(45)
t.circle(30)
t.left(150)
t.forward(90)

#T
v.pensize(20)
v.pencolor("black")
v.penup()
v.goto(170,60)
v.pendown()
v.forward(80)
v.backward(40)
v.right(90)
v.forward(80)



