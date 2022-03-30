# Cyr-Lat-Transliterator
Uzb-Cyrillic-transliterator

for telegram bot 
Installation using pip (a Python package manager):
$ pip install pyTelegramBotAPI

Installation from source (requires git):
```
$ git clone https://github.com/eternnoir/pyTelegramBotAPI.git
$ cd pyTelegramBotAPI
$ python setup.py install
```
```
import telebot

bot = telebot.TeleBot("TOKEN", parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN
```
Note: Make sure to actually replace TOKEN with your own API token.

Let's define a message handler which handles incoming /start and /help commands.
```
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
```
A function which is decorated by a message handler can have an arbitrary name, however, it must have only one parameter (the message).

Let's add another handler:
```
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
```
We now have a basic bot which replies a static message to "/start" and "/help" commands and which echoes the rest of the sent messages. To start the bot, add the following to our source file:
```
bot.infinity_polling()
```
