Many times on [Stackoverflow.com](https://stackoverflow.com) I see function similar to this. It is code from [Sentdex's tutorial](https://pythonprogramming.net/pygame-button-function-events/).

```python
def action_button(x, y, w, h, ic, ac, text, text_colour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    font = pygame.font.SysFont("arial black",20)
    text = font.render(text,True,(text_colour))
    screen.blit(text,[x+w/2-(text.get_rect().w/2),y+h/2-(text.get_rect().h/2)])
```

Mostly it works correctly. But sometimes people has problem because it executes action many times.

There is no problem when action removes button from region where is mouse - 
ie. when action starts game and it removes all buttons from screen.

But there is the problem when button stays in this place or it puts new button in the same place - 
ie. 
- when button in menu starts page with options which has button in the same place,
- when button in options changes settings but it doesn't remove buttons (it doesn't close page with buttons)

The most weird situation is when button in Menu opens Options with button "Back" in the same place 
and this button goes back to Menu with button in the same place which opens Options again, etc. 
It will jump between Menu, Options and Menu again all the time when you keep mouse button pressed.

Problem is because `pygame.mouse.get_pressed()` gives `True` all the time when mouse button is pressed
and function treads it as many clicks so it executes action many times.

Using `event` you can get moment when mouse button change state from not-pressed to pressed and run action only once. 
But putting function in `for event` loop will not works correctly. 
It will run action only once but it will also draw button only when you click region where should be button.
So it will not draw button at star - you have to click in its region - and it will not change button's color when you hover butto.

Easy method is to split this function into two functions

- `action_button_draw` which only draws button and use this function in old place

- `action_button_click` which only runs action and put this function in `for event` loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 1 = left button, 3 = right button
                action_button_click(x, y, w, h, action)

    or at least

        if event.type == pygame.MOUSEBUTTONDOWN:
            action_button_click(x, y, w, h, action)

Functions:

```python
def action_button_click(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()

def action_button_draw(x, y, w, h, ic, ac, text, text_colour):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    font = pygame.font.SysFont("arial black",20)
    text = font.render(text,True,(text_colour))
    screen.blit(text,[x+w/2-(text.get_rect().w/2),y+h/2-(text.get_rect().h/2)])
```

Minimal working example in file `main.py`

These two functions you can also put in class and use class like in [example-class.py](https://github.com/furas/python-examples/tree/master/pygame/button-click-cycle-color)
