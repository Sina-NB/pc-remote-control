import telebot
import yaml
import os
from datetime import datetime

API_TOKEN = None
PASSWORD = None
OS = None
LAST_LOGIN = None
STATE = 'start'

with open('settings.yml', 'r') as f:
    data = yaml.full_load(f)
API_TOKEN = data['bot_token']
PASSWORD = data['password']
OS = data['os']

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global STATE
    STATE = 'start'
    bot.reply_to(message, 'Hi there, I am PC Controller Bot. I will help you to be able to control your system from anywhere.')

@bot.message_handler(commands=['login'])
def send_welcome(message):
    global STATE
    STATE = 'login'
    bot.reply_to(message, 'Please enter your password.')

@bot.message_handler(commands=['shutdown'])
def send_welcome(message):
        if LAST_LOGIN:
            diff_time = datetime.now() - LAST_LOGIN
        else:
            bot.reply_to(message, 'Please login.')
            return
        
        if (diff_time.total_seconds() < 180):
            bot.reply_to(message, 'Your PC shut down.')
            if OS.lower() == 'windows':
                os.system("shutdown /s /t 0")
            elif OS.lower() == 'linux':
                os.system("shutdown now -h")
        else:
            bot.reply_to(message, 'Please login.')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global LAST_LOGIN
    if STATE == 'login':
        entered_password = message.text
        if entered_password == PASSWORD:
            LAST_LOGIN = datetime.now()
            bot.reply_to(message, 'Login was Successful.')
            return
            
        else:
            bot.reply_to(message, 'Incorrect password.')
            return
            

    bot.reply_to(message, 'This is not a valid message.')
    return 

bot.infinity_polling()
