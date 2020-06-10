# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
A collection of things for widgets to use. These can be imported with a
`from _locals import *` line.

Constants:
  GUI: Widgets should use this for the event type of any events emitted.

get_screen(): Returns the screen object.

"""

import pygame.sprite
from pygame.locals import *

try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
except ImportError: pass

# Things for widgets to import
__all__ = ["GUI", "get_screen", "Font"]

# Event type
GUI = USEREVENT

SCREEN = None
get_screen = lambda: SCREEN

# Cursor queue for set_cursor() and remove_cursor()
cursors = []



# ----- EXTERNAL FUNCTIONS -----

def update(time):
    """Updates all active widgets or modal widgets each frame."""

    def _fade(widget):
        """Fade widget."""
        if widget._fade is not None:
            widget.image.set_alpha(widget._fade)
            if widget._fade_up:
                widget._fade += time / 3.
            else:
                widget._fade -= time / 4.
            if widget._fade <= 0:
                # Remove after fading
                widget.kill()
                # Reset widget to be added again
                widget._fade = None
            elif widget._fade >= 255:
                widget._fade = None
                widget.image.set_alpha(255)

    def draw_opengl(image, rect, alpha):
        texture_data = pygame.image.tostring(image, "RGBA")

        w,h = image.get_size()
        tex = glGenTextures(1)
        if alpha is None:
            alpha = 255.
        glColor(0,0,0, alpha/255.)
        glBindTexture(GL_TEXTURE_2D, tex)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_ADD)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA,
                     GL_UNSIGNED_BYTE, texture_data)

        glPushMatrix()
        glTranslatef(rect.x, rect.y, 0)

        glEnable(GL_TEXTURE_2D)
        #glBindTexture(GL_TEXTURE_2D, tex)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(0, 0)
        glTexCoord2f(1, 0)
        glVertex2f(w, 0)
        glTexCoord2f(1, 1)
        glVertex2f(w, h)
        glTexCoord2f(0, 1)
        glVertex2f(0, h)
        glEnd()

        glPopMatrix()

        glDeleteTextures(tex)

    def widget_image(w):
        """Blit extra images, handle transparency fades and blit to screen."""
        copy = w.image.copy()
        # Blit extra images onto copy
        for img in map(lambda x: w._images[x], w._extra_images):
            if img._show:
                copy.blit(img.image, img.rect)
        # Blend transparent surface when fading and blit to screen.
        if w._fade is not None:
            transparent = pygame.surface.Surface(w.rect.size, SRCALPHA)
            transparent.fill((255,255,255, w._fade))
            copy.blit(transparent, (0,0), special_flags=BLEND_RGBA_MULT)
        return copy

    if SCREEN._opengl:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        w,h = SCREEN.get_size()
        glOrtho(0, w, h, 0, 0, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glDisable(GL_LIGHTING)
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_SCISSOR_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Update widgets
    active_widgets.update(time)
    for widget in active_widgets:
        _fade(widget)
    for w in active_widgets:
        copy = widget_image(w)
        if not SCREEN._opengl:
            SCREEN.blit(copy, w.rect)
        else:
            draw_opengl(copy, w.rect, w._fade)

    # Update layered widgets
    layer_widgets.update(time)
    for widget in layer_widgets:
        _fade(widget)
    for w in layer_widgets:
        copy = widget_image(w)
        if not SCREEN._opengl:
            SCREEN.blit(copy, w.rect)
        else:
            draw_opengl(copy, w.rect, w._fade)

    if SCREEN._opengl:
        glDisable(GL_SCISSOR_TEST)
        glPopMatrix()

def event(event):
    """Send event to focused widget and handle widget focus."""
    # Special case gets priority over modal widgets (e.g. scroll handles)
    for w in special_case:
        if event.type == MOUSEBUTTONDOWN:
            if w.rect.collidepoint(event.pos):
                focus.add(2, w)
                break
            else:
                focus.empty()
    else:
        if modal_widgets and not focus:
            modal_widgets.sprites()[-1].add(0)

    # Mouse focus
    if event.type == MOUSEBUTTONDOWN:
        if not modal_widgets:
            hit = False
            for widget_list in (reversed(layer_widgets.sprites()),
                                active_widgets):
                for widget in widget_list:
                    # Check if user clicked a widget
                    if widget._can_focus and \
                       widget.rect.collidepoint(event.pos):
                        if event.button == 1:
                            focus.add(2, widget)
                            if widget in layer_widgets:
                                layer_widgets.move_to_front(widget)
                        elif 4 <= event.button <= 7:
                            widget._event(event)
                        hit = True
                        break
                if hit: break
            # Lose focus if clicking away from widgets
            if not hit:
                focus.empty()
    # Keyboard focus
    elif event.type == KEYDOWN and event.key == K_TAB:
        if not modal_widgets and focus_order:
            # Flattened focus_order
            order = sum(focus_order,())
            if focus.sprite not in order:
                curr_num = None
            else:
                # Focus number for current focused widget
                curr_num = order[order.index(focus.sprite)-1]
            # Sorted list of the focus numbers being used
            list_num = sorted(order[::2])
            if not event.mod & KMOD_SHIFT:  # Move focus to next widget
                if curr_num is None:
                    # If nothing focused, focus first widget
                    new_num = list_num[0]
                elif not focus.sprite._change_focus(True):
                    # Don't change when not at end of container widget
                    new_num = curr_num
                elif list_num.index(curr_num) == len(list_num)-1:
                    # Jump back to first widget
                    new_num = list_num[0]
                else:
                    # Next focus number in the list
                    new_num = list_num[list_num.index(curr_num)+1]
            else:  # Shift key - move focus to previous widget
                if curr_num is None:
                    new_num = list_num[-1]
                elif not focus.sprite._change_focus(False):
                    new_num = curr_num
                elif list_num.index(curr_num) == 0:
                    # Jump back to last widget
                    new_num = list_num[len(list_num)-1]
                else:
                    new_num = list_num[list_num.index(curr_num)-1]
            if curr_num != new_num:
                # Set widget at new focus number
                focus.add(1, order[order.index(new_num)+1])

    # Send event to focused widget
    if focus:
        focus.sprite._event(event)



# ----- FONTS -----

class _Font():
    """Wrapper class for font objects."""
    __slots__ = ("_font",)
    _font = None

    def replace(self, font):
        """Replace the font in-place."""
        self._font = font

    def __getattr__(self, atr):
        return getattr(self._font, atr)

    def __nonzero__(self):
        return True if self._font else False

class FontMetaclass(type):
    """Font metaclass to allow indexing of class."""
    def __getitem__(cls, item):
        return cls._fonts[item]

class Font():
    """
    Class containing fonts available for use.

    Index class to get fonts, such as ``Font["widget"]`` for the widget font.

    The default fonts are:
      widget: The default font for widgets.
      title: A larger title font.
      mono: A monospaced font.

    Attributes:
      col: (r,g,b) tuple, containing the default font colour.

    """

    __metaclass__ = FontMetaclass
    __slots__ = ("_fonts", "col")
    _fonts = {"widget": _Font(), "title": _Font(), "mono": _Font()}
    col = (255,255,255)

    @classmethod
    def set_fonts(cls, fonts={}):
        """
        Set fonts to a specific font. If a font exists, it will be replaced,
        otherwise it will be newly created.

        Args:
          fonts: Dictionary containing fonts to use.
              Key should be name of font. Value should be string
              naming either custom FreeType or a system font.

        """
        for font in fonts:
            if font not in cls._fonts:
                cls._fonts[font] = _Font()
            cls._fonts[font].replace(cls._create_font(fonts[font], 16))

        if not cls._fonts["widget"]:
            cls._fonts["widget"].replace(cls._create_font("Arial", 16))
        if not cls._fonts["title"]:
            name = fonts["widget"] if ("widget" in fonts) else "Arial"
            cls._fonts["title"].replace(cls._create_font(name, 30))
        if not cls._fonts["mono"]:
            cls._fonts["mono"].replace(cls._create_font(
                "Ubuntu Mono, FreeMono, Monospace", 16))

        #if SCREEN._opengl:
        #    cls.mono_w = cls["mono"].font.Advance("e")
        #else:
        cls.mono_w = cls["mono"].render("e", False, (0,0,0)).get_width()

    @classmethod
    def _create_font(cls, font, size):
        """
        Returns the correct font object for FreeType or system font, and
        for OpenGL or Pygame.

        """
        if font[-4:] in (".ttf", ".otf"):
            return pygame.font.Font(font, size)
        else:
            return pygame.font.SysFont(font, size)



# ----- WIDGET GROUPS -----

class Focus(pygame.sprite.GroupSingle):

    """
    Contains currently focused widget.

    """

    def add(self, focus=0, *sprites):
        """Extend add to call _focus_exit and _focus_enter methods."""
        if self.sprite: self.sprite._focus_exit()
        pygame.sprite.GroupSingle.add(self, *sprites)
        self.sprite._focus_enter(focus)

    def empty(self):
        """Extend empty to call _focus_exit method."""
        if self.sprite: self.sprite._focus_exit()
        pygame.sprite.GroupSingle.empty(self)

# Widget groups
active_widgets = pygame.sprite.Group()
modal_widgets = pygame.sprite.OrderedUpdates()
layer_widgets = pygame.sprite.LayeredUpdates()
special_case = set()
# The widget that currently has focus
focus = Focus()
# Order the widgets should receive focus through TAB
focus_order = []



# ----- WIDGET FUNCTIONS -----

def add_widget(widget, order=None, grab_focus=False):
    """
    Add widget to screen. Used by the base widget.

    Args:
      order: Integer representing the order widget should receive focus
          when user presses TAB. The widget with the lowest order will
          receive focus first, then moving up with increasing values.

    Returns:
      True if widget has been added. False if already added.

    """
    added = False
    # Add to group of active widgets
    if widget not in active_widgets and not widget._layered:
        active_widgets.add(widget)
        added = True
        if order is not None and widget._can_focus:
            focus_order.append((order,widget))
    # Add to layered group
    elif widget._layered and widget not in layer_widgets:
        layer_widgets.add(widget)
        added = True
    # Add to group of modal widgets
    if widget._modal and widget not in modal_widgets:
        modal_widgets.add(widget)
        added = True

    # Focus newly added modal widgets
    if grab_focus is not False:
        focus.add(grab_focus, widget)
    elif widget._modal:
        focus.add(0, widget)

    return added

def remove_widget_order(widget):
    """Remove widget from focus order. Called by the base widget."""
    order = sum(focus_order,())
    if widget in order:
        # Remove from focus_order
        num = (order.index(widget)-1)/2
        del focus_order[num]

def has_focus(widget):
    """Checks if a widget currently has focus."""
    for group in widget.groups():
        if isinstance(group, Focus):
            return True
    return False

def is_active(widget):
    """Checks if widget is onscreen."""
    return widget in active_widgets or widget in layer_widgets

def set_cursor(widget, size, hotspot, xormasks, andmasks):
    """
    Sets a cursor and adds to a queue.

    Args:
      widget: The widget that set the cursor, used as an ID in the queue.
      size,hotspot,xormasks,andmasks: Arguments for pygame.mouse.set_cursor().

    """
    if not cursors:
        cursors.append((None, pygame.mouse.get_cursor()))
    cursors.append((widget, (size, hotspot, xormasks, andmasks)))
    pygame.mouse.set_cursor(size, hotspot, xormasks, andmasks)

def remove_cursor(widget):
    """
    Removes the cursor set by widget and sets cursor to whichever cursor
    is now at the end of the queue.

    """
    for w, c in cursors:
        if w == widget:
            cursors.remove((w, c))
    pygame.mouse.set_cursor(*cursors[-1][1])
    if len(cursors) <= 1:
        del cursors[:]
