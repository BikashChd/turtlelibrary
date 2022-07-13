import turtle

# making object of turtle
c=turtle.Turtle()

# making object for screen
s=turtle.Screen()

# putting color in the background
s.bgcolor('yellow')

# adjusting the speed of drawind 
c.speed(1)

# making circle color blue
c.fillcolor('blue')

# filling color 
c.begin_fill()

# drwaing circle
c.circle(200)

# end of filling
c.end_fill()

# hiding the arrow
c.hideturtle()

