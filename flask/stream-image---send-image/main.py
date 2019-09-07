
# date: 2019.09.03
# 

from flask import Flask, Response, render_template, send_file
import time


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World 3"

def get_image():
    while True:
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n'
              b'\r\n'+ img + b'\r\n')
        time.sleep(0.01) # my Firefox needs some time to display image / Chrome displays image without it


def get_image_with_size():
    length = str(len(img)).encode() # convert to bytes
    while True:
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n'
              b'Content-Length: ' + length + b'\r\n'
              b'\r\n'+ img + b'\r\n')
        time.sleep(0.01) # my Firefox needs some time to display image / Chrome displays image without it


@app.route("/stream")
def stream():
    return Response(get_image_with_size(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/image")
def image():
    return send_file('test.jpg')


if(__name__ == "__main__"):
    img = open('test.jpg', 'rb').read()
    app.run(debug = True)
