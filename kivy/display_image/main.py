#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.image import Image

class MyPaintApp(App):
    def build(self):
        return Image(source='image.png')

if __name__ == '__main__':
    MyPaintApp().run()
