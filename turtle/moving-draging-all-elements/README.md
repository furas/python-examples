`turtle` doesn't have special function to move all elements. 

But `turtle` uses `tkinter` which uses `Canvas` to display elements.   
`Canvas` has function to get all displayed elements and move them.

`turtle` gives access to `Canvas` (`get_canvas()`) but later you have to know `tkinter` to do something with `Canvas` and elements.

This example draw element and then it moves by `(300, 50)`.   
You can also click turtle and drag it to move all elements.
