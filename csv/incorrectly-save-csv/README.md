`sample.csv` is incorrectly saved CSV. 

Probably someone created one string with all items in row and used `csv` to save it. 
But `csv` saved it as single column with long string, not as many columns.

Example use `csv` to read it again, and write it back as normal file.
This way it removes `"` at the both sides of long string, 
and it converts double `""` to single `"`

Now it is correct CSV and there is no problem to read it in `pandas.read_csv()`
