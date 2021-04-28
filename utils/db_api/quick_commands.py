from asyncpg import UniqueViolationError

from utils.db_api.Schemas import User, Diesel_data

async def add_diesel_data(username: str,
                          password: str,
                          user_id: int):
    try:
        diesel_datas = Diesel_data(username=username, password=password, user_id=user_id)
        await diesel_datas.create()
    except UniqueViolationError:
        pass

async def diesel_select_user(user_id: int):
    users = await Diesel_data.query.where(Diesel_data.user_id == user_id).gino.first()
    return users

async def update_disel_user(user_id: int, username: str, password: str):
    user = await Diesel_data.query.where(user_id=user_id)
    users_n = await Diesel_data.get(id=user.id)
    await users_n.update(username=username, password=password).apply()






# Profile
# ____________________________________________________________________________________
async def add_user(id: int,
                   username: str,
                   language: str = None,
                   name: str = None,
                   gender: int = None,
                   age: int = None,
                   number: int = None):
    try:
        user = User(id=id, username=username, language=language, name=name, gender=gender, age=age, number=number)
        await user.create()
    except UniqueViolationError:
        pass

async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user




async def update_user_language(id, language):
    user = await User.get(id)
    await user.update(language=language).apply()

async def update_profile_name(id, name):
    user = await User.get(id)
    await user.update(name=name).apply()

async def update_profile_gender(id, gender):
    user = await User.get(id)
    await user.update(gender=gender).apply()

async def update_profile_age(id, age):
    user = await User.get(id)
    await user.update(age=age).apply()

async def update_profile_number(id, number):
    user = await User.get(id)
    await user.update(number=number).apply()