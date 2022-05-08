# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.04
# [How to change whole app's theme when used within Class, Tkinter, ttkThemes, ThemedTk Python - Stack Overflow](https://stackoverflow.com/questions/71726458/how-to-change-whole-apps-theme-when-used-within-class-tkinter-ttkthemes-them/)

# [List of ttk Themes](https://wiki.tcl-lang.org/page/List+of+ttk+Themes)
# [TkDocs Tutorial - Styles and Themes](https://tkdocs.com/tutorial/styles.html)

import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.geometry("800x600")
        
        self.style = ThemedStyle()   # with Tk and ThemedStyle
        
        self.my_notebook = ttk.Notebook(self)
        self.my_notebook.pack(pady=15, fill='both', expand=True)
        
        self.frame = ttk.Frame(self.my_notebook)
        self.my_notebook.add(self.frame, text='Buttons')
        for number in range(10):
            b = ttk.Button(self.frame, text=str(number))
            b.pack()
        
        self.my_menu = tk.Menu(self)
        self.config(menu=self.my_menu)
        
        self.first_lane = tk.Menu(self.my_menu)
        self.first_lane.add_command(label='a')
        self.first_lane.add_command(label='b')
        self.my_menu.add_cascade(label='Menu1', menu=self.first_lane)
        
        self.second_lane = tk.Menu(self.my_menu)
        self.my_menu.add_cascade(label='Menu2', menu=self.second_lane)
        
        self.third_lane = tk.Menu(self.my_menu)
        self.my_menu.add_cascade(label='Style', menu=self.third_lane)
        
        #for item in self.get_themes():       # with ThemedTk
        for item in self.style.get_themes(): # with Tk and ThemedStyle
            self.third_lane.add_command(label=item, command=lambda name=item: self.changer_theme(name))
    
    def changer_theme(self, name):
        print('theme:', name)
        #self.set_theme(name)        # with ThemedTk
        self.style.theme_use(name)   # with Tk and ThemedStyle
    
if __name__ == "__main__":
   app = App()
   app.mainloop()
