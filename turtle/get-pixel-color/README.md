`turtle` doesn't have function to get pixel color

but it use `tkinter.Canvas` which keep all as objects
and it has function to get color of selected/clicked object.

```python
def get_pixel_color(x, y):

    # canvas use different coordinates than turtle
    y = -y

    # get access to tkinter.Canvas
    canvas = turtle.getcanvas()
    
    # find IDs of all objects in rectangle (x, y, x, y)
    ids = canvas.find_overlapping(x, y, x, y)

    # if found objects
    if ids: 
        # get ID of last object (top most)
        index = ids[-1]
        
        # get its color
        color = canvas.itemcget(index, "fill")
        
        # if it has color then return it
        if color:
            return color

    # if there was no object then return "white" - background color in turtle
    return "white" # default color 
```

(based on answer to question ["Get pixel colors of tkinter canvas"](https://stackoverflow.com/a/40313937/1832058) on StackOverflow)
