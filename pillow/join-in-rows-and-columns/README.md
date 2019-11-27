# Python 

- `PIL`/`pillow` in `main-pillow.py`

- `numpy` + `cv2` in `main-numpy-cv2.py`

- `numpy` + `matplotlib` in `main-numpy-matplotlib.py`

- `numpy` + `imageio` in `main-numpy-imageio.py`

# [ImageMagick](https://imagemagick.org)

It can be done without Python.

    $ convert image1.png image2.png +append row1.png
    $ convert image3.png image4.png +append row2.png
    $ convert row1.png row2.png -append new.png

`+append` joins in row, `-append` joins in column.

In one command

    $ convert image1.png image2.png image3.png image4.png +append -crop 2x1@ -append new.png

If you use `new.pdf` instead of `new.png` then it can create `PDF`

These commands can be also used in Python with `os.system('convert ...')`

Python module [Wand](http://docs.wand-py.org/) is wrapper on `ImageMagick`

