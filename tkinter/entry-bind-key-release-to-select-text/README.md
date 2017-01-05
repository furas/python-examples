
StackOverflowa: [CTRL + a select all in entry widget tkinter python](http://stackoverflow.com/questions/41477428/ctrl-a-select-all-in-entry-widget-tkinter-python/41478726#41478726)

Selecting text in `Entry` using `Ctrl+A` as in other programs - it highlights text so it can be coped into cliboard.

# example-1.py

Because after releasing keys `<Control-a>` selection is removed
so I use `after()` to execute selection after 50ms.
It selects all text (but it moves cursor to the beginning)
and moves cursor to the end.

# example-2.py

Before I couldn't find correct combination with `Release`
but it has to be `<Control-KeyRelease-a>`
and now it doesn't need `after()`
