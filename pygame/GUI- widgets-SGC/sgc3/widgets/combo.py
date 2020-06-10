# Copyright 2013 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Combo box widget, allows the user to choose an option from a selection.

"""

import pygame
from pygame.locals import *
from pygame import draw

from _locals import *
from base_widget import Simple

class Combo(Simple):

    """
    A combo box.

    Attributes:
      selection: ``int`` Set or retrieve index of current selection.

    """

    _can_focus = True
    _default_size = (200, 30)
    _settings_default = {"values": ()}

    _selection = -1
    @property
    def selection(self):
        return self._selection
    @selection.setter
    def selection(self, value):
        if value is None:
            self._selection = -1
        else:
            self._selection = min(max(0, value),len(self._settings["values"])-1)
        self._switch()

    _options = None

    def _config(self, **kwargs):
        """
          selection: Index of current selection, None if none selected.
          values: Sequence of strings to allow the user to select from.

        """
        if "values" in kwargs:
            self._settings["values"] = tuple(kwargs["values"])
            self._options = _Selection(values=self._settings["values"],
                                       parent=self)
        if "selection" in kwargs:
            self.selection = kwargs["selection"]
        if "init" in kwargs and self._options is None:
            self._options = _Selection(values=())

    def _draw_base(self):
        self._images["image"].fill((233,233,233))
        r = ((0,0), (self.rect.w-1, self.rect.h-1))
        pygame.draw.rect(self._images["image"], (178, 182, 178), r, 2)
        p = ((self.rect.w-20, self.rect.h/2-3),
             (self.rect.w-15, self.rect.h/2+3),
             (self.rect.w-10, self.rect.h/2-3))
        pygame.draw.line(self._images["image"], (136, 138, 133), p[0], p[1], 2)
        pygame.draw.line(self._images["image"], (136, 130, 133), p[1], p[2], 2)

    def on_select(self):
        """
        Called when the selection is changed.

        Emits an event with attribute 'gui_type' == "select",
        'selection' == index of selection made and
        'value' == value of selection made.

        Override this function to use as a callback handler.

        """
        pygame.event.post(self._create_event(
            "select", selection=self.selection,
             value=self._settings["values"][self.selection]))

    def _event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self._options.add(focus=2)
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                self.selection -= 1
                self.on_select()
            elif event.key == K_DOWN:
                self.selection += 1
                self.on_select()
            elif event.key in (K_PAGEUP, K_HOME):
                self.selection = 0
                self.on_select()
            elif event.key in (K_PAGEDOWN, K_END):
                self.selection = len(self._settings["values"]) - 1
                self.on_select()

    def _switch(self, state=None):
        Simple._switch(self, state)
        if self.selection > -1:
            val = self._settings["values"][self.selection]
            txt = Font["widget"].render(val, True, Color("black"))
            self.image.blit(txt, (5, (self.rect.h-txt.get_height())/2))

    def _focus_enter(self, focus):
        """Draw rectangle when focus is gained from keyboard."""
        if focus == 1:
            self._draw_rect = True
            self._switch()

    def _focus_exit(self):
        """Stop drawing rectangle when focus is lost."""
        self._draw_rect = False
        self._switch()


class _Selection(Simple):
    """Pop-up selection list."""

    _can_focus = True
    _layered = True
    _modal = True
    _extra_images = {"selection": ((1, 0), (0, 26))}  # TODO Dynamic height

    _padding = 6

    _options = ()
    _parent_combo = None
    _item_height = 4
    _col = Color("white")
    _col_selection = (74, 144, 217)

    def _config(self, **kwargs):
        if "parent" in kwargs:
            self._parent_combo = kwargs["parent"]
        if "values" in kwargs:
            self._options = tuple(Font["widget"].render(v, True, Color("black"))
                                  for v in kwargs["values"])
            self._item_height = Font["widget"].size("")[1] + self._padding

        self._create_base_images((self._parent_combo.rect.w - 4,
                                  self._item_height*len(self._options)))
        # TODO Replace alpha with blend flag. Should invert text colour.
        self._images["selection"].image.set_alpha(100)

    def add(self, order=None, fade=True, focus=False):
        self.rect.center = self._parent_combo.rect_abs.center
        # Attempt to keep within screen dimensions
        self.rect.bottom = min(self.rect.bottom, get_screen().rect.bottom)
        self.rect.top = max(self.rect.top, 0)
        Simple.add(self, order, fade, focus)

    def _draw_base(self):
        self._images["image"].fill(self._col)

    def _draw_final(self):
        for i, text in enumerate(self._options):
            self._images["image"].blit(text, (2, self._item_height*i + 2))

    def _draw_selection(self, image, size):
        image.fill(self._col_selection)

    def _event(self, event):
        if event.type == MOUSEMOTION:
            if self.rect_abs.collidepoint(event.pos):
                y = (event.pos[1] - self.pos_abs[1]) / self._item_height
                self._images["selection"].rect.y = y * self._item_height
                self._images["selection"]._show = True
            else:
                self._images["selection"]._show = False
        elif event.type == MOUSEBUTTONDOWN:
            if self.rect_abs.collidepoint(event.pos):
                y = (event.pos[1] - self.pos_abs[1]) / self._item_height
                self._parent_combo.selection = y
                self._parent_combo.on_select()
            self.remove()
