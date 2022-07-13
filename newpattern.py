import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
for i in range(15):
    for colours in ("red","magneta","blue","cyan","green","yellow","white"):
        t.color(colours)
        t.pensize(3)
        t.left(4)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)

