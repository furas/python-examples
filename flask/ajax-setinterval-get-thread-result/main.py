#!/usr/bin/env python3

# date: 2020.01.17
# https://stackoverflow.com/questions/59780007/ajax-with-flask-for-real-time-esque-updates-of-sensor-data-on-webpage/

from flask import Flask, request, render_template_string, jsonify
import datetime
import time
import threading

app = Flask(__name__)

running = False # to control loop in thread
value = 0       

def rpi_function():
    global value
    
    print('start of thread')
    while running: # global variable to stop loop  
        value += 1
        time.sleep(1)
    print('stop of thread')
    
    
@app.route('/')
@app.route('/<device>/<action>')
def index(device=None, action=None):
    global running
    global value

    if device:
        if action == 'on':
            if not running:
                print('start')
                running = True
                threading.Thread(target=rpi_function).start()
            else:
                print('already running')
        elif action == 'off':
            if running:
                print('stop')
                running = False
            else:
                print('not running')
            
    return render_template_string('''<!DOCTYPE html>
   <head>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
   </head>
   <body>
        <a href="/bioR/on">TURN ON</a>  
        <a href="/bioR/off">TURN OFF</a>
        <h1 id="num"></h1>
        <h1 id="time"></h1>
        <script>
            setInterval(function(){$.ajax({
                url: '/update',
                type: 'POST',
                success: function(response) {
                    console.log(response);
                    $("#num").html(response["value"]);
                    $("#time").html(response["time"]);
                },
                error: function(error) {
                    console.log(error);
                }
            })}, 1000);
        </script>
   </body>
</html>
''')

@app.route('/update', methods=['POST'])
def update():
    return jsonify({
        'value': value,
        'time': datetime.datetime.now().strftime("%H:%M:%S"),
    })

app.run(debug=True)


