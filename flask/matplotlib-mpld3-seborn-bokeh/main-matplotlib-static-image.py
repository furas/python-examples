#!/usr/bin/env python3

# date: 2019.08.04
# https://stackoverflow.com/questions/57341566/my-bar-chart-does-not-appear-on-screen-how-can-i-fix-that

from flask import Flask
import matplotlib.pyplot as plt
import os


app = Flask(__name__)


@app.route('/')
def index():
    keys = [1,2,3,4]
    values = [1,4,2,3]

    plt.bar(keys, values, width=0.5)
    
    plt.xlabel("Side Effects")
    plt.ylabel("Percentages of Occurence of Side Effects")
    plt.title("Bar Chart showing Side Effects of Breast \
Cancer Medication(s) With Their Corrresponding Percentages Of \
Occurence")
    #plt.legend()

    if not os.path.exists('static'):
        os.makedirs('static')

    plt.savefig('static/image.png')
    
    return '''<DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body><img src="/static/image.png"></body>
</html>'''


if __name__ == '__main__':
    app.run()
