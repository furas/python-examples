
# per-pixel transparency

- image can have pixels with different transparences (alpha)
- it uses colors (R,G,B,A) instead of (R,G,B)
- it needs `surface.convert_alpha()`
- `surface.fill([0,0,0,0])` gives transparent background (important is only alpha=0)
- it **can't** use `set_alpha()` to change transparency

### with `fill([0,0,0,0])`  

important is only alpha=0

![#1](screenshots/per-pixel.png?raw=true)

### without `fill([0,0,0,0])`

![#1](screenshots/per-pixel-without-fill.png?raw=true)

# full-surface transparency

- it uses `set_alpha()` to change transparency
- it uses colors (R,G,B) - (R,G,B,A) makes no difference
- `surface.set_colorkey([0,0,0])` gives transparent background   
(it can be any color but [0,0,0] is default background color for new surface)

###  with `colorkey([0,0,0]) `

![#1](screenshots/full-surface.gif?raw=true)

### without `colorkey([0,0,0]) `

![#1](screenshots/full-surface-without-colorkey.gif?raw=true)
