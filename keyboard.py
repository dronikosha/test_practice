from telebot import types

menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
but1 = types.KeyboardButton('Выбрать семестр')
but2 = types.KeyboardButton('Написать в поддержку')

start = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
start1 = types.KeyboardButton('Меню')


years = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
first_year = types.KeyboardButton('1 семестр')
second_year = types.KeyboardButton('2 семестр')
