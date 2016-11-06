#!/usr/bin/env python3
print("Content-Type: text/html; charset=utf-8")
print()

# "Content-Type" has to be in first line - without even empty lines
# after headers have to be empty line (another print() or "\n")

result = 1 + 2

print('''<!DOCTYPE html>

<html>

<head>
    <meta charset="utf-8"/>
    <title>Python 3</title>
    <style>
        body {{background-color:#ddd; text-align: center}}
    </style>
</head>

<body>

    <h1>PYTHON 3</h1>

    <h2>1 + 2 = {}</h2>
    
    <a href="/images/transparent.png"><img src="/images/transparent.png"><br/>/images/transparent.png</a><br/>
    <br/>
    
    <a href="/cgi-bin/image.png"><img src="/cgi-bin/image.png"><br/>/cgi-bin/image.png</a><br/>
    (python script with extension .png)<br/>
      
</body>

</html>'''.format(result))

# style needs `{{ }}` instead of `{ }` because `format()` uses `{ }`
