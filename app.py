import asyncio

from aiogram import executor

from loader import dp, db
from utils.db_api import db_gino
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify

async def on_startup(dispatcher):
    # Уведомляет про запуск
    await db_gino.on_starup(dispatcher)
    await asyncio.sleep(10)
    await db.gino.create_all()

    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)