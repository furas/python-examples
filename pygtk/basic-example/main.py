# date: 2019.07.18
# spacing, padding

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)

hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
win.add(hbox)

label1 = Gtk.Label(label="Label #1")
label2 = Gtk.Label(label="Label #2")

hbox.pack_start(label1, True, True, padding=10)
hbox.pack_start(label2, True, True, padding=10)

for item in dir(hbox):
    if 'child' in item:
        print(item)

for item in hbox.get_children():
    print(item, item.padding)
    
win.show_all()
Gtk.main()
