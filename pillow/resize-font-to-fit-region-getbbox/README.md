
Author: Bartlomiej "furas" Burek [https://blog.furas.pl](https://blog.furas.pl)

Date: 2021.05.30

Stackoverflow: [How to add text in a “textbox” to an image?](https://stackoverflow.com/questions/67760340/how-to-add-text-in-a-textbox-to-an-image/67762111#67762111)

- [ImageFont](https://pillow.readthedocs.io/en/stable/reference/ImageFont.html)

- [ImageFont.FreeTypeFont.getbbox()](https://pillow.readthedocs.io/en/stable/reference/ImageFont.html#PIL.ImageFont.FreeTypeFont.getbbox) (needs PIL 8.0.0)

- [ImageFont.ImageFont.getsize()](https://pillow.readthedocs.io/en/stable/reference/ImageFont.html#PIL.ImageFont.ImageFont.getsize) (older versions - but can get `h` little bigger then real size)

- [Text Anchor](https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html)

---

Result with `(200-w//2, 150-h//2)` and `getbbox()`

![#1](https://raw.githubusercontent.com/furas/python-examples/master/pillow/resize-font-to-fit-region-getbbox/center-older-getbbox.png)

Result with `(200-w//2, 150-h//2)` and `getsize()`

![#2](https://raw.githubusercontent.com/furas/python-examples/master/pillow/resize-font-to-fit-region-getbbox/center-older-getsize.png)

Result with `anchor='mm'` (with `getbbox()` or `getsize()`)

![#3](https://raw.githubusercontent.com/furas/python-examples/master/pillow/resize-font-to-fit-region-getbbox/center-newer.png)
