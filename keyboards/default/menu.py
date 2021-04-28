from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji
bt1 = KeyboardButton(text='Мой Профиль ' + emoji.emojize(':man_office_worker:'))
bt2 = KeyboardButton(text='Тарифы')
bt3 = KeyboardButton(text='Контакты')
bt4 = KeyboardButton(text='Площадки для Up объявлений')
bt5 = KeyboardButton(text='Наши проекты')
bt6 = KeyboardButton(text='Поднять сейчас')

mp1 = ReplyKeyboardMarkup(one_time_keyboard=True).row(bt1, bt6).add(bt4).row(bt2, bt3, bt5)
