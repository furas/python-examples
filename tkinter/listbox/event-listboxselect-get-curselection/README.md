 
## listbox populate entry

![#1](images/listbox-populate-entry.png?raw=true)   

After click on list `<<ListboxSelect>>` executes function which gets data from list (as single string) 
splits it to three elements using `slicing` and `strip()`, and puts elements in three `Entries`

Program use 

- `"{:10s}|{:15s}|{:10s}"` to format columns in text, 
- monospaced font `font=('monospace', 10)` to correctly display columns on list.

