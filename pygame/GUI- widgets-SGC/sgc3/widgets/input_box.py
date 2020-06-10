# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Input Box for receiving text input.

"""

import pygame
from pygame.locals import *
from pygame import draw

from _locals import *
from base_widget import Simple
from _interface.text import SelectableText

class InputBox(Simple, SelectableText):

    """
    Input box

    Attributes:
      text: Text entered in input box. Can be set or retrieved directly.

    Images:
      'image': The background of the input box when focused.
      'inactive': The background of the input box when not focused.

    """

    _can_focus = True  # Override Simple
    _default_size = (180, 30)
    _image_state = "inactive"
    _available_images = ("inactive",)
    _settings_default = {"default": "", "blink_interval": 600,
                         "col_selection": (118, 45, 215),
                         "col_focus": (255,255,255),
                         "col_focus_not": (200,200,200), "max_chars": 80,
                         "repeat_begin": 300, "repeat_interval": 30}

    _text_offset = _text_pos = 6

    def _config(self, **kwargs):
        """
          default: ``str`` Contains the default text displayed when nothing
              has been entered and input box does not have focus.
          blink_interval: ``int`` Milliseconds between cursor blink.
          col_focus: ``tuple`` (r,g,b) Background colour when focused.
          col_focus_not: ``tuple`` (r,g,b) Background colour when not focused.
          col_selection: ``tuple`` (r,g,b) Colour of selection rectangle.
          max_chars: ``int`` Maximum number of characters.
          repeat_begin: ``int`` Milliseconds key is held down before repeating.
          repeat_interval: ``int`` Milliseconds between key repeats.
          text: ``str`` Set the text entered in input box.

        """
        if "init" in kwargs:
            self._text = []
        if "text" in kwargs:
            self.text = kwargs["text"]
        
        for key in ("default", "blink_interval", "col_focus", "col_focus_not",
                    "col_selection", "max_chars", "repeat_begin",
                    "repeat_interval"):
            if key in kwargs:
                self._settings[key] = kwargs[key]

    def _draw_base(self):
        # Active state background
        self._images["image"].fill(self._settings["col_focus"])
        draw.rect(self._images["image"], (0,0,1), ((0,0), self.rect.size), 4)

        # Inactive state background
        self._images["inactive"].fill(self._settings["col_focus_not"])
        draw.rect(self._images["inactive"], (0,0,1), ((0,0), self.rect.size), 4)

    # Store the input text as a list
    @property
    def text(self):
        return "".join(self._text)
    @text.setter
    def text(self, txt):
        self._text = [unicode(char) for char in txt]
        # Re-evaluate cursor position.
        self._cursor_pos = self._cursor_pos
        self._calc_chars()

    def on_enter(self):
        """
        Called when the user hits the enter key.

        Emits an event with attribute 'gui_type' == "enter" and
        'text' with the text entered.

        Override this function to use as a callback handler.

        """
        pygame.event.post(self._create_event("enter", text=self.text))

    def update(self, time):
        """Update the input box each frame."""
        if self.has_focus():
            self._update_select_text(time)
            self._update_modify_text(time)
            # Draw input box
            self._switch("image")

    def _event(self, event):
        """Update text field based on input."""
        self._event_select_text(event)
        self._event_modify_text(event)
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.on_enter()

    def _focus_exit(self):
        """Draw non-focused input box when focus is lost."""
        self._switch("inactive")
        # Stop repeat key
        self._repeat_key = None

    def _switch(self, state=None):
        super(InputBox, self)._switch(state)
        # Draw dynamic stuff on active state
        if self._image_state == "image":
            # Draw text
            text = Simple(Font["mono"].render(self.text, True, (0,0,0)))
            text.rect.midleft = (self._text_offset, self.rect.h / 2)
            area = ((6-self._text_pos,0), (self.rect.w-8, self.rect.h))
            self.image.blit(text.image, text.pos, area)
            # Draw cursor
            if self._blink:
                x = self._chars[self._cursor_pos][0] + self._text_pos
                pygame.draw.line(self.image, (0,0,0), (x, 6),
                                 (x, self.rect.h-6))
            # Draw selection highlighting
            self._draw_selection(self.image, 5, self.rect.h - 9)
        # Draw text when switching to non-focused state
        else:
            if self._text:  # Blit input text into box...
                text = Simple(Font["mono"].render(self.text, True, (70,70,70)))
            else:  # ...or default text if empty.
                text = Simple(Font["mono"].render(self._settings["default"],
                                                  True, (70,70,70)))
            text.rect.midleft = (self._text_pos, self.rect.h / 2)
            self.image.blit(text.image, text.pos)

    def _calc_chars(self):
        """Optimised function for mono-width fonts."""
        try:
            p = self._text[0]
        except IndexError:
            return ((0,0),)

        p = Font["mono"].size(p)[0]
        chars = [(0,p)]
        try:  # Fails if text is empty
            for m in Font["mono"].metrics(self.text[1:]):
                chars.append((p, m[4]))
                p += m[4]
        except: pass
        chars.append((p,0))
        self._chars = tuple(chars)
