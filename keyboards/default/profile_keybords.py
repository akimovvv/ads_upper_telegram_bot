from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji
diesle_btn = KeyboardButton(text='Diesel Elcat kg')
lalafo_btn = KeyboardButton(text='Lalafo kg')
bazar_btn = KeyboardButton(text='Bazar kg')
mashina_btn = KeyboardButton(text='Mashina kg')
back = KeyboardButton(text='Назад')

prof_btns = ReplyKeyboardMarkup(one_time_keyboard=True).row(diesle_btn, lalafo_btn).row(mashina_btn, bazar_btn).add(back)