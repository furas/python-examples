#!/usr/bin/env python3

# date: 2020.05.15
# https://stackoverflow.com/questions/61818387/i-want-to-pass-data-from-javascript-code-to-flask-server/

from flask import Flask, request, jsonify, render_template_string
import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string('''
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

<script type=text/javascript>
    $(function() {
      $("a#sender").bind("click", function() {
        $.getJSON(
          "{{ url_for('ajax') }}",  // url /ajax
          {"x": 123, "y": 789},     // data (send to server)
          function(data) {          // callback executed when get answer
            console.log(data);      // data (received from server)

            $('#results').append(data["time"] + " | " + data["x"] + ", " + data["y"] + "<br>");

            window.alert(data["x"] + ',' + data["y"]);
          });
        return false;  // stop <a> to send normal request
      });
    });
</script>

<form>
    <a href="#" id="sender"><button>Send AJAX</button></a>
</form>

<div id="results"></div>
''')


@app.route('/ajax')
def ajax():
    print("Hello AJAX")
    
    # get data from url /ajax?x=...&y=...
    x = request.args.get('x', 0)
    y = request.args.get('y', 0)
    print('x:', x)
    print('y:', y)
    
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    
    # send answer as JSON
    return jsonify({'x': x, 'y': y, 'time': current_time})


if __name__ == "__main__":
    app.run(debug=True) #, use_reloader=False)

