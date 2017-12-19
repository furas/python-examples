#!/usr/bin/env python3

import pygame
import OpenGL.GL 
import OpenGL.GLU


def cube(vertices, edges):
    OpenGL.GL.glBegin(OpenGL.GL.GL_LINES)
    for edge in edges:
        for vertex in edge:
            OpenGL.GL.glVertex3fv(vertices[vertex]) 
    OpenGL.GL.glEnd()

def lines(vertices1, vertices2):
    for v1, v2 in zip(vertices1, vertices2):
        OpenGL.GL.glBegin(OpenGL.GL.GL_LINES)
        OpenGL.GL.glVertex3fv(v1) 
        OpenGL.GL.glVertex3fv(v2) 
        OpenGL.GL.glEnd()

def display_cube():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.DOUBLEBUF | pygame.OPENGL)
    
    OpenGL.GLU.gluPerspective(45, (WINDOW_WIDTH/WINDOW_HEIGHT), 0.1, 50.0)
    OpenGL.GL.glTranslatef(0.0, 0.0, -10)
    
    show_cube_1 = True
    show_cube_2 = True
    show_lines = True
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_1:
                    show_cube_1 = not show_cube_1
                elif event.key == pygame.K_2:
                    show_cube_2 = not show_cube_2
                elif event.key == pygame.K_0:
                    show_lines = not show_lines
                    
                    
        OpenGL.GL.glRotate(1, 3, 10, 10) # (angle,x,y,z)
        OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT | OpenGL.GL.GL_DEPTH_BUFFER_BIT)

        if show_cube_1:
            cube(vertices1, edges) # large cube
        if show_cube_2:
            cube(vertices2, edges) # small cube
        if show_lines:
            lines(vertices1, vertices2)
        
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

# --- 

vertices1 = ((1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,1),(1,1,1),(-1,-1,1),(-1,1,1))
vertices2 = ((2,-2,-2),(2,2,-2),(-2,2,-2),(-2,-2,-2),(2,-2,2),(2,2,2),(-2,-2,2),(-2,2,2))

edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))

display_cube()
