# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.07
#
# [python - Stream OpenCV Video Capture to flask server - Stack Overflow](https://stackoverflow.com/questions/72522805/stream-opencv-video-capture-to-flask-server/)
#
# https://blog.miguelgrinberg.com/post/video-streaming-with-flask

from flask import Flask, Response, render_template_string, request
import time

app = Flask(__name__)

app.frame = None   # special global object `g` to share between processes
                     # `g.frame` to keep single JPG,
                     # at start you could assign bytes from some JPG - ie. empty image
#app.frame = open('empty.jpg', 'rb').read()

@app.route('/upload', methods=['PUT'])
def upload():
    # keep jpg data in global variable
    app.frame = request.data

    return "OK"

def gen():
    while True:
        print('send frame:', len(app.frame))
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n'
               b'\r\n' + app.frame + b'\r\n')
        time.sleep(0.04) # my Firefox needs some time to display image / Chrome displays image without it
                         # 0.04s = 40ms = 25 frames per second

@app.route('/video')
def video():
    if app.frame:
        return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return ""

@app.route('/')
def index():
    #return 'image:<br><img src="/video">'
    return render_template_string('image:<br><img src="{{ url_for("video") }}">')

if __name__ == "__main__":
    app.run(debug=True)#, use_reloader=False)
