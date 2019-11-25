# Copyright 2010-2012 the SGC project developers.
# See the LICENSE file at the top-level directory of this distribution
# and at http://program.sambull.org/sgc/license.html.

"""
Menu widget. Creates a menu for a game.

The menu data format is documented at :doc:`dev.menu`

"""

import json

from pygame import Surface
from pygame.locals import SRCALPHA, BLEND_RGBA_MULT

from _locals import *
from base_widget import Simple
from boxes import VBox
from scroll_box import ScrollBox
from .. import *

class Menu(Simple):

    """
    Menu

    Can be indexed to access widgets by name.

    Attributes:
      func_dict: Assign a lambda to return a dictionary of functions for
          config file to utilise.

    """

    _modal = True
    _layered = True
    _settings_default = {"offset": (100, 50), "col": (0,0,0), "apply": False}

    _menus = []
    _dict = {}  # Dict for indexing widgets
    _old_menu = None
    _curr_menu = 0
    func_dict = lambda self: {}

    def _config(self, **kwargs):
        """
          menu: Either tuple/list containing menu data, or file object to read
              config data from in JSON format.
          apply: TODO ``bool`` True if an apply button should be added.
          col: ``tuple`` (r,g,b), Colour used for the background.
          offset: ``tuple`` (x,y) Contains position of menu widgets. y is
              added to bottom of title.

        """
        for key in ("apply", "col", "offset"):
            if key in kwargs:
                self._settings[key] = kwargs[key]

        if "menu" in kwargs:
            self._menus = []  # Remove previous menus
            self._dict = {}
            # Grab function dictionary
            self._funcs = self.func_dict()

            # Set size to screen size
            if not hasattr(self, "image"):
                self._create_base_images(get_screen().rect.size)
                self._images["image"].fill(self._settings["col"])

            menu = kwargs["menu"]
            # If file, read config tuple
            if isinstance(menu, file):
                menu = json.load(menu)
                # Replace all $tokens
                def check(m):
                    a = m.iteritems() if isinstance(m, dict) else enumerate(m)
                    for i,item in a:
                        if isinstance(item, (str, unicode)) and item[0] == "$":
                            parts = item[1:].split("(")
                            f = self._funcs[parts[0]]
                            if len(parts) > 1:
                                args = parts[1].rstrip(")")
                                m[i] = f(args) if args else f()
                            else:
                                m[i] = f
                        elif isinstance(item, (list, tuple, dict)):
                            check(item)
                check(menu)

            menu_data = [(menu, None)]  # (data, parent)
            # Create each submenu, by iterating through the menu data
            while menu_data:
                self._menus.append(_SubMenu(self._images["image"].copy()))
                self._config_menu(menu_data, self._menus[-1])

    def _config_menu(self, data_queue, menu):
        """
        Configure the passed in menu, using the information from the first
        item in data_queue.

        New sub-menus discovered in the data will be appended to the data_queue
        for later processing.

        """
        data, parent = data_queue.pop(0)
        # Title
        menu._title = Simple(Font["title"].render(data[0][2:], True, Font.col))
        menu._title.rect.midtop = (self.rect.centerx, 40)

        widgets = []
        # Parse menu data
        for item in data[1:]:
            # Sub-menu
            if item[0].startswith("m:"):
                data_queue.append((item, len(self._menus)-1))
                surf = Font["widget"].render(item[0][2:], True, Font.col)
                widgets.append(Button(surf))
                # Change menu on button activate
                num = len(self._menus)-1 + len(data_queue)
                widgets[-1].on_click = lambda n=num: self.change_menu(n)
            # Category/divider
            elif isinstance(item, (str, unicode)):
                Font["widget"].set_underline(True)
                div = Simple(Font["widget"].render(item, True, Font.col))
                Font["widget"].set_underline(False)
                widgets.append(div)
            # Widget
            elif item[0].startswith("w:"):
                args = item[1]
                name = args.pop("name", None)
                try:
                    # Try to load existing widget
                    widget = eval(item[0][2:])
                except NameError:
                    # Try to import custom widget
                    parts = item[0][2:].rpartition(".")
                    mod = __import__(parts[0])
                    widget = getattr(mod, parts[2])
                widget = widget(**args)
                if name: self._dict[name] = widget
                widgets.append(widget)
            # Function
            elif item[0].startswith("f:"):
                surf = Font["widget"].render(item[0][2:], True, Font.col)
                widgets.append(Button(surf=surf))
                if isinstance(item[1], (str, unicode)):
                    widgets[-1].on_click = self._funcs[item[1]]
                else:   
                    widgets[-1].on_click = item[1]

        # Draw a back menu item
        if parent is not None:
            surf = Font["widget"].render("Back", True, Font.col)
            widgets.append(Button(surf=surf))
            widgets[-1].on_click = lambda n=parent: self.change_menu(n)

        menu._widgets = tuple(widgets)

    def _draw_final(self):
        for menu in self._menus:
            # Pack all widgets into a VBox
            box = VBox(widgets=menu._widgets, spacing=15)
            pos = (self._settings["offset"][0],
                   self._settings["offset"][1] + menu._title.rect.bottom)
            box = ScrollBox((self.rect.w - pos[0], self.rect.h - pos[1]),
                            widget=box, pos=pos)
            box._parent = self
            menu.config(menu=box)

    def change_menu(self, menu_num, fade=True):
        """
        Change the currently displayed menu.

        Args:
          menu_num: ``int`` The number representing the menu.
          fade: ``bool`` False if menu should switch immediately without fading.

        """
        self._old_menu = self._curr_menu if fade else None
        self._curr_menu = menu_num
        self._menus[self._curr_menu]._fade = 0

    def update(self, time):
        menu = self._menus[self._curr_menu]
        menu.update(time)
        self._switch()
        if self._old_menu is not None:
            self.image.blit(self._menus[self._old_menu].image, (0,0))
            menu.image.set_alpha(menu._fade)
            menu._fade += time / 3.
            if menu._fade >= 255:
                menu._fade = None
                self._old_menu = None
                menu.image.set_alpha(255)
            else:
                transparent = Surface(self.rect.size, SRCALPHA)
                transparent.fill((255,255,255, menu._fade))
                menu.image.blit(transparent, (0,0),
                                special_flags=BLEND_RGBA_MULT)

        self.image.blit(menu.image, (0,0))

    def _event(self, event):
        self._menus[self._curr_menu]._event(event)

    def __getitem__(self, key):
        """Return widgets by name."""
        return self._dict[key]

    def _focus_exit(self):
        self._menus[self._curr_menu]._focus_exit()

class _SubMenu(Simple):

    """
    A single menu object to be created and managed by the Menu class.

    """
    _settings_default = {"menu": None}

    _title = None
    _widgets = ()

    def _config(self, **kwargs):
        if "menu" in kwargs:
            self._settings["menu"] = kwargs["menu"]

    def _draw_final(self):
        self._switch()
        if self._title:
            self._images["image"].blit(self._title.image, self._title.pos)

    def update(self, time):
        self._switch()
        self._settings["menu"].update(time)
        self.image.blit(self._settings["menu"].image,self._settings["menu"].pos)

    def _event(self, event):
        """Send events to container."""
        self._settings["menu"]._event(event)

    def _focus_exit(self):
        self._settings["menu"]._focus_exit()
