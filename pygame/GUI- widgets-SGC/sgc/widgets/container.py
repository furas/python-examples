# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Container widget, can be inherited to implement more complex behaviour.

"""

import pygame.sprite
from pygame.locals import *

from _locals import *
from _locals import Focus
from base_widget import Simple

class Container(Simple):

    """
    Container widget. Handles focus and events of a group
    of widgets packed into a single container.

    If ``surf`` is not given, container will be the right size to fit all
    widgets.

    """

    _can_focus = True
    _surf_flags = SRCALPHA
    _settings_default = {"border": 0, "col": 0, "widgets": None}

    _focus = None
    _order = None

    def _config(self, **kwargs):
        """
          widgets: ``list`` Contains widgets to be added at creation time.
              The order of widgets in the list denotes order they receive
              focus when user hits :kbd:`TAB`.
          border: ``int`` Number of pixels to space around edges when ``surf``
              is not given.
          col: ``tuple`` (r,g,b) Colour for background, 0 is transparent.

        """
        for key in ("border", "col"):
            if key in kwargs:
                self._settings[key] = kwargs[key]

        if "widgets" in kwargs:
            self._settings["widgets"] = pygame.sprite.Group()
            self._focus = Focus()
            self._order = []
            pad = self._settings["border"]
            for w in kwargs["widgets"]:
                w._parent = self
                w.pos = (w.rect.x + pad, w.rect.y + pad)
                self._settings["widgets"].add(w)
                if w._can_focus: self._order.append(w)
                if w._label is not None:
                    self._settings["widgets"].add(w._label)
            if not hasattr(self, "image"):
                def width_label(w):
                    if w._label is None:
                        return w.rect.right
                    else:
                        return max(w.rect.right, w._label.rect.right)
                def height_label(w):
                    if w._label is None:
                        return w.rect.bottom
                    else:
                        return max(w.rect.bottom, w._label.rect.bottom)
                w = max(kwargs["widgets"], key=width_label)
                if w._label is not None:
                    w = max(w.rect.right, w._label.rect.right)
                else:
                    w = w.rect.right
                h = max(kwargs["widgets"], key=height_label)
                if h._label is not None:
                    h = max(h.rect.bottom, h._label.rect.bottom)
                else:
                    h = h.rect.bottom
                self._create_base_images((w + pad, h + pad))

    def update(self, time):
        """Update widgets each frame."""
        self.image.fill(self._settings["col"])
        self._settings["widgets"].update(time)
        for w in self._settings["widgets"]:
            copy = w.image.copy()
            # Blit extra images onto copy
            for img in map(lambda x: w._images[x], w._extra_images):
                if img._show:
                    copy.blit(img.image, img.rect)
            self.image.blit(copy, w.pos)

    def _event(self, event):
        """Handle focus and send events to sub-widgets."""
        if event.type == MOUSEBUTTONDOWN:
            hit = False if event.button == 1 else True
            for widget in self._settings["widgets"]:
                # Check if user clicked a widget
                if widget._can_focus:
                    if widget.rect_abs.collidepoint(event.pos):
                        if event.button == 1:
                            self._focus.add(2, widget)
                        elif 4 <= event.button <= 7:
                            widget._event(event)
                        hit = True
                        break
            # Lose focus if clicking away from widgets
            if not hit:
                self._focus.empty()
        elif event.type == KEYDOWN and event.key == K_TAB:
            # Focus number for current focused widget
            if self._focus.sprite not in self._order:
                curr_num = None
            else:
                curr_num = self._order.index(self._focus.sprite)
            if not event.mod & KMOD_SHIFT:  # Move focus to next widget
                # Next focus number in the list
                if curr_num is None:
                    # If nothing focused, focus first widget
                    new_num = 0
                elif not self._focus.sprite._change_focus(True):
                    # Test for container widgets
                    new_num = curr_num
                elif curr_num >= len(self._order)-1:
                    new_num = 0
                else:
                    new_num = curr_num + 1
            else:  # Shift key - move focus to previous widget
                if curr_num is None:
                    new_num = -1
                elif not self._focus.sprite._change_focus(False):
                    new_num = curr_num
                elif curr_num <= 0:
                    new_num = -1
                else:
                    new_num = curr_num - 1
            if curr_num != new_num:
                self._focus.add(1, self._order[new_num])
        if self._focus:
            self._focus.sprite._event(event)

    def _change_focus(self, forward=True):
        """Override Simple and check if focus should leave yet."""
        if self._focus and not self._focus.sprite._change_focus(forward):
            return False
        if not self._focus:
            return False
        num = self._order.index(self._focus.sprite)
        if forward and num < len(self._order)-1:
            return False
        if not forward and num > 0:
            return False
        return True

    def _focus_exit(self):
        self._focus.empty()
