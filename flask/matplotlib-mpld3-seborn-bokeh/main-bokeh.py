#!/usr/bin/env python3

# date: 2019.08.04
# https://stackoverflow.com/questions/57341566/my-bar-chart-does-not-appear-on-screen-how-can-i-fix-that
#
# https://bokeh.pydata.org/en/latest/
#
# if you have installed bokeh 1.0.1 (bokeh.__version__) 
# then you have to use `bokeh-1.0.1.min.js`, `bokeh-1.0.1.min.css`

from flask import Flask, redirect
from bokeh.plotting import figure, output_file, save
from bokeh.embed import components
import os


app = Flask(__name__)


@app.route('/')
def embed():
    """Get compopents and use in own HTML"""
    # https://bokeh.pydata.org/en/latest/docs/user_guide/embed.html
    # If you have installed bokeh 1.0.1 (bokeh.__version__) 
    # then you have to use `bokeh-1.0.1.min.js`, `bokeh-1.0.1.min.css`
    # It will not work if there are different versions
    
    #import bokeh
    #print(bokeh.__version__)
    
    keys = [1,2,3,4]
    values = [1,4,2,3]

    plot = figure(
        title='Bar Chart showing Side Effects of Breast \
#Cancer Medication(s) With Their Corrresponding Percentages Of \
#Occurence', 
        x_axis_label='Side Effects', 
        y_axis_label='Percentages of Occurence of Side Effects'
    )

    plot.line(keys, values) # legend=??
 
    script, div = components(plot)

    return '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-1.0.1.min.css" type="text/css" />
<script type="text/javascript" src="http://cdn.pydata.org/bokeh/release/bokeh-1.0.1.min.js"></script>
</head>
<body>''' + div + script + '''
</body>
</html>'''


@app.route('/full')
def full_page():
    """Generate full page with plot."""
    
    keys = [1,2,3,4]
    values = [1,4,2,3]

    output_file('static/plot.html')

    plot = figure(
        title='Bar Chart showing Side Effects of Breast \
#Cancer Medication(s) With Their Corrresponding Percentages Of \
#Occurence', 
        x_axis_label='Side Effects', 
        y_axis_label='Percentages of Occurence of Side Effects'
    )

    plot.line(keys, values) # legend=??
 
    if not os.path.exists('static'):
        os.makedirs('static')

    # output to static HTML file
    save(plot)

    return redirect('/static/plot.html')


if __name__ == '__main__':
    app.run()
