#!/usr/bin/env python3

import tkinter as tk

def cap_filter(selection):
    options = {
        'Arm': ['50kg', '100kg', '200kg', '300kg'],
        'Arm (Food Grade)': ['75kg'],
        'Rail': ['125kg', '300kg'],
        'Drive': ['125kg', '300kg'],
    }

    print(options[selection])

    # remove old elements
    cap_dropdown['menu'].delete(0, 'end')
    
    # add new items
    for text in options[selection]:
        cap_dropdown['menu'].add_command(label=text, command=lambda arg=text:length_filter(arg))

def length_filter(selection):
    type_ = lift_type.get()
    
    if selection == '50kg' and type_ == 'Arm':
        length_choice = ['3m']
    elif selection == '75kg':
        length_choice = ['4.2m']
    elif selection == '100kg' and type_ == 'Arm':
        length_choice = ['3m', '4m', '5m']
    elif selection == '125kg':
        length_choice = ['N/A']
    elif selection == '200kg' and type_ == 'Arm':
        length_choice = ['3m', '4m', '5m']
    elif selection == '300kg' and type_ == 'Arm':
        length_choice = ['3m', '4m']
    elif selection == '300kg' and type_ == 'Rail':
        length_choice = ['N/A']
    elif selection == '300kg' and type_ == 'Drive':
        length_choice = ['N/A']
    else:
        length_choice = ['N/A']
        
    print(length_choice)

app = tk.Tk()

lift_type = tk.StringVar()
lift_type.set('Lift Type')
files = ['Arm', 'Arm (Food Grade)', 'Rail', 'Drive']

lift_dropdown = tk.OptionMenu(app, lift_type, *files, command=cap_filter)
lift_dropdown.pack()

lift_cap = tk.StringVar()
lift_cap.set('Capacity')
cap_choice = ['']

cap_dropdown = tk.OptionMenu(app, lift_cap, *cap_choice, command=length_filter)
cap_dropdown.pack()

app.mainloop()
