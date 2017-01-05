#!/usr/bin/env python3

#
# http://stackoverflow.com/questions/21978044/clock-in-python
#

from pygame import *
from pygame.locals import *
from math import *

#----------------------------------------------------------------------

class Clock(object):

    def __init__(self, hours, minutes, seconds, cx, cy, r):

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.cx = cx
        self.cy = cy
        self.r = r

        self.hours_dx = self.cx
        self.hours_dy = self.cy - self.r*.75
        self.minutes_dx = self.cx
        self.minutes_dy = self.cy - self.r
        self.seconds_dx = self.cx
        self.seconds_dy = self.cy - self.r

    def update(self):

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

clock1 = Clock(5, 59, 0, 400, 300, 200)
clock2 = Clock(5, 59, 0, 100, 100, 100)
clock3 = Clock(3, 9, 0, 700, 100, 100)
clock4 = Clock(7, 24, 0, 100, 500, 100)
clock5 = Clock(11, 30, 0, 700, 500, 100)

CLOCK1 = USEREVENT+1
CLOCK2 = USEREVENT+2
CLOCK3 = USEREVENT+3
CLOCK4 = USEREVENT+4
CLOCK5 = USEREVENT+5

timer1 = time.set_timer(CLOCK1, 1000)
timer2 = time.set_timer(CLOCK2, 100)
timer3 = time.set_timer(CLOCK3, 100)
timer4 = time.set_timer(CLOCK4, 10)
timer5 = time.set_timer(CLOCK5, 10)


running=True
while running:

    # events

    for e in event.get():
        if e.type == QUIT:
            running = False

        elif e.type == CLOCK1:
            clock1.update()
        elif e.type == CLOCK2:
            clock2.update()
        elif e.type == CLOCK3:
            clock3.update()
        elif e.type == CLOCK4:
            clock4.update()
        elif e.type == CLOCK5:
            clock5.update()

    # (variable) modifications

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

    clock.tick(60)

quit()
