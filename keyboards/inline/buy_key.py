from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

first_price = InlineKeyboardButton(text='1 площадка - 500 сомов', callback_data='price_1', )
second_price = InlineKeyboardButton(text='2 площадка - 700 сомов', callback_data='price_2')
third_price = InlineKeyboardButton(text='3 площадка - 1000 сомов', callback_data='price_3')
firth_price = InlineKeyboardButton(text='все доступные площадки - 1500 сомов', callback_data='price_4')

prices = InlineKeyboardMarkup().add(first_price).add(second_price).add(third_price).add(firth_price)