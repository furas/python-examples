import getch

print('Press Ctrl+C to exit\n')

while True:
    key = getch.getch()
    if key == '\x1B':
        print('ESC')
    elif key == '\n':
        print('ENTER')
    elif key == '\x0A':
        print('ENTER')
    else:
        print("key:", key, ord(key), hex(ord(key)))

