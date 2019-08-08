
# date: 2019.08.08
# https://stackoverflow.com/questions/57403682/how-to-change-form-action-before-form-submits

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return '''
<script>
function redirect_form(){
  if(document.getElementById("file").files.length == 0) {
    document.getElementById("mainform").action = "/nofiles";
  } else {
    document.getElementById("mainform").action = "/containsfiles"
  }
}
</script>

<form onclick="redirect_form()" name="mainform" id="mainform" method="POST" action=""
enctype="multipart/form-data">
  <input type="file" id="file" name="file" />
  <input type="submit" />
</form>
'''

@app.route('/nofiles', methods=['GET', 'POST'])
def nofiles():
    return 'nofiles'

@app.route('/containsfiles', methods=['GET', 'POST'])
def containsfiles():
    return 'containsfiles'

app.run()
