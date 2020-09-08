#!/usr/bin/env python3

# https://developers.google.com/web/fundamentals/media/capturing-images
# https://github.com/jhuckaby/webcamjs
# https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob
# https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL
# https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL

# https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data
# https://developer.mozilla.org/en-US/docs/Web/API/Body/blob

from flask import Flask, render_template_string, request, make_response
import cv2
import numpy as np
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string('''
<video id="video" width="{{ width }}" height="{{ height }}" autoplay style="background-color: grey"></video>
<button id="send">Take & Send Photo</button>
<canvas id="canvas" width="{{ width }}" height="{{ height }}" style="background-color: grey"></canvas>
<img id="image" src="" width="{{ width }}" height="{{ height }}" style="background-color: grey"></img>

<script>

// Elements for taking the snapshot
var video = document.getElementById('video');

// Element to display snapshot
// you need canvas to get image - canvas can be hiden using `createElement("canvas")`
// var canvas = document.createElement("canvas");
   
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

var image = document.getElementById('image');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    
        //console.log('setInterval')
        window.setInterval(function() {
            context.drawImage(video, 0, 0, {{ width }}, {{ height }}); // better use size because camera may gives data in different size then <video> is displaying
            canvas.toBlob(upload, "image/jpeg");
        }, 200);    
    });
}

// Trigger photo take

document.getElementById("send").addEventListener("click", function() {
    context.drawImage(video, 0, 0, {{ width }}, {{ height }}); // better use size because camera may gives data in different size then <video> is displaying
    canvas.toBlob(upload, "image/jpeg");
});

function upload(file) {

    // create form and add file
    var formdata = new FormData();
    formdata.append("snap", file);

    // create AJAX connection
    fetch("{{ url_for('upload') }}", {
        method: 'POST',
        body: formdata,
        //headers: {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"}  // makes only problem
    }).then(function(response) {
        return response.blob();
    }).then(function(blob) {
        //console.log(blob);  // it slow down video from server
        image.src = URL.createObjectURL(blob);
    }).catch(function(err) {
        console.log('Fetch problem: ' + err.message);
    });

}
    
</script>
''', width=640, height=480) #, width=320, height=240)

def send_file_data(data, mimetype='image/jpeg', filename='output.jpg'):
    # https://stackoverflow.com/questions/11017466/flask-to-return-image-stored-in-database/11017839
    
    response = make_response(data)
    response.headers.set('Content-Type', mimetype)
    response.headers.set('Content-Disposition', 'attachment', filename=filename)
    
    return response
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        #print(request.files)  # it slowdown video
        #print(request.data)   # it slowdown video
        #fs = request.files['snap'] # it raise error when there is no `snap` in form
        fs = request.files.get('snap')
        if fs:
            #print('FileStorage:', fs)
            #print('filename:', fs.filename)
            
            # https://stackoverflow.com/questions/27517688/can-an-uploaded-image-be-loaded-directly-by-cv2
            # https://stackoverflow.com/a/11017839/1832058
            img = cv2.imdecode(np.frombuffer(fs.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            height, width = img.shape[:2]
            #print('Shape:', img.shape)
            # rectangle(image, start_point, end_point, color, thickness)
            img = cv2.rectangle(img, (20, 20), (width-20, height-20), (0, 0, 255), 2)
            
            text = datetime.datetime.now().strftime('%Y.%m.%d %H.%M.%S.%f')
            img = cv2.putText(img, text, (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA) 
            #cv2.imshow('image', img)
            #cv2.waitKey(1)
            
            # https://jdhao.github.io/2019/07/06/python_opencv_pil_image_to_bytes/
            ret, buf = cv2.imencode('.jpg', img)
            
            #return f'Got Snap! {img.shape}'
            return send_file_data(buf.tobytes())
        else:
            #print('You forgot Snap!')
            return 'You forgot Snap!'
    
    return 'Hello World!'
    
    
if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')

    query_vars = {\"category_name\":\"bollywood-review\",\"error\":\"\",\"m\":\"\",\"p\":0,\"post_parent\":\"\",\"subpost\":\"\",\"subpost_id\":\"\",\"attachment\":\"\",\"attachment_id\":0,\"name\":\"\",\"pagename\":\"\",\"page_id\":0,\"second\":\"\",\"minute\":\"\",\"hour\":\"\",\"day\":0,\"monthnum\":0,\"year\":0,\"w\":0,\"tag\":\"\",\"cat\":7286,\"tag_id\":\"\",\"author\":\"\",\"author_name\":\"\",\"feed\":\"\",\"tb\":\"\",\"paged\":0,\"meta_key\":\"\",\"meta_value\":\"\",\"preview\":\"\",\"s\":\"\",\"sentence\":\"\",\"title\":\"\",\"fields\":\"\",\"menu_order\":\"\",\"embed\":\"\",\"category__in\":[],\"category__not_in\":[],\"category__and\":[],\"post__in\":[],\"post__not_in\":[36896,40871,34019,37264,44457,44397],\"post_name__in\":[],\"tag__in\":[],\"tag__not_in\":[],\"tag__and\":[],\"tag_slug__in\":[],\"tag_slug__and\":[],\"post_parent__in\":[],\"post_parent__not_in\":[],\"author__in\":[],\"author__not_in\":[],\"ignore_sticky_posts\":false,\"suppress_filters\":false,\"cache_results\":true,\"update_post_term_cache\":true,\"lazy_load_term_meta\":true,\"update_post_meta_cache\":true,\"post_type\":\"\",\"posts_per_page\":12,\"nopaging\":false,\"comments_per_page\":\"50\",\"no_found_rows\":false,\"order\":\"DESC\"}",
