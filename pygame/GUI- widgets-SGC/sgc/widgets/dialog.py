# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Dialog window, creates a popup window.

"""

import pygame.mouse
from pygame.locals import *
from pygame import draw

from _locals import *
from base_widget import Simple

class Dialog(Simple):

    """
    Dialog Window

    If ``surf`` is not given, window will be large enough to fit the
    given widget.

    Images:
      'close_off': The close button in the normal state.
      'close_over': The close button when the cursor is hovering over.

    """

    _can_focus = True
    _modal = True
    _layered = True
    _extra_images = {"close_off": ((0, 16), (0, 16)), "close_over": "close_off"}
    _settings_default = {"title": None, "widget": None, "col_bg": (240,240,240),
                         "col_border": (50,40,90), "show_button": True}

    _drag = _over = False

    def _config(self, **kwargs):
        """
          widget: Widget that should be displayed in the dialog window.
          title: ``str`` Text to display in the title bar.
          col_border: ``tuple`` (r,g,b) Window decoration colour.
          col_bg: ``tuple`` (r,g,b) Background colour.
          modal: ``bool`` ``True`` if window should be modal.
              Defaults to ``True``.

        """
        if "widget" in kwargs:
            self._settings["widget"] = kwargs["widget"]
            self._settings["widget"]._parent = self
            self._settings["widget"].pos = (2, 20)
            if not hasattr(self, "image"):
                r = self._settings["widget"].rect
                self._create_base_images((r.w + 4, r.h + 22))
        if "modal" in kwargs:
            self._modal = kwargs["modal"]
        if "show_button" in kwargs:
            self._settings["show_button"] = kwargs["show_button"]
            if not kwargs["show_button"]:
                self._images["close_over"]._show = False
                self._images["close_off"]._show = False

        for key in ("title", "col_border", "col_bg"):
            if key in kwargs:
                self._settings[key] = kwargs[key]

    def _draw_base(self):
        # Draw window
        inner_rect = Rect((2,20), (self.rect.w-4,self.rect.h-22))
        self._images["image"].fill(self._settings["col_border"])
        self._images["image"].fill(self._settings["col_bg"], inner_rect)

    def _draw_close_off(self, image, size):
        image.fill(self._settings["col_border"])
        draw.circle(image, (140,6,15), (size[0]/2, size[1]/2), 8)
        draw.line(image, (0,0,1), (5,5), (11,11), 3)
        draw.line(image, (0,0,1), (5,11), (11,5), 3)

    def _draw_close_over(self, image, size):
        image.fill(self._settings["col_border"])
        draw.circle(image, (234,14,50), (size[0]/2, size[1]/2), 8)
        draw.line(image, (0,0,1), (5,5), (11,11), 5)
        draw.line(image, (0,0,1), (5,11), (11,5), 5)

    def _draw_final(self):
        self._images["close_off"].pos = (2,2)
        self._images["close_over"].pos = (2,2)
        self._set_over()

        if self._settings["title"]:
            t = Simple(Font["widget"].render(
                self._settings["title"], True, Font.col))
            t.rect.x = self._images["close_off"].rect.right
            self._images["image"].blit(t.image, t.pos)

    def _set_over(self, over=None):
        """Set over state and show/hide close button images."""
        if self._settings["show_button"]:
            if over is not None: self._over = over
            self._images["close_over"]._show = self._over
            self._images["close_off"]._show = not self._over

    def on_close(self):
        """
        Called when the dialog window is closed.

        Emits an event with attribute 'gui_type' == "close".

        Override this function to use as a callback handler.

        """
        pygame.event.post(self._create_event("close"))

    def update(self, time):
        """Update dialog window each frame."""
        r = self._images["close_off"].rect_abs
        if not self._over and r.collidepoint(pygame.mouse.get_pos()):
            # Display over button
            self._set_over(True)
        elif self._over and not r.collidepoint(pygame.mouse.get_pos()):
            # Display normal button
            self._set_over(False)

        self._settings["widget"].update(time)
        self.image.blit(self._settings["widget"].image,
                        self._settings["widget"].pos)

    def _event(self, event):
        """Respond to events."""
        minus_pos = lambda p1, p2: (p1[0] - p2[0], p1[1] - p2[1])

        if event.type == MOUSEBUTTONDOWN and event.button == 1 and \
          self.rect.collidepoint(event.pos) and event.pos[1] < self.rect.y + 20:
            # Clicking title bar of window
            self._settings["widget"]._focus_exit()
            if (self._settings["show_button"] and
                self._images["close_off"].rect_abs.collidepoint(event.pos)):
                # Close button
                self.remove()
                self.on_close()
            else:
                # Initialise window drag
                self._offset = minus_pos(event.pos, self.pos)
                self._drag = True
        elif event.type == MOUSEMOTION and self._drag:
            # Move window
            self.pos = minus_pos(event.pos, self._offset)
        elif event.type == MOUSEBUTTONUP and event.button == 1 and self._drag:
            # Stop moving window
            self.pos = minus_pos(event.pos, self._offset)
            self._drag = False
        else:
            self._settings["widget"]._event(event)
