# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
All widgets are imported into sgc namespace. This means you can access
widgets in sgc namespace, such as ``sgc.Button``.

Module Packages:
  :py:mod:`widgets<sgc.widgets>`: All the widgets available for use in this toolkit.

Modules:
  :py:mod:`locals<sgc.locals>`: Constants to be imported into the local namespace for convenience.
  :py:mod:`surface<sgc.surface>`: Extended pygame.surface classes.

"""
__version__ = "0.2.1"

import surface
import locals
import widgets
from widgets._locals import Font, update, event
# Import widgets
from widgets.base_widget import Simple
from widgets.boxes import VBox, HBox
from widgets.button import Button
from widgets.combo import Combo
from widgets.container import Container
from widgets.composite.dialogs import DialogSaveQuit
from widgets.dialog import Dialog
from widgets.fps_counter import FPSCounter
from widgets.input_box import InputBox
from widgets.label import Label
from widgets.radio_button import Radio
from widgets.scroll_box import ScrollBox
from widgets.settings import Keys
from widgets.scale import Scale
from widgets.switch import Switch

# Import Menu last, so it can import the other widgets from here.
from widgets.menu import Menu
