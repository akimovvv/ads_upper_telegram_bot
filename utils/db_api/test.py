import asyncio

from data import config
from utils.db_api.db_gino import db
import quick_commands


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    # await db.gino.create_all()
    # print("adding usres...")
    # # #
    # #
    # await quick_commands.add_user(id=718078109, username='zafasd')
    # await quick_commands.add_user(id=718078109,
    #                               username='123',
    #                               name='baha',
    #                               gender=0,
    #                               age=23,
    #                               number=772429242)
    # # await quick_commands.add_user(3, '3', gender=1, age=99)
    # # print("ready...")
    #
    # await quick_commands.add_diesel_data(user_id=718078109, password='1234123', username='dmmadmoad')
    # users = await quick_commands.diesel_select_user(user_id=718078109)
    # print(f'selected this {users.password}')
loop = asyncio.get_event_loop()
loop.run_until_complete(test())