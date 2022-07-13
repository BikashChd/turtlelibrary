import turtle

def draw_circle(x,y,color,rad):
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(rad)
    t.end_fill()
    t.up()
    t.home()

t=turtle.Turtle()
t.up()
 
draw_circle(0,-50,'red',50)

draw_circle(150,150,'blue',50)

draw_circle(-150,150,'green',50)

draw_circle(-150,-150,'aqua',50)

draw_circle(150,-150,'purple',50)







