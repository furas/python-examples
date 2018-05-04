Standard method

    import pygame.camera

    pygame.camera.init()
    camera = pygame.camera.Camera('/dev/video0')

It will not work

    from pygame.camera import init as camera_init
    from pygame.camera import Camera

    camera_init()
    camera = Camera('/dev/video0')
    
because `Camera` has oryginal class, not replaced by `init()`

It will work

    from pygame.camera import init as camera_init

    camera_init()

    from pygame.camera import Camera
    
    camera = Camera('/dev/video0')
