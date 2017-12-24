It shows how to use time to change color and not freeze program


You can use variable with color in `rect(...)` and ..

... use own event with `pygame.time.set_timer()` to change color in this variable.


```python

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (700, 500)

# --- start ---

pygame.init()
screen = pygame.display.set_mode(size)

# start color
color = RED

# define own event type
CHANGE_COLOR = pygame.USEREVENT + 1
# create event every 250ms
pygame.time.set_timer(CHANGE_COLOR, 250) # 250ms

# --- mainloop ---

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # check if get event
        if event.type == CHANGE_COLOR:
            # change color
            if color == RED:
                color = BLACK
            else:
                color = RED
                
    screen.fill(WHITE)
    pygame.draw.rect(screen, color, [300, 200, 100, 100],0)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
```

... or use `pygame.time.get_ticks()` to get current time and check if it is time to change color.

```python

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (700, 500)

# --- start ---

pygame.init()
screen = pygame.display.set_mode(size)

# start color    
color = RED

# get current time
current_time = pygame.time.get_ticks()

# first change after 250 ms
change_color_time = current_time + 250

# --- mainloop ---

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # get current time 
    current_time = pygame.time.get_ticks()
    
    # check if it is time to change color
    if current_time >= change_color_time:
        # set new time to change color again
        change_color_time = current_time + 250
        # change color
        if color == RED:
            color = BLACK
        else:
            color = RED                    

    screen.fill(WHITE)
    pygame.draw.rect(screen, color, [300, 200, 100, 100],0)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
```
