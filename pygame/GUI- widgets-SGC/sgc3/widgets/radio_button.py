# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Radio Button, allows the user to select a single option from a group.

"""

import pygame.mouse
from pygame.locals import *
from pygame import draw

from _locals import *
from _locals import focus
from base_widget import Simple

class Radio(Simple):

    """
    A selectable radio button.

    Attributes:
      radio_groups: A dictionary containing the active radio button or ``None``
          for each radio group. Key is ``str`` containing the name of the group.
      selected: True if widget is the currently selected radio button in
          it's group.

    Images:
      'image': The default, inactive button state.
      'over': The image used when the cursor is hovering over the button.
      'active': The image used for the active button in a group
          (if applicable).

    """

    _can_focus = True
    _default_size = (15,15)
    _available_images = ("over",)
    _surf_flags = SRCALPHA
    _extra_images = {"active": ((.7, 0), (.7, 0))}
    _settings_default = {"group": None, "col": (255,255,255)}

    _over_state = False

    radio_groups = {}
    _order = {}

    def _config(self, **kwargs):
        """
          group: ``str`` Name of the group for widget to be added to.
          active: ``True`` Makes this the active radio button for it's group.
          col: ``tuple`` (r,g,b) The colour to be used for the 'over' image
              if not using a custom image.

        """
        if "init" in kwargs:
            pos = ((self.rect.w - self._images["active"].rect.w) /2,
                   (self.rect.h - self._images["active"].rect.h) /2)
            self._images["active"].pos = pos
            self._images["active"]._show = False
        if "group" in kwargs:
            if kwargs["group"] not in self.radio_groups:
                self.radio_groups[kwargs["group"]] = None
                self._order[kwargs["group"]] = []
            self._settings["group"] = kwargs["group"]
            self._order[self._settings["group"]].append(self)
        if "col" in kwargs:
            self._settings["col"] = kwargs["col"]
        assert self._settings["group"] is not None, "Must provide group"
        if "active" in kwargs:
            self._activate()

    def _draw_base(self):
        pos = self.rect.center
        r = min(self.rect.size) / 2
        # Background circles
        draw.circle(self._images["image"], (255,255,255), pos, r)
        draw.circle(self._images["over"], self._settings["col"], pos, r)
        # Border circles
        draw.circle(self._images["image"], (0,0,1), pos, r, 1)
        draw.circle(self._images["over"], (0,0,1), pos, r, 1)

    def _draw_active(self, image, size):
        # Central dot for 'active' state
        r = min(size) / 2
        pos = (size[0] / 2, size[1] / 2)
        draw.circle(image, (92,161,233), pos, r)

    def on_select(self):
        """
        Called when the radio button is selected.

        Emits an event with attribute 'gui_type' == "select".

        Override this function to use as a callback handler.

        """
        pygame.event.post(self._create_event("select"))

    def update(self, time):
        """Update the radio button each frame."""
        if self.rect_abs.collidepoint(pygame.mouse.get_pos()):
            if not self._over_state:
                # Draw over state
                self._over_state = True
                self._switch("over")
        elif self._over_state:
            # Draw normal state
            self._over_state = False
            self._switch("image")

    def _event(self, event):
        if event.type == MOUSEBUTTONUP and event.button == 1:
            if self.rect_abs.collidepoint(event.pos):
                self._activate()
        elif event.type == KEYDOWN:
            def focus_change(diff):
                next_widget = order[order.index(widget) + diff]
                next_widget._activate()
                if self._parent:
                    self._parent._focus.add(1, next_widget)
                else:
                    focus.add(1, next_widget)
            order = self._order[self._settings["group"]]
            widget = self.radio_groups[self._settings["group"]]
            if event.key == K_UP and order.index(widget) > 0:
                focus_change(-1)
            elif event.key == K_DOWN and order.index(widget) < len(order)-1:
                focus_change(1)
        elif event.type == KEYUP:
            if event.key in (K_SPACE, K_RETURN):
                self._activate()

    def _focus_enter(self, focus):
        """Draw rectangle when focus is gained from keyboard."""
        if focus == 1:
            self._draw_rect = True
            self._switch()

    def _focus_exit(self):
        """Stop drawing rectangle when focus is lost."""
        self._draw_rect = False
        self._switch()

    def _activate(self):
        """Switch activated widget."""
        self.on_select()
        try:
            self.radio_groups[self._settings["group"]]._images["active"]._show=\
                False
        except AttributeError: pass
        self.radio_groups[self._settings["group"]] = self
        self._images["active"]._show = True

    def clear(self, group=None):
        """
        Clear a group so no radio button is selected.

        Args:
          group: ``str`` Group name to clear. Clear this widget's group if None.

        """
        if group is None: group = self._settings["group"]
        if self.radio_groups[group] is not None:
            self.radio_groups[group]._images["active"]._show = False
        self.radio_groups[group] = None

    @property
    def selected(self):
        return self is self.radio_groups[self._settings["group"]]
