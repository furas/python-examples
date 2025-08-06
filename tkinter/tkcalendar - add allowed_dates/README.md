![](screenshot.png)

Add option `allowed_dates` to `Calendar` to disable other dates.

It needs list of objects `datetime`.

There is also `mycalendar.DateEntry` which uses this `mycalendar.Calendar`.

```python
import datetime as dt
import tkinter as tk
from tkinter import ttk
#from tkcalendar import DateEntry

from mycalendar import Calendar
from mycalendar import DateEntry

# fmt: off
dates = [
    "2024-04-08", "2024-04-10", "2024-04-11", "2024-04-12",
    "2024-04-15", "2024-04-16", "2024-04-17", "2024-04-18", "2024-04-19",
    "2024-04-22",
    "2024-05-21", "2024-05-22", "2024-05-23", "2024-05-24",
    "2024-05-27", "2024-05-28", "2024-05-29", "2024-05-30", "2024-05-31",
    "2024-06-03", "2024-06-04", "2024-06-05", "2024-06-07",
    "2024-06-10", "2024-06-11", "2024-06-12", "2024-06-13", "2024-06-14",
]
# fmt: on

root = tk.Tk()

dt_dates = [ dt.date.fromisoformat(date) for date in dates ]

# example mycalendar.Calendar
cal = Calendar(
    root,
    date_pattern="yyyy-mm-dd",
    mindate=dt_dates[0],
    maxdate=dt_dates[-1],
    allowed_dates=dt_dates,
    #locale="en_GB.utf-8",  # to show it in English instead of my native Polish
                            # to make screenshot
)
cal.pack()

date_entry_var = tk.StringVar()

# example mycalendar.DateEntry
date_entry = DateEntry(
    root,
    textvariable=date_entry_var,
    date_pattern="yyyy-mm-dd",
    mindate=dt_dates[0],
    maxdate=dt_dates[-1],
    allowed_dates=dt_dates,   # <-- DateEntry sends it to Calendar
)
date_entry.pack()

root.mainloop()
```
