# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Common dialog widgets.

"""

import pygame

from .._locals import *

from .. import boxes
from ..container import Container
from ..button import Button
from ..label import Label
from ..dialog import Dialog

class DialogSaveQuit(Dialog):
    """
    This dialog should be called when a user attempts to quit without saving.
    The dialog will remove itself if the user has cancelled the action.

    """

    _settings_default = {"title": "Save Changes?", "widget": None,
                         "col_bg": (240,240,240), "col_border": (50,40,90),
                         "doc": "Untitled", "show_button": True}

    def _config(self, **kwargs):
        """
          doc: ``str`` The file name of the current document.

        """
        if "init" in kwargs:
            self._make_widgets()
            Dialog._config(self, widget=self._settings["widget"])
            if "pos" not in kwargs:
                self.rect.center = get_screen().rect.center
        if "doc" in kwargs:
            self._settings["doc"] = kwargs["doc"]
            self.lbl.text = (
                "Save changes to document \"%s\" before closing?\n\n"
                "If you don't save, changes will be permanently lost."
                 % self._settings["doc"])
        Dialog._config(self, **kwargs)

    def _make_widgets(self):
        self.lbl = Label(
            pos=(10,10), col=(20,20,20),
            text="Save changes to document \"%s\" before closing?\n\n"
                 "If you don't save, changes will be permanently lost." \
                 % self._settings["doc"])
        self.btn_save = Button(label="Save")
        self.btn_save.on_click = self.on_save
        self.btn_quit = Button((200,50), label="Close without saving")
        self.btn_quit.on_click = self.on_quit
        self.btn_cancel = Button(label="Cancel")
        self.btn_cancel.on_click = lambda: self.remove() or self.on_close()
        self.box = boxes.HBox(widgets=(self.btn_quit, self.btn_cancel,
                                       self.btn_save))
        self.box.rect.top = self.lbl.rect.h + 25
        
        self._settings["widget"] = Container(widgets=(self.lbl, self.box))

    def on_quit(self):
        """
        Called when the user clicks 'close without saving'.

        Emits an event with attribute 'gui_type' == "quit".

        Override this function to use as a callback handler.

        """
        ev = pygame.event.Event(GUI, {"gui_type": "quit",
                                      "widget_type": self.__class__,
                                      "widget": self})
        pygame.event.post(ev)

    def on_save(self):
        """
        Called when the user clicks the save button.

        Emits an event with attribute 'gui_type' == "save".

        Override this function to use as a callback handler.

        """
        ev = pygame.event.Event(GUI, {"gui_type": "save",
                                      "widget_type": self.__class__,
                                      "widget": self})
        pygame.event.post(ev)

    def on_close(self):
        """
        Called when the user cancels the action.

        Emits an event with attribute 'gui_type' == "cancel".

        Override this function to use as a callback handler.

        """
        ev = pygame.event.Event(GUI, {"gui_type": "cancel",
                                      "widget_type": self.__class__,
                                      "widget": self})
        pygame.event.post(ev)
