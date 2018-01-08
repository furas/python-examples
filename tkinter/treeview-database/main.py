import tkinter as tk
from tkinter import ttk
import sqlite3

# --- functions ---

def get_data():
    print('updated')

    cursor = db.cursor()
    cursor.execute('SELECT title, url FROM moz_places')
    db.commit()

    # clear all
    #track.delete(*track.get_children())

    for row in cursor.fetchall():
        track.insert('', 'end', values=row)
    cursor.close()

    #root.after(1000, get_data)
    
# --- main ---

db = sqlite3.connect('/home/furas/.mozilla/firefox/mwad0hks.default/places.sqlite')

root = tk.Tk()
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

track = ttk.Treeview(root)
track["columns"] = ("one", "two")
track.column("one", width=40)
track.column("two", width=70)
track.configure(show='')
#track.configure(height='1')
track.grid(row=0, column=1, sticky="WENS", padx=5)

get_data()

root.mainloop()
