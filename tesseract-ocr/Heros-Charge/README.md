
Linux (Debian/Ubuntu/Mint) install:

    apt install tesseract-ocr

Python install:

    pip install pillow
    pip install pytesseract

Links:

    tesseract-ocr: https://github.com/tesseract-ocr/tesseract/wiki
    pytesseract: https://github.com/madmaze/pytesseract
    pillow: http://pillow.readthedocs.io


# Example 1

It finds "Power" 

# Example 2

It finds "Name", "Power" and "Loots" on screenshots from game but it can be used with PyAutoGUI `screenshot()`.

![#1](images/example-2.png?raw=true)

    Name: Adrian
    Power: 101919
    Loot #1: 642
    Loot #2: 2686
    Loot #3: 737

# Example 3

Sometimes tesseract has problem with single digit or some text. But you can try to use option `-psm` to resolve problem.

    $ tesseract -psm 6 image.jpg result.txt
    
Example shows how to use this option in Python with images which can't recognize without `-psm`.

    result = pytesseract.image_to_string(img, config='-psm 6')
    
---

You can download any subfolder using [DownGit](https://minhaskamal.github.io/DownGit/)
