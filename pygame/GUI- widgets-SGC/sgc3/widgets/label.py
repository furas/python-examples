# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Label to display information to the user.

"""

import pygame.mouse
from pygame.locals import *

from _locals import *
from base_widget import Simple
from _interface.text import SelectableText

class Label(Simple, SelectableText):

    """
    Label

    Attributes:
      text: ``str`` displayed in label. Can be assigned as a shortcut for
          ``config(text=)`` with no second paramenter.
    """

    _surf_flags = SRCALPHA
    _settings_default = {"text": "", "col": Font.col, "font": Font["widget"],
                         "col_selection": (118, 45, 215),
                         "repeat_begin": 300, "repeat_interval": 30}

    _over = False

    def _config(self, **kwargs):
        """
          text: Either ``str`` containing text to be displayed or
              ``tuple`` containing two strings. First string is text to
              be displayed, second string is rect attribute to be used
              for position. Defaults to 'topleft' if not passing a tuple.
          col: ``tuple`` (r,g,b) Text colour.
          font: Font object the label will render with.
          selectable: ``bool`` True if the text should be selectable.
          col_selection: ``tuple`` (r,g,b) Colour of selection rectangle.
          repeat_begin: ``int`` Milliseconds key is held down before repeating.
          repeat_interval: ``int`` Milliseconds between key repeats.

        """
        if "init" in kwargs:
            strings = pygame.cursors.textmarker_strings
            cursor = pygame.cursors.compile(strings)
            size = (len(strings[0]), len(strings))
            hotspot = (size[0]/2, size[1]/2)
            self._cursor = (size, hotspot) + cursor
        if "text" in kwargs:
            if isinstance(kwargs["text"], (str, unicode)):
                self._settings["text"] = kwargs["text"]
            else:
                self._settings["text"] = kwargs["text"][0]
                self._temp_pos = kwargs["text"][1]
        if "selectable" in kwargs:
            self._can_focus = kwargs["selectable"]
            if self._can_focus:
                self._calc_chars()

        assert "label" not in kwargs, "Use 'text', don't touch label."
        for key in ("col", "font", "col_selection", "repeat_begin",
                    "repeat_interval"):
            if key in kwargs:
                self._settings[key] = kwargs[key]
        
    def _draw_final(self):
        if hasattr(self, "_temp_pos"):
            pos = getattr(self.rect, self._temp_pos)

        # Split into lines
        text = []
        for line in self._settings["text"].split("\n"):
            text.append(self._settings["font"].render(line, True,
                                                      self._settings["col"]))

        # Dynamically set size
        h = 0
        for line in text:
            h += line.get_height()
        w = max(text, key=lambda x: x.get_width())
        self._create_base_images((w.get_width(), h))

        # Blit each line
        y = 0
        for line in text:
            self._images["image"].blit(line, (0,y))
            y += line.get_height()

        # Copy position attribute over
        if hasattr(self, "_temp_pos"):
            setattr(self.rect, self._temp_pos, pos)
            del self._temp_pos

    def _event(self, event):
        """_event will only be called if selectable."""
        self._event_select_text(event)

    def update(self, time):
        if self._can_focus:
            self._update_select_text(time)
            # Change cursor when mouse not held down
            if not pygame.mouse.get_pressed()[0]:
                if not self._over and \
                  self.rect_abs.collidepoint(pygame.mouse.get_pos()):
                    self._over = True
                    self._set_cursor(*self._cursor)
                elif self._over and \
                  not self.rect_abs.collidepoint(pygame.mouse.get_pos()):
                    self._over = False
                    self._remove_cursor()
            if self.has_focus():
                self._switch()

    def _switch(self, state=None, exiting=False):
        super(Label, self)._switch("image")
        if self._can_focus and exiting is False:
            if self._select is None:
                # Draw cursor in box
                x = self._chars[self._cursor_pos][0] - 1
                pygame.draw.line(self.image, (0,0,1), (x, 2),
                                 (x, self.rect.h-2))
            else:
                self._draw_selection(self.image, 1, self.rect.h - 2)

    @property
    def text(self):
        return self._settings["text"]
    @text.setter
    def text(self, value):
        self._settings["text"] = value
        self._draw()
        if self._can_focus:
            self._calc_chars()

    _text = text  # For SelectableText

    def _focus_exit(self):
        """Cancel any selection when focus is lost."""
        self._switch(exiting=True)
