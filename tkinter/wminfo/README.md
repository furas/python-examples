
### position-on-screen-and-in-parent.py
Code shows `canvas` position on screen and in parent `Frame` (not in `root`).

![#1](images/screenshot.png?raw=true)   


Example result

```
--- before mainloop start ---

  root.geometry: 1x1+0+0
canvas.geometry: 1x1+0+0
canvas.width : 1
canvas.height: 1
canvas.x: 0
canvas.y: 0
canvas.rootx: 0
canvas.rooty: 0

--- after mainloop start ---

  root.geometry: 380x303+770+462
canvas.geometry: 380x267+0+18
canvas.width : 380
canvas.height: 267
canvas.x: 0
canvas.y: 18
canvas.rootx: 770
canvas.rooty: 498
```


`Canvas` position on screen is `(770, 498)`, in `Frame` is `(0, 18)` but in `root` is `(0, 32)`   
(root position on screen is `(770, 462)` so `(770, 498)` minus `(770, 462)` gives `(0, 32)`)
