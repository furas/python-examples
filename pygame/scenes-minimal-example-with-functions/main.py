#!/usr/bin/env python3

#
# source: https://stackoverflow.com/a/47460947/1832058
# author: https://stackoverflow.com/users/6220679/skrx
#
# minimal example of scenes (using functions)
# 

import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 400))
clock = pg.time.Clock()
BLUE = pg.Color('dodgerblue3')
ORANGE = pg.Color('sienna3')


def front_page():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return None
            # Press a key to return the next scene.
            elif event.type == pg.KEYDOWN:
                return menu

        screen.fill(BLUE)
        pg.display.flip()
        clock.tick(60)


def menu():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return None
            # Press a key to return the next scene.
            elif event.type == pg.KEYDOWN:
                return front_page

        screen.fill(ORANGE)
        pg.display.flip()
        clock.tick(60)


def main():
    scene = front_page  # Set the current scene.
    while scene is not None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                scene = None

        # Execute the current scene function. When it's done
        # it returns either the next scene or None which we
        # assign to the scene variable.
        scene = scene()


main()
pg.quit()
