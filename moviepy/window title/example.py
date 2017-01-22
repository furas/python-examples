#!/usr/bin/env python3

from moviepy.editor import *
import pygame

pygame.display.set_caption('Hello World!')

clip = VideoFileClip('video.avi')
clip.preview()

pygame.quit()
