#!/usr/bin/env python3

# date:2020.01.21
# https://stackoverflow.com/questions/59836541/creating-curvature-animation-in-python/

import tkinter as tk
import random

def follow(player_x, player_y, enemy_x, enemy_y, enemy_speed=5):
    diff_x = player_x - enemy_x
    diff_y = player_y - enemy_y
    
    distance = (diff_x**2 + diff_y**2)**0.5  # Pythagoras: a**2 + b**2 = c**2

    if distance <= enemy_speed:
        return diff_x, diff_y
    
    normal_x = diff_x/distance
    normal_y = diff_y/distance
    
    enemy_move_x = enemy_speed * normal_x
    enemy_move_y = enemy_speed * normal_y
    
    return enemy_move_x, enemy_move_y

def update_game():
    global player_x
    global player_y
    global enemy_x
    global enemy_y
    
    # draw line for player
    canvas.create_line(player_x, player_y, player_x+player_move_x, player_y+player_move_y, fill='green')
    
    # move player
    player_x += player_move_x
    player_y += player_move_y
    canvas.move(player_id, player_move_x, player_move_y)
    
    # calculate move for enemy
    enemy_move_x, enemy_move_y = follow(player_x, player_y, enemy_x, enemy_y, enemy_speed)
    
    # draw line for enemy
    canvas.create_line(enemy_x, enemy_y, enemy_x+enemy_move_x, enemy_y+enemy_move_y, fill='red')
    
    # move enemy
    enemy_x += enemy_move_x
    enemy_y += enemy_move_y
    canvas.move(enemy_id, enemy_move_x, enemy_move_y)

    root.after(100, update_game) # repeate after 100ms (0.1s)

# --- main ---

# player start position and move ("speed")
player_x = 5
player_y = 50
player_move_x = 4
player_move_y = 0 # try for `1`

# enemy start position and speed
enemy_x = 5
enemy_y = 500
enemy_speed = 5
    
root = tk.Tk()

canvas = tk.Canvas(root, width=750, height=500)#, bg='gray')
canvas.pack()

player_id = canvas.create_oval(player_x-5, player_y-5, player_x+5, player_y+5, fill='green')
enemy_id = canvas.create_oval(enemy_x-5, enemy_y-5, enemy_x+5, enemy_y+5, fill='red')

update_game()

root.mainloop()

