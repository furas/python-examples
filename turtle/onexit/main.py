import turtle

# --- functions ---

def onexit(callback):
    sc = turtle.getscreen()
    def _onexit():
        callback()
        sc._destroy()
    sc._root.ondestroy(_onexit)

# --- test ---

def test():
    print('test on exit')

onexit(test)

turtle.done()
