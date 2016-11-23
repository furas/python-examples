# Tkinter working with COM ports

(or virtual ports (on Linux))

## Install program to create virtual ports

    $ sudo apt install socat

## Use virtual ports

### Create portal in one terminal
    
    $ socat -d -d pty,raw,echo=0 pty,raw,echo=0

    2016/11/13 16:33:30 socat[18425] N PTY is /dev/pts/5
    2016/11/13 16:33:30 socat[18425] N PTY is /dev/pts/6
    2016/11/13 16:33:30 socat[18425] N starting data transfer loop with FDs [3,3] and [5,5]

    It creates ports `/dev/pts/5` and `/dev/pts/6`

    You read from `/dev/pts/6` and write to `/dev/pts/5`

### Read in another terminal

    $ cat < /dev/pts/6

### Write in another terminal

    $ echo "Hello" > /dev/pts/5

---

PySerial: [Short introduction](https://pythonhosted.org/pyserial/shortintro.html)
