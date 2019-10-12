#!/usr/bin/env python

# date: 2019.09.19
# set real color in background - it need to remove images 
# assigned to `background_normal` and `background_down`

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_string('''
#:kivy 1.7.2

<MyWidget>:
    Button:
        text: 'Button'
        center: self.parent.center

        background_color: (1.0, 0.0, 0.0, 1.0)

        background_normal: ''
        background_down: ''
''')


class MyWidget(Widget):
    pass


class CustomButtonApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    CustomButtonApp().run()


