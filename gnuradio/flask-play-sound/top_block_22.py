
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


def main():
    tb = TopBlock22(32000)
    tb.start()

    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
        
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
    
