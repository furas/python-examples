# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Boxes are container widgets with automatic positioning/padding of widgets.

"""

from container import Container

class VBox(Container):

    """
    VBox is a container widget which sorts widgets into a vertical
    structure.

    If ``surf`` is not given, container will be the right size to fit all
    widgets.

    """

    _settings_default = {"border": 5, "spacing": 5, "col": 0, "widgets": None}

    def _config(self, **kwargs):
        """
          widgets: ``list`` Contains widgets to pack into box.
              The order of widgets in the list denotes order they are packed.
          border: ``int`` Number of pixels to space around edges when ``surf``
              is not given.
          col: ``tuple`` (r,g,b) Colour for background, 0 is transparent.
          spacing: ``int`` Number of pixels to space between widgets.

        """
        if "spacing" in kwargs:
            self._settings["spacing"] = kwargs["spacing"]
        if "widgets" in kwargs:
            pos = 0
            # Shift widget positions so all labels are displayed.
            width = 0
            for w in kwargs["widgets"]:
                if w._label is not None and w._label.side == "left":
                    width = max(width, w._label.rect.w)

            for w in kwargs["widgets"]:
                offset = 0
                if w._label is not None:
                    if w._label.side == "top":
                        offset = w._label.rect.h
                    r = w.rect.union(w._label.rect)
                else:
                    r = w.rect
                w.pos = (width, pos + offset)
                pos += r.h + self._settings["spacing"]
        Container._config(self, **kwargs)

class HBox(Container):

    """
    HBox is a container widget which sorts widgets into a horizontal
    structure.

    If ``surf`` is not given, container will be the right size to fit all
    widgets.

    """

    _settings_default = {"border": 5, "spacing": 5, "col": 0, "widgets": None}

    def _config(self, **kwargs):
        """
          widgets: ``list`` Contains widgets to pack into box.
              The order of widgets in the list denotes order they are packed.
          border: ``int`` Number of pixels to space around edges when ``surf``
              is not given.
          col: ``tuple`` (r,g,b) Colour for background, 0 is transparent.
          spacing: ``int`` Number of pixels to space between widgets.

        """
        if "spacing" in kwargs:
            self._settings["spacing"] = kwargs["spacing"]
        if "widgets" in kwargs:
            pos = 0
            # Shift widget positions so all labels are displayed.
            height = 0
            for w in kwargs["widgets"]:
                if w._label is not None and w._label.side == "top":
                    height = max(height, w._label.rect.h)

            for w in kwargs["widgets"]:
                offset = 0
                if w._label is not None:
                    if w._label.side == "left":
                        offset = w._label.rect.w
                    r = w.rect.union(w._label.rect)
                else:
                    r = w.rect
                w.pos = (pos + offset, height)
                pos += r.w + self._settings["spacing"]
        Container._config(self, **kwargs)
