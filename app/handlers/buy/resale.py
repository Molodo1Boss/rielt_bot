#resale.py
import re
from aiogram import Router, F, Bot, Dispatcher
from dotenv import load_dotenv
import os
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import CallbackQuery
from app.keyboards import keyboards as kb
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from database.database_manager import AsyncDatabaseManager
import asyncio
from aiomysql import Pool
from aiogram.types import Message
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.exceptions import AiogramError
import aiohttp
from aiogram.types.input_media_photo import InputMediaPhoto
from aiogram import types

loop = asyncio.get_event_loop()
db_manager = AsyncDatabaseManager(loop=loop, host='localhost',
                                  user='nmarket', password='10021999', database='your_database')


db_pool: Pool = None


async def create_db_pool(db_manager, loop):
    try:
        if not db_manager.is_pool_created():
            print("Пул соединений не инициализирован. Попытка создания.")
            await loop.run_in_executor(None, db_manager.create_pool)
        else:
            print("Пул соединений уже был инициализирован.")

        if not db_manager.pool:
            print("Уже существующее соединение, пропускаем создание пула.")
        else:
            print("Пул соединений успешно инициализирован.")

        return db_manager.pool
    except Exception as e:
        print(f"Ошибка при создании пула соединений: {e}")
        return None


router_resale = Router()
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(storage=storage, db=db_manager, loop=loop)


class Resale_filter(StatesGroup):
    region = State()
    rooms_count = State()
    area_from = State()
    area_up_to = State()
    floor = State()
    repair = State()
    toilet = State()
    balcony = State()
    Price_from = State()
    Price_up_to = State()
    complete = State()
    current_index = State()


class RegionCallback(CallbackData, prefix="region"):
    action: str
    value: Optional[str] = None


class CountRoom(CallbackData, prefix="CountRoom"):
    action: str
    value: Optional[str] = None


date_messages = {}


@router_resale.message(F.text == "/start")
async def start(message: Message):
    user_id = message.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []
    await message.answer(f"Добро пожаловать @{message.from_user.username}", reply_markup=kb.main, parse_mode='HTML')
    sent_message = (await message.answer(f"Это официальный бот канала @nedvkrasnodar\n"
                                         f"Здесь вы можете подобрать квартиру по вашему запросу",
                                         reply_markup=kb.start_kb)).message_id


@router_resale.callback_query(F.data == 'resale_apt')
async def resale(callback:CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []
    await callback.answer()
    builder = InlineKeyboardBuilder()

    builder.button(text='Москва', callback_data=RegionCallback(action='region', value='Москва'))
    builder.button(text='Санкт-Петербург', callback_data=RegionCallback(action='region', value='Санкт-Петербург'))
    builder.button(text='Краснодар', callback_data=RegionCallback(action='region', value='Краснодар'))
    builder.button(text='Ростов-на-Дону', callback_data=RegionCallback(action='region', value='Ростов-на-Дону'))
    builder.button(text='Черноморское побережье', callback_data=RegionCallback(action='region',
                                                                               value='Черноморское побережье'))
    builder.button(text='Крым', callback_data=RegionCallback(action='region', value='Крым'))
    builder.button(text='Калининград', callback_data=RegionCallback(action='region', value='Калининград'))
    builder.button(text='Казань', callback_data=RegionCallback(action='region', value='Казань'))
    builder.button(text='Ижевск', callback_data=RegionCallback(action='region', value='Ижевск'))
    builder.button(text='Екатеринбург', callback_data=RegionCallback(action='region', value='Екатеринбург'))
    builder.button(text='Владимир', callback_data=RegionCallback(action='region', value='Владимир'))
    builder.button(text='Киров', callback_data=RegionCallback(action='region', value='Киров'))
    builder.button(text='Липецк', callback_data=RegionCallback(action='region', value='Липецк'))
    builder.button(text='Нижний Новгород', callback_data=RegionCallback(action='region', value='Нижний Новгород'))
    builder.button(text='Новосибирск', callback_data=RegionCallback(action='region', value='Новосибирск'))
    builder.button(text='Пенза', callback_data=RegionCallback(action='region', value='Пенза'))
    builder.button(text='Пермь', callback_data=RegionCallback(action='region', value='Пермь'))
    builder.button(text='Воронеж', callback_data=RegionCallback(action='region', value='Воронеж'))
    builder.button(text='Самара', callback_data=RegionCallback(action='region', value='Самара'))
    builder.button(text='Уфа', callback_data=RegionCallback(action='region', value='Уфа'))
    builder.button(text='Челябинск', callback_data=RegionCallback(action='region', value='Челябинск'))
    builder.button(text='Дальний Восток', callback_data=RegionCallback(action='region', value='Дальний Восток'))

    builder.adjust(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)  # Устанавливаем количество кнопок в каждой строке

    print("Запущена FSM 'Ресейл'")
    sent_message = (await callback.message.answer(f'Выберите регион поиска:',
                                                  reply_markup=builder.as_markup(resize_keyboard=True))).message_id
    date_messages[user_id].append(sent_message)
    await state.set_state(Resale_filter.rooms_count)


@router_resale.callback_query(RegionCallback.filter(), Resale_filter.rooms_count)
async def rooms_count(callback_query: types.CallbackQuery, callback_data: CountRoom, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.button(text='Студия', callback_data=CountRoom(action='count_room', value='СТ'))
    builder.button(text='1', callback_data=CountRoom(action='count_room', value=' 1К '))
    builder.button(text='2', callback_data=CountRoom(action='count_room', value=' 2К '))
    builder.button(text='3', callback_data=CountRoom(action='count_room', value=' 3К '))
    builder.button(text='4', callback_data=CountRoom(action='count_room', value=' 4К '))
    builder.button(text='5', callback_data=CountRoom(action='count_room', value=' 5К '))
    builder.button(text='6', callback_data=CountRoom(action='count_room', value=' 6К '))
    builder.adjust(1, 2, 2, 2, 2)  # Устанавливаем количество кнопок в каждой строке
    await callback_query.answer(f'Выбран регион {callback_data.value}')
    await callback_query.message.edit_text(f'Выберите количество комнат:', reply_markup=builder.as_markup())
    await state.update_data(region=callback_data.value)
    data = await state.get_data()
    print(f"В стейт region записано значение: {data.get('region')}")
    await state.set_state(Resale_filter.area_from)


@router_resale.callback_query(CountRoom.filter(), Resale_filter.area_from)
async def area_from(callback_query: types.CallbackQuery, callback_data: CountRoom, state: FSMContext):
    await callback_query.answer(f'Выбрано количество комнат: {callback_data.value}')
    await callback_query.message.edit_text(f'Введите площадь от:')
    await state.update_data(rooms_count=callback_data.value)
    data = await state.get_data()
    print(f"В стейт rooms_count записано значение: {data.get('rooms_count')}")
    await state.set_state(Resale_filter.area_up_to)


@router_resale.message(Resale_filter.area_up_to)
async def area_up_to(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []
    await bot.delete_message(message_id=message.message_id, chat_id=message.from_user.id)
    messages = date_messages[user_id]
    for message1 in messages:
        await bot.edit_message_text(f'Введите площадь квартиры в <b>м²</b>\n'f'До:', parse_mode='HTML',
                                    chat_id=message.from_user.id, message_id=message1)
    await state.update_data(area_from=f"{message.text}")
    data = await state.get_data()
    print(f"В стейт area_from записано значение: {data.get('area_from')}")
    await state.set_state(Resale_filter.floor)


@router_resale.message(Resale_filter.floor)
async def floor(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []
    await bot.delete_message(message_id=message.message_id, chat_id=message.from_user.id)
    messages = date_messages[user_id]
    for message1 in messages:
        await bot.edit_message_text(f'Введите этаж: ', parse_mode='HTML',
                                    chat_id=message.from_user.id, message_id=message1)
    await state.update_data(area_up_to=f'{message.text}')
    data = await state.get_data()
    print(f"В стейт area_up_to записано значение: {data.get('area_up_to')}")
    await state.set_state(Resale_filter.repair)


@router_resale.message(Resale_filter.repair)
async def repair(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []
    await bot.delete_message(message_id=message.message_id, chat_id=message.from_user.id)
    messages = date_messages[user_id]
    for message1 in messages:
        await bot.edit_message_text(f'Выберите тип ремонта: ', parse_mode='HTML',
                                    chat_id=message.from_user.id, message_id=message1, reply_markup=kb.repair)
    await state.update_data(floor=message.text)
    data = await state.get_data()
    print(f"В стейт floor записано значение: {data.get('floor')}")
    await state.set_state(Resale_filter.toilet)


@router_resale.callback_query(F.data == 'With_repair_from_user', Resale_filter.toilet)
async def With_repair_from_user(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(f'Выбран ремонт от собственника')
    user_id = callback_query.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []
    await callback_query.message.edit_text(f'Выберите тип санузла:', reply_markup=kb.bath)
    await state.update_data(repair=' С ремонтом собственника ')
    data = await state.get_data()
    print(f"В стейт repair записано значение: {data.get('repair')}")
    await state.set_state(Resale_filter.balcony)


@router_resale.callback_query(F.data == 'with', Resale_filter.balcony)
async def with_repair(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(f'Выбран тип санузла: "Cовмещенный"')
    user_id = callback_query.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []
    await callback_query.message.edit_text(f'Выберите наличие балкона:', reply_markup=kb.balcony)
    await state.update_data(toilet='  совмещенный ')
    data = await state.get_data()
    print(f"В стейт toilet записано значение: {data.get('toilet')}")
    await state.set_state(Resale_filter.Price_up_to)


@router_resale.callback_query(F.data == 'balcony_have', Resale_filter.Price_up_to)
async def balcony_have(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(f'Выбран тип санузла: "Cовмещенный"')
    user_id = callback_query.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []
    await callback_query.message.edit_text(f'Введите бюджет до:', reply_markup=kb.price)
    await state.update_data(balcony=' Есть ')
    data = await state.get_data()
    print(f"В стейт balcony записано значение: {data.get('balcony')}")
    await state.set_state(Resale_filter.Price_up_to)


@router_resale.callback_query(F.data == 'any_price', Resale_filter.Price_up_to)
async def any_price(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(f'Выбран бюджет без ограничений')
    await state.update_data(Price_up_to='999 999 999  ₽')
    user_id = callback_query.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []
    data = await state.get_data()
    await callback_query.message.edit_text(f'Давайте перепроверим данные:\n\n'
                                           f'Регион: {data.get("region")}\n'
                                           f'Количество комнат: {"rooms_count"}\n'
                                           f'Площадь от: {data.get("area_from")}\n'
                                           f'Площадь до: {data.get("area_up_to")}\n'
                                           f'Этаж: {data.get("floor")}\n'
                                           f'Тип ремонта: {data.get("repair")}\n'
                                           f'Тип сан узла: {data.get("toilet")}\n'
                                           f'Балкон: {data.get("balcony")}\n'
                                           f'Бюджет: {data.get("Price_up_to")}\n', reply_markup=kb.complete_buy)
    print(f"В стейт Price_up_to записано значение: {data.get('Price_up_to')}")


@router_resale.callback_query(F.data == 'complete_buy_search')
async def search_properties(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    data = await state.get_data()
    user_id = callback_query.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []

    try:
        # Инициализация пула соединений через метод объекта db_manager
        if not db_manager.is_pool_created():
            print("Пул соединений не инициализирован. Попытка создания.")
            await db_manager.create_pool()
            if not db_manager.is_pool_created():
                print("Ошибка: db_manager.pool не инициализирован.")
                await callback_query.message.answer("Пожалуйста, повторите запрос позже.")
                return
            else:
                print("Пул соединений успешно инициализирован.")
        else:
            print("Пул соединений уже был инициализирован.")

        async with db_manager.pool.acquire() as conn:
            try:
                # Получаем текущий индекс из состояния
                current_index_data = await state.get_data()
                current_index = current_index_data.get('current_index', 0)
                async with conn.cursor() as cursor:
                    def extract_numeric_area(area_str):
                        try:
                            cleaned_str = ''.join(char for char in area_str if char.isdigit())
                            return int(cleaned_str) if cleaned_str else None
                        except ValueError:
                            # Если возникает ошибка при преобразовании, вернем None
                            return None

                    # Преобразование цены пользователя
                    user_price = extract_numeric_area(data.get('Price_up_to'))
                    print(f"user_price: {user_price}")

                    # Блок кода для поиска в базе данных
                    area_from = extract_numeric_area(data.get('area_from'))
                    area_up_to = extract_numeric_area(data.get('area_up_to'))

                    # Инициализируем sql строкой, чтобы избежать ошибки "local variable 'sql' referenced before assignment"

                    sql = ""

                    if area_from is not None and area_up_to is not None and user_price is not None:
                        try:
                            sql += f"SELECT * FROM `{data.get('region')}` "
                            sql += f"WHERE rooms LIKE %s "  # Обновленная строка
                            sql += f"AND {area_from} <= CAST(SUBSTRING_INDEX(total_area, ' ', 1) AS DECIMAL(10,2)) "
                            sql += f"AND CAST(SUBSTRING_INDEX(total_area, ' ', 1) AS DECIMAL(10,2)) <= {area_up_to} "
                            sql += f"AND ("
                            sql += f"    CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(`floor`, '/', 1), ' ', 1) AS SIGNED) = %s "
                            sql += f"    OR "
                            sql += f"    CAST(SUBSTRING_INDEX(`floor`, ' ', 1) AS SIGNED) = %s "
                            sql += f"    OR "
                            sql += (f"    CAST(SUBSTRING_INDEX(SUBSTRING_INDEX("
                                    f"`floor`, '/', -1), ' ', 1) AS SIGNED) = %s ")
                            sql += f"    OR "
                            sql += f"    CAST(SUBSTRING_INDEX(`floor`, ' ', -1) AS SIGNED) = %s OR `floor` IS NULL"
                            sql += f") "
                            sql += f"AND repair_type = %s "
                            sql += f"AND bathroom = %s "
                            sql += f"AND balcony = %s "
                            sql += f"AND CAST(SUBSTRING_INDEX(`floor`, '/', -1) AS SIGNED) = %s "
                            sql += f"AND `floor` IS NOT NULL AND `floor` != 'None' "
                            sql += f"AND total_price <= %s"

                            # Добавим логирование SQL-запроса
                            print(f"SQL Query: {sql}")

                            if sql.strip() == "":
                                raise ValueError("SQL Query is empty")

                            # Передаем значения параметров в execute
                            parameters = (
                                f"{data.get('rooms_count')}%",
                                int(data.get('floor')),
                                int(data.get('floor')),
                                int(data.get('floor')),
                                int(data.get('floor')),
                                data.get('repair'),
                                data.get('toilet'),
                                data.get('balcony'),
                                int(data.get('floor')),
                                user_price
                            )

                            print(f"Parameters: {parameters}")

                            await cursor.execute(sql, parameters)

                            # Переменная для хранения результатов запроса
                            results = await cursor.fetchall()
                            global count_reluts
                            count_reluts = len(results)
                            print(f"количество найденых объявлений: {count_reluts}")

                            # Проверяем, есть ли следующее объявление
                            if current_index < len(results):
                                result = results[current_index]

                                # Обновляем состояние с новым индексом
                                await state.update_data(current_index=current_index)
                                data = await state.get_data()
                                print(current_index)
                                print(data.get('current_index'))

                                id_anct = result[0]
                                await state.update_data(ids=id_anct)
                                print(f'Значение в переменной id_anct: {id_anct}')
                                data = await state.get_data()
                                print(f"Сохраненные айди показанных объявлений: {data.get('ids')}")
                                # Получаем значения из столбиков image_1, image_2, image_3, image_4, image_5, image_6
                                image_urls = [
                                    result[3],
                                    result[4],
                                    result[5],
                                    result[6],
                                    result[7],
                                    result[8]
                                ]

                                # Проверяем, есть ли хотя бы одна рабочая ссылка
                                if any(url and url.startswith('http') for url in image_urls):
                                    # Формируем подпись с остальной информацией
                                    description = result[25][:500] if result[25] else ""
                                    caption = (f"Адрес: {result[9]}\n\n"
                                               f"Общая площадь:{result[11]}\n"
                                               f"Площадь кухни:{result[12]}\n"
                                               f"Количество комнат:{result[13]}\n"
                                               f"Балкон:{result[14]}\n"
                                               f"Санузел:{result[15]}\n"
                                               f"Этаж: {result[10]}\n"
                                               f"Тип ремонта:{result[16]}\n"
                                               f"Тип дома:{result[17]}\n"
                                               f"Тип лифта:{result[18]}\n"
                                               f"Договор:{result[21]}\n"
                                               f"Тип сделки:{result[22]}\n"
                                               f"Материнский капитал:{result[23]}\n\n"
                                               f"Описание:{description}\n\n"
                                               f"Цена: {result[19]} ({result[20]})\n")

                                    # Формируем медиагруппу
                                    album_builder = MediaGroupBuilder(caption=caption)

                                    # Добавляем непустые и рабочие изображения в медиагруппу
                                    for url in image_urls:
                                        if url and url.startswith('http'):
                                            try:
                                                async with aiohttp.ClientSession() as session:
                                                    async with session.head(url) as resp:
                                                        # Проверяем, что ответ содержит изображение (Content-Type: image/*)
                                                        if resp.content_type.startswith('image'):
                                                            album_builder.add(type="photo", media=url)
                                            except Exception as e:
                                                print(f"Ошибка при проверке типа изображения: {e}")

                                    try:
                                        # Отправляем медиагруппу
                                        sent_message = (await bot.send_media_group(
                                            chat_id=callback_query.message.chat.id,
                                            media=album_builder.build(),
                                        ))
                                        date_messages[user_id] = [sent_message[i].message_id for i in
                                                                  range(len(sent_message))]

                                        print(date_messages[user_id])

                                    except AiogramError as photo_error:
                                        print(f"Ошибка при отправке медиагруппы: {photo_error}")
                                        # Если возникла ошибка, отправляем только текстовое сообщение
                                        await callback_query.answer(caption)
                                else:
                                    # Если нет рабочих ссылок, отправляем только caption
                                    caption = (f"Адрес: {result[9]}\n\n"
                                               f"Общая площадь:{result[11]}\n"
                                               f"Площадь кухни:{result[12]}\n"
                                               f"Количество комнат:{result[13]}\n"
                                               f"Балкон:{result[14]}\n"
                                               f"Санузел:{result[15]}\n"
                                               f"Этаж: {result[10]}\n"
                                               f"Тип ремонта:{result[16]}\n"
                                               f"Тип дома:{result[17]}\n"
                                               f"Тип лифта:{result[18]}\n"
                                               f"Договор:{result[21]}\n"
                                               f"Тип сделки:{result[22]}\n"
                                               f"Материнский капитал:{result[23]}\n\n"
                                               f"Описание:{result[25]}\n\n"
                                               f"Цена: {result[19]} ({result[20]})\n")
                                    await bot.send_message(callback_query.message.chat.id,
                                                           caption)

                            # После отправки 10 строк отправим клавиатуру
                            await callback_query.message.answer("ᅠ ᅠ ", reply_markup=kb.keyboard_menu)

                        except Exception as e:
                            # Обработка ошибок
                            print(f"Ошибка: {e}")
                    else:
                        await callback_query.answer("Нет подходящих объявлений. Попробуйте изменить критерии поиска.")
            except Exception as e:
                # Обработка ошибок внутри блока try
                print(f"Ошибка внутри блока try: {e}")
                await callback_query.answer("Пожалуйста, повторите запрос позже.")
    except Exception as e:
        # Обработка ошибок внутри блока try
        print(f"Ошибка внутри блока try: {e}")
        await callback_query.answer("Пожалуйста, повторите запрос позже.")


@router_resale.callback_query(F.data == 'next_show_more')
async def next_show_more(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()

    # Проверяем, инициализирован ли пул соединений
    if db_manager.pool is None:
        print("Пул соединений не инициализирован. Попытка создания.")
        await create_db_pool()
        if db_manager.pool is None:
            print("Ошибка: db_manager.pool не инициализирован.")
            return

    try:
        # Получаем текущий индекс из состояния
        current_index_data = await state.get_data()
        current_index = current_index_data.get('current_index', 0)

        # Обновляем состояние с новым индексом
        await state.update_data(current_index=current_index + 1)

        # Получаем данные из обновленного состояния
        updated_data = await state.get_data()
        updated_index = updated_data.get('current_index', 0)

        print(updated_index)

        async with db_manager.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                data = await state.get_data()

                def extract_numeric_area(area_str):
                    try:
                        cleaned_str = ''.join(char for char in area_str if char.isdigit())
                        return int(cleaned_str) if cleaned_str else None
                    except ValueError:
                        # Если возникает ошибка при преобразовании, вернем None
                        return None

                # Преобразование цены пользователя
                user_price = extract_numeric_area(data.get('Price_up_to'))
                print(f"user_price: {user_price}")

                # Блок кода для поиска в базе данных
                area_from = extract_numeric_area(data.get('area_from'))
                area_up_to = extract_numeric_area(data.get('area_up_to'))

                # Инициализируем sql строкой, чтобы избежать ошибки "local variable 'sql' referenced before assignment"
                sql = ""

                if area_from is not None and area_up_to is not None and user_price is not None:
                    try:
                        sql += f"SELECT * FROM `{data.get('region')}` "
                        sql += f"WHERE rooms LIKE %s "  # Обновленная строка
                        sql += f"AND {area_from} <= CAST(SUBSTRING_INDEX(total_area, ' ', 1) AS DECIMAL(10,2)) "
                        sql += f"AND CAST(SUBSTRING_INDEX(total_area, ' ', 1) AS DECIMAL(10,2)) <= {area_up_to} "
                        sql += f"AND ("
                        sql += f"    CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(`floor`, '/', 1), ' ', 1) AS SIGNED) = %s "
                        sql += f"    OR "
                        sql += f"    CAST(SUBSTRING_INDEX(`floor`, ' ', 1) AS SIGNED) = %s "
                        sql += f"    OR "
                        sql += f"    CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(`floor`, '/', -1), ' ', 1) AS SIGNED) = %s "
                        sql += f"    OR "
                        sql += f"    CAST(SUBSTRING_INDEX(`floor`, ' ', -1) AS SIGNED) = %s OR `floor` IS NULL"
                        sql += f") "
                        sql += f"AND repair_type = %s "
                        sql += f"AND bathroom = %s "
                        sql += f"AND balcony = %s "
                        sql += f"AND CAST(SUBSTRING_INDEX(`floor`, '/', -1) AS SIGNED) = %s "
                        sql += f"AND `floor` IS NOT NULL AND `floor` != 'None' "
                        sql += f"AND total_price <= %s"

                        # Добавим логирование SQL-запроса
                        print(f"SQL Query: {sql}")

                        if sql.strip() == "":
                            raise ValueError("SQL Query is empty")

                        # Передаем значения параметров в execute
                        parameters = (
                            f"{data.get('rooms_count')}%",
                            int(data.get('floor')),
                            int(data.get('floor')),
                            int(data.get('floor')),
                            int(data.get('floor')),
                            data.get('repair'),
                            data.get('toilet'),
                            data.get('balcony'),
                            int(data.get('floor')),
                            user_price
                        )

                        print(f"Parameters: {parameters}")

                        await cursor.execute(sql, parameters)

                        # Переменная для хранения результатов запроса
                        results = await cursor.fetchall()

                        # Проверяем, есть ли следующее объявление
                        if updated_index < len(results):

                            result = results[updated_index]
                            print(updated_index)

                            id_anct = result[0]
                            await state.update_data(ids=id_anct)
                            print(f'Значение в переменной id_anct: {id_anct}')
                            data = await state.get_data()
                            print(f"Сохраненные айди показанных объявлений: {data.get('ids')}")
                            # Получаем значения из столбиков image_1, image_2, image_3, image_4, image_5, image_6
                            image_urls = [
                                result[3],
                                result[4],
                                result[5],
                                result[6],
                                result[7],
                                result[8]
                            ]

                            # Проверяем, есть ли хотя бы одна рабочая ссылка
                            if any(url and url.startswith('http') for url in image_urls):
                                max_caption_length = 500

                                # Получаем описание из результата запроса
                                description = result[25]

                                # Обрезаем описание, если оно превышает максимальную длину
                                truncated_description = description[:max_caption_length]

                                # Формируем подпись с остальной информацией, включая обрезанное описание
                                caption = (f"Адрес: {result[9]}\n\n"
                                           f"Общая площадь:{result[11]}\n"
                                           f"Площадь кухни:{result[12]}\n"
                                           f"Количество комнат:{result[13]}\n"
                                           f"Балкон:{result[14]}\n"
                                           f"Санузел:{result[15]}\n"
                                           f"Этаж: {result[10]}\n"
                                           f"Тип ремонта:{result[16]}\n"
                                           f"Тип дома:{result[17]}\n"
                                           f"Тип лифта:{result[18]}\n"
                                           f"Договор:{result[21]}\n"
                                           f"Тип сделки:{result[22]}\n"
                                           f"Материнский капитал:{result[23]}\n\n"
                                           f"Описание:{truncated_description}\n\n"
                                           f"Цена: {result[19]} ({result[20]})\n")

                                user_id = callback_query.from_user.id
                                # Добавляем непустые и рабочие изображения в медиагруппу
                                for index, url in enumerate(image_urls):
                                    if url and url.startswith('http'):
                                        try:
                                            async with aiohttp.ClientSession() as session:
                                                async with session.head(url) as resp:
                                                    # Проверяем, что ответ содержит изображение (Content-Type: image/*)
                                                    if resp.content_type.startswith('image'):
                                                        # Проверяем, не является ли новое изображение таким же, как текущее
                                                        if index < len(date_messages[user_id]) and url == \
                                                                date_messages[user_id][index]:
                                                            # Если так, продолжаем следующую итерацию цикла
                                                            continue

                                        except Exception as e:
                                            print(f"Ошибка при проверке типа изображения: {e}")

                                try:

                                    # Редактируем медиагруппу
                                    user_id = callback_query.from_user.id
                                    messages = date_messages[user_id]
                                    caption_id = messages[0]

                                    for index, message_id in enumerate(messages):
                                        if index < len(image_urls):
                                            await bot.edit_message_media(media=InputMediaPhoto(media=image_urls[index]),
                                                                         chat_id=callback_query.from_user.id,
                                                                         message_id=message_id)

                                    await bot.edit_message_caption(caption=caption, chat_id=user_id,
                                                                   message_id=caption_id)

                                    # Редактируем подпись
                                    # await bot.edit_message_caption(caption=caption, chat_id=user_id, message_id=caption_id)

                                    # Проверяем, достиг ли пользователь последнего объявления
                                    if updated_index == len(results):
                                        await callback_query.answer("Это последнее объявление по вашему запросу.",
                                                                    show_alert=True)

                                except AiogramError as photo_error:
                                    print(f"Ошибка при отправке медиагруппы: {photo_error}")
                                    # Если возникла ошибка, отправляем только текстовое сообщение
                                    # await bot.send_message(callback_query.from_user.id, caption)
                        else:
                            await callback_query.answer('Это последнее объявление по вашему запросу',
                                                        show_alert=True)

                    except Exception as e:
                        # Обработка ошибок
                        print(f"Ошибка: {e}")
                        await callback_query.answer(user_id=callback_query.from_user.id,
                                                    text="Произошла ошибка при получении данных."
                                                         " Пожалуйста, попробуйте еще раз.")
                else:
                    await callback_query.answer("Нет подходящих объявлений. Попробуйте изменить критерии поиска.")

    # Предложение начать заново или выполнить другие действия
    except Exception as e:
        # Обработка ошибок
        print(f"Ошибка: {e}")
        await callback_query.answer(user_id=callback_query.from_user.id,
                                    text="Произошла ошибка при выполнении операции. Пожалуйста, попробуйте еще раз.")


@router_resale.callback_query(F.data == 'back_show_more')
async def next_show_more(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()

    # Проверяем, инициализирован ли пул соединений
    if db_manager.pool is None:
        print("Пул соединений не инициализирован. Попытка создания.")
        await create_db_pool()
        if db_manager.pool is None:
            print("Ошибка: db_manager.pool не инициализирован.")
            return

    try:
        # Получаем текущий индекс из состояния
        current_index_data = await state.get_data()
        current_index = current_index_data.get('current_index', 0)

        if current_index > 0:
            # Обновляем состояние с новым индексом
            await state.update_data(current_index=current_index - 1)

            # Получаем данные из обновленного состояния
            updated_data = await state.get_data()
            updated_index = updated_data.get('current_index', 0)

            print(updated_index)
            async with db_manager.pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    data = await state.get_data()

                    def extract_numeric_area(area_str):
                        try:
                            cleaned_str = ''.join(char for char in area_str if char.isdigit())
                            return int(cleaned_str) if cleaned_str else None
                        except ValueError:
                            # Если возникает ошибка при преобразовании, вернем None
                            return None

                    # Преобразование цены пользователя
                    user_price = extract_numeric_area(data.get('Price_up_to'))
                    print(f"user_price: {user_price}")

                    # Блок кода для поиска в базе данных
                    area_from = extract_numeric_area(data.get('area_from'))
                    area_up_to = extract_numeric_area(data.get('area_up_to'))

                # Инициализируем sql строкой, чтобы избежать ошибки "local variable 'sql' referenced before assignment"
                    sql = ""

                    if area_from is not None and area_up_to is not None and user_price is not None:
                        try:
                            sql += f"SELECT * FROM `{data.get('region')}` "
                            sql += f"WHERE rooms LIKE %s "  # Обновленная строка
                            sql += f"AND {area_from} <= CAST(SUBSTRING_INDEX(total_area, ' ', 1) AS DECIMAL(10,2)) "
                            sql += f"AND CAST(SUBSTRING_INDEX(total_area, ' ', 1) AS DECIMAL(10,2)) <= {area_up_to} "
                            sql += f"AND ("
                            sql += f"    CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(`floor`, '/', 1), ' ', 1) AS SIGNED) = %s "
                            sql += f"    OR "
                            sql += f"    CAST(SUBSTRING_INDEX(`floor`, ' ', 1) AS SIGNED) = %s "
                            sql += f"    OR "
                            sql += (f"    CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(`floor`,"
                                    f" '/', -1), ' ', 1) AS SIGNED) = %s ")
                            sql += f"    OR "
                            sql += f"    CAST(SUBSTRING_INDEX(`floor`, ' ', -1) AS SIGNED) = %s OR `floor` IS NULL"
                            sql += f") "
                            sql += f"AND repair_type = %s "
                            sql += f"AND bathroom = %s "
                            sql += f"AND balcony = %s "
                            sql += f"AND CAST(SUBSTRING_INDEX(`floor`, '/', -1) AS SIGNED) = %s "
                            sql += f"AND `floor` IS NOT NULL AND `floor` != 'None' "
                            sql += f"AND total_price <= %s"

                            # Добавим логирование SQL-запроса
                            print(f"SQL Query: {sql}")

                            if sql.strip() == "":
                                raise ValueError("SQL Query is empty")

                            # Передаем значения параметров в execute
                            parameters = (
                                f"{data.get('rooms_count')}%",  # Обновленное значение
                                int(data.get('floor')),
                                int(data.get('floor')),
                                int(data.get('floor')),
                                int(data.get('floor')),
                                data.get('repair'),
                                data.get('toilet'),
                                data.get('balcony'),
                                int(data.get('floor')),
                                user_price
                            )

                            print(f"Parameters: {parameters}")

                            await cursor.execute(sql, parameters)

                            # Переменная для хранения результатов запроса
                            results = await cursor.fetchall()

                            # Проверяем, есть ли следующее объявление
                            if updated_index < len(results):
                                result = results[updated_index]
                                print(updated_index)
                                id_anct = result[0]
                                await state.update_data(ids=id_anct)
                                print(f'Значение в переменной id_anct: {id_anct}')
                                data = await state.get_data()
                                print(f"Сохраненные айди показанных объявлений: {data.get('ids')}")
                                # Получаем значения из столбиков image_1, image_2, image_3, image_4, image_5, image_6
                                image_urls = [
                                    result[3],
                                    result[4],
                                    result[5],
                                    result[6],
                                    result[7],
                                    result[8]
                                ]

                                # Проверяем, есть ли хотя бы одна рабочая ссылка
                                if any(url and url.startswith('http') for url in image_urls):
                                    max_caption_length = 500

                                    # Получаем описание из результата запроса
                                    description = result[25]

                                    # Обрезаем описание, если оно превышает максимальную длину
                                    truncated_description = description[:max_caption_length]

                                    # Формируем подпись с остальной информацией, включая обрезанное описание
                                    caption = (f"Адрес: {result[9]}\n\n"
                                               f"Общая площадь:{result[11]}\n"
                                               f"Площадь кухни:{result[12]}\n"
                                               f"Количество комнат:{result[13]}\n"
                                               f"Балкон:{result[14]}\n"
                                               f"Санузел:{result[15]}\n"
                                               f"Этаж: {result[10]}\n"
                                               f"Тип ремонта:{result[16]}\n"
                                               f"Тип дома:{result[17]}\n"
                                               f"Тип лифта:{result[18]}\n"
                                               f"Договор:{result[21]}\n"
                                               f"Тип сделки:{result[22]}\n"
                                               f"Материнский капитал:{result[23]}\n\n"
                                               f"Описание:{truncated_description}\n\n"
                                               f"Цена: {result[19]} ({result[20]})\n")

                                    user_id = callback_query.from_user.id
                                    # Добавляем непустые и рабочие изображения в медиагруппу
                                    for index, url in enumerate(image_urls):
                                        if url and url.startswith('http'):
                                            try:
                                                async with aiohttp.ClientSession() as session:
                                                    async with session.head(url) as resp:
                                                    # Проверяем, что ответ содержит изображение (Content-Type: image/*)
                                                        if resp.content_type.startswith('image'):
                                                            # Проверяем, не является ли новое изображение таким же, как текущее
                                                            if index < len(date_messages[user_id]) and url == \
                                                                    date_messages[user_id][index]:
                                                                # Если так, продолжаем следующую итерацию цикла
                                                                continue

                                            except Exception as e:
                                                print(f"Ошибка при проверке типа изображения: {e}")

                                    try:

                                        # Редактируем медиагруппу
                                        user_id = callback_query.from_user.id
                                        messages = date_messages[user_id]
                                        caption_id = messages[0]

                                        for index, message_id in enumerate(messages):
                                            if index < len(image_urls):
                                                await bot.edit_message_media(media=InputMediaPhoto(
                                                    media=image_urls[index]),
                                                    chat_id=callback_query.from_user.id,
                                                    message_id=message_id)

                                        await bot.edit_message_caption(caption=caption, chat_id=user_id,
                                                                       message_id=caption_id)
                                        # Проверяем, достиг ли пользователь первого объявления
                                        if updated_index == 0:
                                            await callback_query.answer("Это первое объявление по вашему запросу.",
                                                                        show_alert=True)

                                    except AiogramError as photo_error:
                                        print(f"Ошибка при отправке медиагруппы: {photo_error}")
                                        # Если возникла ошибка, отправляем только текстовое сообщение
                                        # await bot.send_message(callback_query.from_user.id, caption)
                                    else:
                                        pass

                        except Exception as e:
                            # Обработка ошибок
                            print(f"Ошибка: {e}")
                            await callback_query.answer(user_id=callback_query.from_user.id,
                                                        text="Произошла ошибка при получении данных."
                                                             " Пожалуйста, попробуйте еще раз.")
                    else:
                        # Пользователь достиг первого объявления
                        await callback_query.answer("Это первое объявление по вашему запросу.",
                                                    show_alert=True)
        else:
            await callback_query.answer('это последнее объявление')
    # Предложение начать заново или выполнить другие действия
    except Exception as e:
        # Обработка ошибок
        print(f"Ошибка: {e}")
        await callback_query.answer(user_id=callback_query.from_user.id,
                                    text="Произошла ошибка при выполнении операции. Пожалуйста, попробуйте еще раз.")


# Обработчик для предыдущего объявления
# @router_resale.callback_query(F.data == 'back_show_more')
# async def back_show_more(callback_query: types.CallbackQuery, state: FSMContext):
#     await callback_query.answer()
#
#     # Проверяем, инициализирован ли пул соединений
#     if db_manager.pool is None:
#         print("Пул соединений не инициализирован. Попытка создания.")
#         await create_db_pool()
#         if db_manager.pool is None:
#             print("Ошибка: db_manager.pool не инициализирован.")
#             return
#
#     try:
#         # Получаем текущий индекс из состояния
#         current_index_data = await state.get_data()
#         current_index = current_index_data.get('current_index', 0)
#
#         # Проверяем, чтобы индекс не был отрицательным
#         if current_index > 0:
#             # Уменьшаем индекс на 1
#             await state.update_data(current_index=current_index - 1)
#
#             # Получаем данные из обновленного состояния
#             updated_data = await state.get_data()
#             updated_index = updated_data.get('current_index', 0)
#
#             print(updated_index)
#
#             async with db_manager.pool.acquire() as conn:
#                 async with conn.cursor() as cursor:
#                     # Выполняем SQL-запрос SELECT для таблицы Краснодар
#                     sql = "SELECT * FROM Краснодар"
#                     await cursor.execute(sql)
#
#                     # Получаем строки из результата запроса
#                     results = await cursor.fetchall()
#
#                     # Получаем данные по новому индексу
#                     result = results[updated_index]
#                     print(updated_index)
#
#                     # Обновляем состояние с новым индексом
#                     # await state.update_data(current_index=current_index - 1)
#
#                     # Ваш код для вывода объявления...
#                     id_anct = result[0]
#                     await state.update_data(ids=id_anct)
#                     print(f'Значение в переменной id_anct: {id_anct}')
#                     data = await state.get_data()
#                     print(f"Сохраненные айди показанных объявлений: {data.get('ids')}")
#                     # Получаем значения из столбиков image_1, image_2, image_3, image_4, image_5, image_6
#                     image_urls = [
#                         result[3],
#                         result[4],
#                         result[5],
#                         result[6],
#                         result[7],
#                         result[8]
#                     ]
#
#                     # Проверяем, есть ли хотя бы одна рабочая ссылка
#                     if any(url and url.startswith('http') for url in image_urls):
#                         max_caption_length = 500
#
#                         # Получаем описание из результата запроса
#                         description = result[25]
#
#                         # Обрезаем описание, если оно превышает максимальную длину
#                         truncated_description = description[:max_caption_length]
#
#                         # Формируем подпись с остальной информацией, включая обрезанное описание
#                         caption = (f"Адрес: {result[9]}\n\n"
#                                    f"Общая площадь:{result[11]}\n"
#                                    f"Площадь кухни:{result[12]}\n"
#                                    f"Количество комнат:{result[13]}\n"
#                                    f"Балкон:{result[14]}\n"
#                                    f"Санузел:{result[15]}\n"
#                                    f"Тип ремонта:{result[16]}\n"
#                                    f"Тип дома:{result[17]}\n"
#                                    f"Тип лифта:{result[18]}\n"
#                                    f"Договор:{result[21]}\n"
#                                    f"Тип сделки:{result[22]}\n"
#                                    f"Материнский капитал:{result[23]}\n\n"
#                                    f"Описание:{truncated_description}\n\n"
#                                    f"Цена: {result[19]} ({result[20]})\n")
#
#                         user_id = callback_query.from_user.id
#                         # Добавляем непустые и рабочие изображения в медиагруппу
#                         for index, url in enumerate(image_urls):
#                             if url and url.startswith('http'):
#                                 try:
#                                     async with aiohttp.ClientSession() as session:
#                                         async with session.head(url) as resp:
#                                             # Проверяем, что ответ содержит изображение (Content-Type: image/*)
#                                             if resp.content_type.startswith('image'):
#                                                 # Проверяем, не является ли новое изображение таким же, как текущее
#                                                 if index < len(date_messages.get(user_id, [])) and url == \
#                                                         date_messages.get(user_id, [])[index]:
#                                                     # Если так, продолжаем следующую итерацию цикла
#                                                     continue
#
#                                 except Exception as e:
#                                     print(f"Ошибка при проверке типа изображения: {e}")
#
#                         try:
#                             # Редактируем медиагруппу
#                             user_id = callback_query.from_user.id
#                             messages = date_messages.get(user_id, [])
#                             caption_id = date_messages[user_id][0]
#
#                             for index, message_id in enumerate(messages):
#                                 if index < len(image_urls):
#                                     await bot.edit_message_media(media=InputMediaPhoto(media=image_urls[index]),
#                                                                  chat_id=user_id,
#                                                                  message_id=message_id)
#
#                             await bot.edit_message_caption(caption=caption, chat_id=user_id, message_id=caption_id)
#
#                         except AiogramError as photo_error:
#                             print(f"Ошибка при отправке медиагруппы: {photo_error}")
#
#                     else:
#                         max_caption_length = 500
#
#                         # Получаем описание из результата запроса
#                         description = result[25]
#
#                         # Обрезаем описание, если оно превышает максимальную длину
#                         truncated_description = description[:max_caption_length]
#
#                         # Формируем подпись с остальной информацией, включая обрезанное описание
#                         caption = (f"Адрес: {result[9]}\n\n"
#                                    f"Общая площадь:{result[11]}\n"
#                                    f"Площадь кухни:{result[12]}\n"
#                                    f"Количество комнат:{result[13]}\n"
#                                    f"Балкон:{result[14]}\n"
#                                    f"Санузел:{result[15]}\n"
#                                    f"Тип ремонта:{result[16]}\n"
#                                    f"Тип дома:{result[17]}\n"
#                                    f"Тип лифта:{result[18]}\n"
#                                    f"Договор:{result[21]}\n"
#                                    f"Тип сделки:{result[22]}\n"
#                                    f"Материнский капитал:{result[23]}\n\n"
#                                    f"Описание:{truncated_description}\n\n"
#                                    f"Цена: {result[19]} ({result[20]})\n")
#                         await bot.send_message(callback_query.from_user.id, caption)
#         else:
#             await callback_query.answer('Это первое объявление', show_alert=True)
#
#     except Exception as e:
#         # Обработка ошибок
#         print(f"Ошибка: {e}")
#         await callback_query.answer(text="Произошла ошибка при получении данных. Пожалуйста, попробуйте еще раз.",
#                                     show_alert=True)
#
#
# @router_resale.message(F.text == "/show2")
# async def cmd_album(message: Message):
#     album_builder = MediaGroupBuilder(
#         caption="Общая подпись для будущего альбома"
#     )
#     media1 = "https://cdn.nmarket.pro/resale/996452a6-a44d-4b64-99ff-0f82c3c8045e.jpeg"
#     album_builder.add(
#         type="photo",
#         media=media1
#         # caption="Подпись к конкретному медиа"
#
#     )
#     # Если мы сразу знаем тип, то вместо общего add
#     # можно сразу вызывать add_<тип>
#     album_builder.add_photo(
#         # Для ссылок или file_id достаточно сразу указать значение
#         media="https://cdn.nmarket.pro/resale/996452a6-a44d-4b64-99ff-0f82c3c8045e.jpeg"
#     )
#     album_builder.add_photo(
#         media="https://cdn.nmarket.pro/resale/996452a6-a44d-4b64-99ff-0f82c3c8045e.jpeg"
#     )
#     await message.answer_media_group(
#         # Не забудьте вызвать build()
#         media=album_builder.build()
#     )
#
# class Show(StatesGroup):
#     ids = State()
#     current_index = State()
#
#
# delete_messages = {}
# date_captions = {}
#
#
# @router_resale.message(F.text == "show")
# async def show_all_data(message: Message, state: FSMContext):
#     await message.answer(f'запущен просмотр всех объявлений, нажмите /show')
#     await state.set_state(Show.ids)



# @router_resale.message(F.text == "/show", Show.ids)
# async def show_all_data(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     # Проверяем, инициализирован ли пул соединений
#     if db_manager.pool is None:
#         print("Пул соединений не инициализирован. Попытка создания.")
#         await create_db_pool()
#         if db_manager.pool is None:
#             print("Ошибка: db_manager.pool не инициализирован.")
#             return
#
#     try:
#         # Получаем текущий индекс из состояния
#         current_index_data = await state.get_data()
#         current_index = current_index_data.get('current_index', 0)
#
#         async with db_manager.pool.acquire() as conn:
#             async with conn.cursor() as cursor:
#                 # Выполняем SQL-запрос SELECT для таблицы Краснодар
#                 sql = "SELECT * FROM Краснодар"
#                 await cursor.execute(sql)
#
#                 # Получаем строки из результата запроса
#                 results = await cursor.fetchall()
#
#                 # Проверяем, есть ли следующее объявление
#                 if current_index < len(results):
#                     result = results[current_index]
#
#                     # Обновляем состояние с новым индексом
#                     await state.update_data(current_index=current_index)
#                     data = await state.get_data()
#                     print(current_index)
#                     print(data.get('current_index'))
#
#                     # Ваш существующий код для вывода объявления
#                     id_anct = result[0]
#                     await state.update_data(ids=id_anct)
#                     print(f'Значение в переменной id_anct: {id_anct}')
#                     data = await state.get_data()
#                     print(f"Сохраненные айди показанных объявлений: {data.get('ids')}")
#                     # Получаем значения из столбиков image_1, image_2, image_3, image_4, image_5, image_6
#                     image_urls = [
#                         result[3],
#                         result[4],
#                         result[5],
#                         result[6],
#                         result[7],
#                         result[8]
#                     ]
#
#                     # Проверяем, есть ли хотя бы одна рабочая ссылка
#                     if any(url and url.startswith('http') for url in image_urls):
#                         # Формируем подпись с остальной информацией
#                         description = result[25][:500] if result[25] else ""
#                         caption = (f"Адрес: {result[9]}\n\n"
#                                    f"Общая площадь:{result[11]}\n"
#                                    f"Площадь кухни:{result[12]}\n"
#                                    f"Количество комнат:{result[13]}\n"
#                                    f"Балкон:{result[14]}\n"
#                                    f"Санузел:{result[15]}\n"
#                                    f"Тип ремонта:{result[16]}\n"
#                                    f"Тип дома:{result[17]}\n"
#                                    f"Тип лифта:{result[18]}\n"
#                                    f"Договор:{result[21]}\n"
#                                    f"Тип сделки:{result[22]}\n"
#                                    f"Материнский капитал:{result[23]}\n\n"
#                                    f"Описание:{description}\n\n"
#                                    f"Цена: {result[19]} ({result[20]})\n")
#
#                         # Формируем медиагруппу
#                         album_builder = MediaGroupBuilder(caption=caption)
#
#                         # Добавляем непустые и рабочие изображения в медиагруппу
#                         for url in image_urls:
#                             if url and url.startswith('http'):
#                                 try:
#                                     async with aiohttp.ClientSession() as session:
#                                         async with session.head(url) as resp:
#                                             # Проверяем, что ответ содержит изображение (Content-Type: image/*)
#                                             if resp.content_type.startswith('image'):
#                                                 album_builder.add(type="photo", media=url)
#                                 except Exception as e:
#                                     print(f"Ошибка при проверке типа изображения: {e}")
#
#                         try:
#
#                             # Отправляем медиагруппу
#
#                             sent_message = (await bot.send_media_group(
#                                 chat_id=message.chat.id,
#                                 media=album_builder.build(),
#                             ))
#                             date_messages[user_id] = [sent_message[i].message_id for i in range(len(sent_message))]
#
#                             print(date_messages[user_id])
#
#
#                         except AiogramError as photo_error:
#                             print(f"Ошибка при отправке медиагруппы: {photo_error}")
#                             # Если возникла ошибка, отправляем только текстовое сообщение
#                             await message.answer(caption)
#                     else:
#                         # Если нет рабочих ссылок, отправляем только caption
#                         caption = (f"Адрес: {result[9]}\n\n"
#                                    f"Общая площадь:{result[11]}\n"
#                                    f"Площадь кухни:{result[12]}\n"
#                                    f"Количество комнат:{result[13]}\n"
#                                    f"Балкон:{result[14]}\n"
#                                    f"Санузел:{result[15]}\n"
#                                    f"Тип ремонта:{result[16]}\n"
#                                    f"Тип дома:{result[17]}\n"
#                                    f"Тип лифта:{result[18]}\n"
#                                    f"Договор:{result[21]}\n"
#                                    f"Тип сделки:{result[22]}\n"
#                                    f"Материнский капитал:{result[23]}\n\n"
#                                    f"Описание:{result[25]}\n\n"
#                                    f"Цена: {result[19]} ({result[20]})\n")
#                         await message.answer(caption)
#
#                     # После отправки 10 строк отправим клавиатуру
#                     await message.answer("ᅠ ᅠ ", reply_markup=kb.keyboard_menu)
#
#     except Exception as e:
#         # Обработка ошибок
#         print(f"Ошибка: {e}")
#         await message.answer("Произошла ошибка при получении данных. Пожалуйста, попробуйте еще раз.")


@router_resale.callback_query(F.data == 'next_show_more1')
async def next_show_more1(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    # Проверяем, инициализирован ли пул соединений
    if db_manager.pool is None:
        print("Пул соединений не инициализирован. Попытка создания.")
        await create_db_pool()
        if db_manager.pool is None:
            print("Ошибка: db_manager.pool не инициализирован.")
            return

    try:
        # Получаем текущий индекс из состояния
        current_index_data = await state.get_data()
        current_index = current_index_data.get('current_index', 0)

        # Обновляем состояние с новым индексом
        await state.update_data(current_index=current_index + 1)

        # Получаем данные из обновленного состояния
        updated_data = await state.get_data()
        updated_index = updated_data.get('current_index', 0)

        print(updated_index)

        async with db_manager.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                data = await state.get_data()

                def extract_numeric_area(area_str):
                    try:
                        cleaned_str = ''.join(char for char in area_str if char.isdigit())
                        return int(cleaned_str) if cleaned_str else None
                    except ValueError:
                        # Если возникает ошибка при преобразовании, вернем None
                        return None

                # Преобразование цены пользователя
                user_price = extract_numeric_area(data.get('Price_up_to'))
                print(f"user_price: {user_price}")

                # Блок кода для поиска в базе данных
                area_from = extract_numeric_area(data.get('area_from'))
                area_up_to = extract_numeric_area(data.get('area_up_to'))

                # Инициализируем sql строкой, чтобы избежать ошибки "local variable 'sql' referenced before assignment"
                sql = ""

                if area_from is not None and area_up_to is not None and user_price is not None:
                    try:
                        sql += f"SELECT * FROM `{data.get('region')}` "
                        sql += f"WHERE rooms LIKE %s "  # Обновленная строка
                        sql += f"AND {area_from} <= CAST(SUBSTRING_INDEX(total_area, ' ', 1) AS DECIMAL(10,2)) "
                        sql += f"AND CAST(SUBSTRING_INDEX(total_area, ' ', 1) AS DECIMAL(10,2)) <= {area_up_to} "
                        sql += f"AND ("
                        sql += f"    CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(`floor`, '/', 1), ' ', 1) AS SIGNED) = %s "
                        sql += f"    OR "
                        sql += f"    CAST(SUBSTRING_INDEX(`floor`, ' ', 1) AS SIGNED) = %s "
                        sql += f"    OR "
                        sql += f"    CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(`floor`, '/', -1), ' ', 1) AS SIGNED) = %s "
                        sql += f"    OR "
                        sql += f"    CAST(SUBSTRING_INDEX(`floor`, ' ', -1) AS SIGNED) = %s OR `floor` IS NULL"
                        sql += f") "
                        sql += f"AND repair_type = %s "
                        sql += f"AND bathroom = %s "
                        sql += f"AND balcony = %s "
                        sql += f"AND CAST(SUBSTRING_INDEX(`floor`, '/', -1) AS SIGNED) = %s "
                        sql += f"AND `floor` IS NOT NULL AND `floor` != 'None' "
                        sql += f"AND total_price <= %s"

                        # Добавим логирование SQL-запроса
                        print(f"SQL Query: {sql}")

                        if sql.strip() == "":
                            raise ValueError("SQL Query is empty")

                        # Передаем значения параметров в execute
                        parameters = (
                            f"{data.get('rooms_count')}%",
                            int(data.get('floor')),
                            int(data.get('floor')),
                            int(data.get('floor')),
                            int(data.get('floor')),
                            data.get('repair'),
                            data.get('toilet'),
                            data.get('balcony'),
                            int(data.get('floor')),
                            user_price
                        )

                        print(f"Parameters: {parameters}")

                        await cursor.execute(sql, parameters)

                        # Переменная для хранения результатов запроса
                        results = await cursor.fetchall()

                        # Проверяем, есть ли следующее объявление
                        if updated_index < len(results):

                            result = results[updated_index]
                            print(updated_index)

                            id_anct = result[0]
                            await state.update_data(ids=id_anct)
                            print(f'Значение в переменной id_anct: {id_anct}')
                            data = await state.get_data()
                            print(f"Сохраненные айди показанных объявлений: {data.get('ids')}")
                            # Получаем значения из столбиков image_1, image_2, image_3, image_4, image_5, image_6
                            image_urls = [
                                result[3],
                                result[4],
                                result[5],
                                result[6],
                                result[7],
                                result[8]
                            ]

                            # Проверяем, есть ли хотя бы одна рабочая ссылка
                            if any(url and url.startswith('http') for url in image_urls):
                                max_caption_length = 500

                                # Получаем описание из результата запроса
                                description = result[25]

                                # Обрезаем описание, если оно превышает максимальную длину
                                truncated_description = description[:max_caption_length]

                                # Формируем подпись с остальной информацией, включая обрезанное описание
                                caption = (f"Адрес: {result[9]}\n\n"
                                           f"Общая площадь:{result[11]}\n"
                                           f"Площадь кухни:{result[12]}\n"
                                           f"Количество комнат:{result[13]}\n"
                                           f"Балкон:{result[14]}\n"
                                           f"Санузел:{result[15]}\n"
                                           f"Этаж: {result[10]}\n"
                                           f"Тип ремонта:{result[16]}\n"
                                           f"Тип дома:{result[17]}\n"
                                           f"Тип лифта:{result[18]}\n"
                                           f"Договор:{result[21]}\n"
                                           f"Тип сделки:{result[22]}\n"
                                           f"Материнский капитал:{result[23]}\n\n"
                                           f"Описание:{truncated_description}\n\n"
                                           f"Цена: {result[19]} ({result[20]})\n")

                                user_id = callback_query.from_user.id
                                # Добавляем непустые и рабочие изображения в медиагруппу
                                for index, url in enumerate(image_urls):
                                    if url and url.startswith('http'):
                                        try:
                                            async with aiohttp.ClientSession() as session:
                                                async with session.head(url) as resp:
                                                    # Проверяем, что ответ содержит изображение (Content-Type: image/*)
                                                    if resp.content_type.startswith('image'):
                                                        # Проверяем, не является ли новое изображение таким же, как текущее
                                                        if index < len(date_messages[user_id]) and url == \
                                                                date_messages[user_id][index]:
                                                            # Если так, продолжаем следующую итерацию цикла
                                                            continue

                                        except Exception as e:
                                            print(f"Ошибка при проверке типа изображения: {e}")

                                try:

                                    # Редактируем медиагруппу
                                    user_id = callback_query.from_user.id
                                    messages = date_messages[user_id]
                                    caption_id = messages[0]

                                    for index, message_id in enumerate(messages):
                                        if index < len(image_urls):
                                            await bot.edit_message_media(media=InputMediaPhoto(media=image_urls[index]),
                                                                         chat_id=callback_query.from_user.id,
                                                                         message_id=message_id)

                                    await bot.edit_message_caption(caption=caption, chat_id=user_id,
                                                                   message_id=caption_id)

                                    # Редактируем подпись
                                    # await bot.edit_message_caption(caption=caption, chat_id=user_id, message_id=caption_id)

                                    # Проверяем, достиг ли пользователь последнего объявления
                                    if updated_index == len(results):
                                        await callback_query.answer("Это последнее объявление по вашему запросу.",
                                                                    show_alert=True)

                                except AiogramError as photo_error:
                                    print(f"Ошибка при отправке медиагруппы: {photo_error}")
                                    # Если возникла ошибка, отправляем только текстовое сообщение
                                    # await bot.send_message(callback_query.from_user.id, caption)
                        else:
                            await callback_query.answer('Это последнее объявление по вашему запросу',
                                                        show_alert=True)

                    except Exception as e:
                        # Обработка ошибок
                        print(f"Ошибка: {e}")
                        await callback_query.answer(user_id=callback_query.from_user.id,
                                                    text="Произошла ошибка при получении данных."
                                                         " Пожалуйста, попробуйте еще раз.")

    # Предложение начать заново или выполнить другие действия
    except Exception as e:
        # Обработка ошибок
        print(f"Ошибка: {e}")
        await callback_query.answer(user_id=callback_query.from_user.id,
                                    text="Произошла ошибка при выполнении операции. Пожалуйста, попробуйте еще раз.")