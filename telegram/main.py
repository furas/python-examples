#!/usr/bin/env python3

# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2020.12.16

import os
import telegram

TOKEN =  os.getenv('TELEGRAM_TOKEN')

print('\n'.join(os.environ.keys()))
if not TOKEN:
    print("Need TELEGRAM_TOKEN")
    exit(1)

bot = telegram.Bot(TOKEN)

bot.run()

