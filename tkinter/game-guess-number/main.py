import tkinter
import random
import pygame

# --- functions ---

def on_click(event=None): # default value for event because `command=` doesn't send event
    global low, high

    guess = int(entry.get())  # entry needs `.get()` to get value

    if guess == answer:
        bg.itemconfig(image_id, image=bg_p_bingo)  # replace image in PhotoImage

        low = guess
        high = guess        
        label_low['text'] = str(low)    # replace text in Label
        label_high['text'] = str(high)  # replace text in Label
        
        #bingo = pygame.mixer.Sound("bingo.mp3")
        #bingo.play(0)

    elif guess > answer:
        bg.itemconfig(image_id, image=bg_p_high)  # replace image in PhotoImage

        high = guess
        label_high['text'] = str(high)  # replace text in Label

        #lol = pygame.mixer.Sound("lol.mp3")
        #lol.play(0)
    else:
        bg.itemconfig(image_id, image=bg_p_low)    # replace image in PhotoImage

        low = guess
        label_low['text'] = str(low)    # replace text in Label

        #lol = pygame.mixer.Sound("lol.mp3")
        #lol.play(0)
    
# --- main ---

low = 0
high = 101

# --- 

answer = random.randrange(low, high)

#pygame.mixer.init()

root = tkinter.Tk()

label = tkinter.Label(root, text="Guess a number: ")
label.pack(padx=5, pady=5)

entry = tkinter.Entry(root)
entry.pack(padx=5, pady=5)

button = tkinter.Button(root, text='CHECK', command=on_click)
button.pack(padx=5, pady=5)

entry.bind('<Return>', on_click)  # run function on pressing ENTER - it sends `event` to function

bg = tkinter.Canvas(root, width=300, height=300)
bg.pack()

bg_p = tkinter.PhotoImage(file="bg.png")
bg_p_bingo = tkinter.PhotoImage(file="bingo.png")
bg_p_low   = tkinter.PhotoImage(file="too_low.png")
bg_p_high  = tkinter.PhotoImage(file="too_high.png")

image_id = bg.create_image(150, 150, image=bg_p, anchor='center')

frame = tkinter.Frame(root)  # create Frame to put widgets in one row
frame.pack(fill='both', expand=True)

label_low = tkinter.Label(frame, text=f'{low}',  font=("Arial", 30), bg="white", width=3)
label_low.pack(side='left', padx=5, pady=5, fill='x', expand=True)

label_high = tkinter.Label(frame, text=f'{high}', font=("Arial", 30), bg="white", width=3)
label_high.pack(side='right', padx=5, pady=5, fill='x', expand=True)

#bgm = pygame.mixer.Sound("bgm.mp3")
#bgm.play(-1)

root.mainloop()  

pygame.mixer.quit()
