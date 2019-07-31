from pynput import keyboard

def on_press(key):
    global key_pressed
    
    try:
        if key.char in ("c", "v"):
            key_pressed = key.char
            return False # stop listener
    except AttributeError as ex:
        print(ex)

def on_release(key):
    if key == keyboard.Key.esc:
        return False # stop listener


def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join() # wait till listener stops

    if key_pressed == 'c':    
        # do something
    elif key_pressed == "v":
        # do something else
    elif key_pressed == keyboard.Key.esc:
        print('You pressed ESC')

