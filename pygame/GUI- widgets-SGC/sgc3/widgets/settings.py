# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Settings for games, these include:

  * CONTROLS
  
    * Keymap
    * Mouse Sensitivity (speed) TODO
    
  * DISPLAY
  
    * Resolution (width, height) TODO
    * Fullscreen (bool) TODO

"""

import pygame
from pygame.locals import *

from ..locals import *
from _locals import *
from base_widget import Simple


class Keys(Simple):

    _can_focus = True  # Override Simple

    """
    Screen used to change keymap settings.

    Keys is a special widget that will fill the screen and take
    over the game loop for maximum effiencency.

    """

    def __init__(self, keymap_file, parent=None, **kwargs):
        """
        Extend Simple and prepare the key order.

        keymap_file -- String containing filename containing keymap.
                       Key order should be on second line.
        parent,kwargs -- Pass through to Simple

        """
        size = self._default_screen.size
        Simple.__init__(self, size, parent, **kwargs)
        # Load key order
        with open(keymap_file) as f:
            f.readline()
            self._key_order = eval(f.readline())
        assert isinstance(self._key_order, list)

    def add(self):
        """
        Display the settings for the keymap to the player.

        """
        # Display title
        message = Surface(font_title.render("Keymap Settings",
                                            True, font_col))
        message.y = 30
        message.x = (self._parent.w - message.w)/2
        self._parent().blit(message(), message.pos)
        # Display settings
        positions = {}
        temp_y = 100
        row = 0
        for key in self._key_order:
            if temp_y > (self._parent.h - message.h*2):
                row += 1
                temp_y = 100
            # Render name
            message = Surface(font_widget.render(key.title(),
                                                 True, font_col))
            message.y = temp_y
            message.x = 30 + ((self._parent.w-30)/3) * row
            self._parent().blit(message(), message.pos)
            # Render keymap
            message = Surface(font_widget.render(
                              pygame.key.name(keymap[key]),
                              True, font_col))
            message.y = temp_y
            message.x = ((((self._parent.w-30)/3) * (row+1) - 30) -
                         message.w/2)
            self._parent().blit(message(), message.pos)
            positions[key] = message
            temp_y += message.h*2

        # Event loop
        keypress_wait = False
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                exit() #TODO exit to menu

            elif event.type == MOUSEBUTTONDOWN and not keypress_wait:
                # If clicking a key, then prepare to change keymap
                for key in positions:
                    if pygame.mouse.get_pos()[0] >= positions[key].x and \
                      pygame.mouse.get_pos()[1] >= positions[key].y and \
                      pygame.mouse.get_pos()[0] <= positions[key].x + \
                                                   positions[key].w and \
                      pygame.mouse.get_pos()[1] <= positions[key].y + \
                                                   positions[key].h:

                        # Replace key with 'press key...' message
                        self._parent().fill((0,0,0), positions[key].rect)
                        message = Surface(font_widget.render(
                                          "press key...", True, font_col))
                        message.y = positions[key].y
                        message.x = positions[key].x - \
                                    (message.w - positions[key].w)/2
                        positions[key] = message
                        self._parent().blit(message(), message.pos)
                        keypress_wait = key

            elif event.type == KEYDOWN and keypress_wait:
                # When waiting for new key, replace text with new key
                if event.key != K_ESCAPE:
                    keymap[keypress_wait] = event.key
                self._parent().fill((0,0,0), positions[keypress_wait].rect)
                message = Surface(font_widget.render(
                                  pygame.key.name(keymap[keypress_wait]),
                                  True, font_col))
                message.y = positions[keypress_wait].y
                message.x = positions[keypress_wait].x - \
                            (message.w - positions[keypress_wait].w)/2
                positions[keypress_wait] = message
                self._parent().blit(message(), message.pos)
                keypress_wait = None
            pygame.display.update()
