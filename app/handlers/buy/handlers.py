# from aiogram import Router, F, Bot, Dispatcher
# from aiogram.types import Message
# from app.keyboards import keyboards as kb
# from app.keyboards.Rostov import keyboards_rostov, rostov_rent as kb
# from app.keyboards.krasnodar import keyboards_krasnodar as kb
# # from app.keyboards.krasnodar import keyboards_rent as kb
# from app.keyboards import keyboards as kb
# from dotenv import load_dotenv
# import os
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import CallbackQuery
# from aiogram import types
#
#
# router = Router()
# form_router = Router()
# load_dotenv()
# bot = Bot(os.getenv('TOKEN'))
# storage = MemoryStorage()
# dp = Dispatcher()
#
#
# # @router.message(F.text == "/start")
# # async def start(message: Message):
# #     await message.answer(f"Добро пожаловать @{message.from_user.username}",reply_markup=kb.main, parse_mode='HTML')
# #     await message.answer(f"Это официальный бот канала @nedvkrasnodar\n"
# #                          f"Здесь вы можете подобрать квартиру по вашему запросу",reply_markup=kb.inquiry)
#
#
#
#
#
# @router.message(F.text == "/menu")
# async def start(message: Message):
#     await message.answer(f"Добро пожаловать @{message.from_user.username}",reply_markup=kb.main, parse_mode='HTML')
#     await message.answer(f"Это официальный бот канала @nedvkrasnodar\n"
#                          f"Здесь вы можете подобрать квартиру по вашему запросу",reply_markup=kb.inquiry)
#
#
# class Show_buy(StatesGroup):
#
#     region = State()
#     region_edit = State()
#
#
#     rooms_count = State()
#     rooms_count_edit = State()
#
#
#     raion = State()
#     raion_edit = State()
#
#
#     S_ot = State()
#     S_ot_edit = State()
#
#
#     S_do = State()
#     S_do_edit = State()
#
#
#     Floor_build = State()
#     Floor_build_edit = State()
#
#
#     Floor_apt = State()
#     Floor_apt_edit = State()
#
#
#     repair = State()
#     repair_edit = State()
#
#
#     bath = State()
#     bath_edit = State()
#
#
#     balcony = State()
#     balcony_edit = State()
#
#     Price = State()
#     Price_edit = State()
#
#
#     complete = State()
#
#
# date_messages = {}
#
#
# @router.callback_query(F.data == 'buy_apt')
# async def buy_apt(callback:CallbackQuery, state: FSMContext):
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await callback.answer()
#     print("Запущена FSM 'Покупка'")
#     sent_message = (await callback.message.answer(f'Выберите регион поиска:',
#                                                   reply_markup=kb.region)).message_id
#     date_messages[user_id].append(sent_message)
#     # await state.set_state(Show_buy.rooms_count)
#
#
# @router.callback_query(F.data == 'Krasnodar_region')
# async def buy_apt(callback:CallbackQuery, state: FSMContext):
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await callback.answer()
#     await state.update_data(region='Краснодарский край')
#     print("Выбран регион 'Краснодарский край'")
#     await callback.message.edit_text(f'Выберите количество комнат:', reply_markup=kb.count_rooms)
#     # await state.set_state(Show_buy.rooms_count)
#
#
# @router.callback_query(F.data == 'Rostov_region')
# async def buy_apt(callback:CallbackQuery, state: FSMContext):
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await callback.answer()
#     await state.update_data(region='Ростовская область')
#     print("Выбран регион 'Ростовская область'")
#     await callback.message.edit_text(f'Выберите количество комнат:', reply_markup=kb.count_rooms)
#     # await state.set_state(Show_buy.rooms_count)
#
#
# @router.callback_query(F.data == 'Moscow_region')
# async def buy_apt(callback:CallbackQuery, state: FSMContext):
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await callback.answer()
#     await state.update_data(region='Московская область')
#     print("Выбран регион 'Московская область'")
#     await callback.message.edit_text(f'Выберите количество комнат:', reply_markup=kb.count_rooms)
#     # await state.set_state(Show_buy.rooms_count)
#
#
# @router.callback_query(F.data == 'Leningrad_region')
# async def buy_apt(callback:CallbackQuery, state: FSMContext):
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await callback.answer()
#     await state.update_data(region='Ленинградская область')
#     print("Выбран регион 'Ленинградская область'")
#     await callback.message.edit_text(f'Выберите количество комнат:', reply_markup=kb.count_rooms)
#     # await state.set_state(Show_buy.rooms_count)
#
#
# @router.callback_query(F.data == 'Krim_region')
# async def buy_apt(callback:CallbackQuery, state: FSMContext):
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await callback.answer()
#     await state.update_data(region='Республика Крым')
#     print("Выбран регион 'Республика Крым'")
#     await callback.message.edit_text(f'Выберите количество комнат:', reply_markup=kb.count_rooms)
#     # await state.set_state(Show_buy.rooms_count)
#
#
# @router.callback_query(F.data == '1', Show_buy.rooms_count)
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     Count_apt = callback.data
#     await state.update_data(rooms_count=Count_apt)
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await state.set_state(Show_buy.raion)
#     await callback.message.edit_text(f'Выберите район:',reply_markup=kb.raion_krd)
#
#
# @router.callback_query(F.data == '2')
# async def count_apt2(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     Count_apt = callback.data
#     await state.update_data(rooms_count=Count_apt)
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await state.set_state(Show_buy.raion)
#     await callback.message.edit_text(f'Выберите район:',reply_markup=kb.raion_krd)
#
#
# @router.callback_query(F.data == '3')
# async def count_apt3(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     Count_apt = callback.data
#     await state.update_data(rooms_count=Count_apt)
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await state.set_state(Show_buy.raion)
#     await callback.message.edit_text(f'Выберите район:',reply_markup=kb.raion_krd)
#
#
# @router.callback_query(F.data == '4')
# async def count_apt4(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     Count_apt = callback.data
#     await state.update_data(rooms_count=Count_apt)
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await state.set_state(Show_buy.raion)
#     await callback.message.edit_text(f'Выберите район:', reply_markup=kb.raion_krd)
#
#
# @router.callback_query(F.data == '0')
# async def count_apt0(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     Count_apt = callback.data
#     await state.update_data(rooms_count=Count_apt)
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}(Студия)")
#     await state.set_state(Show_buy.raion)
#     await callback.message.edit_text(f'Выберите район:',reply_markup=kb.raion_krd)
#
#
# @router.callback_query(F.data == 'any_count_rooms')
# async def any_count_rooms(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count='Любое количество')
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await state.set_state(Show_buy.raion)
#     if data.get('region') == 'Краснодарский край':
#         await callback.message.edit_text(f'Выберите район:', reply_markup=kb.raion_krd)
#     if data.get('region') == 'Ростовская область':
#         await callback.message.edit_text(f'Выбрана Ростовская область', reply_markup=kb.city_krasnodar_region)
#     if data.get('region') == 'Московская область':
#         await callback.message.edit_text(f'Выбрана Московская область')
#     if data.get('region') == 'Ленинградская область':
#         await callback.message.edit_text(f'Выбрана Ленинградская область')
#     if data.get('region') == 'Республика Крым':
#         await callback.message.edit_text(f'Выбрана Республика Крым')
#
#
#
# @router.callback_query(F.data == 'Zapadniy_rajon', Show_buy.raion)
# async def Zapadniy_rajon(callback:CallbackQuery, state: FSMContext):
#     await state.update_data(raion='Западный')
#     data = await state.get_data()
#     print(f"Выбран район: {data.get('raion')}")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML',reply_markup=kb.kvadrat_ot)
#     await state.set_state(Show_buy.S_do)
#
#
# @router.callback_query(F.data == 'Karasun_rajon',Show_buy.raion)
# async def Karasun_rajon(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Карасунский')
#     data = await state.get_data()
#     print(f"Выбран район: {data.get('raion')}")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML',reply_markup=kb.kvadrat_ot)
#     await state.set_state(Show_buy.S_do)
#
#
# @router.callback_query(F.data == 'Prikubanskiy_rajon',Show_buy.raion)
# async def Prikubanskiy_rajon(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Прикубанский')
#     data = await state.get_data()
#     print(f"Выбран район: {data.get('raion')}")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML',reply_markup=kb.kvadrat_ot)
#     await state.set_state(Show_buy.S_do)
#
#
# @router.callback_query(F.data == 'Central_rajon', Show_buy.raion)
# async def Central_rajon(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Центральный')
#     data = await state.get_data()
#     print(f"Выбран район: {data.get('raion')}")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML',reply_markup=kb.kvadrat_ot)
#     await state.set_state(Show_buy.S_do)
#
#
# @router.callback_query(F.data == 'any_raion', Show_buy.raion)
# async def any_raion(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Любой')
#     data = await state.get_data()
#     print(f"Выбран район: {data.get('raion')}")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML',reply_markup=kb.kvadrat_ot)
#     await state.set_state(Show_buy.S_do)
#
#
# @router.message(Show_buy.S_do)
# async def S_do(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     messages = date_messages[user_id]
#     for message1 in messages:
#         await bot.edit_message_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                     f'До:', parse_mode='HTML', chat_id=message.from_user.id, message_id=message1,
#                                     reply_markup=kb.kvadrat_do)
#     await state.update_data(S_ot=message.text)
#     data = await state.get_data()
#     s1 = int(data.get('S_ot'))
#     print(f'Введена площадь от {s1}м²')
#     await bot.delete_message(message_id=message.message_id, chat_id=message.from_user.id)
#     await state.set_state(Show_buy.Floor_build)
#
#
# @router.callback_query(F.data == 'Any_kvadrat_ot')
# async def Any_kvadrat_ot(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(S_ot='Любая')
#     await state.update_data(S_do='Любая')
#     data = await state.get_data()
#     print(f"Введена квадратура от: {data.get('S_ot')}")
#     print(f"Введена квадратура до: {data.get('S_do')}")
#     await callback.message.edit_text('Введите этаж:',reply_markup=kb.floor)
#     await state.set_state(Show_buy.S_do)
#
#
# @router.callback_query(F.data == 'Any_kvadrat_do')
# async def Any_kvadrat_ot(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(S_do=1000)
#     data = await state.get_data()
#     print(f"Введена площадь от: {data.get('S_ot')}")
#     print(f"Введена площадь до: {data.get('S_do')}")
#     await callback.message.edit_text('Введите этаж:', reply_markup=kb.floor)
#     await state.set_state(Show_buy.Floor_build)
#
#
# @router.message(Show_buy.Floor_build)
# async def Floor_build(message: Message, state: FSMContext):
#     await state.update_data(S_do=message.text)
#     data = await state.get_data()
#     print(f"Введена площадь до {data.get('S_do')}м²")
#     await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
#     user_id = message.from_user.id
#     data = await state.get_data()
#     s1 = int(data.get('S_ot'))
#     s2 = int(data.get('S_do'))
#     if s1 > s2:
#         sent_message = (await message.answer(f"Введенная максимальная площадь <b>меньше</b> минимальной\n"
#                                              f"Вы указали площадь от: <b>{data.get('S_ot')}м²</b>\n\n"
#                                              f"Введите корректную максимальную площадь в <b>м²</b> :", parse_mode='HTML',
#                                              reply_markup=kb.edit_kvadrat)).message_id
#     else:
#         if user_id not in date_messages:
#             date_messages[user_id] = []
#         messages = date_messages[user_id]
#         for message1 in messages:
#             await bot.edit_message_text(text='Введите этаж:', chat_id=message.from_user.id,
#                                         message_id=message1, reply_markup=kb.floor)
#             await state.set_state(Show_buy.repair)
#
#
# @router.message(Show_buy.repair)
# async def S_do(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await state.update_data(Floor_build=message.text)
#     await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
#     data = await state.get_data()
#     print(f"Выбран этаж: {data.get('Floor_build')}")
#     messages = date_messages[user_id]
#     for message1 in messages:
#         await bot.edit_message_text(text='Выберите тип ремонта:', reply_markup=kb.repair,
#                                     chat_id=message.from_user.id, message_id=message1)
#
#
# @router.callback_query(F.data == 'Any_floor')
# async def Any_floor(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await state.update_data(Floor_build='Любой')
#     data = await state.get_data()
#     print(f"Выбран этаж: {data.get('Floor_build')}")
#     await state.set_state(Show_buy.repair)
#     await callback.message.edit_text('Выберите тип ремонта:',reply_markup=kb.repair)
#
#
# @router.callback_query(F.data == 'not_first_floor')
# async def Any_floor(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await state.update_data(Floor_build='Любой кроме первого')
#     data = await state.get_data()
#     print(f"Выбран этаж: {data.get('Floor_build')}")
#     await state.set_state(Show_buy.repair)
#     await callback.message.edit_text('Выберите тип ремонта:',reply_markup=kb.repair)
#
#
# @router.callback_query(F.data == 'not_last_floor')
# async def Any_floor(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await state.update_data(Floor_build='Любой кроме последнего')
#     data = await state.get_data()
#     print(f"Выбран этаж: {data.get('Floor_build')}")
#     await state.set_state(Show_buy.repair)
#     await callback.message.edit_text('Выберите тип ремонта:',reply_markup=kb.repair)
#
#
# @router.callback_query(F.data == 'With_repair')
# async def With_repair(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(repair='С ремонтом')
#     data = await state.get_data()
#     print(f"Выбрана категория ремонта:'{data.get('repair')}'")
#     await callback.message.edit_text('Выберите количество санузлов', reply_markup=kb.bath)
#     await state.set_state(Show_buy.balcony)
#
#
# @router.callback_query(F.data == 'Without_repair')
# async def Without_repair(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(repair='Без ремонта')
#     data = await state.get_data()
#     print(f"Выбрана категория ремонта:'{data.get('repair')}'")
#     await callback.message.edit_text('Выберите количество санузлов:', reply_markup=kb.bath)
#     await state.set_state(Show_buy.balcony)
#
#
# @router.callback_query(F.data == 'any_repair')
# async def Without_repair(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(repair='Любой ремонт')
#     data = await state.get_data()
#     print(f"Выбрана категория ремонта:'{data.get('repair')}'")
#     await callback.message.edit_text('Выберите количество санузлов:', reply_markup=kb.bath)
#     await state.set_state(Show_buy.balcony)
#
#
# @router.callback_query(F.data == 'bath_1')
# async def bath_1(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(bath=1)
#     data = await state.get_data()
#     print(f"Выбрано количество санузлов: '{data.get('bath')}'")
#     await callback.message.edit_text('Выберите тип балкона:', reply_markup=kb.balcony)
#     await state.set_state(Show_buy.Price)
#
#
# @router.callback_query(F.data == 'bath_2')
# async def bath_2(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(bath=2)
#     data = await state.get_data()
#     print(f"Выбрано количество санузлов: '{data.get('bath')}'")
#     await callback.message.edit_text('Выберите тип балкона:', reply_markup=kb.balcony)
#     await state.set_state(Show_buy.Price)
#
#
# @router.callback_query(F.data == 'Any_count_bath')
# async def bath_2(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(bath='Любое колличество')
#     data = await state.get_data()
#     print(f"Выбрано количество санузлов: '{data.get('bath')}'")
#     await callback.message.edit_text('Выберите тип балкона:', reply_markup=kb.balcony)
#     await state.set_state(Show_buy.Price)
#
#
# @router.callback_query(F.data == 'balcony_type')
# async def bath_2(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(balcony='Балкон')
#     data = await state.get_data()
#     print(f"Выбрана категория '{data.get('balcony')}'")
#     await callback.message.edit_text('Введите ваш бюджет в рублях:')
#     await state.set_state(Show_buy.Price)
#
#
# @router.callback_query(F.data == 'loggia_type')
# async def loggia_type(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(balcony='Лоджия')
#     data = await state.get_data()
#     print(f"Выбрана категория '{data.get('balcony')}'")
#     await callback.message.edit_text('Введите ваш бюджет в рублях:', reply_markup=kb.price, parse_mode='HTML')
#     await state.set_state(Show_buy.Price)
#
#
# @router.callback_query(F.data == 'Any_balcony_type')
# async def loggia_type(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(balcony='Любой тип')
#     data = await state.get_data()
#     print(f"Выбрана категория '{data.get('balcony')}'")
#     await callback.message.edit_text('Введите ваш бюджет в рублях:', reply_markup=kb.price, parse_mode='HTML')
#     await state.set_state(Show_buy.Price)
#
#
# @router.message(Show_buy.Price)
# async def Price(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#
#     raw_price = message.text
#
#     # Убираем пробелы и знаки препинания из введенной цены
#     raw_price = ''.join(filter(str.isdigit, raw_price))
#
#     # Преобразуем введенное значение в целое число
#     price_value = int(raw_price)
#
#     # Форматирование цены с разделителями между разрядами
#     formatted_price = '{:,}'.format(price_value).replace(',', '.')
#     formatted_price += " ₽"
#
#     # Сохраняем отформатированное значение в state.Price
#     await state.update_data(Price=formatted_price)
#
#     await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
#
#     data = await state.get_data()
#
#     print(f"Введен бюджет: {data.get('Price')}")
#
#     await state.set_state(Show_buy.Price)
#
#     messages = date_messages[user_id]
#
#     for message_id in messages:
#         await bot.edit_message_text(text=f'Давайте перепроверим данные:\n\n'
#                                          f"Регион поиска: <b>{data.get('region')}</b>\n"
#                                          f"Район: <b>{data.get('raion')}</b>\n"
#                                          f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                          f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                          f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                          f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                          f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                          f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                          f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                          f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                     chat_id=message.from_user.id, message_id=message_id,
#                                     reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'any_price')
# async def any_price(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(Price='Не ограничено')
#     data = await state.get_data()
#     print(f"Введен бюджет:'{data.get('Price')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Регион поиска: <b>{data.get('region')}</b>\n"
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>",parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'edit_buy_search')
# async def edit_buy_search(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await callback.message.edit_text(f"Выберите категорию для редактирования:", reply_markup=kb.edit_buy_search)
#
#
# @router.callback_query(F.data == 'raion_edit')
# async def raion_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     data = await state.get_data()
#     print(f"Выбрано редактирование категории: Район")
#     await callback.message.edit_text(f'Выберите район:', reply_markup=kb.raion_edit)
#     await state.set_state(Show_buy.complete)
#
#
# @router.callback_query(F.data == 'Zapadniy_rajon_edit', Show_buy.complete)
# async def Zapadniy_rajon_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Западный')
#     data = await state.get_data()
#     print(f"Введен бюджет:'{data.get('Price')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'Karasun_rajon_edit', Show_buy.complete)
# async def Karasun_rajon_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Карасунский')
#     data = await state.get_data()
#     print(f"Введен бюджет:'{data.get('Price')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'Prikubanskiy_rajon_edit', Show_buy.complete)
# async def Prikubanskiy_rajon_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Прикубанский')
#     data = await state.get_data()
#     print(f"Введен бюджет:'{data.get('Price')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'Central_rajon_edit', Show_buy.complete)
# async def Central_rajon_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Центральный')
#     data = await state.get_data()
#     print(f"Введен бюджет:'{data.get('Price')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'any_raion_edit', Show_buy.complete)
# async def any_raion_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Любой')
#     data = await state.get_data()
#     print(f"Введен бюджет:'{data.get('Price')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'count_rooms_edit')
# async def raion_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Количество комнат")
#     await callback.message.edit_text(f'Выберите количество комнат:',reply_markup=kb.count_rooms_edit)
#     await state.set_state(Show_buy.complete)
#
#
# @router.callback_query(F.data == '1_edit')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count=1)
#     data = await state.get_data()
#     await state.set_state(Show_buy.complete)
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == '2_edit')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count=2)
#     data = await state.get_data()
#     await state.set_state(Show_buy.complete)
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == '3_edit')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count=3)
#     data = await state.get_data()
#     await state.set_state(Show_buy.complete)
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == '4_edit')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count=4)
#     data = await state.get_data()
#     await state.set_state(Show_buy.complete)
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == '0_edit')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count='0 (Студия)')
#     data = await state.get_data()
#     await state.set_state(Show_buy.complete)
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'any_count_rooms_edit')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count='Любое количество')
#     data = await state.get_data()
#     await state.set_state(Show_buy.complete)
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'kvadrat_ot_edit')
# async def kvadrat_ot_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     data = await state.get_data()
#     print(f"Выбрано редактирование категории: Площадь От")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML', reply_markup=kb.kvadrat_ot_edit)
#     await state.set_state(Show_buy.S_ot_edit)
#
#
# @router.message(Show_buy.S_ot_edit)
# async def kvadrat_ot_edit_func(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     await state.update_data(S_ot=message.text)
#     await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
#     data = await state.get_data()
#     print(f"Введена площадь от:'{data.get('S_ot')}'")
#     messages = date_messages[user_id]
#     for message1 in messages:
#         print(message1)
#         await bot.edit_message_text(f'Давайте перепроверим данные:\n\n'
#                                          f"Район: <b>{data.get('raion')}</b>\n"
#                                          f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                          f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                          f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                          f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                          f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                          f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                          f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                          f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                          chat_id=message.from_user.id, message_id=message1,
#                                          reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'Any_kvadrat_ot_edit')
# async def Any_kvadrat_ot_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(S_ot='Любая')
#     data = await state.get_data()
#     await state.set_state(Show_buy.S_ot_edit)
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'kvadrat_do_edit')
# async def kvadrat_do_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     data = await state.get_data()
#     print(f"Выбрано редактирование категории: Площадь До")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'До:', parse_mode='HTML', reply_markup=kb.kvadrat_do_edit)
#     await state.set_state(Show_buy.S_do_edit)
#
#
# @router.message(Show_buy.S_do_edit)
# async def kvadrat_do_edit_func(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     await state.update_data(S_do=message.text)
#     await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
#     data = await state.get_data()
#     print(f"Введена площадь до:'{data.get('S_do')}'")
#     messages = date_messages[user_id]
#     for message1 in messages:
#         print(message1)
#         await bot.edit_message_text(f'Давайте перепроверим данные:\n\n'
#                                          f"Район: <b>{data.get('raion')}</b>\n"
#                                          f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                          f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                          f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                          f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                          f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                          f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                          f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                          f"Бюджет: <b>{data.get('Price')}</b>",
#                                          parse_mode='HTML', chat_id=message.from_user.id, message_id=message1,
#                                          reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'Any_kvadrat_do_edit')
# async def Any_kvadrat_do_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(S_do='Любая')
#     data = await state.get_data()
#     print(f"Введена площадь до:'{data.get('S_do')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'floor_edit')
# async def Any_kvadrat_do_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Этаж")
#     await callback.message.edit_text(f'Введите этаж:', parse_mode='HTML', reply_markup=kb.floor_edit)
#     await state.set_state(Show_buy.Floor_build_edit)
#
#
# @router.message(Show_buy.Floor_build_edit)
# async def Floor_build_edit(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     await state.update_data(Floor_build=message.text)
#     await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
#     data = await state.get_data()
#     print(f"Выбран этаж:'{data.get('Floor_build')}'")
#     messages = date_messages[user_id]
#     for message1 in messages:
#         print(message1)
#         await bot.edit_message_text(f'Давайте перепроверим данные:\n\n'
#                                          f"Район: <b>{data.get('raion')}</b>\n"
#                                          f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                          f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                          f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                          f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                          f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                          f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                          f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                          f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                          chat_id=message.from_user.id, message_id=message1,
#                                          reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'Any_floor_edit')
# async def Any_floor_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(Floor_build='Любой этаж')
#     data = await state.get_data()
#     print(f"Выбран этаж:'{data.get('Floor_build')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'not_first_floor_edit')
# async def not_first_floor_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(Floor_build='Любой, кроме первого')
#     data = await state.get_data()
#     print(f"Введен этаж:'{data.get('Floor_build')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'not_last_floor_edit')
# async def not_last_floor_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(Floor_build='Любой, кроме последнего')
#     data = await state.get_data()
#     print(f"Введен этаж:'{data.get('Floor_build')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'repair_edit')
# async def repair_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Ремонт")
#     await callback.message.edit_text(f'Выберите тип ремонта:', parse_mode='HTML', reply_markup=kb.repair_edit)
#     await state.set_state(Show_buy.repair_edit)
#
#
# @router.callback_query(F.data == 'Without_repair_edit')
# async def Without_repair_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(repair='Без ремонта')
#     data = await state.get_data()
#     print(f"Выбрана категория ремонта:'{data.get('repair')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'With_repair_edit')
# async def With_repair_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(repair='С ремонтом')
#     data = await state.get_data()
#     print(f"Выбрана категория ремонта:'{data.get('repair')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'any_repair_edit')
# async def any_repair_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(repair='Любой')
#     data = await state.get_data()
#     print(f"Выбрана категория ремонта:'{data.get('repair')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'bath_edit')
# async def bath_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Количество санузлов")
#     await callback.message.edit_text('Выберите количество санузлов:', reply_markup=kb.bath_edit)
#     await state.set_state(Show_buy.bath_edit)
#
#
# @router.callback_query(F.data == 'bath_1_edit')
# async def bath_1_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(bath=1)
#     data = await state.get_data()
#     print(f"Выбрано количество санузлов:'{data.get('bath')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'bath_2_edit')
# async def bath_2_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(bath=2)
#     data = await state.get_data()
#     print(f"Выбрано количество санузлов:'{data.get('bath')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'Any_count_bath_edit')
# async def Any_count_bath_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(bath='Любое количество')
#     data = await state.get_data()
#     print(f"Выбрано количество санузлов:'{data.get('bath')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'balcony_edit')
# async def balcony_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Балкон")
#     await callback.message.edit_text('Выберите тип балкона:', reply_markup=kb.balcony_edit)
#     await state.set_state(Show_buy.balcony_edit)
#
#
# @router.callback_query(F.data == 'balcony_type_edit')
# async def balcony_type_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(balcony='Балкон')
#     data = await state.get_data()
#     print(f"Выбрано тип балкона:'{data.get('balcony')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'loggia_type_edit')
# async def loggia_type_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(balcony='Лоджия')
#     data = await state.get_data()
#     print(f"Выбрано тип балкона:'{data.get('balcony')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'Any_balcony_type_edit')
# async def Any_balcony_type_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(balcony='Любой тип')
#     data = await state.get_data()
#     print(f"Выбрано тип балкона:'{data.get('balcony')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.callback_query(F.data == 'price_edit')
# async def price_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Бюджет")
#     await callback.message.edit_text('Введите ваш бюджет в рублях:', reply_markup=kb.price_edit)
#     await state.set_state(Show_buy.Price_edit)
#
#
# @router.callback_query(F.data == 'any_price_edit')
# async def any_price_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(Price='Неограничен')
#     data = await state.get_data()
#     await state.set_state(Show_buy.Price_edit)
#     print(f"Введен бюджет:'{data.get('Price')}'")
#     await callback.message.edit_text(f'Давайте перепроверим данные:\n\n'
#                                      f"Район: <b>{data.get('raion')}</b>\n"
#                                      f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                      f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                      f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                      f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                      f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                      f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                      f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                      f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                      reply_markup=kb.complete_buy)
#
#
# @router.message(Show_buy.Price_edit)
# async def Price_edit(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     raw_price = message.text
#
#     # Убираем пробелы и знаки препинания из введенной цены
#     raw_price = ''.join(filter(str.isdigit, raw_price))
#
#     # Преобразуем введенное значение в целое число
#     price_value = int(raw_price)
#
#     # Форматирование цены с разделителями между разрядами
#     formatted_price = '{:,}'.format(price_value).replace(',', '.')
#     formatted_price += " ₽"
#
#     # Сохраняем отформатированное значение в state.Price
#     await state.update_data(Price=formatted_price)
#     await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
#     data = await state.get_data()
#     print(f"Введен бюджет:'{data.get('Price')}'")
#     messages = date_messages[user_id]
#     for message1 in messages:
#         print(message1)
#         await bot.edit_message_text(f'Давайте перепроверим данные:\n\n'
#                                          f"Район: <b>{data.get('raion')}</b>\n"
#                                          f"Количество комнат: <b>{data.get('rooms_count')}</b>\n"
#                                          f"Площадь квартиры от: <b>{data.get('S_ot')}</b>\n"
#                                          f"Площадь квартиры до: <b>{data.get('S_do')}</b>\n"
#                                          f"Этаж: <b>{data.get('Floor_build')}</b>\n"
#                                          f"Тип ремонта: <b>{data.get('repair')}</b>\n"
#                                          f"Количество санузлов: <b>{data.get('bath')}</b>\n"
#                                          f"Тип балкона: <b>{data.get('balcony')}</b>\n"
#                                          f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                          chat_id=message.from_user.id, message_id=message1,
#                                          reply_markup=kb.complete_buy)