import logging

import emoji
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.inline import imp2
from loader import dp
from states import My_profile
from utils.db_api import quick_commands as db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         "Тилди тандаңыз 'kg'\nВыберите язык 'ru'\nChoose "
                         "language 'en'", reply_markup=imp2)
    await db.add_user(id=message.from_user.id, username=message.from_user.full_name)


@dp.message_handler(state=My_profile.name)
async def get_user_name(message: types.Message, state=FSMContext):
    answer = message.text
    if answer.isalpha() and (len(answer.strip()) > 0 and len(answer.strip()) < 20):
        await db.update_profile_name(id=message.from_user.id, name=answer)
        await state.update_data(answer_1=answer)
        await message.answer(text='Введите Ваш возраст...')
        await My_profile.next()
    else:
        await message.answer(text='Некорректно ввели Ваше имя должно быть больше 0 и меньше 20 символов...')
        await My_profile.first()


@dp.message_handler(state=My_profile.age)
async def get_user_age(message: types.Message, state=FSMContext):
    answer = message.text
    if (answer.isdigit() and int(answer[0]) != 0) and (int(answer) > 0 and int(answer) < 150):
        await db.update_profile_age(id=message.from_user.id, age=int(answer))
        await state.update_data(answer_2=(answer))
        await message.answer(text=f'Введите Ваш пол {emoji.emojize(":man:")} (0)|{emoji.emojize(":woman:")} (1)')
        await My_profile.next()
    else:
        await message.answer(text='Некорректно ввели Ваш возраст, пожалуйста введите снова...')
        await My_profile.age()


@dp.message_handler(state=My_profile.gender)
async def get_user_gender(message: types.Message, state=FSMContext):
    answer = message.text
    if answer.isdigit() and (int(answer) == 0 or int(answer) == 1):
        await db.update_profile_gender(id=message.from_user.id, gender=int(answer))
        await state.update_data(answer_3=answer)
        await message.answer(text='Введите Ваш телефонный номер в формате (0 555 55 55 55) можно без пробелов...')
        await My_profile.next()
    else:
        await message.answer(text='Некорректно ввели Ваш гендерный пол, пожалуйста введите 0 или 1 снова...')
        await My_profile.gender()


@dp.message_handler(state=My_profile.num)
async def get_user_num(message: types.Message, state=FSMContext):
    answer = message.text
    answer = answer.replace(' ', '')
    if (answer.startswith('0') and answer.isalnum()) and len(answer) == 10:
        await db.update_profile_number(id=message.from_user.id, number=int(answer))
        data = await state.get_data()
        name = data.get('answer_1')
        age = data.get('answer_2')
        gender = data.get('answer_3')
        if int(gender) == 0:
            gender = 'Мужской'
        else:
            gender = 'Женский'
        await message.answer(
            text=f'Ваше имя - {name}\nВаш возраст - {age}\nВаш пол - {gender}\nВаш телефонный номер - {answer}\n\n'
                 'Спасибо за анкету!')
        await state.finish()
    else:
        await message.answer(
            text='Некорректно ввели Ваш телефонный номер, пожалуйста введите в формате (0 555 55 55 55) можно без пробелов...')
        await My_profile.num()




@dp.callback_query_handler(lambda c: c.data == 'kg')
async def ans_lan(call: CallbackQuery):
    await call.answer(cache_time=60)
    await db.update_user_language(id=call.from_user.id, language=call.data)
    logging.info(call.data)
    await call.message.answer(text='Тил алмаштырылды')
    await call.message.edit_reply_markup()
    user = await db.select_user(id=call.from_user.id)
    if user.number == None:
        await call.message.answer(
            text='Пожалуйста ответьте на вопросы ниже, так мы улучшим качество наших услуг.\n\nВведите Ваше имя...')
        await My_profile.first()

@dp.callback_query_handler(lambda c: c.data == 'ru')
async def ans_lan(call: CallbackQuery):
    await call.answer(cache_time=60)
    await db.update_user_language(id=call.from_user.id, language=call.data)
    logging.info(call.data)
    await call.message.answer(text='Язык изменён')
    await call.message.edit_reply_markup()
    user = await db.select_user(id=call.from_user.id)
    if user.number == None:
        await call.message.answer(
            text='Пожалуйста ответьте на вопросы ниже, так мы улучшим качество наших услуг.\n\nВведите Ваше имя...')
        await My_profile.first()

@dp.callback_query_handler(lambda c: c.data == 'en')
async def ans_lan(call: CallbackQuery):
    await call.answer(cache_time=60)
    await db.update_user_language(id=call.from_user.id, language=call.data)
    logging.info(call.data)
    await call.message.answer(text='Language changed')
    await call.message.edit_reply_markup()
    user = await db.select_user(id=call.from_user.id)
    if user.number == None:
        await call.message.answer(
            text='Пожалуйста ответьте на вопросы ниже, так мы улучшим качество наших услуг.\n\nВведите Ваше имя...')
        await My_profile.first()