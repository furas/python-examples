Structure

    project
    ├── README.md
    ├── cgi-bin
    │   ├── image.png
    │   ├── image.py
    │   ├── test
    │   ├── test.pl
    │   ├── test.py
    │   ├── test.rb
    │   ├── test.sh
    │   ├── test1.php
    │   └── test2.php
    ├── images
    │   ├── normal.png
    │   └── transparent.png
    ├── index.html
    ├── server.py
    └── src
        ├── makefile
        └── test.c

# Simple CGI Server

Normally you can start

    python3 -m http.server --cgi 8000

and it will serve directly all files in current folder and subolfers but it will send source code for scripts. You have to put scripts in `cgi-bin` folder

On Linux you have to set `execution attribut` for every script (ie. `chmod +x script.py`) and you have to use `shebang` in first line of script (ie. `#!/usr/bin/env python3`) because Linux doesn't care of file extensions (ie, `.py`) and it can run script without extension or with incorrect extension (ie. `script.png`)

    +-----------+--------------------+----------------------------+------------------------+
    | LANG      | FILE               | OTHER                      | SHEBANG                |
    ========================================================================================
    | Sh / Bash | /cgi-bin/test.sh   |                            | #!/bin/sh              |
    | C         | /cgi-bin/test      | /src/test.c, /src/makefile |                        |
    +-----------+--------------------+----------------------------+------------------------+
    | Perl      | /cgi-bin/test.pl   |                            | #!/usr/bin/env perl    |
    | PHP #1    | /cgi-bin/test1.php |                            | #!/usr/bin/env php     |
    | PHP #2    | /cgi-bin/test2.php |                            | #!/usr/bin/env php     |
    +-----------+--------------------+----------------------------+------------------------+
    | Python 3  | /cgi-bin/test.py   |                            | #!/usr/bin/env python3 |
    | Ruby      | /cgi-bin/test.rb   |                            | #!/usr/bin/env ruby    |
    +-----------+--------------------+----------------------------+------------------------+
