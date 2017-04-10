# -*- coding: utf-8 -*-

import telebot
import time
from telebot import types

bot = telebot.TeleBot("377187368:AAECNE2hy833K-udC5S2gOrztUjUQqpk558")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kochka = types.KeyboardButton('1. Качалочка')
    prachka = types.KeyboardButton('...')
    markup.row(kochka, prachka)
    bot.send_message(message.chat.id, "Привет, чел! Я твой карманный помощник в этом студгородке. Что хочешь?",
                     reply_markup=markup)

@bot.message_handler(regexp='1. Качалочка')
def kochka(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    korpus1 = types.KeyboardButton('1, 2, 3, 4, 5')
    korpus2 = types.KeyboardButton('7, 8, 9, 10, 11')
    back = types.KeyboardButton('0. Главное меню')
    markup.row(korpus1, korpus2)
    markup.row(back)
    bot.send_message(message.chat.id, "*Спортзал*\n\nБесплатное время посещения:\nпн-пт: 7:00-16:00, 22:00-23:00\nсб: 7:00-16:00, 21:00-22:00\nвс: 8:00-16:00, 21:00-22:00\n\nУкажите свой корпус", reply_markup=markup, parse_mode='Markdown')


@bot.message_handler(regexp='\d,\s\d,\s\d,*')
def kochka_more(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('0. Главное меню')
    markup.row(back)

    good = 100
    week = {"0": "воскресенье, 8:00-16:00, 21:00-22:00",
            '1': "понедельник, 7:00-16:00, 22:00-23:00",
            "2": "вторник, 7:00-16:00, 22:00-23:00",
            "3": "среда, 7:00-16:00, 22:00-23:00",
            "4": "четверг, 7:00-16:00, 22:00-23:00",
            "5": "пятница, 7:00-16:00, 22:00-23:00",
            "6": "суббота, 7:00-16:00, 21:00-22:00"}

    if message.text:
        if message.text == '1, 2, 3, 4, 5':
            good = 0
        elif message.text == '7, 8, 9, 10, 11':
            good = 1
    day = int(time.strftime("%d"))
    opportunity = "Сегодня твой день!"
    if day%2 == good:
        opportunity = "Сегодня твой день!\n{}".format(week[time.strftime('%w')])
    else:
        opportunity = "Приходи завтра"
    bot.send_message(message.chat.id, "*Спортзал*\n\n"+opportunity,
                     reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(regexp='0. Главное меню')
def home(message):
    send_welcome(message)

bot.polling()