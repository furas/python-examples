Event [KEYDOWN](http://pygame.org/docs/ref/event.html0 has `event.key`, `event.unicode`, `event.mod`.

You can compare key with char 

    if event.type == pygame.KEYDOWN:
        if event.unicode == "a":

or to check `"a"` and `"A"` without checking `event.mod`

    if event.type == pygame.KEYDOWN:
        if event.unicode.lower() == "a":

To check char in word

    if event.type == pygame.KEYDOWN:  
        if event.unicode.lower() in some_word.lower():

Code uses `event.unicode` to render text with pressed keys.

![#1](images/pygame-key-event-unicode.png?raw=true)   

BTW: It is not some `Entry` widget so it doesn't delete char when you press `backspace`

