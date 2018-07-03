import turtle

def item(lenght, level):
    if level <= 0:
        return
    
    for _ in range(8):
        turtle.forward(lenght)
        
        item(lenght/4, level-1)
        
        turtle.backward(lenght)
        
        turtle.right(360/8)
    
    
turtle.tracer(0, 0)
turtle.hideturtle()

item(200, 4)

turtle.update() # traced may not display few last elements.

turtle.mainloop()
