import tkinter as tk
import selenium.webdriver

# --- functions ---

def on_open():
    global driver

    if not driver:
        driver = selenium.webdriver.Firefox()
        url = e.get()
        driver.get(url)
        # ... rest ...

def on_close():
    global driver

    if driver:
        driver.close()
        driver = None

# --- main ---

driver = None

root  = tk.Tk()

e = tk.Entry(root)
e.pack()
e.insert('end', 'https://stackoverflow.com')

b = tk.Button(root, text='Selenium Open', command=on_open)
b.pack()

b = tk.Button(root, text='Selenium Close', command=on_close)
b.pack()

root.mainloop()
