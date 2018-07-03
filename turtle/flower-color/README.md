
# Turtle flower(s)

Because code use `traces(0, 0)` so it may need `update()` to display some last elements. And `update()` may needs `mainloop()` to work.

Besides, without `mainloop()` it may not keep open window when you run it outside IDLE (which runs own `mainloop()` adn it keeps open window). And without `mainloop()` you can't close window using `X`.

## main.py

Base version without colors

![#1](images/image-0.png?raw=true)   

## main-colors.py

It uses list with colors to draw every level in different color.

Images for different modifications

 `lenght/4`

![#1](images/image-1.png?raw=true)   

 `lenght/3`

![#1](images/image-2.png?raw=true)   

`lenght/2`

![#1](images/image-3.png?raw=true)   

`range(5)` and `right(360/5)`

![#1](images/image-4.png?raw=true)   

## main-colors-asimetric.py

I use some modifications to draw asymmetrically.
