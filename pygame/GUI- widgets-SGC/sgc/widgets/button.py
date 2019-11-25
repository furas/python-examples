# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Button widget, allows input from the user clicking the button.

"""

import pygame
from pygame.locals import *
from pygame import draw

from _locals import *
from base_widget import Simple

class Button(Simple):

    """
    A clickable button.

    Images:
      'image': The default button state.
      'over': The image used when the cursor is hovering over the button.
      'down': The image used when the user is clicking down on the button.

    """

    _can_focus = True
    _default_size = (110, 50)
    _available_images = ("over", "down")
    _settings_default = {"label": ("",), "col": (127, 127, 169),
                         "label_col": Font.col, "label_font": Font["widget"]}

    _state = None

    def _config(self, **kwargs):
        """
          label: ``str`` Text to display on the button.
          col: ``tuple`` (r,g,b) The central colour used if no image is
              provided. If you want to avoid the colours saturating keep the
              RGB values below 200.
          label_col: ``tuple`` (r,g,b) The text colour for the button's label.
          label_font: Font object for label.

        """
        assert "label_side" not in kwargs, \
            "label_side is an invalid option for %s" % self.__class__
        # Label in middle of button
        if "label" in kwargs:
            # Save string as first argument
            self._settings["label"] = [kwargs["label"]]
            self._draw_label()
        if "col" in kwargs:
            self._settings["col"] = kwargs["col"]
        if "label_col" in kwargs:
            self._settings["label_col"] = kwargs["label_col"]
            self._draw_label()
        if "label_font" in kwargs:
            self._settings["label_font"] = kwargs["label_font"]
            self._draw_label()

    def _draw_label(self):
        # Clear previous renderings
        del self._settings["label"][1:]
        label = self._settings["label"][0].split("\n")
        f = self._settings["label_font"]
        h = f.get_ascent()
        for count, line in enumerate(label):
            lbl = Simple(f.render(line, True, self._settings["label_col"]))
            self._settings["label"].append(lbl)
            y = (self.rect.h - (h * len(label)) + f.get_descent()) / 2 + \
                (h * count)
            lbl.rect.midtop = (self.rect.w/2, y)

    def _draw_base(self):
        # Frames around edge of button
        x = min(self.image.get_size()) / 8
        self._frame_lt = ((0,0), (self.rect.w,0), (self.rect.w-x,x),
                          (x,x), (x,self.rect.h-x), (0,self.rect.h))
        self._frame_rb = ((self.rect.w,self.rect.h),
                          (0,self.rect.h), (x,self.rect.h-x),
                          (self.rect.w-x,self.rect.h-x),
                          (self.rect.w-x,x), (self.rect.w,0))
        cols = {}
        cols["image"] = self._settings["col"]
        cols["over"] = [min(c*1.1, 255) for c in self._settings["col"]]
        cols["down"] = [c*0.8 for c in self._settings["col"]]
        for img in cols:
            self._images[img].fill(cols[img])
            # Draw a frame around the edges of the button
            frame_lt_c = [min(c*1.3,255) for c in cols[img]]
            frame_rb_c = [c*0.8 for c in cols[img]]
            draw.polygon(self._images[img], frame_lt_c, self._frame_lt)
            draw.polygon(self._images[img], frame_rb_c, self._frame_rb)

    def _draw_final(self):
        for img in self._images.values():
            # Blit label onto button
            for line in self._settings["label"][1:]:
                img.blit(line.image, line.pos)

    def on_click(self):
        """
        Called when the button is clicked through either mouse or keyboard.

        Emits an event with attribute 'gui_type' == "click".

        Override this function to use as a callback handler.

        """
        pygame.event.post(self._create_event("click"))

    def update(self, time):
        """Update the button each frame."""
        if self.rect_abs.collidepoint(pygame.mouse.get_pos()):
            if self._state not in ("over","down"):
                # Draw over state
                self._state = "over"
                self._switch(self._state)
        elif self._state not in ("image","down"):
            # Draw normal state
            self._state = "image"
            self._switch(self._state)

    def _event(self, event):
        """Respond to events."""
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Draw down state
            self._state = "down"
            self._switch(self._state)
        elif (event.type == MOUSEBUTTONUP and event.button == 1 and
              self._state == "down"):
            self._state = None
            # If releasing mouse on button, call function
            if self.rect_abs.collidepoint(event.pos):
                self.on_click()
        elif event.type == KEYDOWN:
            if event.key in (K_SPACE, K_RETURN):
                self._state = "down"
                self._switch(self._state)
        elif event.type == KEYUP:
            if event.key in (K_SPACE, K_RETURN) and self._state == "down":
                self._state = None
                self.on_click()

    def _focus_enter(self, focus):
        """Draw rectangle when focus is gained from keyboard."""
        if focus == 1:
            self._draw_rect = True
            self._switch()

    def _focus_exit(self):
        """Stop drawing rectangle when focus is lost."""
        self._state = None
        self._draw_rect = False
        self._switch()
