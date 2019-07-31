from pynput import keyboard

def on_press(key):
    try:
        if key.char == "c":
            # do something
            return False # stop listener
        elif key.char == "v":
            # do something
            return False # stop listener
    except AttributeError as ex:
        print(ex)

def on_release(key):
    if key == keyboard.Key.esc:
        return False # stop listener

def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join() # wait for listener stop

