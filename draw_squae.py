import turtle

# making turtle object
s=turtle.Turtle()
sc=turtle.Screen()

# for adjusting the speed of drawing
s.speed(1)

# for making the background color 
sc.bgcolor('red')

# filling color
s.begin_fill()

# color in drawn square
s.fillcolor('aqua')

# drawing square
for i in range(4):
    s.forward(100)
    s.left(90)

# for ending the color filling
s.end_fill()


