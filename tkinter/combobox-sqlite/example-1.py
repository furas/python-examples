#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

class Example:

    def __init__(self,master):
        self.master = master

        self.db = sqlite3.connect('database.db')

        tk.Label(master, text='All:').pack()

        self.cb = ttk.Combobox(master)
        self.cb.pack()

        self.cb['values'] = self.get_data()

        tk.Label(master, text='P:').pack()

        self.cb_p = ttk.Combobox(master)
        self.cb_p.pack()

        self.cb_p['values'] = self.get_data('p')


    def get_data(self, where=None):
        cursor = self.db.cursor()

        # COLLATE NOCASE - sort case insensitive
        if where:
            cursor.execute("SELECT item FROM stocks WHERE item LIKE ? ORDER BY item COLLATE NOCASE ASC", (where+'%',))
        else:
            cursor.execute('SELECT item FROM stocks ORDER BY item COLLATE NOCASE ASC')

        data = []

        for row in cursor.fetchall():
            data.append(row[0])

        cursor.close()

        return data

# --- functions ---

def create_db():
    data = ['Hello', 'World', 'Python', 'tkinter', 'pandas', 'pygame', 'requests']

    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute('CREATE TABLE stocks (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT)')

    for word in data:
        cursor.execute('INSERT INTO stocks (item) VALUES(?)', (word,))

    cursor.close()
    db.commit()

# --- main ---

#create_db()

root = tk.Tk()
Example(root)
root.mainloop()
