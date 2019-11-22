#!/usr/bin/env python3 

# date: 2019.11.20
# https://stackoverflow.com/questions/58962814/how-to-print-calendar-for-whole-year-2019

import calendar 

class MyCalendar(calendar.TextCalendar):
    
    def formatmonthname(self, theyear, themonth, width, withyear=True):
        """
        Return a formatted month name.
        """
        s = calendar.month_name[themonth]
        #if withyear:
        s = "%s %r" % (s, theyear)
        return s.center(width)

c = MyCalendar()
print(c.formatyear(2019,1,1,1,3))


