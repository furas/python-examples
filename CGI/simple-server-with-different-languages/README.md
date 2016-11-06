# Simple CGI Server - with CGI scripts in different languages.


Structure:

    project
    ├── README.md
    ├── cgi-bin
    │   ├── image.png
    │   ├── image.py
    │   └── tests
    │       ├── test
    │       ├── test.pl
    │       ├── test.py
    │       ├── test.rb
    │       ├── test.sh
    │       ├── test1.php
    │       └── test2.php
    ├── images
    │   ├── normal.png
    │   └── transparent.png
    ├── index.html
    ├── server.py
    └── src
        ├── makefile
        └── test.c


Normally you can start simple HTML server using

    python3 -m http.server 8000

and connect on address `http://localhost:8000`.

It will serve all files in current folder and subolfers but it will not execute scripts - it will send source code for scripts.

To start CGI Server you can add `--cgi`

    python3 -m http.server --cgi 8000

Now it will execute scripts in `cgi-bin` folder.

On Linux you have to

- set `execution attribute` for this scripts (ie. `chmod +x script.py`)
- use `shebang` in first line of script (ie. `#!/usr/bin/env python3`)

because Linux doesn't care of file extension (ie, `.py`) and it uses path in `shebang` to run this script. It can even run script without extension (ie. `script`) or with incorrect extension (ie. `script.png`).

In example is Python script with extension `.png` - see `/cgi-bin/image.png`

CGI server can run scripts in different languages

    +-----------+--------------------------+----------------------------+------------------------+
    | LANG      | FILE                     | OTHER                      | SHEBANG                |
    ==============================================================================================
    | Bash / Sh | /cgi-bin/tests/test.sh   |                            | #!/bin/sh              |
    +-----------+--------------------------+----------------------------+------------------------+
    | C         | /cgi-bin/tests/test      | /src/test.c, /src/makefile |                        |
    +-----------+--------------------------+----------------------------+------------------------+
    | Perl      | /cgi-bin/tests/test.pl   |                            | #!/usr/bin/env perl    |
    +-----------+--------------------------+----------------------------+------------------------+
    | PHP #1    | /cgi-bin/tests/test1.php |                            | #!/usr/bin/env php     |
    | PHP #2    | /cgi-bin/tests/test2.php |                            | #!/usr/bin/env php     |
    +-----------+--------------------------+----------------------------+------------------------+
    | Python 3  | /cgi-bin/tests/test.py   |                            | #!/usr/bin/env python3 |
    +-----------+--------------------------+----------------------------+------------------------+
    | Ruby      | /cgi-bin/tests/test.rb   |                            | #!/usr/bin/env ruby    |
    +-----------+--------------------------+----------------------------+------------------------+
