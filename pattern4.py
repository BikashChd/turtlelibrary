import turtle
t=turtle.Turtle()

list1=['purple','red','orange','blue','green']
# t.speed()

for i in range(400):
    t.color(list1[i%5])
    t.pensize(1)
    t.forward(i/10+i)
    t.right(59)
t.done()