#!/usr/bin/env python4.13

# date: 2025.08.06

# [python - Restrict date selection from calendar to specific dates - Stack Overflow](https://stackoverflow.com/questions/79727284/restrict-date-selection-from-calendar-to-specific-dates)

# https://tkcalendar.readthedocs.io/en/stable/DateEntry.html
# https://tkcalendar.readthedocs.io/en/stable/Calendar.html

# https://tkcalendar.readthedocs.io/en/stable/_modules/tkcalendar/dateentry.html#DateEntry

import datetime as dt
import tkinter as tk
#from tkinter import ttk
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
tk.Label(root, text="Calendar").pack()
cal = Calendar(
    root,
    date_pattern="yyyy-mm-dd",
    mindate=dt_dates[0],
    maxdate=dt_dates[-1],
    allowed_dates=dt_dates,
    locale="en_GB.utf-8",  # to show it in English instead of my native Polish
                            # to make screenshot
)
cal.pack()

date_entry_var = tk.StringVar()

# example mycalendar.DateEntry
tk.Label(root, text="DateEntry").pack()
date_entry = DateEntry(
    root,
    textvariable=date_entry_var,
    date_pattern="yyyy-mm-dd",
    mindate=dt_dates[0],
    maxdate=dt_dates[-1],
    allowed_dates=dt_dates,
    locale="en_GB.utf-8",  # to show it in English instead of my native Polish
                            # to make screenshot
)
date_entry.pack()

# --- test buttons ---

#widget = cal
widget = date_entry

# ---

def show_allowed_dates():
    for date in widget['allowed_dates']:  # not `cal.allowed_dates`
        print('allowed:', date)

button_show = tk.Button(root, text="Show Allowed Dates", command=show_allowed_dates)
button_show.pack(fill='x')

# ---

def add_allowed_date(date):
    dt_date = dt.date.fromisoformat(date)

    if dt_date not in widget['allowed_dates']:
        print('add allowed:', date)

        widget['allowed_dates'].append(dt_date)
        # other methods
        #widget['allowed_dates'] += [append(dt.date.fromisoformat(date)]
        #widget['allowed_dates'].extend( [append(dt.date.fromisoformat(date)] )

        widget['allowed_dates'] = sorted(widget['allowed_dates'])

        # what if new date is not in `mindate`, `maxdate` ???
        if widget['allowed_dates'][0] < widget['mindate']:
            widget['mindate'] = widget['allowed_dates'][0]

        if widget['allowed_dates'][-1] > widget['maxdate']:
            widget['maxdate'] = widget['allowed_dates'][-1]

        # redraw it
        if widget == cal:
            widget._display_calendar()


for date in ('2024-06-06', '2024-06-26', '2024-07-10'):
    button_add = tk.Button(root, text=f"Add Allowed Date: {date}", command=lambda x=date:add_allowed_date(x))
    button_add.pack(fill='x')

# ---

def remove_allowed_date(date):
    dt_date = dt.date.fromisoformat(date)

    if dt_date in widget['allowed_dates']:
        print('remove allowed:', date)

        widget['allowed_dates'].remove(dt_date)

        # what if removed date is `mindate` or  `maxdate` ???
        if widget['mindate'] < widget['allowed_dates'][0]:
            widget['mindate'] = widget['allowed_dates'][0]

        if  widget['maxdate'] > widget['allowed_dates'][-1]:
            widget['maxdate'] = widget['allowed_dates'][-1]

        # redraw it
        if widget == cal:
            widget._display_calendar()

for date in ('2024-06-06', '2024-06-26', '2024-07-10'):
    button_remove = tk.Button(root, text=f"Remove Allowed Date: {date}", command=lambda x=date:remove_allowed_date(x))
    button_remove.pack(fill='x')

# ---

root.mainloop()
