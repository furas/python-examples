#!/usr/bin/env python3

#
# http://stackoverflow.com/questions/21978044/clock-in-python
#

from pygame import *
from pygame.locals import *
from math import *

#----------------------------------------------------------------------

init()

screen = display.set_mode((800,600))

clock = time.Clock()

hours = 5
minutes = 59
seconds = 50

hours2 = 5
minutes2 = 59
seconds2 = 50

time_to_move_clock_1 = time.get_ticks()
time_to_move_clock_2 = time.get_ticks()

running=True
while running:

    # events

    for e in event.get():
        if e.type == QUIT:
            running = False

    # (variable) modifications

    if time_to_move_clock_1 <= time.get_ticks():
        time_to_move_clock_1 += 1000 # 1000ms = 1s

        seconds_ang = 270 + 6 * seconds

        seconds_dx = int(cos(radians(-seconds_ang))*200)
        seconds_dy = int(sin(radians(-seconds_ang))*200)

        minutes_ang = 270 + 6 * (minutes + seconds/60.)

        minutes_dx = int(cos(radians(-minutes_ang))*200)
        minutes_dy = int(sin(radians(-minutes_ang))*200)

        hours_ang = 270 + 30 * (hours + minutes/60.)

        hours_dx = int(cos(radians(-hours_ang))*150)
        hours_dy = int(sin(radians(-hours_ang))*150)

        seconds += 1

        if seconds == 60:
            seconds = 0
            minutes += 1

            if minutes == 60:
                minutes = 0
                hours += 1

                if hours == 12:
                    hours = 0

    if time_to_move_clock_2 <= time.get_ticks():
        time_to_move_clock_2 += 100 # 100ms = 0.1s (10 times faster)

        seconds_ang2 = 270 + 6 * seconds2

        seconds_dx2 = int(cos(radians(-seconds_ang2))*100)
        seconds_dy2 = int(sin(radians(-seconds_ang2))*100)

        minutes_ang2 = 270 + 6 * (minutes2 + seconds2/60.)

        minutes_dx2 = int(cos(radians(-minutes_ang2))*100)
        minutes_dy2 = int(sin(radians(-minutes_ang2))*100)

        hours_ang2 = 270 + 30 * (hours2 + minutes2/60.)

        hours_dx2 = int(cos(radians(-hours_ang2))*75)
        hours_dy2 = int(sin(radians(-hours_ang2))*75)

        seconds2 += 1

        if seconds2 == 60:
            seconds2 = 0
            minutes2 += 1

            if minutes2 == 60:
                minutes2 = 0
                hours2 += 1

                if hours2 == 12:
                    hours2 = 0

    # draw

    screen.fill((0,0,0))
    draw.circle(screen, (255,255,255), (400,300), 200, 3)
    draw.line(screen,(0,255,255), (400,300), (400 + hours_dx, 300 - hours_dy), 5)
    draw.line(screen,(255,255,0), (400,300), (400 + minutes_dx, 300 - minutes_dy), 2)
    draw.line(screen,(255,0,255), (400,300), (400 + seconds_dx, 300 - seconds_dy), 1)

    draw.circle(screen, (255,255,255), (100,100), 100, 3)
    draw.line(screen,(0,255,255), (100,100), (100 + hours_dx2, 100 - hours_dy2), 5)
    draw.line(screen,(255,255,0), (100,100), (100 + minutes_dx2, 100 - minutes_dy2), 2)
    draw.line(screen,(255,0,255), (100,100), (100 + seconds_dx2, 100 - seconds_dy2), 1)

    # flip

    display.flip()

    # FPS (Frames Per Seconds)

    clock.tick(25)

quit()

