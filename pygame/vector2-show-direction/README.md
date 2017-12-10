# Vector2

Red lines are always directed to mouse and they always have the same length.

    length = 100

    mouse = pygame.mouse.get_pos()
    
    start = pygame.math.Vector2(x, y)

    end = start + (mouse - start).normalize() * length
    
    pygame.draw.line(screen, RED, start, end)
    
## direction.py


![#1](images/screenshot-1.png?raw=true)   

## direction-many-lines-1.py

![#2](images/screenshot-2.png?raw=true)   

## direction-many-lines.py

![#3](images/screenshot-3.png?raw=true)   
