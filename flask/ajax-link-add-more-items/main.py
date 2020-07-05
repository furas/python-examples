#!/usr/bin/env python3

# date: 2020.06.30

from flask import Flask, request, jsonify, render_template_string
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string('''
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

<script type=text/javascript>
    var offset = 0;  // offset for first item to get
    var count = 10;  // number of items to get
    
    $(function() {
      $("a#sender").bind("click", function() {
        $.getJSON(
            "{{ url_for('ajax') }}",             // url /ajax
            {"offset": offset, "count": count},  // data (send to server)
            function(data) {                     // callback executed when get answer
              console.log(data);                 // data (received from server)
            
              // append date and time 
              $('#result').append(data['dt'] + '<br>');
            
              // append every item from list
              $.each(data['items'], function(index, value){
                $('#result').append(value + '<br>');
              });
            
              offset = offset + count;           // update offset
            }
        );
        return false;  // stop <a> to send normal request
      });
    });
</script>

<a href="#" id="sender">More ...</a>

<div id="result"></div>
''')


@app.route('/ajax')
def ajax():
    print('url: /ajax')
    
    # get data from url /ajax?offset=...&count=...
    offset = int(request.args.get('offset', 0))
    count  = int(request.args.get('count', 0))
    print('offset:', offset)
    print(' count:', count)
    
    dt = datetime.datetime.now().strftime('%Y.%m.%d - %H:%M:%S')
    
    # generate list based on data from browser
    items = list(range(offset, offset+count))
    
    # send answer as JSON
    return jsonify({'dt': dt, 'items': items})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

