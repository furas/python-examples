# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Scroll box. A container widget that provides scroll bars to be able to
view a larger widget.

"""

import pygame.mouse
from pygame.locals import *
from pygame import draw

from _locals import *
from _locals import special_case, modal_widgets
from base_widget import Simple

class ScrollBox(Simple):

    """
    Scroll Box

    """

    _can_focus = True
    _default_size = (300, 200)
    _surf_flags = SRCALPHA
    _settings_default = {"widget": None, "col": (118, 45, 215)}

    _scroll_x = _scroll_y = None
    _handle_x = _handle_y = None

    def _config(self, **kwargs):
        """
          widget: Widget that should be displayed in scroll box.
          col: ``tuple`` (r,g,b) Colour used for scroll bars and handles.

        """
        if "widget" in kwargs:
            self._settings["widget"] = kwargs["widget"]
            self._settings["widget"]._parent = self
            self._settings["widget"].pos = (0,0)
            self._create_handles()
        if "col" in kwargs:
            self._settings["col"] = kwargs["col"]

    def _create_handles(self):
        # Create scroll bars and handles
        self._scroll_x = self._scroll_y = None
        self._handle_x = self._handle_y = None
        if self._settings["widget"].rect.w > self.rect.w:
            ratio = float(self.rect.w) / self._settings["widget"].rect.w
            self._scroll_x = Simple((self.rect.w * ratio, 3))
            self._scroll_x._parent = self
            self._scroll_x.image.fill(self._settings["col"])
            self._scroll_x.pos = (0, self.rect.h - 3)
            self._handle_x = _ScrollHandleH(widget=self)
        if self._settings["widget"].rect.h > self.rect.h:
            ratio = float(self.rect.h) / self._settings["widget"].rect.h
            self._scroll_y = Simple((3, self.rect.h * ratio))
            self._scroll_y._parent = self
            self._scroll_y.image.fill(self._settings["col"])
            self._scroll_y.pos = (self.rect.w - 3, 0)
            self._handle_y = _ScrollHandleV(widget=self)

    def update(self, time):
        """Update scroll box each frame."""
        self._settings["widget"].update(time)

        self.image.fill((255,255,255,0))
        self.image.blit(self._settings["widget"].image,
                        self._settings["widget"].pos)

        pos = pygame.mouse.get_pos()
        if self._scroll_y is not None:
            self.image.blit(self._scroll_y.image, self._scroll_y.pos)
            r = self._scroll_y.rect_abs
            # Add scroll handles when cursor moves near scroll bar
            if not self._handle_y.active() and \
               r.inflate(20, 5).collidepoint(pos):
                # Position to left if handle would be off-screen.
                edge = (r.right + self._handle_y.rect.w)
                if edge < get_screen().rect.w:
                    self._handle_y.rect.x = r.right
                else:
                    self._handle_y.rect.right = r.left
                self._handle_y.update_pos(pos[1])
                self._handle_y.add()

        if self._scroll_x is not None:
            self.image.blit(self._scroll_x.image, self._scroll_x.pos)
            r = self._scroll_x.rect_abs
            if not self._handle_x.active() and \
               r.inflate(5, 20).collidepoint(pos):
                edge = (r.bottom + self._handle_x.rect.h)
                if edge < get_screen().rect.h:
                    self._handle_x.rect.y = r.bottom
                else:
                    self._handle_x.rect.bottom = r.top
                self._handle_x.update_pos(pos[0])
                self._handle_x.add()

    def _event(self, event):
        """Respond to events."""
        self._settings["widget"]._event(event)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                self.scroll(y=-10)
            elif event.button == 5:  # Scroll down
                self.scroll(y=10)
            elif event.button == 6:  # Scroll left
                self.scroll(x=-10)
            elif event.button == 7:  # Scroll right
                self.scroll(x=10)

    def scroll(self, x=None, y=None):
        """Scroll by x and y coordinates."""
        if x is not None and self._scroll_x is not None:
            # Set scroll bar position
            r = self._scroll_x.rect
            r.x = max(min(r.x + x, self.rect.w - r.w), 0)
            # Set widget's position
            ratio = r.x / float(self.rect.w - r.w)
            max_w = self._settings["widget"].rect.w - self.rect.w
            self._settings["widget"].rect.x = -max_w * ratio
        if y is not None and self._scroll_y is not None:
            r = self._scroll_y.rect
            r.y = max(min(r.y + y, self.rect.h - r.h), 0)
            ratio = r.y / float(self.rect.h - r.h)
            max_h = self._settings["widget"].rect.h - self.rect.h
            self._settings["widget"].rect.y = -max_h * ratio

    def _change_focus(self, forward=True):
        return self._settings["widget"]._change_focus(forward)

    def _focus_enter(self, focus):
        self._settings["widget"]._focus_enter(focus)

    def _focus_exit(self):
        self._settings["widget"]._focus_exit()



class _ScrollHandle(Simple):

    """
    Scroll bar to manipulate scroll box.

    To be inherited from by _ScrollHandle[V/H], not to be used directly.

    Uses lots of getattr() and other tricks to provide inheritable functions.

    """

    _can_focus = True
    _layered = True

    _drag = None

    def _config(self, **kwargs):
        """
          widget: Scroll box that this handle should be synced to.

        """
        if "init" in kwargs:
            self._rect2 = self.rect_abs.inflate(20, 20)
        if "widget" in kwargs:
            self._parent_view = kwargs["widget"]

    def _draw_base(self):
        img = self._images["image"]
        img.fill(self._parent_view._settings["col"])
        img.fill((200,200,200), self.rect.inflate(-4, -4))
        # Draw line in center
        r = self.rect
        start_pos = (3, r.centery) if self.xy == "y" else (r.centerx, 3)
        end_pos = (r.w-4, r.centery) if self.xy == "y" else (r.centerx, r.h-4)
        draw.line(img, (100,100,100), start_pos, end_pos)
        # Draw arrows
        if self.xy == "y":
            points1 = ((3, r.h/4), (r.centerx, r.h/5-1), (r.w-3, r.h/4))
            points2 = ((3, r.h*.75), (r.centerx, r.h*.8), (r.w-3, r.h*.75))
        else:
            points1 = ((r.w/4, 3), (r.w/5-1, r.centery), (r.w/4, r.h-3))
            points2 = ((r.w*.75, 3), (r.w*.8, r.centery), (r.w*.75, r.h-3))
        draw.polygon(img, (50,50,50), points1)
        draw.polygon(img, (50,50,50), points2)

    def update_pos(self, xy):
        """
        Change position of scroll handle.

        Args:
          xy: Integer to move the scroll handle to, along the correct axis.

        """
        scroll_bar = getattr(self._parent_view, "_scroll_%s" % self.xy)
        if scroll_bar is not None:
            r = scroll_bar.rect_abs
            a,b = (r.bottom, r.top) if self.xy == "y" else (r.right, r.left)
            xy = min(a, max(xy, b))
            setattr(self.rect, "center%s" % self.xy, xy)
            self._rect2.center = self.rect.center

    def update(self, time):
        # Move handle to cursor when cursor not hovering over.
        if not self.rect.collidepoint(pygame.mouse.get_pos()):
            self.update_pos(pygame.mouse.get_pos()[0 if self.xy == "x" else 1])
        # Hide handle when cursor moves too far.
        if self._drag is None and \
           not self._rect2.collidepoint(pygame.mouse.get_pos()):
            self.remove()

    def _event(self, event):
        index = 1 if self.xy == "y" else 0
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and \
          self.rect.collidepoint(event.pos):
            # Initialise drag
            center = getattr(self.rect_abs, "center%s" % self.xy)
            self._offset = event.pos[index] - center
            self._drag = event.pos[index]
        elif self._drag is not None:
            if event.type == MOUSEMOTION:
                # Move scroll handle and bar
                self.update_pos(event.pos[index] - self._offset)
                kwarg = {self.xy: event.rel[index]}
                self._parent_view.scroll(**kwarg)
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                # Move scroll box up when clicked
                if -5 < (self._drag - event.pos[index]) < 5:
                    center = getattr(self.rect_abs, "center%s" % self.xy)
                    if event.pos[index] < center:
                        kwarg = {self.xy: -40}
                        self._parent_view.scroll(**kwarg)
                    else:
                        kwarg = {self.xy: 40}
                        self._parent_view.scroll(**kwarg)
                # Or stop moving and set final position after drag
                else:
                    self.update_pos(event.pos[index] - self._offset)
                self._drag = None

    def add(self, order=None, fade=True):
        # Only add if child of modal widget or no modal widget.
        try:
            modal = modal_widgets.sprites()[-1]
            parent = self._parent_view
            while parent:
                if parent is modal:
                    break
                parent = parent._parent
            else:
                return
        except IndexError: pass

        special_case.add(self)
        super(_ScrollHandle, self).add(order, fade)

    def remove(self, fade=True):
        special_case.discard(self)
        super(_ScrollHandle, self).remove(fade)

class _ScrollHandleV(_ScrollHandle):
    _default_size = (12,50)
    xy = "y"

class _ScrollHandleH(_ScrollHandle):
    _default_size = (50,12)
    xy = "x"
