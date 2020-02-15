#!/usr/bin/env python3

# date: 2020.02.15

from flask import Flask, send_file
import requests
import io

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://github.com/furas/mate-python-applets/archive/master.zip')
    zip_content = io.BytesIO(response.content)
    return send_file(zip_content, mimetype='application/zip', as_attachment=True, attachment_filename='archive.zip')

if __name__ == '__main__':
    app.run()
