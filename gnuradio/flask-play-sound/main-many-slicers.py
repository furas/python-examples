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

    def __init__(self, sample_rate=32000, amplitude=0, frequency=0):

        gr.top_block.__init__(self, "Top Block 22")
        ##################################################
        # Variables
        ##################################################
        self.sample_rate = sample_rate
        print('[TopBlock22] __init__: sample_rate:', self.sample_rate)
        
        self.amplitude = amplitude
        print('[TopBlock22] __init__: amplitude:', self.amplitude)

        self.frequency = frequency
        print('[TopBlock22] __init__: frequency:', self.frequency)

        # for mute_on, mute_off
        #self.old_sample_rate = self.sample_rate
        #self.old_ampliture = self.ampliture
        #self.old_frequency = self.frequency

        ##################################################
        # Blocks
        ##################################################
        self.blocks_add_xx = blocks.add_vff(1)
        self.audio_sink = audio.sink(32000, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(sample_rate, analog.GR_COS_WAVE, 440,  amplitude, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(sample_rate, analog.GR_COS_WAVE, 350, amplitude, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN,  amplitude, -42)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx, 2))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx, 1))
        self.connect((self.blocks_add_xx, 0), (self.audio_sink, 0))

    def change_sample_rate(self, value=None):
        if value is not None:
            self.sample_rate = value
            print('[TopBlock22] change: sample_rate:', value)
            self.analog_sig_source_x_1.set_sampling_freq(value)
            self.analog_sig_source_x_0.set_sampling_freq(value)

    def change_amplitude(self, value=None):
        if value is not None:
            value /= 10000.
            self.amplitude = value
            print('[TopBlock22] change: amplitude:', value)
            self.analog_sig_source_x_1.set_amplitude(value)
            self.analog_sig_source_x_0.set_amplitude(value)
            self.analog_noise_source_x_0.set_amplitude(value)

    def change_frequency(self, value=None):
        if value is not None:
            self.frequency = value
            print('[TopBlock22] change: frequency:', value)
            #TODO: change some values

    def change(self, sample_rate=None, amplitude=None, frequency=None):
        #self.change_sample_rate(sample_rate)
        #self.change_amplitude(amplitude)
        #self.change_frequency(frequency)

        if sample_rate is not None:
            self.change_sample_rate(sample_rate)

        if amplitude is not None:
            self.change_amplitude(amplitude)

        if frequency is not None:
            self.change_frequency(frequency)

    def turn_off(self):
        self.change(0, 0, 0)

    #def mute_on(self):
    #    # remember values
    #    self.old_sample_rate = self.sample_rate
    #    self.old_ampliture = self.ampliture
    #    self.old_frequency = self.frequency
    #    # turn off sound
    #    self.change(0, 0, 0)

    #def mute_off(self):
    #    # set old values
    #    self.change(self.old_sample_rate, self.old_ampliture, self.old_frequency)
        
# -----------------------------------------------------------------------------

from flask import Flask, request, jsonify

app = Flask(__name__)

# start with default values 
#tb = TopBlock22()
tb = TopBlock22(0, 0, 0)
tb.start()


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

<style>

.slider {
 position: absolute;
 align:center;
}    

.row1 {top:100px;}
.row2 {top:450px;}

.col1 {left:75px;}
.col2 {left:470px;}
.col3 {left:870px;}

</style>
</head>

<body>

<div id="slider1" class='slider row1 col1'></div>
<!--  <p>Sample Rate Slider</p> -->

<div id="slider2" class='slider row1 col2'></div>
<!--  <p>Amplitude Slider2</p> -->

<div id="slider3" class='slider row1 col3'></div>
<!-- <p>Frequency Slider3</p> -->

<div id="slider4" class='slider row2 col1'></div>
<!-- <p>Slider4</p>  -->

<div id="slider5" class='slider row2 col2'></div>
<!-- <p>Slider5</p>  -->

<div id="slider6" class='slider row2 col3'></div>
<!-- <p>Slider6</p>  -->

<button id="turn_off_button">TURN OFF</button>

<script>

  // create sliders
  
  $("#slider1").roundSlider({
    radius: 150,
    min: 0,
    max: 10000,
    value: 0, // default value at start
    //change: function(event) { $.getJSON('/valueofslider', {slide1_val: event.value}); }
    change: function(event) { $.getJSON('/set_sample_rate/' + event.value); }
  });

  $("#slider2").roundSlider({
    radius: 150,
    min: 0,
    max: 10000,
    value: 0, // default value at start
    //change: function(event) { $.getJSON('/valueofslider', {slide2_val: event.value}); }
    change: function(event) { $.getJSON('/set_amplitude/' + event.value); }
  });

  $("#slider3").roundSlider({
    radius: 150,
    min: 0,
    max: 10000000000,
    value: 0, // default value at start
    //change: function(event) { $.getJSON('/valueofslider', {slide3_val: event.value}); }
    change: function(event) { $.getJSON('/set_frequency/' + event.value); }
  });

  $("#slider4").roundSlider({
    radius: 150,
    min: 0,
    max: 10000000000,
    value: 0, // default value at start
    change: function(event) { $.getJSON('/valueofslider', {slide4_val: event.value}); }
  });

  $("#slider5").roundSlider({
    radius: 150,
    min: 0,
    max: 10000000000,
    value: 0, // default value at start
    change: function(event) { $.getJSON('/valueofslider', {slide5_val: event.value}); }
  });

  $("#slider6").roundSlider({
    radius: 150,
    min: 0,
    max: 10000000000,
    value: 0, // default value at start
    change: function (event) { $.getJSON('/valueofslider', {slide6_val: event.value}); }
  });
  
  $("#turn_off_button").click(function(){
      // set sliders
      $("#slider1").data("roundSlider").setValue(0);
      $("#slider2").data("roundSlider").setValue(0);
      $("#slider3").data("roundSlider").setValue(0);

      // send to server
      $.getJSON('/valueofslider', {
        slide1_val: 0,
        slide2_val: 0,
        slide3_val: 0,
      });
  });
 
</script>

</body>
</html>'''

@app.route('/off')
def off():
    """Turn off sound."""
    tb.turn_off()
    #return jsonify({'val': 0})
    return 'off'

@app.route('/set_sample_rate/<int:value>')
def set_sample_rate(value):
    #sound(sample_rate=value)
    tb.change_sample_rate(value)
    #return jsonify({'sample_rate': value})
    return str(value)

@app.route('/set_amplitude/<int:value>')
def set_amplitude(value):
    #sound(amplitude=value)
    tb.change_amplitude(value)
    #return jsonify({'amplitude': value})
    return str(value)

@app.route('/set_frequency/<int:value>')
def set_frequency(value):
    #sound(frequency=value)
    tb.change_frequency(value)
    #return jsonify({'frequency': value})
    return str(value)


@app.route('/valueofslider')
def slide():
    sample_rate = request.args.get('slide1_val', None)
    amplitude   = request.args.get('slide2_val', None)
    frequency   = request.args.get('slide3_val', None)
    
    sound(
        sample_rate=sample_rate, 
        amplitude=amplitude, 
        frequency=frequency,
    )

    #return jsonify({
    #        'sample_rate': sample_rate, 
    #        'amplitude': amplitude,
    #        'frequency ': frequency ,
    #        })
    
    return 'sample_rate: {}, amplitude: {}, frequency : {}'.format(sample_rate, amplitude, frequency )

def sound(sample_rate=None, amplitude=None, frequency=None):
    """version which uses `change()`"""

    if sample_rate is not None:
        sample_rate = int(sample_rate)
        tb.change_sample_rate(sample_rate)
        
    if amplitude is not None:
        amplitude = int(amplitude)
        tb.change_amplitude(amplitude)

    if frequency is not None:
        frequency = int(frequency )
        tb.change_frequency(frequency )

    print('[sound] sample_rate:', sample_rate)
    print('[sound] amplitude:', amplitude)
    print('[sound] frequency:', frequency)

    #if tb: # if tb is not None
    #    tb.change(sample_rate, amplitude, frequency)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
