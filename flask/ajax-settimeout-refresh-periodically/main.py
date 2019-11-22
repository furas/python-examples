#!/usr/bin/env python3 

# date: 2019.11.22
# https://stackoverflow.com/questions/58996870/update-flask-web-page-with-python-script

import datetime
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""<!DOC html>
<html>
<head>
<meta charset="utf-8" />
<title>Test AJAX</title>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.8.0.min.js"></script>
<script type="text/javascript">
  (function worker() {
    $.get('/data', function(data) {
      $('#time').html(data);    // update page
      setTimeout(worker, 1000); // run it again after 1000ms (1s)
    });
  })();
</script>
</head>
<body>
   Date & Time: <span id="time"><span>
</body>
</html>""")


@app.route('/data')
def data():
    """send data to AJAX as string"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    app.run(debug=True)
