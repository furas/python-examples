import tkinter as tk

# --- class ---

class FormatLabel(tk.Label):
    
    def __init__(self, master=None, cnf={}, **kw):

        # default values
        self._format = '{}'  
        self._textvariable = None
        
        # get `format` and remove from `kw` so later `Label.__init__` doesn't get it
        if 'format' in kw:
            self._format = kw['format']
            del kw['format']
            
        # get `textvariable` and remove from `kw` so later `Label.__init__` doesn't get it
        # Assign own function to format text in Label when variable change value
        if 'textvariable' in kw:
            self._textvariable = kw['textvariable']
            self._textvariable.trace('w', self._update_text)
            del kw['textvariable']
            
        # run `Label.__init__` without `format` and `textvariable`
        super().__init__(master, cnf={}, **kw)

        # update text after running `Label.__init__`
        if self._textvariable:
            self._update_text(self._textvariable, '', 'w')
        
    def _update_text(self, a, b, c):
        """update text in label when variable change value"""
        #print(f'|{a}|{b}|{c}|')
        self["text"] = self._format.format(self._textvariable.get())
        
# --- main ---

root = tk.Tk()

myvar = tk.DoubleVar(value=0.05)

label = FormatLabel(root, textvariable=myvar, format="Today: {:.0%} and growing")
#label = FormatLabel(root, textvariable=myvar, format="{:.0%}")
label.pack()

myvar.set(0.1)

root.mainloop()
