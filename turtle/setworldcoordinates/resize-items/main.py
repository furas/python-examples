
# date: 2019.07.31
# https://stackoverflow.com/questions/57298067/is-there-a-native-function-in-turtle-that-resizes-an-image-to-fit-the-window 

from turtle import *
import time

screen = getscreen()
screen.setworldcoordinates(-50,-20, 50, 20)

for _ in range(8):
    left(45)
    fd(4)
   
x = 2.5 # 50/20
y = 1
for i in range(20):
    time.sleep(0.1)
    screen.setworldcoordinates(-50 - x*i, -20 - y*i, 50 + x*i, 20 + y*i)

exitonclick()

