# Listbox

### Table of Content

- [event-listboxselect-get-curselection.py](event-listboxselect-get-curselectionpy)
- [listbox-populate-entry.py](listbox-populate-entrypy)

---

## event-listboxselect-get-curselection.py

It shows how to use event `<<ListboxSelect>>` to execute function after selectiong row on list.

It also shows how to use `event` to get access to `Listbox` and get setlected element.

---
 
## listbox-populate-entry.py

![#1](images/listbox-populate-entry.png?raw=true)   


After click on list `<<ListboxSelect>>` executes function which gets data from list (as single string) 
splits it to three elements using `slicing` and `strip()`, and puts elements in three `Entries`

Program use 

- `"{:10s}|{:15s}|{:10s}"` to format columns in text, 
- monospaced font `font=('monospace', 10)` to correctly display columns on list.

---
