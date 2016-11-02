### Change default code page of Windows console to UTF-8

[Change default code page of Windows console to UTF-8](http://superuser.com/questions/269818/change-default-code-page-of-windows-console-to-utf-8)


- Start -> Run -> regedit
- Go to [HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\Autorun]
- Change the value to chcp 65001

`print(sys.stdout.encoding)`
