import turtle
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
a.width('40')
a.color('gold')
a.forward(150)
a.left(120)
a.forward(150)
a.left(120)
a.forward(150)
a.left(120)
a.right(60)
a.forward(150)
a.left(120)
a.forward(150)
a.right(120)
a.forward(150)
a.right(120)
a.forward(300)
a.right(120)
a.forward(150)
a.forward(250)
a.color('cyan')
a.forward(150)
a.left(90)
a.forward(150)
a.left(90)
a.forward(150)
a.left(90)
a.forward(150)
a.color('magenta')
a.forward(250)
a.left(120)
a.forward(150)
a.left(120)
a.forward(150)
for x in range(6):
    b.width('25')
    b.color('blue')
    b.forward(40)
    b.left(60)
for x in range(3):
    c.color('Lavender')
    c.width('40')
    c.forward(200)
    c.left(120)
for x in range(4):
    d.width(100)
    d.color('pink')
    d.forward(500)
    d.left(90)
a.Screen().exitonclick()
b.Screen().exitonclick()
c.Screen().exitonclick()
d.Screen().exitonclick()