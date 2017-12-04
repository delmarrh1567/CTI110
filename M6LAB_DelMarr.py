#CTI-110
#M6LAB - Nested Loops
#Hasan DelMarr
#3 December 2017

#Defining Nested Loops


import turtle          
win = turtle.Screen()  
t = turtle.Turtle()


t.pensize(9)            
t.pencolor("purple")     
t.shape("turtle")


 
t.left(180)             



for i in (1,2,3,4,5,6,7,8,9,10,11,12,13):
    
    for j in (1,2,3,4,5,6,7,8,9,10,11,12,13):
        t.forward(100)
        t.right(120)
    t.forward(100)
    t.left(72)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.left(72)
    t.forward(100)
    t.right(120)



win.mainloop()             

            
