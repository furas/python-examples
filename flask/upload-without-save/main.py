from flask import Flask, request, redirect, make_response, render_template_string
from PIL import Image
import base64
import pandas as pd
import io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string('''
<form action="getfile" method="POST" enctype="multipart/form-data">
    File: <input type="file" name="uploaded_file"><br>
    <input type="submit" value="Submit">
</form>
''')


@app.route('/getfile', methods=['GET', 'POST'])
def getfile():
    html = '[empty]'

    if request.method == 'POST':

        uploaded_file = request.files.get('uploaded_file')

        filename = uploaded_file.filename
        print('filename:', filename)
        html = f'filename: {filename}<hr>'

        if filename.lower().endswith( ('.png', '.jpg') ):
            img = Image.open(uploaded_file)
            #img.save('new_name.jpg')
            img.thumbnail((200,200))

            file_object = io.BytesIO()
            img.save(file_object, 'JPEG')

            data = file_object.getvalue()  # get data directly
            # OR
            #file_object.seek(0)           # move to the beginning of file after previous writing/reading
            #data = file_object.read()     # read like from normal file

            data = base64.b64encode(data).decode()
            html += f'<img src="data:image/jpg;base64, {data}">'

        elif filename.lower().endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            html += df.to_html()
        elif filename.lower().endswith( ('.txt', '.md') ):
            data = uploaded_file.read()
            data = data.decode()
            html += f'<pre>{data}</pre>'
        else:
            data = uploaded_file.read()
            html += f'<pre>{data}</pre>'

    return html

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
