#!/usr/bin/env python3

import calendar

def print_full_html(cal):
    print('''<!DOCTYPE html>

<html>

<head>
    <meta charset='UTF-8'/>
    <title>2017</title>
    <style>
    .year td {
        vertical-align: top;
    }
    .month td {
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

<body>''')

    print(cal.encode('utf-8'))

    print('''</body>

</html>''')


cal = calendar.LocaleHTMLCalendar(calendar.MONDAY, 'pl_PL')

# only table
#print(cal.formatmonth(2017, 1))
#print(cal.formatyear(2017))

# full HTML
#print_full_html(cal.formatmonth(2017, 1))
print_full_html(cal.formatyear(2017))

