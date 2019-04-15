
# date: 2019.04.14
# https://stackoverflow.com/questions/55672653/python-http-server-not-responding-on-post-and-get-requests/55672850#55672850

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['name'], request.form['last_name'])
        return "Hello " + request.form['last_name']
    return "Hello World"

app.run(port=8080)

