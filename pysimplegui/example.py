
# date: 2019.07.07
# https://stackoverflow.com/questions/56918976/how-to-generate-file-txt-if-pop-up-click-on-sg-submit-from-pysimplegui/56919032#56919032

import PySimpleGUI as sg

layout = [
    [sg.Text('Name1', size=(15, 1), background_color="white" ), sg.InputText()],
    [sg.Text('Name2', size=(15, 1), background_color="white" ), sg.InputText()],
    [sg.Text('Name3', size=(15, 1), background_color="white" ), sg.InputText()],

    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Test', layout, background_color="white")
event, values = window.Read()
window.Close()

if event == 'Submit':
    # create before next GUI because I want to use the same name for variable `values`
    all_values = values.values() # values from dictionary
    text = "\n".join(all_values) # put values in separated lines

    layout = [
        [sg.Text('Filename', size=(15, 1), background_color="white" ), sg.InputText()],

        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Test', layout, background_color="white")
    event, values = window.Read()
    window.Close()

    if event == 'Submit':
        name_file = values[0]

        try:
            fh = open(name_file, 'r+')
        except FileNotFoundError:
            fh = open(name_file, 'w+')
    
        fh.write(text) # write all as one string
    
        fh.close()
