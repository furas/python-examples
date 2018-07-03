import turtle


def item(lenght, level, color):
    if level <= 0:
        return
    
    for _ in range(5):    # 5
        turtle.color(colors[color])
        turtle.forward(lenght)
        
        item(lenght/4, level-1, color+1)
        
        turtle.penup() # there is no need to draw again the same line  (and it can use differnt color)
        turtle.backward(lenght)
        turtle.pendown()
        
        turtle.right(360/8) # 8
    
    turtle.right(360/8 * 3) # 3 = 8 - 5
    
    
colors = ["white", "green", "blue", "yellow", "red"]

turtle.tracer(0, 0)
turtle.hideturtle()
turtle.bgcolor("black")

item(200, 4, 0)

turtle.update() 

turtle.mainloop()
