#!/usr/bin/env python3

import pygame
import cv2

pygame.init()

# --- create PyGame image ---

pg_img = pygame.Surface((400, 200))
pygame.draw.circle(pg_img, (255,0,0), (0,0), 200)

# --- display PyGame image ---

screen = pygame.display.set_mode((400, 400))

screen.fill((255,255,255))
screen.blit(pg_img, pg_img.get_rect())
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False

pygame.quit()

# --- move from PyGame to CV2 ---

color_image = pygame.surfarray.array3d(pg_img)

color_image = cv2.transpose(color_image)
color_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)

# --- display CV2 image ---

cv2.imshow('Color', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- change CV2 image ---

color_image = cv2.rotate(color_image, cv2.ROTATE_90_CLOCKWISE)
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# --- display CV2 image ---

cv2.imshow('Gray', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- save in file in CV2 ---

cv2.imwrite('test.png', color_image)

# --- move back from CV2 to PyGame ---

gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)
gray_image = cv2.transpose(gray_image)

pg_img = pygame.surfarray.make_surface(gray_image)

# --- display PyGame image ---

screen = pygame.display.set_mode((400, 400))

screen.fill((255,255,255))
screen.blit(pg_img, pg_img.get_rect())
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False

pygame.quit()

