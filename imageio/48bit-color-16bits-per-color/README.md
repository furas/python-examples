
```
# date: 2019.08.10
# https://stackoverflow.com/questions/57440861/resizing-a-48bit-png-retaining-its-48bits-without-dropping-it-to-a-24bit-file
# https://github.com/imageio/imageio/issues/329
# http://freeimage.sourceforge.net/
```

Image: 

![#1](input_48bit.png?raw=true) 

![#1](output_48bit.png?raw=true) 

Example use imageio with library FreeImage to work with 48bit color.

```
$ file input_48bit.png 
input_48bit.png: PNG image data, 1242 x 375, 16-bit/color RGB, non-interlaced
```

```
file output_48bit.png 
output_48bit.png: PNG image data, 5 x 5, 16-bit/color RGB, non-interlaced
```

---

Install `FreeImage` using `imageio`

    $ imageio_download_bin freeimage
    
or using python

    import imageio

    imageio.plugins.freeimage.download()

Information from source code of [freeimage.py](https://github.com/imageio/imageio/blob/master/imageio/plugins/freeimage.py) in `imageio`

---

Download from [FreeImage webpage](http://freeimage.sourceforge.net/download.html)
