`tag_configure` is only to configure `tag` but `tag` has to be assigned to word in text to change its color.


You can use `text.tag_add(tag_name, text_start, text_end)` to add tag to selected text.

Problem can be how to find `text_start`and `text_end` for word or line.

Tkinter has special values like `end`, `insert`, `wordstart`, etc.

I differnt tags to change color for last line and for last word. It shows different situations.

I use `-2c` to skip last `Return` but in other system it can need only `-1c`. Without `-2c` it will use color when you put new chars in new line.

If you put space after last word in line the it doesn't find last word.

If you change order of `tag_configure` then it may not work.


    import tkinter as tk

    # --- functions ---

    def on_return(event):
        # -2c (-2chars) to skip `Return`

        # red color for last line
        text.tag_add('red_fg', 'end-2c linestart', 'end-2c')

        # blue color for last word
        text.tag_add('blue_fg', 'insert-2c wordstart', 'end-2c')


    # --- main ---

    root = tk.Tk()

    text = tk.Text(root)
    text.pack()

    # tag's order can be important
    text.tag_configure("red_fg", foreground="red")
    text.tag_configure("blue_fg", foreground="blue")

    root.bind("<Return>", on_return)

    root.mainloop()

effbot.org: [Text](http://effbot.org/tkinterbook/text.htm)

Tcl/Tk: [Text indices](https://www.tcl.tk/man/tcl8.5/TkCmd/text.htm#M7)

TkDocs: [Text](https://tkdocs.com/tutorial/text.html) -> Text Positions and Indices
