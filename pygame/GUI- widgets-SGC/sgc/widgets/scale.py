# Copyright 2013 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Scale widget, allows the user to select a value along a scale using a slider.

"""

import pygame
from pygame.locals import *
from pygame import draw

from _locals import *
from base_widget import Simple

class Scale(Simple):

    """
    A scale slider.

    Attributes:
      value: Set and retrieve the value the slider is currently set to.

    Images:
      'image': The default button state.
      'handle': The slider handle.
      'handle_drag': The slider handle when the mouse is held down.

    """

    _can_focus = True
    _default_size = (200, 40)
    _surf_flags = SRCALPHA
    _extra_images = {"handle": ((), (0.5, 0)), "handle_drag": "handle"}
    _settings_default = {"col": (127, 127, 169), "inverted": False,
                         "show_value": 0, "min_step": 0, "small_step": 1,
                         "max_step": 10, "min": 0, "max": 100,
                         "label_col": Font.col, "label_font": Font["widget"]}

    _offset = None  # Offset from handle when dragging
    _old_value = None  # Old value used when cancelling drag

    _value = 0
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, val):
        if self._settings["min_step"] > 0:
            # Restrict value to a multiple of min_step
            temp = (int(val / self._settings["min_step"]) *
                    self._settings["min_step"])
            if (val%self._settings["min_step"] < self._settings["min_step"]/2):
                val = temp
            else:
                val = temp + self._settings["min_step"]
        self._value = max(self._settings["min"], min(self._settings["max"],val))

        # Position handle
        w = self.rect.w - 6 - self._images["handle"].rect.w
        percentage = (float(self.value - self._settings["min"]) /
                      (self._settings["max"] - self._settings["min"]))
        if self._settings["inverted"]:
            percentage = 1 - percentage
        self._images["handle"].rect.x = self._images["handle_drag"].rect.x = \
            3 + w*percentage
        self._switch()  # Redraw the value label

    def _config(self, **kwargs):
        """
          col: ``tuple`` (r,g,b) The colour of the fill bar.
          inverted: ``bool`` True if scale should go from right to left.
          show_value: Number of decimal digits to display, or False to
            display nothing.
          min: Value at low end of scale.
          max: Value at high end of scale.
          min_step: Minimum step, value will be a multiple of this.
          small_step: Step to increment by when using arrow keys.
          max_step: Step to increment by when holding Ctrl.
          label_col: Colour of value label.
          label_font: Font for value label.

        """
        for key in ("col", "inverted", "min", "max", "min_step", "max_step",
                    "show_value", "label_col", "label_font"):
            if key in kwargs:
                self._settings[key] = kwargs[key]

        if "init" in kwargs:
            self._images["handle"].rect.topleft = (3, self.rect.h / 2)
            self._images["handle_drag"].rect.topleft = (3, self.rect.h / 2)
            self._images["handle_drag"]._show = False
            # Make sure handle is in correct place when inverted
            self.value = self._settings["min"]

    def _draw_handle(self, image, size, col=(158,162,152)):
        pygame.draw.circle(image, (244,244,243),
                           (size[0]/2, size[1]/2), size[0]/2-1)
        pygame.draw.circle(image, col,
                           (size[0]/2, size[1]/2), size[0]/2, 2)

    def _draw_handle_drag(self, image, size):
        self._draw_handle(image, size, (149,181,216))

    def _draw_base(self):
        y = int(self.rect.h * .75) - 2
        colors = ((167,171,167), (181,184,181), (237,237,237), (167,171,167))
        for x, y, col in zip((1,0,0,1), range(y, y+4), colors):
            pygame.draw.line(self._images["image"], col,
                             (3+x,y), (self.rect.w-3-x,y))

    def _switch(self, state=None):
        Simple._switch(self, state)
        if self._settings["show_value"] is not False:
            lbl = "%.*f" % (self._settings["show_value"], self.value)
            val = self._settings["label_font"].render(
                lbl, True, self._settings["label_col"])
            x = self._images["handle"].rect.centerx - (val.get_width() / 2)
            x = max(0, min(self.rect.w - val.get_width(), x))
            y = self._images["handle"].rect.top - val.get_height()
            self.image.blit(val, (x,y))

    def _event(self, event):
        """Respond to events."""
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if self._images["handle"].rect_abs.collidepoint(event.pos):
                    # Start drag
                    self._images["handle"]._show = False
                    self._images["handle_drag"]._show = True
                    self._offset = (event.pos[0] -
                                    self._images["handle"].rect_abs.x)
                    self._old_value = self.value
                else:
                    # Jump to click
                    x = ((event.pos[0] - self._images["handle"].rect.w/2) -
                         (self.rect_abs.x + 3.))
                    x /= (self.rect.w - 6 - self._images["handle"].rect.w)
                    if self._settings["inverted"]:
                        x = 1 - x
                    diff = self._settings["max"] - self._settings["min"]
                    self.value = self._settings["min"] + (x * diff)
            elif event.button == 3:
                # Jump towards mouse on right-click
                mod = -1 if self._settings["inverted"] else 1    
                if event.pos[0] > self._images["handle"].rect_abs.centerx:
                    self.value += mod * self._settings["max_step"]
                else:
                    self.value -= mod * self._settings["max_step"]
            # Scroll
            elif event.button in (4,6):
                inc = (self._settings["max"] - self._settings["min"]) * .017
                inc = max(inc, self._settings["min_step"])
                if self._settings["inverted"]:
                    inc = -inc
                self.value -= inc
            elif event.button in (5,7):
                inc = (self._settings["max"] - self._settings["min"]) * .017
                inc = max(inc, self._settings["min_step"])
                if self._settings["inverted"]:
                    inc = -inc
                self.value += inc
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            # Stop drag
            self._images["handle"]._show = True
            self._images["handle_drag"]._show = False
        elif event.type == MOUSEMOTION and self._images["handle_drag"]._show:
            # Dragging
            x = (event.pos[0] - self._offset) - (self.rect_abs.x + 3.)
            x /= (self.rect.w - 6 - self._images["handle"].rect.w)
            if self._settings["inverted"]:
                x = 1 - x
            diff = self._settings["max"] - self._settings["min"]
            self.value = self._settings["min"] + (x * diff)
        elif event.type == KEYDOWN:
            mod = -1 if self._settings["inverted"] else 1   
            if event.key in (K_LEFT, K_MINUS, K_KP_MINUS):
                if event.mod & KMOD_CTRL:
                    self.value -= mod * self._settings["max_step"]
                else:
                    self.value -= mod * self._settings["small_step"]
            elif event.key in (K_RIGHT, K_PLUS, K_KP_PLUS):
                if event.mod & KMOD_CTRL:
                    self.value += mod * self._settings["max_step"]
                else:
                    self.value += mod * self._settings["small_step"]
            elif event.key == K_PAGEUP:
                self.value -= mod * self._settings["max_step"]
            elif event.key == K_PAGEDOWN:
                self.value += mod * self._settings["max_step"]
            elif event.key == K_HOME:
                self.value = self._settings["min"]
            elif event.key == K_END:
                self.value = self._settings["max"]
            elif event.key == K_ESCAPE and self._images["handle_drag"]._show:
                # Cancel drag
                self._images["handle"]._show = True
                self._images["handle_drag"]._show = False
                self.value = self._old_value

    def _focus_enter(self, focus):
        """Draw rectangle when focus is gained from keyboard."""
        if focus == 1:
            self._draw_rect = True
            self._switch()

    def _focus_exit(self):
        """Stop drawing rectangle when focus is lost."""
        self._draw_rect = False
        self._switch()
