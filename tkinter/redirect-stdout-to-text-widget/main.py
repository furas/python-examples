import tkinter as tk
import sys

class Redirect():
    def __init__(self, output):
        self.output = output
        
    def write(self, text):
        self.output.insert('end', text + '\n')
        
    def flush(self):
        pass
    
    
root = tk.Tk()
root.title('Output')

text_output = tk.Text(root)
text_output.pack(fill='both', expand=True)

old_stdout = sys.stdout
sys.stdout = Redirect(text_output)

print("Text")

button = tk.Button(root, text='OK', command=root.destroy)
button.pack()

root.mainloop()

sys.stdout = old_stdout
print('koniec')
