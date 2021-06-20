
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.05.31
#
# title: Python telegram bot create/modify variable from input
# url: https://stackoverflow.com/questions/67766468/python-telegram-bot-create-modify-variable-from-input/67766651#67766651

import os
from telegram.ext import Updater, CommandHandler

# global variable
variables = {
    'percentup': 2,
    'percentdown': 0,
}

def set_value(update, context):
    if len(context.args) == 2:
        var = context.args[0]
        value = context.args[1]
        try:
            if var in variables:
                variables[var] = int(value)
            else:
                update.message.reply_text(f"I don't know variable '{var}'")
        except:
            update.message.reply_text(f"Wrong integer value '{value}'")            
    else:
        update.message.reply_text(f"usage: /set variable value")

def get_value(update, context):
    if len(context.args) == 1:
        var = context.args[0]
        if var in variables:
            update.message.reply_text(variables[var])
        else:
            update.message.reply_text(f"I don't know variable '{var}'")
    else:
        update.message.reply_text(f"usage: /get variable")

if __name__ == '__main__':

    TOKEN = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("set", set_value))
    dispatcher.add_handler(CommandHandler("get", get_value))

    updater.start_polling()
    updater.idle()

