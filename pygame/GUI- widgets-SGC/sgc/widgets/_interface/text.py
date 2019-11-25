# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

import warnings

import pygame
from pygame.locals import *

from .._locals import *

class SelectableText:
    _text = ""
    _text_offset = _text_pos = 0

    __blink = True
    _blink_time = 0
    _chars = ((0,0),)
    _repeat_key = None
    _repeat_time = 0
    _select = None  # Starting point of selection
    __cursor_pos = 0

    @property
    def _blink(self):
        """Always return False when a selection is made."""
        return self.__blink and not bool(self._select)
    @_blink.setter
    def _blink(self, value):
        self.__blink = value

    def _select_fix(self):
        """
        Returns the selection area corrected, so if the selection is
        right-to-left it returns the positions reversed.

        """
        if self._select > self._cursor_pos:
            return (self._cursor_pos, self._select)
        else:
            return (self._select, self._cursor_pos)

    def _calc_chars(self):
        """
        Calculates the position and size of each character.
        Stores the results in self._chars as a tuple of (pos, width) tuples.

        """
        p = self._settings["font"].size(self._text[0])[0]
        chars = [(0,p)]
        for c in range(len(self._text)):
            w = self._settings["font"].size(self._text[:c+2])[0]
            xmax, advance = self._settings["font"].metrics(
                self._text[c])[0][1::3]
            if xmax > advance:  # Adjust for overhang
                chars.append((p - (xmax - advance), w - p))
            else:
                chars.append((p, w - p))
            p = w
        self._chars = tuple(chars)

    def _mouse_cursor(self, mouse_pos):
        """Return the text cursor position of the mouse."""
        pos = mouse_pos[0] - self.rect_abs.x - self._text_pos
        for index, (p,w) in enumerate(self._chars):
            if pos <= p + w/2:
                break
        return index

    def _update_select_text(self, time):
        """
        Update text stuff for selectable text.

        Should be called from widget's update() method.

        """
        # Repeat key if held down
        if self._repeat_key:
            self._repeat_time += time
            while self._repeat_time > self._settings["repeat_begin"]:
                self._repeat_time -= self._settings["repeat_interval"]
                self._event(self._repeat_key)

    def _event_select_text(self, event):
        """
        Handles events for selectable text.

        Call from widget's _event() method.

        """
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Begin drawing selection
            if pygame.key.get_mods() & KMOD_SHIFT and self._select is None:
                self._select = self._cursor_pos
            self._cursor_pos = self._mouse_cursor(event.pos)
            if not pygame.key.get_mods() & KMOD_SHIFT:
                self._select = self._cursor_pos
        elif event.type == MOUSEMOTION and event.buttons[0]:
            # Continue drawing selection while mouse held down
            self._cursor_pos = self._mouse_cursor(event.pos)
        elif event.type == MOUSEBUTTONUP:
            # Set cursor position with mouse click
            self._cursor_pos = self._mouse_cursor(event.pos)
            if self._select == self._cursor_pos:
                self._select = None
        elif event.type == KEYDOWN:
            # Save last key press for repeat
            if self._repeat_key != event:
                self._repeat_key = event
                self._repeat_time = 0
            if event.key == K_ESCAPE:
                self._select = None
            elif event.key == K_LEFT:
                if not event.mod & KMOD_SHIFT:
                    self._select = None  # Break selection
                elif self._select is None:
                    # Reset selection if not selecting
                    self._select = self._cursor_pos
                self._cursor_pos -= 1
                # Remove selection when cursor is at same position
                if self._select == self._cursor_pos:
                    self._select = None
            elif event.key == K_RIGHT:
                if not event.mod & KMOD_SHIFT:
                    self._select = None  # Break selection
                elif self._select is None:
                    self._select = self._cursor_pos
                self._cursor_pos += 1
                if self._select == self._cursor_pos:
                    self._select = None
            elif event.key == K_HOME:
                if not event.mod & KMOD_SHIFT:
                    self._select = None
                elif self._select is None:
                    self._select = self._cursor_pos
                self._cursor_pos = 0
                if self._select == self._cursor_pos:
                    self._select = None
            elif event.key == K_END:
                if not event.mod & KMOD_SHIFT:
                    self._select = None
                elif self._select is None:
                    self._select = self._cursor_pos
                self._cursor_pos = len(self._text)
                if self._select == self._cursor_pos:
                    self._select = None
            elif event.mod & KMOD_CTRL:
                if event.key == K_a:  # Select all
                    self._select = 0
                    self._cursor_pos = len(self._text)
                elif event.key == K_c and self._select is not None:  # Copy
                    select = self._select_fix()
                    string = "".join(self._text[select[0]:select[1]])
                    try:
                        pygame.scrap.put(SCRAP_TEXT, string)
                    except pygame.error:
                        warnings.warn("Please run 'pygame.scrap.init()'"
                                      " to use the clipboard.", RuntimeWarning)
        elif event.type == KEYUP:
            if self._repeat_key and self._repeat_key.key == event.key:
                self._repeat_key = None  # Stop repeat

    def _update_modify_text(self, time):
        """
        Update text stuff for editable text (e.g. input box).

        Should be called from widget's update() method.

        """
        # If enough time has passed, blink cursor
        self._blink_time += time
        if self._blink_time > self._settings["blink_interval"]:
            self._blink_time -= self._settings["blink_interval"]
            self._blink = not self._blink

    def _event_modify_text(self, event):
        """
        Handles events for editable text (e.g. input box).

        Should be called from widget's _event() method.
        Will typically be used alongside `_event_select_text()`.

        """
        if event.type == KEYDOWN:
            # Reset cursor blink when typing
            self._blink_time = 0
            self._blink = True
            if event.key in (9,K_RETURN,K_ESCAPE):  # Keys to ignore
                return
            elif event.key == K_BACKSPACE:
                if self._select is not None:
                    self._delete_selection()
                elif self._cursor_pos > 0:
                    self._cursor_pos -= 1
                    self._text.pop(self._cursor_pos)
                    self._calc_chars()
            elif event.key == K_DELETE:
                if self._select is not None:
                    self._delete_selection()
                elif self._cursor_pos < len(self._text):
                    self._text.pop(self._cursor_pos)
                    self._calc_chars()
            elif event.unicode:
                if event.mod & KMOD_CTRL:
                    if event.key == K_v:  # Paste
                        text = pygame.scrap.get(SCRAP_TEXT)
                        if text:
                            if self._select is not None:
                                sel = self._select_fix()
                                self._select = None
                            else:
                                sel = (self._cursor_pos, self._cursor_pos)
                            # Get list of text to insert into input_text
                            text = [unicode(char) for char in text]
                            self._text[sel[0]:sel[1]] = text
                            self._calc_chars()
                            self._cursor_pos = sel[0] + len(text)
                    elif event.key == K_x and self._select is not None:  # Cut
                        select = self._select_fix()
                        string = "".join(self._text[select[0]:select[1]])
                        try:
                            pygame.scrap.put(SCRAP_TEXT, string)
                        except pygame.error:
                            warnings.warn("Please run 'pygame.scrap.init()'"
                                          " to use the clipboard",
                                          RuntimeWarning)
                        self._delete_selection()
                else:
                    # Delete selection
                    if self._select is not None:
                        self._delete_selection()
                    # Insert new character
                    if len(self._text) < self._settings["max_chars"]:
                        self._text.insert(self._cursor_pos, event.unicode)
                        self._calc_chars()
                        self._cursor_pos += 1

    def _delete_selection(self):
        """Delete the current selection of text."""
        select = self._select_fix()
        del self._text[select[0]:select[1]]
        self._select = None
        self._cursor_pos = select[0]
        self._calc_chars()

    def _draw_selection(self, image, y, height):
        """Draw selection onto image. Does nothing if no selection."""
        if self._select is None:
            return
        select = self._select_fix()
        # Semi-transparent selection rectangle
        w = self._chars[select[1]][0] - self._chars[select[0]][0]
        x = self._chars[select[0]][0] + self._text_pos - 1
        r = Rect((x,y), (w+2,height))
        selection = pygame.surface.Surface(r.size, flags=SRCALPHA)
        selection.fill(self._settings["col_selection"] + (100,))
        image.blit(selection, r)
        # Border around selection rectangle
        pygame.draw.rect(image, self._settings["col_selection"], r, 1)

    @property
    def _cursor_pos(self):
        """
        The cursor position in characters. Will ensure cursor is always in
        valid location when set.

        """
        return self.__cursor_pos
    @_cursor_pos.setter
    def _cursor_pos(self, value):
        # Keep cursor position within text
        self.__cursor_pos = min(max(value, 0), len(self._text))

        # Ensure text is visible when less than full width
        if self._chars[-1][0] < self.rect.w - self._text_offset:
            self._text_pos = self._text_offset
        else:
            # Scroll text in input box when it's too long
            pos = self._chars[self._cursor_pos][0]
            if pos > (self.rect.w - self._text_pos):
                self._text_pos = -(pos - self.rect.w + self._text_offset)
            elif pos < (self._text_offset - self._text_pos):
                self._text_pos = self._text_offset - pos
            # Ensure no unnecessary space is left at right-edge
            right_edge = self._chars[-1][0] - self.rect.w + self._text_offset
            if right_edge > 0:
                self._text_pos = max(-right_edge, self._text_pos)
