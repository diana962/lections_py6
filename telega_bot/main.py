import telebot
from telebot import types
import random

token = '6610865586:AAHCkP7duffqFr34EXxvgXsYb2rBzbTyE_Y'
bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Play')
btn2 = types.KeyboardButton('No Play')

keyboard.add(btn1, btn2)


@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, 'Hello, Champion! Wanna start a game?', reply_markup=keyboard)
    bot.register_next_step_handler(bot_message, check_answer)

def check_answer(message):
    if message.text == 'Play':
        bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число, которое я загадаю в диапазоне от 1 до 10 вкючительно! У тебя будет 3 попытки! Если не угадаешь я тебя повешу! :)')
        number = random.randint(1, 10)
        print(number)
        game(message, 3, number)
    elif message.text == 'No Play':
        bot.send_message(message.chat.id, 'No then no. Tschuess')
    else: 
        bot_message = bot.send_message(message.chat.id, 'Wrong number. Try again!.', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, check_answer)


def game(message, attempts, number):
    message_bot = bot.send_message(message.chat.id, 'Guess number: ')
    bot.register_next_step_handler(message_bot, ckeck_number, attempts-1, number) 

def ckeck_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'You have a luck!')
    elif attempts == 0:
        bot.send_message(message.chat.id, 'You\'ve lost! Next time you shoot')
        # with open('Chase Atlantic - HEAVEN AND BACK (Lyrics)', 'rb') as f:
        #     bot.send_video(message.chat.id, f)
    else:
        bot.send_message(message.chat.id, f'Wrong answer. You have {attempts} yet')
        game(message,attempts, number)
bot.polling()
