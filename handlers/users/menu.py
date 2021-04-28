from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from utils.db_api import quick_commands as db

from keyboards.default import mp1, prof_btns
from keyboards.inline import imp1, num_1k, prices, edit_diesel_profiles
from loader import dp
from states import Login_info, Profile_choose, Update_login_info
import emoji

from selenium import webdriver
from diesel import diesel_upper
from data.diesel_upper_text import text
import random
import time




# Main page fonksion
# __________________________________________________________________________________________________________________
@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer(text='Главное Меню', reply_markup=mp1)





# Contacts fonksiyon
# _________________________________________________________________________________________________________________
@dp.callback_query_handler(lambda c: c.data == 'usual_number')
async def send_us_num(call: CallbackQuery):
    await call.answer(cache_time=60, text="Звонить с 9:00 до 20:00 ", show_alert=True)
    await call.message.answer_contact(phone_number='+996 772 42 92 42', first_name='Artur')
    await call.message.answer_contact(phone_number='+996 500 06 04 02', first_name='Artur')
    await call.message.answer_contact(phone_number='+996 990 55 01 25', first_name='Artur')
    await call.message.edit_reply_markup()


@dp.message_handler(text='Контакты')
async def rate(message: types.Message):
    await message.answer("Контакты", reply_markup=num_1k)





# Price fonksiyon
# ___________________________________________________________________________________________________________________
@dp.callback_query_handler(lambda c: c.data == "price_1")
async def ans_price_1(call: CallbackQuery):
    await call.answer(cache_time=60)


@dp.callback_query_handler(lambda c: c.data == "price_2")
async def ans_price_2(call: CallbackQuery):
    await call.answer(cache_time=60)


@dp.callback_query_handler(lambda c: c.data == "price_3")
async def ans_price_3(call: CallbackQuery):
    await call.answer(cache_time=60)


@dp.callback_query_handler(lambda c: c.data == "price_4")
async def ans_price_4(call: CallbackQuery):
    await call.answer(cache_time=60)


@dp.message_handler(text='Тарифы')
async def rate(message: types.Message):
    await message.answer(text='Тарифы\n\nВсе цены указаны за 1 месяц.', reply_markup=prices)




# About us
# _______________________________________________________________________________________________________________________________
@dp.message_handler(text='Наши проекты')
async def show_menu(message: types.Message):
    await message.answer(text='Разработал @arturkgz\n'
    "Телеграм бот для автоматического поднятия рекламы\n@bishkek_tele_bot\n\n"
                              "Элсом:   +996990550125\n"
                              "Demir Bank:   1180000132525044\nМой О кошелёк:   +996500060402\n"
    'Спасибо за пддержку проектов...')








# Up now
# __________________________________________________________________________________________________________________

@dp.message_handler(text='Поднять сейчас')
async def login_an_up_ads(message: types.Message):
    users = await db.diesel_select_user(user_id=message.from_user.id)
    if users != None:
        browser = webdriver.Chrome(r'C:\Users\user\Downloads/chromedriver.exe')
        await message.answer(text="Выполняется вход в дизель...")
        diesel_upper.sing_in(username=users.username, password=users.password, browser=browser)
        diesel_upper.count_ads_user(browser)
        time.sleep(random.randrange(5))
        a = random.randrange(0, 4)
        diesel_upper.upper(text=text[a], browser=browser)
        await message.answer(text="Ваше объявление Апнуто, спасибо за доверие...")
    else:
        await message.answer(text="Вы не ввели данные для входа в аккаунт.\n\n"
                                  "Перейдите а главное меню и нажмите на 'Площадки для Up объявлений'")





# Up fonksiyon
# __________________________________________________________________________________________________________________
@dp.callback_query_handler(lambda c: c.data == 'ibt1')
async def send_poll(call: CallbackQuery):
    await call.answer(cache_time=60)
    users = await db.diesel_select_user(user_id=call.from_user.id)
    if users == None:
        await call.message.answer(
            text='Введите ваши данные Diesel Elcat kg для дальнейшей работы\n\nВведите username...')
        await call.message.edit_reply_markup()
        await Login_info.first()
    else:
        await call.message.answer(text='Вы уже входили на данную площадку для полной информации зайдите в главное меню в "Мой профиль"')


@dp.callback_query_handler(lambda c: c.data == 'ibt2')
async def send_poll(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(text='Заглушка...')
    await call.message.edit_reply_markup()


@dp.callback_query_handler(lambda c: c.data == 'ibt3')
async def send_poll(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(text='Заглушка...')
    await call.message.edit_reply_markup()


@dp.callback_query_handler(lambda c: c.data == 'ibt4')
async def send_poll(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(text='Заглушка...')
    await call.message.edit_reply_markup()


@dp.message_handler(text='Площадки для Up объявлений')
async def rate(message: types.Message):
    await message.answer('Выберите площадку для UP', reply_markup=imp1)
    await message.answer(reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=Login_info.q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if len(answer) <= 20:
        await state.update_data(answer1=answer)
        await message.answer(text="Введите password...")
        await Login_info.next()
    else:
        await message.answer(text="В username символов должно быть меньше 20...")
        await Login_info.first()


@dp.message_handler(state=Login_info.q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer_1 = data.get("answer1")
    answer_2 = message.text
    if len(answer_2) <= 20:
        if True:
            try:
                await message.answer(text="Выполняется вход в дизель...")
                browser = webdriver.Chrome(r'C:\Users\user\Downloads/chromedriver.exe')
                diesel_upper.sing_in(username=answer_1, password=answer_2, browser=browser)
                if diesel_upper.sing_in_check(browser) == True:
                    diesel_upper.count_ads_user(browser=browser)
                    browser.close()
                    browser.quit()
                    await message.answer(text=f'Вход в Diesel был успешен.\n\nВсего объявлений - {len(diesel_upper.user_ads_links)}')
                    await db.add_diesel_data(username=answer_1, password=answer_2, user_id=message.from_user.id)
                    await message.answer(
                        text=f"Ваши данные занесены в базу данных\n\nusername {answer_1}")
                    await state.finish()
                else:
                    browser.close()
                    browser.quit()
                    await message.answer(
                        text='Неправильно ввели логин или пароль пожалуйста перейдите на https://diesel.elcat.kg/ проверьте и введите обратно точные данные...')
                    await state.finish()
            except Exception as ex:
                print(ex)
    else:
        await message.answer(text="В password символов должно быть меньше 20...")
        await Login_info.q2()






# Profile functions
# ________________________________________________________________________________________________________________________________________
@dp.callback_query_handler(lambda c: c.data == 'edit_diesel')
async def edit_diesel_profile(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup()
    await call.message.answer(
        text='Введите ваши данные Diesel Elcat kg\n\nВведите username...', reply_markup=ReplyKeyboardRemove())
    await Login_info.first()

@dp.message_handler(state=Update_login_info.ques1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if len(answer) <= 20:
        await state.update_data(answer1=answer)
        await message.answer(text="Введите password...")
        await Login_info.next()
    else:
        await message.answer(text="В username символов должно быть меньше 20...")
        await Update_login_info.ques1()


@dp.message_handler(state=Update_login_info.ques2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer_1 = data.get("answer1")
    answer_2 = message.text
    if len(answer_2) <= 20:
        if True:
            try:
                await message.answer(text="Выполняется вход в дизель...")
                browser = webdriver.Chrome(r'C:\Users\user\Downloads/chromedriver.exe')
                diesel_upper.sing_in(username=answer_1, password=answer_2, browser=browser)
                time.sleep(5)
                if diesel_upper.sing_in_check(browser) == True:
                    diesel_upper.count_ads_user(browser=browser)
                    browser.close()
                    browser.quit()
                    await message.answer(text=f'Вход в Diesel был успешен.\n\nВсего объявлений - {len(diesel_upper.user_ads_links)}')
                    await db.update_disel_user(user_id=message.from_user.id, username=answer_1, password=answer_2)
                    await message.answer(
                        text=f"Ваши данные занесены в базу данных\n\nusername {answer_1}")
                    await state.finish()
                else:
                    browser.close()
                    browser.quit()
                    await message.answer(
                        text='Неправильно ввели логин или пароль пожалуйста перейдите на https://diesel.elcat.kg/ проверьте и введите обратно точные данные...')
                    await state.finish()
            except Exception as ex:
                print(ex)
    else:
        await message.answer(text="В password символов должно быть меньше 20...")
        await Update_login_info.ques2()



@dp.callback_query_handler(lambda c: c.data == 'cancel')
async def edit_cancel(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup()
    await call.message.answer(text='Вы отменили редактирование...', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text=f"Мой Профиль {emoji.emojize(':man_office_worker:')}")
async def my_profile(message: types.Message):
    await message.answer(text='Доступные площадки', reply_markup=prof_btns)
    await Profile_choose.first()



@dp.message_handler(state=Profile_choose.main_menu)
async def choose_profile(message: types.Message, state=FSMContext):
    ans = message.text

    if ans == 'Назад':
        await message.answer(text='Главное меню', reply_markup=mp1)
        await state.finish()

    elif ans == 'Diesel Elcat kg':
        users = await db.diesel_select_user(user_id=message.from_user.id)
        if users == None:
            await message.answer(
                "Ваш профиль пуст.\nПожалуйста зайдите в главное меню и в разделе 'Площадки для Up объявлений' войдите в нужную площадку объявлений...")
        else:
            await message.answer(text=f"Ваш профиль\n\nusername {users.username}", reply_markup=edit_diesel_profiles)
            await state.finish()

    elif ans == 'Lalafo kg':
        await message.answer(text='Заглушка...')

    elif ans == 'Bazar kg':
        await message.answer(text='Заглушка...')

    elif ans == 'Mashina kg':
        await message.answer(text='Заглушка...')

    else:
        await state.finish()
        await message.answer(text="Я вас не понял...", reply_markup=mp1)