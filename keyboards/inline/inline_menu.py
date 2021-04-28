from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ibt1 = InlineKeyboardButton(text='Diesel Elcat kg', callback_data='ibt1')
ibt2 = InlineKeyboardButton(text='Bazar kg', callback_data='ibt2')
ibt3 = InlineKeyboardButton(text='Mashina kg', callback_data='ibt3')
ibt4 = InlineKeyboardButton(text='Lalafo kg', callback_data='ibt4')

imp1 = InlineKeyboardMarkup().row(ibt1, ibt2).add(ibt3, ibt4)