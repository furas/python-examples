
# date: 2019.10.15

# In documentation it uses lowercase `read` `close` but it has to be `Read` `Close

import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText("Hello World")],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)

print(window)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.Read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.Close()
