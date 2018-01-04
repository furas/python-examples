
import pygame
import numpy

# --------------------------------------------------------------------

WIDTH = 1200
HEIGHT = 800

BLACK = (0, 0, 0)
#REDRAW = pygame.USEREVENT

# --------------------------------------------------------------------

def on_quit(event):
    global running
    
    running = False

def on_keydown(event):
    global running
    
    if event.key == pygame.K_ESCAPE:
        running = False
    
def on_mouse_press(event):
    global redrawing
    global button_rect
    
    #button_rect.center = event.pos

    #pygame.event.post(pygame.event.Event(REDRAW))
    #pygame.event.post(pygame.event.Event(pygame.VIDEOEXPOSE))
        
def on_mouse_move(event):
    global redrawing
    global button_rect
    
    #if event.buttons[0]:
        #button_rect.center = event.pos

        #pygame.event.post(pygame.event.Event(REDRAW))
        #pygame.event.post(pygame.event.Event(pygame.VIDEOEXPOSE))
        #redrawing = True

def on_draw(event=None):
    global screen
    global widgets
    
    #screen.fill(BLACK)

    for w in widgets:
        w.draw(screen)
    
    #pygame.display.flip()
    pygame.display.update()
    
# --------------------------------------------------------------------

class Widget:

    events_table = []
    
    def handle_event(self, event):
        if event.type in self.events_table:
            for func in self.events_table[event.type]:
                if func(event) == False:
                    break

    def draw(self, surface):
        screen.blit(self.image, self.rect)
    
    def update(self):
        pass
        
    def draw_border(self, surface, rect, color, border=True, corners=True, other=False):
        
        left, top,  = 0, 0
        width, height = rect.size
        right, bottom = width-1, height-1

        color2 = tuple(x*50//100 for x in color)

        # --- border ---
        
        if border:
            thickness = border
            if border is True:
                thickness = 1
                
            pygame.draw.rect(surface, color2, (left, top, right+1, bottom+1), thickness) 

        # --- corners ---

        if corners:
            thickness = corners
            if corners is True:
                thickness = 5
                
            # left top
            pygame.draw.line(surface, color, (left, top), (left+15, top), thickness) 
            pygame.draw.line(surface, color, (left, top), (left, top+15), thickness) 

            # right top
            pygame.draw.line(surface, color, (right, top), (right-15, top), thickness) 
            pygame.draw.line(surface, color, (right, top), (right, top+15), thickness) 

            # right bottom
            pygame.draw.line(surface, color, (right, bottom), (right-15, bottom), thickness) 
            pygame.draw.line(surface, color, (right, bottom), (right, bottom-15), thickness) 

            # left bottom
            pygame.draw.line(surface, color, (left, bottom), (left+15, bottom), thickness) 
            pygame.draw.line(surface, color, (left, bottom), (left, bottom-15), thickness) 
        
        # --- other ---

        if other:
            points = ( (left+5, top+5), (left+5, top+30), (left+50, top+30), (left+50+10, top+20), (right-5, top+20), (right-5, top+5) )
            
            pygame.draw.polygon(surface, (*color2, 128), points)
            #pygame.draw.polygon(surface, color, points, 1)
            pygame.draw.lines(surface, color, False, points[1:-1], 1)
            

            points = ( (left+5, bottom-5), (left+5, bottom-20), (right-50-10, bottom-20), (right-50, bottom-30), (right-5, bottom-30), (right-5, bottom-5) )
            
            pygame.draw.polygon(surface, (*color2, 128), points)
            #pygame.draw.polygon(surface, color, points, 1)
            pygame.draw.lines(surface, color, False, points[1:-1], 1)

class MovableWidget(Widget):

    def handle_event(self, event):
        global redrawing

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover:
                if event.button == 1:
                    if self.movable:
                        self.moving = True
                        redrawing = True
                        return True
                elif event.button == 3:
                    print(self.rect.topleft)
                    return True
                    
        if event.type == pygame.MOUSEBUTTONUP:
            
            if self.hover:
                if self.movable and self.moving:
                    self.moving = False
                    redrawing = True
                    return True

        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
            
            if self.movable and self.moving:
                self.rect.move_ip(event.rel)
                self.border_rect.move_ip(event.rel)
                redrawing = True
                return True

    def draw(self, surface):
        screen.blit(self.image, self.rect)
        screen.blit(self.border, self.border_rect)

class StaticImage(Widget):
    
    def __init__(self, x, y, filename, alpha=128):
        self.filename = filename
        self.alpha = alpha
        
        self.image = pygame.image.load(filename)
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect()
        
        self.alpha_up = True
        self.alpha_min = 0
        self.alpha_max = 255
        self.alpha_step = 4
        
        self.alpha_deltatime = 25
        self.alpha_time = pygame.time.get_ticks() + self.alpha_deltatime
        
    def update(self):
        global redrawing
        
        time = pygame.time.get_ticks()
        
        if time >= self.alpha_time:
            if self.alpha_up:
                self.alpha += self.alpha_step
                if self.alpha >= self.alpha_max:
                    self.alpha = self.alpha_max
                    self.alpha_up = False
            else:
                self.alpha -= self.alpha_step
                if self.alpha <= self.alpha_min:
                    self.alpha = self.alpha_min
                    self.alpha_up = True
            self.image.set_alpha(self.alpha)
            self.alpha_time = time + self.alpha_deltatime
            redrawing = True
                
class Button(MovableWidget):
    
    def __init__(self, x, y, width, height, movable=False, color=(0, 100, 255), black_margin=5):
        self.hover = False
        self.moving = False
        
        self.movable = movable
        self.color = color
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        
        # ---
        
        self.color25 = tuple(x*25//100 for x in color)
        self.color50 = tuple(x*50//100 for x in color)
        self.color75 = tuple(x*75//100 for x in color)

        # --- object ---
        
        pygame.draw.rect(self.image, self.color25, (black_margin, black_margin, width-(black_margin*2), height-(black_margin*2)), 0) 
        pygame.draw.rect(self.image, self.color50, (15, 15, width-30, height-30), 0) 
        self.image.set_alpha(194)

        # --- border ---
        
        self.border_rect = pygame.Rect(x, y, width, height)
        self.border = pygame.Surface( self.border_rect.size ).convert_alpha()
        self.border.fill((0,0,0,0))
        self.draw_border(self.border, self.border_rect, self.color, 0, 1, False)
        
class Window(MovableWidget):
    
    def __init__(self, x, y, width, height, movable=False, color=(0, 100, 255)):
        self.hover = False
        self.moving = False
        
        self.movable = movable
        self.color = color
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.image.fill((255,255,255,16)) #128
        #self.image.fill((0,0,0,32)) #128

        # ---
        
        self.color25 = tuple(x*25//100 for x in color)
        self.color50 = tuple(x*50//100 for x in color)
        self.color75 = tuple(x*75//100 for x in color)

        self.color_alpha = (0, 0, 0, 128)
        
        # --- object ---

        # - window -
        pygame.draw.rect(self.image, self.color_alpha, (5, 5, width-10, height-10), 0) 

        # - title -
        pygame.draw.rect(self.image, (*self.color, 128), (5, 5, width-10, 20), 0) 

        # `render` 
        # - doesn't respect alpha in color used to render font.
        # - lock surface so it have to be unlock() to change alpha
        # - if aliasing is True then it can't change alpha
        #  
        text_image = font_monospace_20.render('Hello World', True, (0,0,0))
        text_rect = text_image.get_rect()
        text_image.unlock() 
        text_image.set_alpha(128)
        
        self.image.blit(text_image, (10, 5, *text_rect.size))
        
        # - content -
        #pygame.draw.rect(self.image, self.color50, (15, 15+15, width-30, height-30-15), 0) 
        pygame.draw.rect(self.image, (*self.color50, 128), (5, 20+5, width-10, height-20-10), 0) 
        
        #pygame.draw.rect(self.image, self.color, (0, 0, width, height), 1) 

        #self.image.set_alpha(194)

        # --- border ---
        
        self.border_rect = pygame.Rect(x, y, width, height)
        self.border = pygame.Surface( self.border_rect.size ).convert_alpha()
        self.border.fill((0,0,0,0))
        self.draw_border(self.border, self.border_rect, self.color, True, 3, False)
        
class Rectangle(MovableWidget):
    
    def __init__(self, x, y, width, height, movable=False, color=(0, 100, 255), fill=(0,0,0,128), grid=False):
        self.hover = False
        self.moving = False

        self.movable = movable
        self.color = color
        self.fill = fill
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.image.fill(fill)
        
        # --- grid ---
        
        if grid:
            for j in range(0, width, 30):
                pygame.draw.line(self.image, (255,255,255,16), (j, 0), (j, height))

            for j in range(0, height, 30):
                pygame.draw.line(self.image, (255,255,255,16), (0, j), (width, j))

            for j in range(0, height, 30):
                for i in range(0, width, 30):
                    pygame.draw.rect(self.image, (255,255,255,24), (i-1, j-1, 3, 3))
        
        # --- boder ---
        
        self.border_rect = pygame.Rect(x, y, width, height)
        self.border = pygame.Surface( self.border_rect.size ).convert_alpha()
        self.border.fill((0,0,0,0))
        self.draw_border(self.border, self.border_rect, self.color, False, 1, False)
        
class Circle(MovableWidget):
    
    def __init__(self, x, y, radius, movable=False, color=(0, 100, 255), fill=(0,0,0,128), grid=False):
        self.hover = False
        self.moving = False

        self.radius = radius
        self.movable = movable
        self.color = color
        self.fill = fill
        
        width = height = 2*radius
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.image.fill((0,0,0,0))
        #self.image.fill(fill)
        pygame.draw.circle(self.image, fill, (width//2, height//2), self.radius, 0) 
        
        # --- boder ---
        
        self.border_rect = pygame.Rect(x, y, width, height)
        self.border = pygame.Surface(self.border_rect.size).convert_alpha()
        self.border.fill((0,0,0,0))
        
        self.draw_border(self.border, self.border_rect, self.color, 5, 1, True)
      
        # ---
        
        self.alpha = 255
        
        self.alpha_min = 0
        self.alpha_max = 255
        self.alpha_step = 10
        
        self.alpha_deltatime = 25
        self.alpha_time = pygame.time.get_ticks() + self.alpha_deltatime

        self.points_rect = pygame.Rect(x, y, width, height)
        self.points_image = pygame.Surface((width, height)).convert_alpha()
        self.points_image.fill((0,0,0,0))
        
        self.points = [
            [200, 100, 150, 150, 5, 5, True], 
            [100, 100, 150, 150, -5, 5, True], 
            [170, 210, 120, 210, -5, -5, True]
        ]
        #pygame.draw.rect(self.points_image, (255, 0, 0, self.alpha), (100, 100, 5, 5))
        #pygame.draw.rect(self.points_image, (255, 0, 0, self.alpha), (170, 230, 5, 5))
        
    def draw_border(self, surface, rect, color, border=True, corners=True, other=False):
        
        left, top  = 0, 0
        width, height = rect.size
        right, bottom = width-1, height-1
        center_x, center_y = width//2, height//2
        center = (center_x, center_y)
        
        color2 = tuple(x*50//100 for x in color)

        # --- border ---
        
        if border:
            thickness = border
            if border is True:
                thickness = 1
                
            pygame.draw.circle(surface, color2, center, self.radius, thickness) 
            
        # --- corners ---

        if corners:
            thickness = corners
            if corners is True:
                thickness = 5
                
            angle = 15
            # left top
            import math
            s1 = math.radians(90+45-angle)
            s2 = math.radians(90+45+angle)
            pygame.draw.arc(surface, color, (0, 0, width, height), s1, s2, thickness)
            
            # right top
            s1 = math.radians(45-angle)
            s2 = math.radians(45+angle)
            pygame.draw.arc(surface, color, (0, 0, width, height), s1, s2, thickness)

            # right bottom
            s1 = math.radians(-45-angle)
            s2 = math.radians(-45+angle)
            pygame.draw.arc(surface, color, (0, 0, width, height), s1, s2, thickness)

            # left bottom
            s1 = math.radians(180+45-angle)
            s2 = math.radians(180+45+angle)
            pygame.draw.arc(surface, color, (0, 0, width, height), s1, s2, thickness)
        
        # --- other ---

        if other:
            color = (255, 0, 0, 128)
            for r in range(10, self.radius, 40):
                pygame.draw.circle(surface, color, center, r, thickness) 
        
            pygame.draw.line(surface, color, (10, center_y), (center_x-10, center_y))
            pygame.draw.line(surface, color, (center_x+10, center_y), (width-10, center_y))
            pygame.draw.line(surface, color, (center_x, 10), (center_x, center_y-10))
            pygame.draw.line(surface, color, (center_x, center_y+10), (center_x, height-10))

    def update(self):
        global redrawing
        
        time = pygame.time.get_ticks()
        
        if time >= self.alpha_time:
            self.alpha -= self.alpha_step
            if self.alpha <= self.alpha_min:
                self.alpha = self.alpha_max

                new_points = []
                for point in self.points:
                    x, y, max_x, max_y, step_x, step_y, direction = point

                    x += step_x
                    if x >= max_x:
                        step_x = 0

                    y += step_y
                    if y >= max_y:
                        step_y = 0

                    new_points.append([x, y, max_x, max_y, step_x, step_y, direction])

                self.points = new_points
                
            self.points_image.fill((0,0,0,0))
            
            for point in self.points:
                x, y, max_x, max_y, step_x, step_y, direction = point
                pygame.draw.rect(self.points_image, (255, 0, 0, self.alpha), (x, y, 5, 5))
                pygame.draw.line(self.points_image, (255, 0, 0, 255), (x+2, y+2), (x+2+15, y+2-15))
                pygame.draw.line(self.points_image, (255, 0, 0, 255), (x+2+15, y+2-15), (x+2+15+30, y+2-15))
            
            self.alpha_time = time + self.alpha_deltatime
            redrawing = True
         
    def draw(self, surface):
        screen.blit(self.image, self.rect)
        screen.blit(self.border, self.border_rect)
        screen.blit(self.points_image, self.rect)
        
class ImageNormal(MovableWidget):
    
    def __init__(self, x, y, width, height, movable=False, color=(0, 100, 255), filename=None):
        self.hover = False
        self.moving = False
       
        self.movable = movable
        self.color = color
        self.filename = filename

        self.image = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, width, height)
        
        self.border_rect = pygame.Rect(x-5, y-5, width+10, height+10)
        self.border = pygame.Surface( self.border_rect.size ).convert_alpha()
        self.border.fill((0,0,0,0))
        self.draw_border(self.border, self.border_rect, self.color, False, True, True)
        
    def draw(self, surface):
        screen.blit(self.image, self.rect, self.rect)
        screen.blit(self.border, self.border_rect)

class ImageInvert(MovableWidget):
    
    def __init__(self, x, y, width, height, movable=False, color=(0, 100, 255), filename=None):
        self.hover = False
        self.moving = False
        
        self.movable = movable
        self.color = color
        self.filename = filename

        self.image = pygame.image.load(filename)
        self.image = self.invert(self.image)
        self.rect = pygame.Rect(x, y, width, height)
        
        self.border_rect = pygame.Rect(x-5, y-5, width+10, height+10)
        self.border = pygame.Surface( self.border_rect.size ).convert_alpha()
        self.border.fill((0,0,0,0))
        self.draw_border(self.border, self.border_rect, self.color, False, 1,)
        
    def invert(self, image):
        array = pygame.surfarray.array3d(image)
        array = 255 - array
        return pygame.surfarray.make_surface(array)

    def draw(self, surface):
        screen.blit(self.image, self.rect, self.rect)
        screen.blit(self.border, self.border_rect)

class Border1(MovableWidget):
    
    def __init__(self, x, y, width, height, movable=False, color=(0, 100, 255), fill=(0,0,0,128)):
        self.hover = False
        self.moving = False

        self.movable = movable
        self.color = color
        self.fill = fill
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.image.fill(fill)
        
        # --- object ---

        self.points = []
        for _ in range(15, width-15, 10):
            self.points.append(random.randint(5, height-30))
        
        self.draw_bars(self.image, self.rect)
        
        # --- boder ---
 
        self.border_rect = pygame.Rect(x, y, width, height)
        self.border = pygame.Surface( self.border_rect.size ).convert_alpha()
        self.border.fill((0,0,0,0))
        self.draw_border(self.border, self.border_rect, self.color, True, 3, False)
        
        self.anim_deltatime = 250
        self.anim_time = pygame.time.get_ticks() + self.anim_deltatime

    def draw_border(self, surface, rect, color, border=True, corners=True, other=False):
        
        left, top = 0, 0
        width, height = rect.size
        right, bottom = width-1, height-1

        color2 = tuple(x*50//100 for x in color)

        # --- border ---
        
        if border:
            thickness = border
            if border is True:
                thickness = 1

            size_x = 50 
            size_y = 50
            
            points = [
                    (left, top), 
                        (left+size_x, top), (left+size_x+5, top+5),
                        (right-size_x-5, top+5), (right-size_x, top), 
                    (right, top),
                        (right, top+size_y), (right-5, top+size_y+5),
                        (right-5, bottom-size_y-5), (right, bottom-size_y), 
                    (right, bottom),
                        (right-size_x, bottom), (right-size_x-5, bottom-5), 
                        (left+size_x+5, bottom-5), (left+size_x, bottom),
                    (left, bottom), 
                         (left, bottom-size_y), (left+5, bottom-size_y-5),
                        (left+5, top+size_y+5), (left, top+size_y), 
                    (left, top), 
                    ]
                      
            pygame.draw.lines(surface, color2, False, points) 

        # --- corners ---

        if corners:
            thickness = corners
            if corners is True:
                thickness = 5
                
            # left top
            pygame.draw.line(surface, color, (left, top), (left+15, top), thickness) 
            pygame.draw.line(surface, color, (left, top), (left, top+15), thickness) 

            # right top
            pygame.draw.line(surface, color, (right, top), (right-15, top), thickness) 
            pygame.draw.line(surface, color, (right, top), (right, top+15), thickness) 

            # right bottom
            pygame.draw.line(surface, color, (right, bottom), (right-15, bottom), thickness) 
            pygame.draw.line(surface, color, (right, bottom), (right, bottom-15), thickness) 

            # left bottom
            pygame.draw.line(surface, color, (left, bottom), (left+15, bottom), thickness) 
            pygame.draw.line(surface, color, (left, bottom), (left, bottom-15), thickness) 
        
        # --- other ---

        if other:
            points = ( (left+5, top+5), (left+5, top+30), (left+50, top+30), (left+50+10, top+20), (right-5, top+20), (right-5, top+5) )
            
            pygame.draw.polygon(surface, (*color2, 128), points)
            #pygame.draw.polygon(surface, color, points, 1)
            pygame.draw.lines(surface, color, False, points[1:-1], 1)
            

            points = ( (left+5, bottom-5), (left+5, bottom-20), (right-50-10, bottom-20), (right-50, bottom-30), (right-5, bottom-30), (right-5, bottom-5) )
            
            pygame.draw.polygon(surface, (*color2, 128), points)
            #pygame.draw.polygon(surface, color, points, 1)
            pygame.draw.lines(surface, color, False, points[1:-1], 1)

    def draw_bars(self, surface, rect):
        #pygame.draw.rect(surface, 
        width, height = rect.size
        
        color1 = self.color
        color2 = (0, 80, 110, 128)
        
        for x, size in zip(range(15, width-15, 10), self.points):
            pygame.draw.rect(surface, color2, (x, 15, 5, height-30), 0) 
            pygame.draw.rect(surface, color1, (x, 15+size, 5, height-30-size), 0) 

    def update(self):
        global redrawing
        
        time = pygame.time.get_ticks()
        
        if time >= self.anim_time:
            self.draw_bars(self.image, self.rect)
            
            self.points.pop(0)
            self.points.append(random.randint(5, self.rect.height-30))

            self.anim_time = time + self.anim_deltatime
            redrawing = True            

class Border2(MovableWidget):
    
    def __init__(self, x, y, width, height, movable=False, color=(0, 100, 255), fill=(0,0,0,128)):
        self.hover = False
        self.moving = False

        self.movable = movable
        self.color = color
        self.fill = fill
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.image.fill(fill)
        
        # --- object ---

        self.points = []
        for _ in range(25, width-15, 50):
            self.points.append(random.randint(5, height-30))
        
        self.draw_bars(self.image, self.rect)
        
        # --- boder ---
 
        self.border_rect = pygame.Rect(x, y, width, height)
        self.border = pygame.Surface( self.border_rect.size ).convert_alpha()
        self.border.fill((0,0,0,0))
        self.draw_border(self.border, self.border_rect, self.color, True, 3, False)
        
        self.anim_deltatime = 250
        self.anim_time = pygame.time.get_ticks() + self.anim_deltatime

    def draw_border(self, surface, rect, color, border=True, corners=True, other=False):
        
        left, top = 0, 0
        width, height = rect.size
        right, bottom = width-1, height-1

        color2 = tuple(x*50//100 for x in color)

        # --- border ---
        
        if border:
            thickness = border
            if border is True:
                thickness = 1

            size_x = 50 
            size_y = 50
            
            print(left)
            points = [
                    (left, top), 
                        (left+size_x, top), (left+size_x+5, top+5),
                        (right-size_x-5, top+5), (right-size_x, top), 
                    (right, top),
                        (right, top+size_y), (right-5, top+size_y+5),
                        (right-5, bottom-size_y-5), (right, bottom-size_y), 
                    (right, bottom),
                        (right-size_x, bottom), (right-size_x-5, bottom-5), 
                        (left+size_x+5, bottom-5), (left+size_x, bottom),
                    (left, bottom), 
                         (left, bottom-size_y), (left+5, bottom-size_y-5),
                        (left+5, top+size_y+5), (left, top+size_y), 
                    (left, top), 
                    ]
                      
            pygame.draw.lines(surface, color2, False, points) 

        # --- corners ---

        if corners:
            thickness = corners
            if corners is True:
                thickness = 5
                
            # left top
            pygame.draw.line(surface, color, (left, top), (left+15, top), thickness) 
            pygame.draw.line(surface, color, (left, top), (left, top+15), thickness) 

            # right top
            pygame.draw.line(surface, color, (right, top), (right-15, top), thickness) 
            pygame.draw.line(surface, color, (right, top), (right, top+15), thickness) 

            # right bottom
            pygame.draw.line(surface, color, (right, bottom), (right-15, bottom), thickness) 
            pygame.draw.line(surface, color, (right, bottom), (right, bottom-15), thickness) 

            # left bottom
            pygame.draw.line(surface, color, (left, bottom), (left+15, bottom), thickness) 
            pygame.draw.line(surface, color, (left, bottom), (left, bottom-15), thickness) 
        
        # --- other ---

        if other:
            points = ( (left+5, top+5), (left+5, top+30), (left+50, top+30), (left+50+10, top+20), (right-5, top+20), (right-5, top+5) )
            
            pygame.draw.polygon(surface, (*color2, 128), points)
            #pygame.draw.polygon(surface, color, points, 1)
            pygame.draw.lines(surface, color, False, points[1:-1], 1)
            

            points = ( (left+5, bottom-5), (left+5, bottom-20), (right-50-10, bottom-20), (right-50, bottom-30), (right-5, bottom-30), (right-5, bottom-5) )
            
            pygame.draw.polygon(surface, (*color2, 128), points)
            #pygame.draw.polygon(surface, color, points, 1)
            pygame.draw.lines(surface, color, False, points[1:-1], 1)

    def draw_bars(self, surface, rect):
        #pygame.draw.rect(surface, 
        width, height = rect.size
        
        color1 = self.color
        color2 = (0, 80, 110, 128)
        color3 = (255, 190, 50, 255)
        
        points = []
        
        for x, size in zip(range(25, width-15, 50), self.points):
            points.append( (x, size) )
            
        import pygame.gfxdraw
        
        for p1, p2 in zip(points, points[1:]):
            pygame.gfxdraw.line(surface, *p1, *p2, color2)
        
        for x, y in points:
            pygame.draw.rect(surface, color3, (x-2, y-2, 4, 4), 0) 
            #pygame.gfxdraw.circle(surface, color1, (x, y), 10, 1) 
            pygame.gfxdraw.aacircle(surface, x, y, 10, color1) 
            

    def update(self):
        global redrawing
        
        time = pygame.time.get_ticks()
        
        if time >= self.anim_time:
            self.draw_bars(self.image, self.rect)
            
            #self.points.pop(0)
            #self.points.append(random.randint(5, self.rect.height-30))

            self.anim_time = time + self.anim_deltatime
            redrawing = True            

# --------------------------------------------------------------------
import random # choice
import itertools # cycle

colors = (
        (255, 0, 0), 
        (0, 255, 0), 
        (0, 0, 255), 
        
        (255, 255, 0), 
        (255, 0, 255), 
        (0, 255, 255), 
        
        (255, 128, 0), 
        (255, 0, 128), 
        (0, 255, 128), 
        (128, 255, 0), 
        (0, 128, 255), 
        (128, 0, 255), 
        (0, 0, 0),
        (255, 255, 255),
    )

events_table = {
    pygame.QUIT: [on_quit],
    pygame.KEYDOWN: [on_keydown],
    #pygame.MOUSEMOTION: [on_mouse_move],
    #pygame.MOUSEBUTTONDOWN: [on_mouse_press],
    #REDRAW: [on_draw],
    #pygame.VIDEOEXPOSE: [on_draw],
}

# ---

pygame.init()
pygame.mixer.quit()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font_monospace_20 = pygame.font.SysFont('Monospace', 20, True)

# --- background ---

widgets = [
    Rectangle(0, 0, WIDTH, HEIGHT, False, (100, 255,0), fill=(255,255,255,0), grid=True),
    StaticImage(0, 0, 'image.jpg'),
]

# --- buttons ---

margin_x = ((WIDTH+10)%110) // 2
margin_y = ((HEIGHT+10)%110) // 2

colors_cycle = itertools.cycle(colors[:6])

for y in range(margin_y, HEIGHT-margin_y, 110)[:3]:
    for x in range(margin_x, WIDTH-margin_x, 110)[:5]:
        #color = random.choice(color)
        color = next(colors_cycle)
        widgets.append(Button(x, y, 100, 100, True, color, black_margin=15))

# --- windows ---

# blue window
widgets.append(Window(WIDTH-320, 20, 300, 300, True, (0, 128, 255)))

# green window
widgets.append(Window(WIDTH-640, 20, 300, 100, True, (100, 255,0))) 

# --- rectangles ---

# white rectangle
for i, color in enumerate(colors[:3] + colors[-1:]):
    widgets.append(Rectangle(20+i*290, HEIGHT-170, 275, 150, True, (100, 255,0), fill=(*color,32)))

#widgets.append(Rectangle(WIDTH-320, HEIGHT-170, 101, 151, True, (100, 255,0), fill=(255,255,255,32)))
#widgets.append(Rectangle(WIDTH//2-150, HEIGHT-170, 101, 151, True, (100, 255,0), fill=(0,0,255,32)))

# --- circles ---

widgets.append(Circle(900, 50, 130, True, (100, 255,0), fill=(*color,32)))

# --- borders ---

widgets.append(Border1(20, 200, 305, 200, True, (0, 180, 220)))
widgets.append(Border2(325, 200, 305, 200, True, (0, 180, 220)))
widgets.append(Border1(325, 400, 305, 200, True, (0, 180, 220)))
widgets.append(Border2(20, 400, 305, 200, True, (0, 180, 220)))

# --- images ---

# inverted image
widgets.append(ImageInvert(920, 360, 250, 250, True, (100, 255,0), 'image.jpg'))

# normal image
widgets.append(ImageNormal(650, 360, 250, 250, True, (100, 255,0), 'image.jpg'))

# ---------------------------------------------------------------------

running = True
redrawing = True

#pygame.event.post(pygame.event.Event(REDRAW))
#pygame.event.post(pygame.event.Event(pygame.VIDEOEXPOSE))

while running:

    for event in pygame.event.get():
        if event.type in events_table:
            for func in events_table[event.type]:
                if func(event) == True:
                    break
        for w in reversed(widgets):
            if w.handle_event(event) == True:
                break
            
    for w in widgets:
        w.update()
        
    if redrawing:
        screen.fill(BLACK)
        on_draw()
        redrawing = False
    
    clock.tick(25)
    
pygame.quit()

# --------------------------------------------------------------------
