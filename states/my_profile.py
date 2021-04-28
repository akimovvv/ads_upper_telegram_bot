from aiogram.dispatcher.filters.state import State, StatesGroup


class My_profile(StatesGroup):
    name = State()
    age = State()
    gender = State()
    num = State()
