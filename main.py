# main.py
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from app.handlers.buy.resale import router_resale, create_db_pool
from database.database_manager import AsyncDatabaseManager

logging.basicConfig(level=logging.INFO)

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
loop = asyncio.get_event_loop()  # Добавьте эту строку


async def create_db_manager(loop):
    try:
        db_manager = AsyncDatabaseManager(
            loop=loop,
            host='localhost',
            user='nmarket',
            password='10021999',
            database='your_database'
        )

        if not db_manager.is_pool_created():
            await db_manager.create_pool()  # Инициализация пула соединений
            await db_manager.initialize()
            await db_manager.connect()

        return db_manager
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


async def start_bot(dp, db_manager):
    if db_manager is None:
        print("Ошибка: db_manager не инициализирован.")
        return
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage, db=db_manager, loop=loop)
    dp.include_router(router_resale)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    db_manager = loop.run_until_complete(create_db_manager(loop))
    if db_manager:
        loop.run_until_complete(create_db_pool(db_manager, loop))  # Передаем db_manager и loop
        dp = Dispatcher()
        loop.run_until_complete(start_bot(dp, db_manager))
        loop.run_forever()
