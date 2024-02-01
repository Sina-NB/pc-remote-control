#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import yaml

with open('settings.yml', 'r') as f:
    data = yaml.full_load(f)
API_TOKEN = data['token']
print(API_TOKEN)

bot = telebot.TeleBot('6929643510:AAF7sILSALJWnSSYj8ymEJqNhHIz1MKRYqQ')


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print('recieved')
#     bot.reply_to(message, """\
# Hi there, I am EchoBot.
# I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# """)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.polling()