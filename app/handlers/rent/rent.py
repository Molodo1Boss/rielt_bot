# from aiogram import Router, F, Bot, Dispatcher
# from aiogram.types import Message
# from app.keyboards.krasnodar import keyboards_rent as kb
# from dotenv import load_dotenv
# import os
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import CallbackQuery
#
#
# router_rent = Router()
# load_dotenv()
# bot = Bot(os.getenv('TOKEN'))
# storage = MemoryStorage()
# dp = Dispatcher()
#
#
# class Show_rent(StatesGroup):
#
#     region = State()
#     region_edit = State()
#
#
#     rooms = State()
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
#
#
# @router_rent.callback_query(F.data == 'rent_apt')
# async def rent_apt(callback:CallbackQuery, state: FSMContext):
#     # await state.set_state(Show_rent.rooms)
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await callback.answer()
#     print("Запущена FSM 'Аренда'")
#     sent_message = (await callback.message.answer(f'Выберите количество комнат:',
#                                                   reply_markup=kb.count_rooms_rent)).message_id
#     date_messages[user_id].append(sent_message)
#
#
# @router_rent.callback_query(F.data == '1_rent')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     Count_apt = 1
#     await state.update_data(rooms_count=Count_apt)
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')} Аренда")
#     await state.set_state(Show_rent.raion)
#     await callback.message.edit_text(f'Выберите район:',reply_markup=kb.raion_rent)
#
# @router_rent.callback_query(F.data == '2_rent')
# async def count_apt2(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     Count_apt = 2
#     await state.update_data(rooms_count=Count_apt)
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')} Аренда")
#     await state.set_state(Show_rent.raion)
#     await callback.message.edit_text(f'Выберите район:',reply_markup=kb.raion_rent)
#
#
# @router_rent.callback_query(F.data == '3_rent')
# async def count_apt3(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     Count_apt = 3
#     await state.update_data(rooms_count=Count_apt)
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')} Аренда")
#     await state.set_state(Show_rent.raion)
#     await callback.message.edit_text(f'Выберите район:',reply_markup=kb.raion_rent)
#
#
# @router_rent.callback_query(F.data == '4_rent')
# async def count_apt4(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     Count_apt = 4
#     await state.update_data(rooms_count=Count_apt)
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')} Аренда")
#     await state.set_state(Show_rent.raion)
#     await callback.message.edit_text(f'Выберите район:', reply_markup=kb.raion_rent)
#
#
# @router_rent.callback_query(F.data == '0_rent')
# async def count_apt0(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     Count_apt = 0
#     await state.update_data(rooms_count=Count_apt)
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')} Аренда")
#     await state.set_state(Show_rent.raion)
#     await callback.message.edit_text(f'Выберите район:',reply_markup=kb.raion_rent)
#
#
# @router_rent.callback_query(F.data == 'any_count_rooms_rent')
# async def any_count_rooms(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count='Любое колличество Аренда')
#     data = await state.get_data()
#     print(f"Выбрано количество комнат: {data.get('rooms_count')}")
#     await state.set_state(Show_rent.raion)
#     await callback.message.edit_text(f'Выберите район:', reply_markup=kb.raion_rent)
#
#
# @router_rent.callback_query(F.data == 'Zapadniy_rajon_rent', Show_rent.raion)
# async def Zapadniy_rajon(callback:CallbackQuery, state: FSMContext):
#     await state.update_data(raion='Западный')
#     data = await state.get_data()
#     print(f"Выбран район: {data.get('raion')}")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML',reply_markup=kb.kvadrat_ot_rent)
#     await state.set_state(Show_rent.S_do)
#
#
# @router_rent.callback_query(F.data == 'Karasun_rajon_rent',Show_rent.raion)
# async def Karasun_rajon(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Карасунский')
#     data = await state.get_data()
#     print(f"Выбран район: {data.get('raion')}")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML',reply_markup=kb.kvadrat_ot_rent)
#     await state.set_state(Show_rent.S_do)
#
#
# @router_rent.callback_query(F.data == 'Prikubanskiy_rajon_rent', Show_rent.raion)
# async def Prikubanskiy_rajon(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Прикубанский')
#     data = await state.get_data()
#     print(f"Выбран район: {data.get('raion')}")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML',reply_markup=kb.kvadrat_ot_rent)
#     await state.set_state(Show_rent.S_do)
#
#
# @router_rent.callback_query(F.data == 'Central_rajon_rent', Show_rent.raion)
# async def Central_rajon(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Центральный')
#     data = await state.get_data()
#     print(f"Выбран район: {data.get('raion')}")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML',reply_markup=kb.kvadrat_ot_rent)
#     await state.set_state(Show_rent.S_do)
#
#
# @router_rent.callback_query(F.data == 'any_raion_rent', Show_rent.raion)
# async def any_raion(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(raion='Любой')
#     data = await state.get_data()
#     print(f"Выбран район: {data.get('raion')}")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML',reply_markup=kb.kvadrat_ot_rent)
#     await state.set_state(Show_rent.S_do)
#
#
# @router_rent.message(Show_rent.S_do)
# async def S_do1(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     messages = date_messages[user_id]
#     for message1 in messages:
#         await bot.edit_message_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                     f'До:', parse_mode='HTML', chat_id=message.from_user.id, message_id=message1,
#                                     reply_markup=kb.kvadrat_do_rent)
#     await state.update_data(S_ot=message.text)
#     data = await state.get_data()
#     s1 = int(data.get('S_ot'))
#     print(f'Площадь от = {s1}')
#     await bot.delete_message(message_id=message.message_id, chat_id=message.from_user.id)
#     data = await state.get_data()
#     print(data.get('S_ot'))
#     await state.set_state(Show_rent.Floor_build)
#
#
# @router_rent.callback_query(F.data == 'Any_kvadrat_ot_rent')
# async def Any_kvadrat_ot(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(S_ot='Любая')
#     await state.update_data(S_do='Любая')
#     data = await state.get_data()
#     print(f"Введена квадратура от: {data.get('S_ot')}")
#     print(f"Введена квадратура до: {data.get('S_do')}")
#     await callback.message.edit_text('Введите этаж:',reply_markup=kb.floor_rent)
#     await state.set_state(Show_rent.S_do)
#
#
# @router_rent.callback_query(F.data == 'Any_kvadrat_do_rent')
# async def Any_kvadrat_ot(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(S_do=1000)
#     data = await state.get_data()
#     print(f"Введена квадратура от: {data.get('S_ot')}")
#     print(f"Введена квадратура до: {data.get('S_do')}")
#     await callback.message.edit_text('Введите этаж:', reply_markup=kb.floor_rent)
#     await state.set_state(Show_rent.Floor_build)
#
#
# @router_rent.message(Show_rent.Floor_build)
# async def Floor_build(message: Message, state: FSMContext):
#     await state.update_data(S_do=message.text)
#     data = await state.get_data()
#     print(data.get('S_do'))
#     await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
#     user_id = message.from_user.id
#     data = await state.get_data()
#     s1 = int(data.get('S_ot'))
#     s2 = int(data.get('S_do'))
#     if s1 > s2:
#         sent_message = (await message.answer(f"Введенная максимальная квадратура <b>меньше</b> минимальной\n"
#                              f"Вы указали квадратуру от: <b>{data.get('S_ot')}м²</b>\n\n"
#                              f"Введите корректную максимальную квадратуру в <b>м²</b> :", parse_mode='HTML',
#                                              reply_markup=kb.edit_kvadrat_rent)).message_id
#     else:
#         if user_id not in date_messages:
#             date_messages[user_id] = []
#         messages = date_messages[user_id]
#         for message1 in messages:
#             print(message1)
#             await bot.edit_message_text(text='Введите этаж:',chat_id=message.from_user.id, message_id=message1,
#                                         reply_markup=kb.floor_rent)
#             await state.set_state(Show_rent.repair)
#
#
# @router_rent.message(Show_rent.repair)
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
#         print(message1)
#         await bot.edit_message_text(text='Выберите тип ремонта:',reply_markup=kb.repair_rent,
#                                     chat_id=message.from_user.id,
#                                     message_id=message1)
#
#
# @router_rent.callback_query(F.data == 'Any_floor_rent')
# async def Any_floor(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await state.update_data(Floor_build='Любой')
#     data = await state.get_data()
#     print(f"Выбран этаж: {data.get('Floor_build')}")
#     await state.set_state(Show_rent.repair)
#     await callback.message.edit_text('Выберите тип ремонта:', reply_markup=kb.repair_rent)
#
#
# @router_rent.callback_query(F.data == 'not_first_floor_rent')
# async def Any_floor(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await state.update_data(Floor_build='Любой кроме первого')
#     data = await state.get_data()
#     print(f"Выбран этаж: {data.get('Floor_build')}")
#     await state.set_state(Show_rent.repair)
#     await callback.message.edit_text('Выберите тип ремонта:',reply_markup=kb.repair_rent)
#
#
# @router_rent.callback_query(F.data == 'not_last_floor_rent')
# async def Any_floor(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     user_id = callback.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
#     await state.update_data(Floor_build='Любой кроме последнего')
#     data = await state.get_data()
#     print(f"Выбран этаж: {data.get('Floor_build')}")
#     await state.set_state(Show_rent.repair)
#     await callback.message.edit_text('Выберите тип ремонта:',reply_markup=kb.repair_rent)
#
#
# @router_rent.callback_query(F.data == 'With_repair_rent')
# async def With_repair(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(repair='С ремонтом')
#     data = await state.get_data()
#     print(f"Выбрана категория ремонта:'{data.get('repair')}'")
#     await callback.message.edit_text('Выберите количество санузлов', reply_markup=kb.bath_rent)
#     await state.set_state(Show_rent.balcony)
#
#
# @router_rent.callback_query(F.data == 'Without_repair_rent')
# async def Without_repair(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(repair='Без ремонта')
#     data = await state.get_data()
#     print(f"Выбрана категория ремонта:'{data.get('repair')}'")
#     await callback.message.edit_text('Выберите количество санузлов:', reply_markup=kb.bath_rent)
#     await state.set_state(Show_rent.balcony)
#
#
# @router_rent.callback_query(F.data == 'any_repair_rent')
# async def Without_repair(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(repair='Любой ремонт')
#     data = await state.get_data()
#     print(f"Выбрана категория ремонта:'{data.get('repair')}'")
#     await callback.message.edit_text('Выберите количество санузлов:', reply_markup=kb.bath_rent)
#     await state.set_state(Show_rent.balcony)
#
#
# @router_rent.callback_query(F.data == 'bath_1_rent')
# async def bath_1(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(bath=1)
#     data = await state.get_data()
#     print(f"Выбрано количество санузлов: '{data.get('bath')}'")
#     await callback.message.edit_text('Выберите тип балкона:', reply_markup=kb.balcony_rent)
#     await state.set_state(Show_rent.Price)
#
#
# @router_rent.callback_query(F.data == 'bath_2_rent')
# async def bath_2(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(bath=2)
#     data = await state.get_data()
#     print(f"Выбрано количество санузлов: '{data.get('bath')}'")
#     await callback.message.edit_text('Выберите тип балкона:', reply_markup=kb.balcony_rent)
#     await state.set_state(Show_rent.Price)
#
#
# @router_rent.callback_query(F.data == 'Any_count_bath_rent')
# async def bath_2(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(bath='Любое количество')
#     data = await state.get_data()
#     print(f"Выбрано количество санузлов: '{data.get('bath')}'")
#     await callback.message.edit_text('Выберите тип балкона:', reply_markup=kb.balcony_rent)
#     await state.set_state(Show_rent.Price)
#
#
# @router_rent.callback_query(F.data == 'balcony_type_rent')
# async def bath_2(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(balcony='Балкон')
#     data = await state.get_data()
#     print(f"Выбрана категория '{data.get('balcony')}'")
#     await callback.message.edit_text('Введите ваш бюджет в рублях:')
#     await state.set_state(Show_rent.Price)
#
#
# @router_rent.callback_query(F.data == 'loggia_type_rent')
# async def loggia_type(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(balcony='Лоджия')
#     data = await state.get_data()
#     print(f"Выбрана категория '{data.get('balcony')}'")
#     await callback.message.edit_text('Введите ваш бюджет в рублях:', reply_markup=kb.price_rent, parse_mode='HTML')
#     await state.set_state(Show_rent.Price)
#
#
# @router_rent.callback_query(F.data == 'Any_balcony_type_rent')
# async def loggia_type(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(balcony='Любой тип')
#     data = await state.get_data()
#     print(f"Выбрана категория '{data.get('balcony')}'")
#     await callback.message.edit_text('Введите ваш бюджет в рублях:', reply_markup=kb.price_rent, parse_mode='HTML')
#     await state.set_state(Show_rent.Price)
#
#
# @router_rent.message(Show_rent.Price)
# async def Price(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     if user_id not in date_messages:
#         date_messages[user_id] = []
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
#     print(f"Введен бюджет '{data.get('Price')}'")
#     await state.set_state(Show_rent.Price)
#     messages = date_messages[user_id]
#     for message1 in messages:
#         await bot.edit_message_text(text=f'Давайте перепроверим данные:\n\n'
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
#                                          reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'any_price_rent')
# async def any_price(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(Price='Не ограничено')
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
#                                      f"Бюджет: <b>{data.get('Price')}</b>",parse_mode='HTML',
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'edit_buy_search_rent')
# async def edit_buy_search(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await callback.message.edit_text(f"Выберите категорию для редактирования:",
#                                      reply_markup=kb.edit_buy_search_rent)
#
#
# @router_rent.callback_query(F.data == 'raion_edit_rent')
# async def raion_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     data = await state.get_data()
#     print(f"Выбрано редактирование категории: Район")
#     await callback.message.edit_text(f'Выберите район:', reply_markup=kb.raion_edit_rent)
#     await state.set_state(Show_rent.complete)
#
#
# @router_rent.callback_query(F.data == 'Zapadniy_rajon_edit_rent', Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'Karasun_rajon_edit_rent', Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'Prikubanskiy_rajon_edit_rent', Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'Central_rajon_edit_rent', Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'any_raion_edit_rent', Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'count_rooms_edit_rent')
# async def raion_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Количество комнат")
#     await callback.message.edit_text(f'Выберите количество комнат:',reply_markup=kb.count_rooms_edit_rent)
#     await state.set_state(Show_rent.complete)
#
#
# @router_rent.callback_query(F.data == '1_edit_rent')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count=1)
#     data = await state.get_data()
#     await state.set_state(Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == '2_edit_rent')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count=2)
#     data = await state.get_data()
#     await state.set_state(Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == '3_edit_rent')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count=3)
#     data = await state.get_data()
#     await state.set_state(Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == '4_edit_rent')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count=4)
#     data = await state.get_data()
#     await state.set_state(Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == '0_edit_rent')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count='0 (Студия)')
#     data = await state.get_data()
#     await state.set_state(Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'any_count_rooms_edit_rent')
# async def count_apt(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(rooms_count='Любое количество')
#     data = await state.get_data()
#     await state.set_state(Show_rent.complete)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'kvadrat_ot_edit_rent')
# async def kvadrat_ot_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     data = await state.get_data()
#     print(f"Выбрано редактирование категории: Площадь От")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'От:', parse_mode='HTML', reply_markup=kb.kvadrat_ot_edit_rent)
#     await state.set_state(Show_rent.S_ot_edit)
#
#
# @router_rent.message(Show_rent.S_ot_edit)
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
#                                          reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'Any_kvadrat_ot_edit_rent')
# async def Any_kvadrat_ot_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(S_ot='Любая')
#     data = await state.get_data()
#     await state.set_state(Show_rent.S_ot_edit)
#     print(f"Введена площадь от: {data.get('rooms_count')}")
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'kvadrat_do_edit_rent')
# async def kvadrat_do_edit(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     data = await state.get_data()
#     print(f"Выбрано редактирование категории: Площадь До")
#     await callback.message.edit_text(f'Введите площадь квартиры в <b>м²</b>\n'
#                                      f'До:', parse_mode='HTML', reply_markup=kb.kvadrat_do_edit_rent)
#     await state.set_state(Show_rent.S_do_edit)
#
#
# @router_rent.message(Show_rent.S_do_edit)
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
#                                          f"Бюджет: <b>{data.get('Price')}</b>", parse_mode='HTML',
#                                          chat_id=message.from_user.id, message_id=message1,
#                                          reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'Any_kvadrat_do_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'floor_edit_rent')
# async def Any_kvadrat_do_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Этаж")
#     await callback.message.edit_text(f'Введите этаж:', parse_mode='HTML', reply_markup=kb.floor_edit_rent)
#     await state.set_state(Show_rent.Floor_build_edit)
#
#
# @router_rent.message(Show_rent.Floor_build_edit)
# async def Floor_build_edit(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     await state.update_data(Floor_build=message.text)
#     await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
#     data = await state.get_data()
#     print(f"Введена этаж:'{data.get('Floor_build')}'")
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
#                                          reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'Any_floor_edit_rent')
# async def Any_floor_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(Floor_build='Любой этаж')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'not_first_floor_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'not_last_floor_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'repair_edit_rent')
# async def repair_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Ремонт")
#     await callback.message.edit_text(f'Выберите тип ремонта:', parse_mode='HTML', reply_markup=kb.repair_edit_rent)
#     await state.set_state(Show_rent.repair_edit)
#
#
# @router_rent.callback_query(F.data == 'Without_repair_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'With_repair_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'any_repair_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'bath_edit_rent')
# async def bath_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Количество санузлов")
#     await callback.message.edit_text('Выберите количество санузлов:', reply_markup=kb.bath_edit_rent)
#     await state.set_state(Show_rent.bath_edit)
#
#
# @router_rent.callback_query(F.data == 'bath_1_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'bath_2_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'Any_count_bath_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'balcony_edit_rent')
# async def balcony_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Балкон")
#     await callback.message.edit_text('Выберите тип балкона:', reply_markup=kb.balcony_edit_rent)
#     await state.set_state(Show_rent.balcony_edit)
#
#
# @router_rent.callback_query(F.data == 'balcony_type_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'loggia_type_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'Any_balcony_type_edit_rent')
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.callback_query(F.data == 'price_edit_rent')
# async def price_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     print(f"Выбрано редактирование категории: Бюджет")
#     await callback.message.edit_text('Введите ваш бюджет в рублях:', reply_markup=kb.price_edit_rent)
#     await state.set_state(Show_rent.Price_edit)
#
#
# @router_rent.callback_query(F.data == 'any_price_edit_rent')
# async def any_price_edit(callback:CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await state.update_data(Price='Неограничен')
#     data = await state.get_data()
#     await state.set_state(Show_rent.Price_edit)
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
#                                      reply_markup=kb.complete_buy_rent)
#
#
# @router_rent.message(Show_rent.Price_edit)
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
#                                          reply_markup=kb.complete_buy_rent)
