from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
ibt1 = InlineKeyboardButton(text='kg', callback_data='kg')
ibt2 = InlineKeyboardButton(text='ru', callback_data='ru')
ibt3 = InlineKeyboardButton(text='en', callback_data='en')

imp2 = InlineKeyboardMarkup().row(ibt1, ibt2, ibt3)