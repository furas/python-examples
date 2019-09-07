
# date: 2019.08.26
# layout as function to change it in any reload
import dash
import dash_html_components as html
import datetime


app = dash.Dash(__name__)

# static layout. It has to restart script to change date
#app.layout = html.Div([
#     html.Div(datetime.datetime.now().strftime("%H:%M:%S"))
#])

# dynamic layout. It change date in every reload 

def layout():
    return html.Div([
        html.Div(datetime.datetime.now().strftime("%H:%M:%S"))
    ])

app.layout = layout


if __name__ == '__main__':
    app.run_server()#debug=True)
