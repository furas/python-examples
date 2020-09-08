#!/usr/bin/env python3

# https://developers.google.com/web/fundamentals/media/capturing-images
# https://github.com/jhuckaby/webcamjs
# https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob
# https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL
# https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL

from flask import Flask, render_template_string, request, make_response
import cv2
import numpy as np
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string('''
<video id="video" width="320" height="240" autoplay style="background-color: grey"></video>
<button id="send">Take & Send Photo</button>
<canvas id="canvas" width="320" height="240" style="background-color: grey"></canvas>
<img id="image" src="" width="320" height="240" style="background-color: grey"></img>

<script>

// Elements for taking the snapshot
var video = document.getElementById('video');

// Element to display snapshot

    // you need canvas to get image - canvas can be hiden using `createElement("canvas")`
    // var canvas = document.createElement("canvas");
   
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

var image = document.getElementById('image');
var image64 = document.getElementById('image64');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    
        //console.log('setInterval')
        window.setInterval(function() {
            //context.drawImage(video, 0, 0);
            context.drawImage(video, 0, 0, 320, 240); // better use size because camera may gives data in different size then <video> is displaying
            
            image64.src = canvas.toDataURL();  
            canvas.toBlob(upload, "image/jpeg");
        }, 100);    
    });
}

// Trigger photo take
document.getElementById("send").addEventListener("click", function() {
    //context.drawImage(video, 0, 0);
    context.drawImage(video, 0, 0, 320, 240); // better use size because camera may gives data in different size then <video> is displaying
    image64.src = canvas.toDataURL();  

    canvas.toBlob(upload, "image/jpeg");
});

function upload(file) {

    // create form 
    var formdata =  new FormData();
    
    // add file to form
    formdata.append("snap", file);
    
    // create AJAX connection
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{{ url_for('upload') }}", true);
    xhr.responseType = 'blob';   
    // define function which get response
    xhr.onload = function() {
        
        if(this.status = 200) {
            //console.log(this.response);
        } else {
            console.error(xhr);
        }
        
        //alert(this.response);

        //img.onload = function(){
        //    ctx.drawImage(img, 0, 0)
        //}

        image.src = URL.createObjectURL(this.response); // blob
    };
    
    // send form in AJAX
    xhr.send(formdata);
    
    //image.src = URL.createObjectURL(file);
}

    
</script>
''')

def send_file_data(data, mimetype='image/jpeg', filename='output.jpg'):
    # https://stackoverflow.com/questions/11017466/flask-to-return-image-stored-in-database/11017839
    
    response = make_response(data)
    response.headers.set('Content-Type', mimetype)
    response.headers.set('Content-Disposition', 'attachment', filename=filename)
    
    return response
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        #fs = request.files['snap'] # it raise error when there is no `snap` in form
        fs = request.files.get('snap')
        if fs:
            #print('FileStorage:', fs)
            #print('filename:', fs.filename)
            
            # https://stackoverflow.com/questions/27517688/can-an-uploaded-image-be-loaded-directly-by-cv2
            # https://stackoverflow.com/a/11017839/1832058
            img = cv2.imdecode(np.frombuffer(fs.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            #print('Shape:', img.shape)
            # rectangle(image, start_point, end_point, color, thickness)
            img = cv2.rectangle(img, (20, 20), (300, 220), (0, 0, 255), 2)
            
            text = datetime.datetime.now().strftime('%Y.%m.%d %H.%M.%S.%f')
            img = cv2.putText(img, text, (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA) 
            #cv2.imshow('image', img)
            #cv2.waitKey(1)
            
            # https://jdhao.github.io/2019/07/06/python_opencv_pil_image_to_bytes/
            ret, buf = cv2.imencode('.jpg', img)
            
            #return f'Got Snap! {img.shape}'
            return send_file_data(buf.tobytes())
        else:
            return 'You forgot Snap!'
    
    return 'Hello World!'
    
    
if __name__ == '__main__':    
    app.run(debug=True, port=5000)

