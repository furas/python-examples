import random
import time

#
# https://stackoverflow.com/questions/47934184/mortal-kombat-console-game-python2/47934454#47934454
#

# --- functions ---

def ask_for_magnitute():
    while True:
        value = input("Choose your attack magnitude between 1 and 50: ")

        if value > 50:
            print "The attack magnitude must be between 1 and 50."
        elif value < 1:
            print "The attack magnitude must be between 1 and 50."
        else:
            return value


def attack(points, name):

    chance_of_damaging = random.randint(0, 100)

    print "---------------", name, "Attacks !! ---------------"

    attack_magnitute = ask_for_magnitute()

    if chance_of_damaging > attack_magnitute:
        print name, "hits", attack_magnitute, "damage!!"
        points -= attack_magnitute
    else:
        print "Ooopsy!", name, "missed the attack!"

    return points


def display(points1, points2, name1, name2):
    print name1, "                                                                 ", name2
    print "HP [%s]:" % points2, points2/2 * "|" ,"        ",  # comma at the end and it doesn't add `"\n"`
    print "HP [%s]:" % points1, points1/2 * "|" 


def ask_name(text, other_heros_list):
    print '-----', text, 'Hero -----'

    while True:

        name = raw_input("Please type your hero's name: ")
        name = name.capitalize()

        if len(name) <= 1:
            print "Length of hero's name must be longer than 1 character."        
        elif name in other_heros_list:
            print name, "is taken, please choose another name!"
        else:
            print text, "hero's name is", name
            break

    return name


def main():

    players_list = []

    hero_name = ask_name("First", players_list)
    players_list.append(hero_name)

    hero_name = ask_name("Second", players_list)
    players_list.append(hero_name)

    random.shuffle(players_list)

    coin_toss = players_list[0]
    player    = players_list[1] 

    print "Coin toss result: %s starts first!" % coin_toss #Coin toss result
    print "The game begins in 5 seconds!" #countdown

    # --- loop ----

    running = True

    while running:

        # --- init --- 

        # (re)set points
        hp1, hp2 = (100, 100)

        # --- game ---

        while hp1 > 1 and hp2 > 1:
            hp1 = attack(hp1, coin_toss)
            display(hp1, hp2, coin_toss, player)

            if hp1 <= 1:
                break

            hp2 = attack(hp2, player)
            display(hp1, hp2, coin_toss, player)

        # --- game over ---

        if hp1 <= 1:
            print coin_toss, " win"
        if hp2 <= 1:
            print player, " win"

        # --- play again ---

        answer = raw_input('Play again [Y/n]?').lower().strip()

        # exit only if `n` - other answers starts again  
        if answer == 'n':
            running = False

# --- main ---

main()
