from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

whats_num = InlineKeyboardButton(text='Whats App', url='https://api.whatsapp.com/send?phone=996500060402')
telegram_num = InlineKeyboardButton(text='Telegram', url='https://t.me/arturkgz')
usual_num = InlineKeyboardButton(text='Контакты для вызова', callback_data='usual_number')
num_1k = InlineKeyboardMarkup().row(whats_num, telegram_num).add(usual_num)