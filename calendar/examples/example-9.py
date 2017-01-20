#!/usr/bin/env python3

import calendar
#import locale

#locale.setlocale(locale.LC_ALL, 'pl_PL')

#print(calendar.month_name[10].capitalize())
#print(calendar.day_name[1].capitalize())

#print(calendar.calendar(2017))

cal = calendar.LocaleHTMLCalendar(calendar.MONDAY, 'pl_PL')
print(dir(cal))

print(cal.formatmonthname(2017,3))

def print_html(cal):
    print('''<!DOCTYPE html>

<html>

<head>
    <meta charset='UTF-8'/>
    <title>2017</title>
<style>

.year td {
    vertical-align: top;
    border: 1px solid #eee;
}

.month {
    padding: 10px;
}

.sun, .mon, .tue, .wed, .thu, .fri, .sat {
    padding: 5px;
    text-align: right;
}

.sun {
    color: red;
    font-weight: bold;
}
</style>

</head>


<body>
''')

    print(cal.formatyear(2017).encode('utf-8'))

    print('''
</body>
</html>''')
