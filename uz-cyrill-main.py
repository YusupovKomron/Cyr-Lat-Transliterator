# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:42:26 2022

@author: asliddinxanov
"""

from transliterate import to_cyrillic, to_latin
import telebot #pip install pyTelegramBotAPI

token = "------------" #You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot(token, parse_mode = None)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    a = "Welcome to Transliterator"
    a += "/nEnter word : "
    bot.reply_to(message, a)

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    
    msg = message.text
    a = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, a(msg))
    
    # or
    
    # if msg.isascii():
    #     a = to_cyrillic(msg)
    # else:
    #     a = to_latin(msg)
    # bot.reply_to(message, a)

bot.polling()