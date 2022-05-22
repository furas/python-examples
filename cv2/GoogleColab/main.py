# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.05.10
# [python - OpenCV (-215:Assertion failed) !_src.empty() in function 'cvtColor - Stack Overflow](https://stackoverflow.com/questions/60551469/opencv-215assertion-failed-src-empty-in-function-cvtcolor/60551714)

# Google Colab: https://colab.research.google.com/drive/1a2seyb864Aqpu13nBjGRJK0AIU7JOdJa?usp=sharing

#
# based on: https://colab.research.google.com/notebooks/snippets/advanced_outputs.ipynb#scrollTo=2viqYx97hPMi
#

from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode, b64encode
import numpy as np

def init_camera():
  """Create objects and functions in HTML/JavaScript to access local web camera"""

  js = Javascript('''

    // global variables to use in both functions
    var div = null;
    var video = null;   // <video> to display stream from local webcam
    var stream = null;  // stream from local webcam
    var canvas = null;  // <canvas> for single frame from <video> and convert frame to JPG
    var img = null;     // <img> to display JPG after processing with `cv2`

    async function initCamera() {
      // place for video (and eventually buttons)
      div = document.createElement('div');
      document.body.appendChild(div);

      // <video> to display video
      video = document.createElement('video');
      video.style.display = 'block';
      div.appendChild(video);

      // get webcam stream and assing to <video>
      stream = await navigator.mediaDevices.getUserMedia({video: true});
      video.srcObject = stream;

      // start playing stream from webcam in <video>
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // <canvas> for frame from <video>
      canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      //div.appendChild(input_canvas); // there is no need to display to get image (but you can display it for test)

      // <img> for image after processing with `cv2`
      img = document.createElement('img');
      img.width = video.videoWidth;
      img.height = video.videoHeight;
      div.appendChild(img);
    }

    async function takeImage(quality) {
      // draw frame from <video> on <canvas>
      canvas.getContext('2d').drawImage(video, 0, 0);

      // stop webcam stream
      //stream.getVideoTracks()[0].stop();

      // get data from <canvas> as JPG image decoded base64 and with header "data:image/jpg;base64,"
      return canvas.toDataURL('image/jpeg', quality);
      //return canvas.toDataURL('image/png', quality);
    }

    async function showImage(image) {
      // it needs string "data:image/jpg;base64,JPG-DATA-ENCODED-BASE64"
      // it will replace previous image in `<img src="">`
      img.src = image;
      // TODO: create <img> if doesn't exists,
      // TODO: use `id` to use different `<img>` for different image - like `name` in `cv2.imshow(name, image)`
    }

  ''')

  display(js)
  eval_js('initCamera()')

def take_frame(quality=0.8):
  """Get frame from web camera"""

  data = eval_js('takeImage({})'.format(quality))  # run JavaScript code to get image (JPG as string base64) from <canvas>

  header, data = data.split(',')  # split header ("data:image/jpg;base64,") and base64 data (JPG)
  data = b64decode(data)  # decode base64
  data = np.frombuffer(data, dtype=np.uint8)  # create numpy array with JPG data

  img = cv2.imdecode(data, cv2.IMREAD_UNCHANGED)  # uncompress JPG data to array of pixels

  return img

def show_frame(img, quality=0.8):
  """Put frame as <img src="data:image/jpg;base64,...."> """

  ret, data = cv2.imencode('.jpg', img)  # compress array of pixels to JPG data

  data = b64encode(data)  # encode base64
  data = data.decode()  # convert bytes to string
  data = 'data:image/jpg;base64,' + data  # join header ("data:image/jpg;base64,") and base64 data (JPG)

  eval_js('showImage("{}")'.format(data))  # run JavaScript code to put image (JPG as string base64) in <img>
                                           # argument in `showImage` needs `" "`

print("[INFO] defined: init_camera(), take_frame(), show_frame()")

#----------------------------------------------------------------------------------------------------------------------

# class similar to `cv2.VideoCapture(src=0)`
# but it uses JavaScript function to get frame from web browser canvas

import cv2

class BrowserVideoCapture():

    width  = 640
    height = 480
    fps    = 30
    frames_count = 100
    pos_frames = 0

    def __init__(self, src=None):
        # init JavaScript code
        init_camera()
        #self.pos_frames = 0

    def read(self):
        # value for `cv2.CAP_PROP_POS_FRAMES`
        self.pos_frames += 1

        # return the frame most recently read from JS function
        return True, take_frame()

    def get(self, key):
        # get WIDTH, HEIGHT, FPS, etc.

        if key == cv2.CAP_PROP_POS_FRAMES:  # 1
            return self.pos_frames
        elif key == cv2.CAP_PROP_FRAME_WIDTH:  # 3
            return self.width
        elif key == cv2.CAP_PROP_FRAME_HEIGHT:  # 4
            return self.height
        elif key == cv2.CAP_PROP_FPS:  # 5
            return self.fps
        elif key == cv2.CAP_PROP_FRAME_COUNT:  # 7
            return self.frames_count  # ??
        else:
            print('[BrowserVideoCapture] get(key): unknown key:', key)
            print('See: https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html')

        return 0

    #def set(self, key, val):
    #    # set WIDTH, HEIGHT, FPS, etc.
    #    if key == cv2.CAP_PROP_FRAME_WIDTH:
    #        self.width = val
    #    elif key == cv2.CAP_PROP_FRAME_HEIGHT:
    #        self.height = val
    #    elif key == cv2.CAP_PROP_FPS:
    #        self.fps = val
    #    else:
    #        print('[BrowserVideoCapture] set(key, val): unknown key:', key)
    #        print('See: https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html')


print("[INFO] defined: BrowserVideoCapture()")

#----------------------------------------------------------------------------------------------------------------------

#
# example how to use `BrowserVideoCapture` in `BrowserWebcamVideoStream` 
# but I didn't test it because `scenedetect` doesn't need `BrowserWebcamVideoStream`.
# `scenedetect` needs `cv2.VideoCapture` or `BrowserVideoCapture`
# which have `read()` and also `get(key)`.
# maybe if you would add `.get(key)` like in `BrowserVideoCapture()` 
# then you could use `BrowserWebcamVideoStream()` instead of `cv2.VideoCapture`
#

from threading import Thread
import cv2

# class similar to WebcamVideoStream

class BrowserWebcamVideoStream():
    
  def __init__(self, src=0):
    # initialize the video camera stream and read the first frame
    # from the stream

    #self.stream = BrowserVideoCapture(0)  # argument is not used    
    self.stream = BrowserVideoCapture()
    
    (self.grabbed, self.frame) = self.stream.read()
    # initialize the variable used to indicate if the thread should
    # be stopped
    self.stopped = False
    
  def start(self):
    # start the thread to read frames from the video stream
    Thread(target=self.update).start()
    return self

  def update(self):
    # keep looping infinitely until the thread is stopped
    while True:
      # if the thread indicator variable is set, stop the thread
      if self.stopped:
        return
      # otherwise, read the next frame from the stream
      (self.grabbed, self.frame) = self.stream.read()
      
  def read(self):
    # I don't use directly `take_frame()` 
    # but I use `read()` from `BrowserVideoCapture()` 
    # which runs `take_frame()`.
    return self.stream.read()  

  def stop(self):
    # indicate that the thread should be stopped
    self.stopped = True

print("[INFO] defined: BrowserWebcamVideoStream()")

#----------------------------------------------------------------------------------------------------------------------

import cv2

# - code -

#vs = BrowserWebcamVideoStream(src=0)  #  instead of `WebcamVideoStream`
#vs.start()

#cap = cv2.VideoCapture('Our Story.mp4', 0)   # video on server
cap = BrowserVideoCapture(src=0)

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.putText(frame, "Hello World!", (0,0), cv2.FONT_HERSHEY_PLAIN, 50, (255,255,255))
        show_frame(frame)


