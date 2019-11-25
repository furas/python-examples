# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Switch widget, allows the user to change a boolean setting.

"""

import pygame
from pygame.locals import *
from pygame import display, draw

from _locals import *
from _locals import focus
from base_widget import Simple

class Switch(Simple):

    """
    A switch widget, allowing the user to select between two states.

    Attributes:
      state: True if switched on.

    Images:
      'image': The background when the widget is set to off.
      'active': The background when the widget is set to on.
      'handle': The image used for the slider.

    """

    _can_focus = True
    _default_size = (85,26)
    _available_images = ("active",)
    _extra_images = {"handle": ((0.5, -4), (1, -4))}
    _settings_default = {"state": False, "on_col": (88, 158, 232),
                         "off_col": (191, 191, 186),
                         "on_label_col": (255,255,255),
                         "off_label_col": (93,82,80)}

    _drag = None
    _handle_rect = None

    def _config(self, **kwargs):
        """
          state: ``bool`` Sets the state of the widget (False by default).
          on_col: ``tuple`` (r,g,b) The background colour when the widget is
              set to the 'on' state.
          off_col: ``tuple`` (r,g,b) The background colour when the widget is
              set to the 'off' state.
          on_label_col: ``tuple`` (r,g,b) The on/off text colour when the
              widget is set to the 'on' state.
          off_label_col: ``tuple`` (r,g,b) The on/off text colour when the
              widget is set to the 'off' state.

        """
        if "init" in kwargs:
            self._images["handle"].rect.y = 2
        if "state" in kwargs:
            self._settings["state"] = bool(kwargs["state"])

        for key in ("on_col", "off_col", "on_label_col", "off_label_col"):
            if key in kwargs:
                self._settings[key] = kwargs[key]

    def on_click(self):
        """
        Called when the switch widget is clicked by mouse or keyboard.

        Emits an event with attribute 'gui_type' == "click" and
        'on' == (True or False) depending on whether the switch is set to
        the on position or not.

        Override this function to use as a callback handler.

        """
        pygame.event.post(self._create_event("click", on=self.state))

    def _draw_base(self):
        # Draw main images
        for state in ("off", "on"):
            image = "image" if (state == "off") else "active"
            self._images[image].fill(self._settings[state + "_col"])

            # Render the labels
            col = self._settings[state + "_label_col"]
            on = Simple(Font["widget"].render("ON", True, col))
            off = Simple(Font["widget"].render("OFF", True, col))
            on.rect.center = (self.rect.w*.25 - 1, self.rect.h/2)
            off.rect.center = (self.rect.w*.75 + 1, self.rect.h/2)

            # Blit all text
            self._images[image].blit(on.image, on.pos)
            self._images[image].blit(off.image, off.pos)

    def _draw_handle(self, image, size):
        # Draw handle
        image.fill((245,245,244))
        w,h = size
        for x in range(2,5):  # Grips
            draw.line(image, (227,227,224), ((w/6)*x, h*.3), ((w/6)*x, h*.7), 3)

    def _event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # If clicking handle
            if self._images["handle"].rect.collidepoint(
                (event.pos[0]-self.pos_abs[0], event.pos[1]-self.pos_abs[1])):
                self._drag = (event.pos[0],
                              event.pos[0] - self._images["handle"].rect.x)
        elif event.type == MOUSEMOTION and event.buttons[0]:
            if self._drag is not None:
                # Move handle
                self._images["handle"].rect.x = max(min(
                    self.rect.w/2 + 2, event.pos[0] - self._drag[1]), 2)
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            if self._drag is not None:
                if abs(self._drag[0] - event.pos[0]) < 5:  # Clicked
                    self._settings["state"] = not self._settings["state"]
                else:  # Dragged
                    # Determine if dropped in on/off position
                    if self._images["handle"].rect.centerx < self.rect.w/2:
                        self._settings["state"] = False
                    else:
                        self._settings["state"] = True
                self._drag = None
                self.on_click()
                self._switch()
            elif self.rect_abs.collidepoint(event.pos):
                # Clicked outside of handle
                self._settings["state"] = not self._settings["state"]
                self.on_click()
                self._switch()
        elif event.type == KEYUP:
            if event.key in (K_RETURN, K_SPACE):
                self._settings["state"] = not self._settings["state"]
                self.on_click()
                self._switch()
        
    def _focus_enter(self, focus):
        """Draw dotted rect when focus is gained from keyboard."""
        if focus == 1:
            self._draw_rect = True
            self._switch()

    def _focus_exit(self):
        """Stop drawing dotted rect when focus is lost."""
        self._draw_rect = False
        self._switch()

    def _switch(self):
        img = "image" if (self._settings["state"] is False) else "active"
        super(Switch, self)._switch(img)

        self._fix_handle()

    def _fix_handle(self):
        """Fix handle position in place."""
        if self._drag is None:
            # Fix handle in place when not dragging
            if self._settings["state"] is False:
                self._images["handle"].rect.x = 2
            else:
                self._images["handle"].rect.x = self.rect.w/2 + 2

    @property
    def state(self):
        return self._settings["state"]
