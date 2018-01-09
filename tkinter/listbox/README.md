# tkinter.Listbox()

### Table of Contents

- [Links](links)
- [event-listboxselect-get-curselection](#event-listboxselect-get-curselection)
- [listbox-filtered-by-entry](#listbox-filtered-by-entry)
- [listbox-populate-entry](#listbox-populate-entry)

---

### Links

- Effbot.org: [The Tkinter Listbox Widget](http://effbot.org/tkinterbook/listbox.htm)
- New Mexico Tech: [Tkinter 8.5 reference: a GUI for Python](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/listbox.html)
- TkDocs.com: [More Widgets](http://www.tkdocs.com/tutorial/morewidgets.html)
- TutorialsPoint.com: [Python - Tkinter Listbox](https://www.tutorialspoint.com/python/tk_listbox.htm)

---

## event-listboxselect-get-curselection

It shows how to use event `<<ListboxSelect>>` to execute function after selecting row on list.

It also shows how to use `event` to get access to `Listbox` and get selected element from listbox.

---

## listbox-filtered-by-entry
 
It uses `Entry` to filter items on `Listbox`

---

## listbox-populate-entry

After click on list `<<ListboxSelect>>` executes function which gets data from list (as single string) 
splits it to three elements using `slicing` and `strip()`, and puts elements in three `Entries`

Program use:

- `"{:10s}|{:15s}|{:10s}"` to format columns in text, 
- monospaced font `font=('monospace', 10)` to correctly display columns on list.

![#1](listbox-populate-entry/images/listbox-multicolumn.png?raw=true)   

---
