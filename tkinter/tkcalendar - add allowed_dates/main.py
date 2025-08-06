]
# fmt: on

root = tk.Tk()

dt_dates = [ dt.date.fromisoformat(date) for date in dates ]

cal = mycalendar.Calendar(
    root,
    date_pattern="yyyy-mm-dd",
    mindate=dt.date.fromisoformat(dates[0]),
    maxdate=dt.date.fromisoformat(dates[-1]),
    allowed_dates=dt_dates,
    locale="en_GB.utf-8",  # to show it in English instead of my native Polish
)
cal.pack()

#date_entry_var = tk.StringVar()
#date_entry = DateEntry(
#    root,
#    textvariable=date_entry_var,
#    date_pattern="yyyy-mm-dd",
#    mindate=dt.date.fromisoformat(dates[0]),
#    maxdate=dt.date.fromisoformat(dates[-1]),
#)
#date_entry.pack()

root.mainloop()
