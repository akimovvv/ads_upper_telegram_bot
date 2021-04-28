from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

edit = InlineKeyboardButton(text='Редактировать профиль', callback_data='edit_diesel')
cancel = InlineKeyboardButton(text='Отмена', callback_data='cancel')

edit_diesel_profiles = InlineKeyboardMarkup().add(edit).add(cancel)