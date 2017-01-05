#!/usr/bin/env python3

#
# http://stackoverflow.com/questions/21978044/clock-in-python
#

from pygame import *
from pygame.locals import *
from math import *

#----------------------------------------------------------------------

class Clock(object):

    def __init__(self, hours, minutes, seconds, cx, cy, r, ticks):

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.cx = cx
        self.cy = cy
        self.r = r
        self.ticks = ticks
        self.time_to_move = 0

    def update(self, current_ticks):

        if current_ticks > self.time_to_move:
            self.time_to_move += self.ticks

            self.seconds_ang = 270 + 6 * self.seconds

            self.seconds_dx = self.cx + int(cos(radians(-self.seconds_ang))*self.r)
            self.seconds_dy = self.cy - int(sin(radians(-self.seconds_ang))*self.r)

            self.minutes_ang = 270 + 6 * (self.minutes + self.seconds/60.)

            self.minutes_dx = self.cx + int(cos(radians(-self.minutes_ang))*self.r)
            self.minutes_dy = self.cy - int(sin(radians(-self.minutes_ang))*self.r)

            self.hours_ang = 270 + 30 * (self.hours + self.minutes/60.)

            self.hours_dx = self.cx + int(cos(radians(-self.hours_ang))*self.r*.75)
            self.hours_dy = self.cy - int(sin(radians(-self.hours_ang))*self.r*.75)

            self.seconds += 1

            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1

                if self.minutes == 60:
                    self.minutes = 0
                    self.hours += 1

                    if self.hours == 12:
                        self.hours = 0

    def draw(self, screen):
        draw.circle(screen, (255,255,255), (self.cx,self.cy), self.r, 3)
        draw.line(screen, (0,255,255), (self.cx,self.cy), (self.hours_dx, self.hours_dy), 5)
        draw.line(screen, (255,255,0), (self.cx,self.cy), (self.minutes_dx, self.minutes_dy), 2)
        draw.line(screen, (255,0,255), (self.cx,self.cy), (self.seconds_dx, self.seconds_dy), 1)

#----------------------------------------------------------------------

init()

screen = display.set_mode((800,600))

clock = time.Clock()

clock1 = Clock(5, 59, 0, 400, 300, 200, 1000)
clock2 = Clock(5, 59, 0, 100, 100, 100, 100)
clock3 = Clock(3, 9, 0, 700, 100, 100, 100)
clock4 = Clock(7, 24, 0, 100, 500, 100, 10)
clock5 = Clock(11, 30, 0, 700, 500, 100, 10)

running=True
while running:

    # events

    for e in event.get():
        if e.type == QUIT:
            running = False

    # (variable) modifications

    clock1.update(time.get_ticks())
    clock2.update(time.get_ticks())
    clock3.update(time.get_ticks())
    clock4.update(time.get_ticks())
    clock5.update(time.get_ticks())

    # draw

    screen.fill((0,0,0))

    clock1.draw(screen)
    clock2.draw(screen)
    clock3.draw(screen)
    clock4.draw(screen)
    clock5.draw(screen)

    # flip

    display.flip()

    # FPS (Frames Per Seconds)

    #clock.tick(60)

quit()
