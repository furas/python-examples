Structure

    project
    ├── README.md
    ├── cgi-bin
    │   ├── image.py
    │   ├── test.php
    │   ├── test.pl
    │   ├── test.py
    │   ├── test.rb
    │   ├── test.sh
    │   └── test2.php
    ├── images
    │   ├── normal.png
    │   └── transparent.png
    ├── index.html
    └── server.py

# Simple CGI Server

Normally you can start

    python3 -m http.server --cgi 8000

and it will serve directly all files in current folder and subolfers but it will send source code for scripts. You have to put scripts in `cgi-bin` folder

On Linux you have to set `execution attribut` for every script (ie. `chmod +x script.py`) and you have to use `shebang` in first line of script (ie. `#!/usr/bin/env python3`) because Linux doesn't care of file extensions (ie, `.py`) and it can run script without extension or with incorrect extension (ie. `script.png`)
    
