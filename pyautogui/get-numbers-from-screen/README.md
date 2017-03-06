It finds digits on screenshot (or screen) using images of digits (Monospace Regular 12). 

![#1](digits/digits.png?raw=true)   

And then it groups digits by "y" coordinate and later group by "x" coordinate to (re)create numbers.

Example screenshot for test:

![#2](screenshot-example.png?raw=true)   

---

Doc: [PyAutoGUI - Screenshot Functions](https://pyautogui.readthedocs.io/en/latest/screenshot.html)

---

Tested on Linux Mint.

It needs to install:

    apt-get install scrot # to grab screenshot
    pip install pyautogui
