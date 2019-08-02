
# date: 2019.08.01
# https://stackoverflow.com/questions/57311774/wbserver-roundslider-widget-doesnt-start-update-audio-tone-program

from gnuradio import analog
from gnuradio import audio

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class TopBlock22(gr.top_block):

    def __init__(self, sample_rate):

        gr.top_block.__init__(self, "Top Block 22")        
        ##################################################
        # Variables
        ##################################################
        self.sample_rate = sample_rate
        print('[TopBlock22] sample_rate:', self.sample_rate)
        
        ##################################################
        # Blocks
        ##################################################
        self.blocks_add_xx = blocks.add_vff(1)
        self.audio_sink = audio.sink(32000, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(sample_rate, analog.GR_COS_WAVE, 440, 0.4, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(sample_rate, analog.GR_COS_WAVE, 350, 0.4, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 0.005, -42)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx, 2))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx, 1))
        self.connect((self.blocks_add_xx, 0), (self.audio_sink, 0))

# -----------------------------------------------------------------------------

from threading import Thread
import time

class MyThread(Thread):

    def __init__(self, sample_rate):
        Thread.__init__(self)

        self.sample_rate = sample_rate

        self.running = True
        
    def run(self):

        tb = TopBlock22(self.sample_rate)
        tb.start()

        while self.running:
            time.sleep(0.5)  # need it to head sound

        tb.stop()
        tb.wait()
    
# -----------------------------------------------------------------------------

from flask import Flask, request


app = Flask(__name__)

my_thread = None


@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>GNURadio Slider Example</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/roundSlider/1.3.2/roundslider.min.css" rel="stylesheet" />
  <script src="https://cdnjs.cloudflare.com/ajax/libs/roundSlider/1.3.2/roundslider.min.js"></script>
</head>
<body>

<div id="slider"></div>

<script>
  var val;

  $("#slider").roundSlider({
    radius: 215,
    min: 0,
    max: 100000,
    value: 10,
    change: function () {
      var obj = $("#slider").data("roundSlider");
      val = obj.getValue();
      $.getJSON('/valueofslider', {
        slide_val: val
      });
    }
  });
</script>

</body>
</html>'''

@app.route('/test')
def test():
    HTML = 'HEAR:'

    for item in (0, 20000, 25000, 32000):
        HTML += ' <a href="/valueofslider?slide_val={}">{}</a>'.format(item, item)

    return HTML

@app.route('/off')
def off():
    '''Use `slide_val=0` to turn it off.'''
    
    sound(0)
    
    return 'off'

@app.route('/valueofslider')
def slide():
    sample_rate = request.args.get('slide_val', 32000)
    sound(sample_rate)
    
    return sample_rate

def sound(sample_rate):
    global my_thread
    
    print('[sound] sample_rate:', sample_rate)
    sample_rate = int(sample_rate)

    if my_thread:
        my_thread.running = False
        my_thread.join()
    
    if samp_rate > 0:
        my_thread = MyThread(samp_rate)
        my_thread.start()

    
if __name__ == '__main__':    
    app.run(debug=True)
