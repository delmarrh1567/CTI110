#CTI-110
#M6T1A - Turtle/Shapes
#Hasan DelMarr
#29 November 2017

#Statement provides code for a square and triangle.

import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("orange")     # set pencolor (takes string)
#t.shape("turtle")

#commands from here to the last line can be replaced
# triangle, sides are 360 / 3 = 120 degrees
#draw Triangle
t.forward(100)          
t.left(120)            
t.forward(100)
t.left(120)
t.forward(100)
#draw square
t.penup
t.forward(10)
t.pendown
t.forward(50)           # Tell alex to move forward by 50 units
t.left(90)             # Tell alex to turn by 90 degrees
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)


# end commands
#win.mainloop()             # Wait for user to close window

