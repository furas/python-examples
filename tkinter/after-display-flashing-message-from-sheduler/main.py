
# date: 2019.04.12
# https://stackoverflow.com/a/55654621/1832058

import tkinter as tk
import datetime

# --- functions ----

# function which create window with message
def message_start(text):
    global repeates
    global message_window
    global message_label
    
    repeates = 3

    # create window with messages
    message_window = tk.Toplevel()
    message_label = tk.Label(message_window, text=text, bg='red')
    message_label.pack()

    # update window after 500ms
    root.after(500, message_update)
               
# function which change background in displayed window
def message_update():
    global message_window
    global repeates
    
    if repeates > 0:
        repeates -= 1
        
        if message_label['bg'] == 'red':
            message_label['bg'] = 'green'
        else:
            message_label['bg'] = 'red'
            
        # update window after 500ms
        root.after(500, message_update)
    else:
        # close window 
        message_window.destroy()
        
        # inform `check_time` that window is not busy
        message_window = None
                
# loop which update current time and check which message need to display        
def check_time():
    
    # display current time
    current_time = datetime.datetime.now()
    root_label_time['text'] = current_time.strftime('%Y.%m.%d %H:%M:%S')

    # check if there is message to display
    for message in messages:
        if current_time >= message['start']:  # it is time to display message
            if message['state'] == 'waiting': # message is not displayed at this moment
                if message_window is None: # window is not busy
                    message['state'] = 'displayed' # don't display it again
                    message_start(message['text'])  # display message

    # update time after 1000ms (1s)
    root.after(1000, check_time)
    
# --- main ---

messages = [
    {
        'text': 'Time for coffee',
        'start': datetime.datetime.now() + datetime.timedelta(seconds=5),
        'state': 'waiting',
    },
    {
        'text': 'Back to work',
        'start': datetime.datetime.now() + datetime.timedelta(seconds=15),
        'state': 'waiting',
    },
]

message_window = None
repeates = 3

# ---

root = tk.Tk()

# label with current time
root_label_time = tk.Label(root, text='- wait -')
root_label_time.pack()

# label with sheduler
root_label_sheduler = tk.Label(root)
root_label_sheduler.pack()

# displa messages in sheduler
for message in messages:
    root_label_sheduler['text'] +=  "\n" + message['start'].strftime('%Y.%m.%d %H:%M:%S ') + message['text']
    
# start displaying time    
check_time()

root.mainloop()
