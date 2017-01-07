`PyGame` which uses `SDL 1.2` doesn't have function to set window position.

And you can't move window which can't have frame.

    import os
    import pygame

    pygame.init()

    os.environ['SDL_VIDEO_WINDOW_POS'] = '50, 500'
    screen = pygame.display.set_mode((300,300), 32, pygame.NOFRAME)

    (2)
    pygame.quit()

To move to new place you can change `SDL_VIDEO_WINDOW_POS` but you have to use `set_mode()` again.

To center window you can use `SDL_VIDEO_CENTERED`

    import os
    import pygame

    pygame.init()

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((300,300), 32, pygame.NOFRAME)

    time.sleep(2)
    pygame.quit()

If you used `SDL_VIDEO_WINDOW_POS` then you have to delete this to use `SDL_VIDEO_CENTERED`

    del os.environ['SDL_VIDEO_WINDOW_POS']
    os.environ['SDL_VIDEO_CENTERED'] = '1'

---

SDL doc: https://www.libsdl.org/release/SDL-1.2.15/docs/html/sdlenvvars.html
