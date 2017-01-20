#!/usr/bin/env python3

import calendar

cal = calendar.LocaleTextCalendar(calendar.MONDAY, 'pl_PL')

print(cal.formatmonth(2017, 1))

print(cal.formatyear(2017))

