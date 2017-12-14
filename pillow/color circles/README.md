![#1](images/normal_rgb.png?raw=true)   

## Using [Image.merge()](http://pillow.readthedocs.io/en/4.3.x/reference/Image.html#PIL.Image.merge)

Using grayscale layers to create `RGB` image with color circles.
 
![#1](images/normal_result.png?raw=true)   

Using inverted layers.

![#1](images/inverted_result.png?raw=true)   

## Using [ImageChop.add()](en/3.4.x/reference/ImageChops.html#PIL.ImageChops.add)

![#1](images/normal_result_add.png?raw=true)   

![#1](images/inverted_result_add.png?raw=true)   

---

### Creating preview using [ImageMagick](https://www.imagemagick.org/script/index.php#)

    $ montage -tile 4x1 normal_layer_r.png normal_layer_g.png normal_layer_b.png normal_rgb.png normal_result.png

    $ montage -background black -tile 4x1 inverted_layer_r.png inverted_layer_g.png inverted_layer_b.png inverted_rgb.png inverted_result.png



    $ montage -tile 4x1 inverted_layer_r.png inverted_layer_g.png inverted_layer_b.png inverted_add.png inverted_result_add.png
    
    $ montage -background black -tile 4x1 normal_layer_r.png normal_layer_g.png normal_layer_b.png normal_add.png normal_result_add.png
    

