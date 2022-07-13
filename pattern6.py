import turtle
t=turtle.Turtle()


list1=['red','magneta','blue','cyan','white','green','yellow']



for i in range(400):
    t.color(list1[i%7])
    t.circle(100)
    t.left(30)


# t.hideturtle()
# turtle.mainloop()