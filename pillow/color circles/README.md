## main.py

Using grayscale layers to create `RGB` image with color circles.
 
![#1](images/normal_rgb.png?raw=true)   

Using inverted layers.

![#1](images/inverted_rgb.png?raw=true)   

---

### Merging images using ImageMagick

    $ montage -tile 4x1 normal_layer_r.png normal_layer_g.png normal_layer_b.png normal_rgb.png normal_result.png

    $ montage -background black -tile 4x1 inverted_layer_r.png inverted_layer_g.png inverted_layer_b.png inverted_rgb.png inverted_result.png

![#1](images/normal_result.png?raw=true)   

![#1](images/inverted_result.png?raw=true)   

