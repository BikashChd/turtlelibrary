import turtle
t=turtle.Turtle()
list1=["red","green","yellow","aqua"]
t.up()
t.goto(200,0)

for i in range(4):
    t.down()
    
    t.color(list1[i])
    t.pensize(20)
    t.circle(50)
    t.up()
    t.backward(100)

    