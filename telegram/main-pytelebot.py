#!/usr/bin/env python3

# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2020.12.16

import os
import telebot

TOKEN =  os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TOKEN)

users_id = [1079414868]

@bot.message_handler(commands=['authorize'])
def start_command(message):
    print(message.chat.id, type(message.chat.id))
    if message.from_user.id not in users_id:
        text = 'u are not permitted to run this bot'
    else:
        text = 'u are welcome'
    bot.send_message(message.chat.id, text)
    #bot.reply_to(message, text)

@bot.message_handler(commands=['test'])
def test_command(message):
    #bot.reply_to(message, '1, 2, 3, testing')
    bot.send_message(message.chat.id, '1, 2, 3, testing')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	#bot.reply_to(message, "I don't understand: " + message.text)
    bot.send_message(message.chat.id, "I don't understand: " + message.text)

print('running ...')
bot.polling()
