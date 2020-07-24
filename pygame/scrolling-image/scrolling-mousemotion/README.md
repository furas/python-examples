
author: https://blog.furas.pl

date: 2020.07.16

link: https://stackoverflow.com/questions/62940130/how-to-implement-a-scroll-view-in-pygame/

---

Code moves images when mouse is moved (without clicking button)

`camera_rect` keeps `offset` used to move/positioning image.

Event `MOUSEMOTION` and `event.rel` is used to change value in `camera_rect`.

It was created for image `800x600` and window `400x300` and it moves full image 
but for different sizes it may need different calculations - 
or it may need to calculate mouse position as percentage 
and use this percentage to calculate image position.
