#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass


class MainWidgetApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MainWidgetApp().run()
