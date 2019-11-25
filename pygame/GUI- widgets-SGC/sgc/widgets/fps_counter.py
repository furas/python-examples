# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
FPS counter, display current FPS performance to the user.

"""

from pygame.locals import SRCALPHA

from _locals import *
from base_widget import Simple

class FPSCounter(Simple):

    """
    FPS counter

    """

    _default_size = (80, 30)
    _settings_default = {"label": "", "clock": None}
    _surf_flags = SRCALPHA

    def _config(self, **kwargs):
        """
          clock: ``pygame.time.Clock`` Clock used to time the game loop.
          label: ``str`` Text to display in front of the value.

        """
        for key in ("clock", "label"):
            if key in kwargs:
                self._settings[key] = kwargs[key]

    def toggle(self):
        """Toggle the FPS counter, adding or removing this widget."""
        if self.active():
            if self._fade is not None:
                if self._fade_up:
                    self.remove()
                else:
                    self.add()
            else:
                self.remove()
        else:
            self.add()

    def update(self, time):
        """Update counter each frame."""
        text = Simple(Font["widget"].render(
            self._settings["label"] +
            str(round(self._settings["clock"].get_fps(), 1)),
            True, Font.col))
        text.rect.center = (self.rect.w/2, self.rect.h/2)
        self.image = text.image
