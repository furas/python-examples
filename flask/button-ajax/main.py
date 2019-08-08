
# date: 2019.08.05
# 

from flask import Flask, jsonify
#from flask_cors import CORS, cross_origin


app = Flask(__name__)
#CORS(app, support_credentials=True)


@app.route('/')
def index():
    return """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

<script type=text/javascript>
$(function() {
  $('a#sender').bind('click', function() {
    $.getJSON('/ajax',
      function(data) {
        console.log(data);
        window.alert(data['status']);
      });
    return false; // stop <a> to send normal request
  });
});
</script>

<form>
    <a href="#" id="sender"><button>Send AJAX</button></a>
</form>
"""

@app.route('/ajax')
#@cross_origin(supports_credentials=True)
def ajax():
    print("Hello AJAX")
    return jsonify({'status': 'OK'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)#, debug=True)

