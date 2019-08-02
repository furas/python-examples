
# date: 2019.08.01
# https://stackoverflow.com/questions/57311774/wbserver-roundslider-widget-doesnt-start-update-audio-tone-program

from __future__ import print_function

from gnuradio import analog
from gnuradio import audio

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class TopBlock22(gr.top_block): # PEP8: CamelCaseName for classes

    def __init__(self, sample_rate=32000):

        gr.top_block.__init__(self, "Top Block 22")        
        ##################################################
        # Variables
        ##################################################
        self.sample_rate = sample_rate
        print('[TopBlock22] __init__: sample_rate:', self.sample_rate)
        
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
    
    def change_1(self, sample_rate):
        """First version"""
        
        self.sample_rate = sample_rate
        print('[TopBlock22] change 1: sample_rate:', self.sample_rate)

        # it doesn't change sound if it is not locked/unlocked
        
        # lock
        self.lock()
        
        # disconect - needs two endpoints (not like in FAQ)
        self.disconnect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx, 0))
        self.disconnect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx, 1))

        # create new
        self.analog_sig_source_x_1 = analog.sig_source_f(sample_rate, analog.GR_COS_WAVE, 440, 0.4, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(sample_rate, analog.GR_COS_WAVE, 350, 0.4, 0)

        # connect again
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx, 1))

        # unlock
        self.unlock()

    def change_2(self, sample_rate):
        """Second version - it creates new `sig_source_f` before locking.
        
        Maybe to will work faster and there will be not click when it changes sample rate.
        
        After using it I don't head big difference. Maybe sometimes it works better but not so much.
        """
        
        self.sample_rate = sample_rate
        print('[TopBlock22] change 2: sample_rate:', self.sample_rate)

        # create new
        new_1 = analog.sig_source_f(sample_rate, analog.GR_COS_WAVE, 440, 0.4, 0)
        new_0 = analog.sig_source_f(sample_rate, analog.GR_COS_WAVE, 350, 0.4, 0)

        # lock
        self.lock()
        
        # disconect - needs two endpoints (not like in FAQ)
        self.disconnect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx, 0))
        self.disconnect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx, 1))

        # connect again
        self.connect((new_0, 0), (self.blocks_add_xx, 0))
        self.connect((new_1, 0), (self.blocks_add_xx, 1))

        # unlock
        self.unlock()

        self.analog_sig_source_x_1 = new_1
        self.analog_sig_source_x_0 = new_0
        

    def change(self, sample_rate):
        """Third version - it doesn't create new `sig_source_f`.

        I think I don't hear clicks but I fill there is delay before it changes sound after mouse click.
        
        Sources:
        https://wiki.gnuradio.org/index.php/TutorialsWritePythonApplications#Choosing.2C_defining_and_configuring_blocks
        https://www.gnuradio.org/doc/doxygen/classgr_1_1analog_1_1sig__source__f.html
        """
        
        self.sample_rate = sample_rate
        print('[TopBlock22] change: sample_rate:', self.sample_rate)

        self.analog_sig_source_x_1.set_sampling_freq(sample_rate)
        self.analog_sig_source_x_0.set_sampling_freq(sample_rate)

# -----------------------------------------------------------------------------

"""        
To see all methods in object: 

print('\n'.join(dir(self.analog_sig_source_x_1)))

set_amplitude
set_block_alias
set_frequency
set_max_noutput_items
set_max_output_buffer
set_min_noutput_items
set_min_output_buffer
set_offset
set_processor_affinity
set_sampling_freq
set_thread_priority
set_waveform
"""

# -----------------------------------------------------------------------------

from flask import Flask, request, jsonify


app = Flask(__name__)

tb = None  # global variable to keep it between requests


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

  // keep slider's value
  var val;
  
  // create slider
  $("#slider").roundSlider({
    radius: 215,
    min: 0,
    max: 100000,
    value: 32000, // default value at start
    change: function () {
      var obj = $("#slider").data("roundSlider");
      val = obj.getValue();
      $.getJSON('/valueofslider', {
        slide_val: val
      });
    }
  });
  
  // play sound at start
  $.getJSON('/valueofslider', {slide_val: val});

</script>

</body>
</html>'''

@app.route('/test')
def test():
    HTML = 'HEAR:'
    for item in (0, 10000, 20000, 25000, 32000):
        HTML += ' <a href="/set/{}">{}</a>'.format(item, item)
    return HTML

@app.route('/off')
def off():
    """Turn off sound."""
    sound(0)
    #return jsonify({'val': 0})
    return 'off'

@app.route('/set/<int:value>')
def set_value(value):
    """Set value. Use 0 to turn it off."""
    sound(value)
    #return jsonify({'val': value})
    return str(value)

@app.route('/get')
def get_value():
    """Get value. Returns 0 when turned off."""
    if tb:
        value = tb.sample_rate
    else:
        value = 0
    #return jsonify({'val': value})
    return str(value)
    
@app.route('/valueofslider')
def slide():
    sample_rate = request.args.get('slide_val', '32000')
    sample_rate = int(sample_rate)
    sound(sample_rate)
    #return jsonify({'val': sample_rate})
    return str(sample_rate)

def sound_old(sample_rate):
    """version which doesn't use `change()`"""
    global tb
    
    print('[sound] sample_rate:', sample_rate)
    sample_rate = int(sample_rate)

    # stop old sound
    if tb: # if tb is not None
        tb.stop()
        tb.wait()
        tb = None 
            
    # create new sound (if not zero)
    if sample_rate > 0:
        tb = TopBlock22(sample_rate)
        tb.start()

def sound(sample_rate):
    """version which uses `change()`"""
    global tb
    
    print('[sound] sample_rate:', sample_rate)
    sample_rate = int(sample_rate)

    # change or stop old sound
    if tb: # if tb is not None
        if sample_rate > 0:
            tb.change(sample_rate)
        else:        
            tb.stop()
            tb.wait()
            tb = None 
            
    # create new sound (if not zero)
    if not tb:
        if sample_rate > 0:
            tb = TopBlock22(sample_rate)
            tb.start()

    
if __name__ == '__main__':    
    app.run(debug=True)
