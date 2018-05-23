#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


# kivy sends `touch` events to all widgets
# so every widget has to check if touch was made in widget area
# or you have to use `on_press` or `on_release` instead `on_touch_down`
# https://stackoverflow.com/a/45942518/1832058


class Calculate(GridLayout):
    
    def touch_button(self, instance, touch, *args):
        if instance.collide_point(*touch.pos):
            self.ids.entry.text += instance.text
            return False # don't send event to other buttons


class CalcApp(App):
    def build(self):
        return Calculate()


if __name__ == '__main__':
    CalcApp().run()
