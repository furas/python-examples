import pygame


def to2D(point3D, dx=1, dy=1, dz=1):
    x, y, z = point3D
    u = (x*dx) // (z/dz)
    v = (y*dy) // (z/dz)
    return (u, v)
    
def center(point2D):
    x, y = point2D
    return x+400, 300-y
    
def move(point3D, dx=0, dy=0, dz=200):
    x, y, z = point3D
    return (x+dx, y+dy, z+dz)
    
# --- init ---
    
pygame.init()

screen = pygame.display.set_mode((800, 600))

# --- objects ---

points = [
    (100, 100, 100), 
    (100, -100, 100),
    (-100, -100, 100),
    (-100, 100, 100),
    (100, 100, -100), 
    (100, -100, -100),
    (-100, -100, -100),
    (-100, 100, -100),
]

lines = [
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4),
    (0,4), (1,5), (2,6), (3,7),
]
    
distance = 100

dx = 0
dy = 0
dz = 0

camera_x = 0
camera_y = 0
camera_z = 200
# --- mainloop ---

clock = pygame.time.Clock()
quit = False

while not quit:
    
    # --- events ---
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit = True
            elif  event.key == pygame.K_UP:
                dy -= 5
            elif  event.key == pygame.K_DOWN:
                dy += 5
            elif  event.key == pygame.K_LEFT:
                dx += 5
            elif  event.key == pygame.K_RIGHT:
                dx -= 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                quit = True
            elif  event.key == pygame.K_UP:
                dy += 5
            elif  event.key == pygame.K_DOWN:
                dy -= 5
            elif  event.key == pygame.K_LEFT:
                dx -= 5
            elif  event.key == pygame.K_RIGHT:
                dx += 5
                
    # --- updates ---
    
    camera_x += dx
    camera_y += dy
    camera_z += dz
    
    points_2D = [center(to2D(move(p, camera_x, camera_y, camera_z), distance, distance, 2)) for p in points]
    
    # --- draws ---
    
    screen.fill((0, 0, 0))

    for a, b in lines:
        p1 = points_2D[a]
        p2 = points_2D[b] 
        pygame.draw.line(screen, (255, 255, 255), p1, p2)
    pygame.display.flip()
    
    # --- FPS ---
    
    clock.tick(25)
    
pygame.quit()    
    
