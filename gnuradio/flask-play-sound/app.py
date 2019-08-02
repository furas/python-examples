
# date: 2019.08.01
# https://stackoverflow.com/questions/57311774/wbserver-roundslider-widget-doesnt-start-update-audio-tone-program

from flask import Flask, request
from top_block_22 import TopBlock22 
import time


app = Flask(__name__)


@app.route('/')
def index():
    HTML = 'HEAR:'
    for item in (20000, 25000, 32000):
        HTML += ' <a href="/valueofslider?slide_val={}">{}</a>'.format(item, item)
    return HTML

@app.route('/valueofslider')
def slide():
    sample_rate = request.args.get('slide_val', 32000)
    sound(sample_rate)
    return sample_rate

def sound(sample_rate):
    sample_rate = int(sample_rate)
    print('[sound] sample_rate:', sample_rate)

    tb = TopBlock22(sample_rate)
    tb.start()

    time.sleep(0.5) # need it to head sound

    tb.stop()
    tb.wait()
    
    
if __name__ == '__main__':    
    app.run(debug=True)
