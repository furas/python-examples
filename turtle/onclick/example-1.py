import turtle

# --- functions ---

def on_click_1(x, y):
    print('Turtle 1 clicked:', x, y)

def on_click_2(x, y):
    print('Turtle 2 clicked:', x, y)

def on_click_screen(x, y):
    print('Screen clicked:', x, y)

# --- main ---

a = turtle.Turtle()
a.bk(100)
a.onclick(on_click_1)

b = turtle.Turtle()
b.fd(100)
b.onclick(on_click_2)

turtle.onscreenclick(on_click_screen)

turtle.mainloop()
