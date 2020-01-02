

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.files)
    
    return render_template_string('''<form method="POST" enctype="multipart/form-data">
<input type="file" name="file1"/><br/>
<input type="file" name="file2"/><br/>
<input type="file" name="file3"/><br/>
<input type="file" name="file4" multiple=True/><br/>
<button type="submit">SEND</button>
</form>''')

app.run() #debug=True 
