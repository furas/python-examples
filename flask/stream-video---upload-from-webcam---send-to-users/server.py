# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.07
#
# [python - Stream OpenCV Video Capture to flask server - Stack Overflow](https://stackoverflow.com/questions/72522805/stream-opencv-video-capture-to-flask-server/72524761#72524761)
#
# https://blog.miguelgrinberg.com/post/video-streaming-with-flask

from flask import Flask, Response, render_template_string, request
import time

app = Flask(__name__)

frame = None   # global variable to keep single JPG,
               # at start you could assign bytes from some JPG - ie. empty image
#frame = open('empty.jpg', 'rb').read()

@app.route('/upload', methods=['PUT'])
def upload():
    global frame

    # keep jpg data in global variable
    frame = request.data

    return "OK"

def gen():
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n'
               b'\r\n' + frame + b'\r\n')
        time.sleep(0.04) # my Firefox needs some time to display image / Chrome displays image without it
                         # 0.04s = 40ms = 25 frames per second (this can be enough)

def gen_with_size():
    while True:
        length = len(frame)   # `upload` may replace image with different size before it will send
                              # so it may need to copy image or lock image before `len()` and send
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n'
               b'Content-Length: ' + length + b'\r\n'
               b'\r\n' + frame + b'\r\n')
        time.sleep(0.04) # my Firefox needs some time to display image / Chrome displays image without it
                         # 0.04s = 40ms = 25 frames per second (this can be enough)

@app.route('/video')
def video():
    if frame:
        # if you use `boundary=other_name` then you have to yield `b--other_name\r\n`
        return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return ""

@app.route('/')
def index():
    #return 'image:<br><img src="/video">'
    return render_template_string('image:<br><img src="{{ url_for("video") }}">')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
