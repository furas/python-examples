
# date: 2019.07.13
# https://stackoverflow.com/questions/57014217/putting-an-image-from-flask-to-an-html5-canvas/57015262#57015262
#
# more on Canvas: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Pixel_manipulation_with_canvas
# 

from flask import Flask, send_file

import numpy as np
from PIL import Image
import io


app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
<body>
<canvas></canvas>
<script>
var canvas = document.getElementsByTagName('canvas');
var ctx = canvas[0].getContext('2d');

var img = new Image();
img.src = "/api/b";

// it can't draw it at once. it has to wait till it is loaded
//ctx.drawImage(img, 0, 0);

img.onload = function() {
  img.style.display = 'none'; // I don't know why they hide it
  
  console.log('WxH: ' + img.width + 'x' + img.height)

  // convert Image to ImageData
  //(it has to draw on canvas so it could need second canvas for this)
  
  ctx.drawImage(img, 0, 0);
  var imageData = ctx.getImageData(0, 0, img.width, img.height)

  //put ImageData many times  
  for(x = 0 ; x < 100 ; x += 10) {
    for(y = 0 ; y < 100 ; y += 10) {
       ctx.putImageData(imageData, x, y);
    }
  }
};

</script>
</body>
</html>
'''


@app.route('/api/a')
def image():
    '''send image from disk'''
    return send_file('/home/furas/Obrazy/ball.png',  mimetype='image/png')


@app.route('/api/b')
def array():
    '''
    generate image from numpy.array using PIL.Image
    and send without saving on disk using io.BytesIO'''
    
    arr = np.array([
        [255, 255,   0,   0,   0,   0,   0,   0, 255, 255],
        [255,   0, 255, 255, 255, 255, 255, 255,   0, 255],
        [  0, 255, 255, 255, 255, 255, 255, 255, 255,   0],
        [  0, 255, 255,   0, 255, 255,   0, 255, 255,   0],
        [  0, 255, 255, 255, 255, 255, 255, 255, 255,   0],
        [  0, 255, 255, 255, 255, 255, 255, 255, 255,   0],
        [  0, 255,   0, 255, 255, 255, 255,   0, 255,   0],
        [  0, 255, 255,   0,   0,   0,   0, 255, 255,   0],
        [255,   0, 255, 255, 255, 255, 255, 255,   0, 255],
        [255, 255,   0,   0,   0,   0,   0,   0, 255, 255],
    ])
    
    img = Image.fromarray(arr.astype('uint8')) # convert arr to image
    
    file_object = io.BytesIO()   # create file in memory 
    img.save(file_object, 'PNG') # save as PNG in file in memory
    file_object.seek(0)          # move to beginning of file
                                 # so send_file() will read data from beginning of file

    return send_file(file_object,  mimetype='image/png')


app.run()
