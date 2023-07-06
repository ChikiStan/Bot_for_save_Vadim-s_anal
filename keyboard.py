from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import WebAppInfo


start_keyboard = InlineKeyboardMarkup()

autoriz = InlineKeyboardButton('Authorization', callback_data='login')

start_keyboard.add(autoriz)

denied_keyboard = InlineKeyboardMarkup()

support = InlineKeyboardButton('Support', callback_data='support')

denied_keyboard.add(autoriz, support)

success_keyboard = InlineKeyboardMarkup()

courses = InlineKeyboardButton('Courses', web_app=WebAppInfo(url='https://habr.com/ru/'))

success_keyboard.add(courses, support)
