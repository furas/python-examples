# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Base widget, all widgets inherit from this.

"""

import pygame
from pygame.locals import Rect, SRCALPHA
from pygame import draw

from _locals import *
from _locals import (has_focus, is_active, add_widget, remove_widget_order,
                     set_cursor, remove_cursor)
class Simple(pygame.sprite.Sprite):

    """
    Widget foundations all widgets should inherit from.
    This can also be used as a simple widget that does nothing, such as
    displaying an image.

    Attributes:
      image: The current surface that will be drawn to the screen.
      rect: The ``pygame.Rect`` used for the widget's position and size.
      rect_abs: A ``pygame.Rect`` using the absolute screen position.
      pos: The widget's position. Can be retrieved or assigned as a shortcut
          for rect.topleft. Also a shortcut for setting pos through config().
      pos_abs: The widget's absolute screen position.

    """

    # Widget settings
    _can_focus = False
    _modal = False
    _layered = False  # Layered updates for dialog windows etc.
    _default_size = None
    _image_state = "image"
    _parent = None
    _draw_rect = False
    _surf_flags = 0
    _available_images = ()
    _extra_images = {}
    _settings_default = {}

    _fade = None  # Alpha level when fading
    _fade_up = True
    _custom_image = False
    _custom_extra = ()
    _label = None

    def __init__(self, surf=None, flags=None, **kwargs):
        """
        Args:
          surf: The surface that should be drawn to screen, of type:
            pygame.Surface: Use an existing surface.
            tuple,list: Contains size as (width,height), creates a new surface.
            str: Contains file name to load an image.
            dict: Contains multiple images to be loaded. The documentation will
                specify if a widget uses multiple images and what names to use.
          flags: Override the flags passed to `pygame.surface.Surface`.
          kwargs: Any number of keyword arguments matching those for config().

        """
        pygame.sprite.Sprite.__init__(self)

        # Initialise attributes
        self._images = {}
        self._available_images = ("image",) + self._available_images
        self._settings = self._settings_default.copy()
        self.rect = Rect((0,0), (0,0))

        # Use default size if none specified
        if surf is None:
            surf = self._default_size
        elif isinstance(surf, (tuple, list)) and (isinstance(surf[0], str) or
                                                  isinstance(surf[1], str)):
            size = get_screen().rect.size
            s = list(surf)
            for i in (0,1):
                if isinstance(surf[i], str):
                    ratio = float(surf[i].rstrip("%")) / 100.
                    s[i] = size[i] * ratio
            surf = tuple(s)

        if flags is not None:
            self._surf_flags = flags

        # Create base surfaces if not None.
        # If None, widget is expected to call this function later.
        if surf is not None:
            self._create_base_images(surf)

        self.config(init=None, **kwargs)

    def _create_event(self, gui_type, **kwargs):
        """
        Returns a GUI `pygame.event.Event` object. The first argument must be
        the value for `gui_type` and should roughly describe the event.
        Optional keyword arguments can also be passed with additional
        attributes for the event.

        """
        return pygame.event.Event(
            GUI,
            dict(kwargs, **{"gui_type": gui_type, "widget_type": self.__class__,
                            "widget": self}))

    def config(self, **kwargs):
        """
        Update widget configuration and redraw the widget.

        Keyword Args:
          pos: ``tuple`` (x,y) Position to set widget to.
          label: ``str`` Text to display next to widget.
          label_side: ``str`` `("top", "right", "bottom", "left")`
              Which side of the widget to display the label.

        """
        if "pos" in kwargs:
            self.pos = kwargs["pos"]
        if "label" not in self._settings_default:
            if "label" in kwargs:
                if self._label is None:
                    self._label = _Label(kwargs["label"], self)
                else:
                    self._label.text = kwargs["label"]
                    self._label._draw()
            if "label_col" in kwargs:
                self._label_col = kwargs["label_col"]
                if self._label is not None:
                    self._label._draw()
            if "label_font" in kwargs:
                self._label_font = kwargs["label_font"]
                if self._label is not None:
                    self._label._draw()
            if "label_side" in kwargs:
                assert kwargs["label_side"] in ("top", "right",
                                                "bottom", "left"), \
                    "Must use: 'top', 'right', 'bottom' or 'left'"
                self._label_side = kwargs["label_side"]
        # Check if any callbacks have been passed in.
        callbacks = [x for x in kwargs if x.startswith("on_")]
        for f in callbacks:
            assert f in dir(self), "Invalid callback name: %s" % f
            assert callable(kwargs[f]), \
                "Callback '%s' must be callable: %s" % (f, kwargs[f])
            setattr(self, f, kwargs[f])
        self._config(**kwargs)
        self._draw()

    def _config(self, **kwargs):
        """Widgets should overload for custom widget configuration."""
        pass

    def add(self, order=None, fade=True, focus=False):
        """
        Add widget to screen.

        Args:
          order: Integer representing the order widget should receive focus
              when user presses TAB. The widget with the lowest order will
              receive focus first, then moving up with increasing values.
          fade: True if widget should fade in, False if not.
          focus: To focus widget immediately, use 1 if focused by keyboard,
              2 if by mouse, otherwise 0.

        """
        added = add_widget(self, order, focus)

        # Fade widget in
        if fade:
            self._fade_up = True
            if added and self._fade is None: self._fade = 1
            self.image.set_alpha(self._fade)
        else:
            self._fade = None
            self.image.set_alpha(255)

        # Add any associated label
        if self._label is not None:
            self._label.add(fade=fade)

    def remove(self, fade=True):
        """
        Remove widget from screen.

        Args:
          fade: True if widget should fade out.

        """
        if fade:  # Fade widget out
            self._fade_up = False
            if self._fade is None: self._fade = 250
        else:  # Remove widget immediately
            self.kill()
        remove_widget_order(self)
        if self.has_focus(): self._focus_exit()

        # Remove any associated label
        if self._label is not None:
            self._label.remove(fade)

    def active(self):
        """Return True if widget is active (onscreen)."""
        return is_active(self)

    def has_focus(self):
        """Return True if this widget has focus."""
        return has_focus(self)

    def _switch(self, image=None):
        """
        Switch image state to the given image name.

        Given no arguments will simply refresh the current image.

        """
        if image is not None:
            assert image in self._images, "Invalid image state %s" % image
            self._image_state = image
        assert self._images, ("Subclass of %s not initialised properly." %
                              self.__class__)
        self.image = self._images[self._image_state].copy()

        if self._draw_rect:
            self._dotted_rect()

    def update(self, time):
        """
        Overload to update the widget per frame.

        Args:
          time: Milliseconds passed since last frame.

        """
        pass

    def _event(self, event):
        """Overload to process events received by the widget one at a time."""
        pass

    def _draw(self):
        if not self._custom_image: self._draw_base()
        for name in self._custom_extra:
            f = getattr(self, "_draw_%s" % name)
            f(self._images[name].image, self._images[name].rect.size)
        self._draw_final()
        self._switch()

    def _draw_base(self):
        """
        Widgets should overload to draw default images found in self._images.
        This method will not be called when the user gives a custom image.

        """
        pass

    def _draw_final(self):
        """
        Widgets should overload to draw final things that should
        be drawn regardless of whether a custom image was used or not.

        """
        pass

    def _create_base_images(self, surf, parent=None):
        """
        Creates the base surfaces to draw on, or uses existing images.

        If self._default_size is None, widget is expected to call this
        function manually when no size is given.

        """
        Image = pygame.Surface
    
        def create_image(surf):
            """Return a created surface."""
            if isinstance(surf, Image):
                return surf
            elif isinstance(surf, (tuple,list)):
                if isinstance(surf[0], (tuple,list)):
                    assert (len(surf[0]) > 0 or len(surf[1]) > 0), "Must specify atleast one size"
                    if len(surf[0]) > 0:
                        w = self.rect.w * surf[0][0] + surf[0][1]
                    if len(surf[1]) > 0:
                        h = self.rect.h * surf[1][0] + surf[1][1]
                    if len(surf[0]) == 0:
                        w = h
                    if len(surf[1]) == 0:
                        h = w
                    surf = (w, h)
                surf = Image(surf, self._surf_flags)
                return surf
            elif isinstance(surf, str):
                return pygame.image.load(surf).convert_alpha()
            else:
                raise ValueError("Invalid surface object: %s" % type(surf))

        # Create base images
        self._custom_image = False
        images = False
        custom_extra = []
        if isinstance(surf, dict):
            for img in surf:
                assert (img in self._available_images or
                        img in self._extra_images), "Incorrect image"
                if img in self._extra_images:
                    if not isinstance(surf[img], (tuple,list)):
                        custom_extra.append(img)
                    self._images[img] = Simple(create_image(surf[img]))
                    self._images[img]._parent = self
                    self._images[img]._show = True
                else:
                    images = True
                    if not isinstance(surf[img], (tuple,list)):
                        self._custom_image = True
                    self._images[img] = create_image(surf[img])
        else:
            images = True
            if not isinstance(surf, (tuple,list)):
                self._custom_image = True
            self._images["image"] = create_image(surf)

        if not images and self._default_size is not None:
            images = True
            self._images["image"] = create_image(self._default_size)

        if images:
            # Copy other images, if any have not been supplied.
            assert "image" in self._images, "Must supply 'image'"
            for count, name in enumerate(self._available_images):
                if name not in self._images:
                    img = self._images[self._available_images[count-1]]
                    self._images[name] = img.copy()

            self.image = self._images["image"].copy()
            self.rect.size = self.image.get_size()

        # Set up extra images
        self._custom_extra = []
        for name in self._extra_images:
            if name not in self._images:
                copy = False
                n = name
                while isinstance(self._extra_images[n], str):
                    copy = True
                    n = self._extra_images[n]

                self._images[name] = Simple(create_image(self._extra_images[n]))
                self._images[name]._parent = self
                self._images[name]._show = True
                if copy and n in custom_extra:
                    self._images[name].image = self._images[n].image.copy()
                else:
                    self._custom_extra.append(name)

    def _change_focus(self, forward=True):
        """
        Called when focus should be changed. Used primarily by the Container
        widget.

        Args:
          forward: True if toggling focus forwards, False if backwards.

        Returns:
          True if widget should change focus from this widget.

        """
        return True

    def _focus_enter(self, focus=0):
        """
        Called when the widget gains focus. Overload to customise behaviour.

        Args:
          focus: 1 if focused by keyboard, 2 if by mouse.

        """
        pass

    def _focus_exit(self):
        """
        Called when the widget loses focus.
        Overload to customise behaviour.

        """
        pass

    def _dotted_rect(self, col=(255,255,255)):
        """Draw a dotted rectangle to show keyboard focus."""
        self.image.lock()
        for i in range(0, self.rect.w, 3):
            # Draw horizontal lines
            self.image.set_at((i, 0), col)
            self.image.set_at((i, self.rect.h-1), col)
        for i in range(0, self.rect.h, 2):
            # Draw vertical lines
            self.image.set_at((0, i), col)
            self.image.set_at((self.rect.w-1, i), col)
        self.image.unlock()

    def _set_cursor(self, size, hotspot, xormasks, andmasks):
        set_cursor(self, size, hotspot, xormasks, andmasks)

    def _remove_cursor(self):
        remove_cursor(self)


    # --PROPERTIES--

    @property
    def rect_abs(self):
        if self._parent is None:
            return self.rect
        else:
            p_abs = self._parent.pos_abs
            p = (self.rect.x + p_abs[0], self.rect.y + p_abs[1])
            return Rect(p, self.rect.size)

    @property
    def pos(self):
        return self.rect.topleft
    @pos.setter
    def pos(self, value):
        if not isinstance(value[0], str) and not isinstance(value[1], str):
            self.rect.topleft = value
        else:
            if self._parent is not None:
                size = self._parent.rect.size
            else:
                size = get_screen().rect.size
            pos = list(value)
            for i in (0,1):
                if isinstance(value[i], str):
                    ratio = float(value[i].rstrip("%")) / 100.
                    pos[i] = size[i] * ratio
            self.rect.topleft = pos
            
    @property
    def pos_abs(self):
        if self._parent is None:
            return self.rect.topleft
        else:
            p_abs = self._parent.pos_abs
            return (self.rect.x + p_abs[0], self.rect.y + p_abs[1])

class _Label(Simple):
    """
    Simple label that can be displayed next to widgets.

    This differs from the normal label widget in that it is attached to a widget
    and should not be used standalone. This is automatically attached by the
    base widget when the user passes the label argument to config().

    """
    _surf_flags = SRCALPHA

    text = ""

    def __init__(self, text, parent):
        """
        Args:
          text: Text label should display.
          parent: Widget label should be attached to.

        """
        pygame.sprite.Sprite.__init__(self)

        self.text = text
        self.parent = parent
        self._rect = Rect(0,0,0,0)

        self._draw()
        
    def _draw(self):
        """Redraw label."""
        # Split into lines
        text = []
        for line in self.text.split("\n"):
            text.append(self.font.render(line, True, self.col))

        # Dynamically set size
        h = 0
        for line in text:
            h += line.get_height()
        w = max(text, key=lambda x: x.get_width())
        self._rect.size = (w.get_width(), h)

        Image = pygame.Surface
        self.image = Image((w.get_width(), h), SRCALPHA)

        # Blit each line
        y = 0
        for line in text:
            self.image.blit(line, (0,y))
            y += self.font.get_linesize()

    @property
    def col(self):
        """
        Colour of label text. Defaults to Font.col. Changed in the
        base widget when "label_col" is passed to `self.config()`.

        """
        try:
            return self.parent._label_col
        except AttributeError:
            return Font.col

    @property
    def font(self):
        """
        Font used for label text. Defaults to Font["widget"]. Changed in
        the base widget when "label_font" is passed to `self.config()`.

        """
        try:
            return self.parent._label_font
        except AttributeError:
            return Font["widget"]

    @property
    def side(self):
        """
        Return which side widget should be attached to.
        Returns parent._label_side or defaults to "right".

        """
        try:
            return self.parent._label_side
        except AttributeError:
            return "right"

    @property
    def rect(self):
        """Returns the rect aligned to the appropriate side of it's parent."""
        if self.side == "left":
            self._rect.midright = self.parent.rect.midleft
        elif self.side == "right":
            self._rect.midleft = self.parent.rect.midright
        elif self.side == "top":
            self._rect.midbottom = self.parent.rect.midtop
        elif self.side == "bottom":
            self._rect.midtop = self.parent.rect.midbottom

        return self._rect
