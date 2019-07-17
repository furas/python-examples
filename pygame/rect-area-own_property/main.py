
# date: 2019.07.08
# https://stackoverflow.com/questions/56927412/is-it-possible-to-create-a-new-assignable-attribute-for-pygame-rect-objects/56927535#56927535

import math
import pygame

class MyRect(pygame.Rect):

    @property    
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, value):
        self.width = self.height = int(math.sqrt(value))

a_rectangle = MyRect(0, 0, 10, 10) 
print( a_rectangle.center )

print( a_rectangle.area )

a_rectangle.area = 144

print( a_rectangle.area )
print( a_rectangle.width, a_rectangle.height )

