#!/usr/bin/env python3

# https://developers.google.com/web/fundamentals/media/capturing-images
# https://github.com/jhuckaby/webcamjs
# https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob

from flask import Flask, render_template_string, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string('''
<video id="video" width="640" height="480" autoplay style="background-color: grey"></video>
<button id="send">Take & Send Photo</button>
<canvas id="canvas" width="640" height="480" style="background-color: grey"></canvas>

<script>

// Elements for taking the snapshot
var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    });
}

// Trigger photo take
document.getElementById("send").addEventListener("click", function() {
    context.drawImage(video, 0, 0, 640, 480);
    canvas.toBlob(upload, "image/jpeg");
});

function upload(file) {
    var formdata =  new FormData();
    formdata.append("snap", file);
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{{ url_for('upload') }}", true);
    xhr.onload = function() {
        if(this.status = 200) {
            console.log(this.response);
        } else {
            console.error(xhr);
        }
        alert(this.response);
    };
    xhr.send(formdata);
}

</script>
''')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        #fs = request.files['snap'] # it raise error when there is no `snap` in form
        fs = request.files.get('snap')
        if fs:
            print('FileStorage:', fs)
            print('filename:', fs.filename)
            fs.save('image.jpg')
            return 'Got Snap!'
        else:
            return 'You forgot Snap!'
    
    return 'Hello World!'
    
    
if __name__ == '__main__':    
    app.run(debug=True, port=5000)

