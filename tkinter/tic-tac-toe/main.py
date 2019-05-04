
# date: 2019.05.01
# author: Bartłomiej 'furas' Burek

import tkinter as tk

def check_row(y, char):
    return ((buttons[0][y]['text'] == char)
        and (buttons[1][y]['text'] == char)
        and (buttons[2][y]['text'] == char))

def check_col(x, char):
    return ((buttons[x][0]['text'] == char)
        and (buttons[x][1]['text'] == char)
        and (buttons[x][2]['text'] == char))

def check_diagonals(char):
    return (((buttons[0][0]['text'] == char)
         and (buttons[1][1]['text'] == char)
         and (buttons[2][2]['text'] == char))
           or
            ((buttons[0][2]['text'] == char)
         and (buttons[1][1]['text'] == char)
         and (buttons[2][0]['text'] == char)))

def check_all(char):
    for i in range(3):
        if check_row(i, char):
            print('row', i)
            return True
        if check_col(i, char):
            print('col', i)
            return True

    if check_diagonals(char):
        print('diagonals')
        return True

    return False

def count_empty():
    result = 0
    for x in range(3):
        for y in range(3):
            if buttons[x][y]['text'] == '':
                result += 1
    return result

def on_button_click(x, y):
    global player
    global gameover

    if not gameover:
        if buttons[x][y]['text'] == '':
            buttons[x][y]['text'] = player
            gameover = check_all(player)

            if gameover:
                print('win:', player)
            elif count_empty() == 0:
                gameover = True
                print('win: nobody')
            else:
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'

# --- main ---

player = 'X'
gameover = False
buttons = []

root = tk.Tk()

# create board
for x in range(3):
    row = []
    for y in range(3):
        b = tk.Button(root, text='', command=lambda bx=x, by=y: on_button_click(bx, by))
        b.grid(row=y, column=x)
        row.append(b)
    buttons.append(row)

root.mainloop()
