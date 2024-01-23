# from aiogram import Router, F, Bot, Dispatcher
# from aiogram.types import Message
# from app import keyboards as kb
# from dotenv import load_dotenv
# import os
# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
# from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton,
#                            KeyboardButton, CallbackQuery)
# from aiogram.filters.callback_data import CallbackData
# from aiogram import types
# from typing import Optional
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import ReplyKeyboardRemove
# from aiogram.types import CallbackQuery
# import datetime
# import calendar
# import locale
#
#
#
# router = Router()
# message_to_delete = []
# date_messages = {}
# calendar_message = []
#
#
# class Form(StatesGroup):
#     project_category = State()
#     project_category_edit = State()
#
#     project_name = State()
#     project_name_edit = State()
#
#     username = State()
#     username_edit = State()
#
#
#     project_description = State()
#     project_description_edit = State()
#
#
#     project_priority = State()
#     project_priority_edit = State()
#
#
#     deadline = State()
#     deadline_edit = State()
#
#
#     project_photo = State()
#     project_photo_edit = State()
#
#
#     creation_date = State()
#     complete = State()
#
#
# @router.message(F.text == '/test')
# async def cmd_add_new_project(message: Message, state: FSMContext) -> None:
#     # Получаем айди чата и айди треда
#     chat_id = message.chat.id
#     thread_id = message.message_thread_id
#     print(thread_id)
#
#     if thread_id == None:
#         sent_message = (await message.reply('Вы начали процесс добавления новой задачи\n\n'
#                             'Выберите категорию',reply_markup=kb.category_form_kb)).message_id
#         await state.set_state(Form.project_category)
#         message_to_delete.append(message.message_id)
#         message_to_delete.append(sent_message)
#         print(message_to_delete)
#     else:
#         await message.answer("Управление доступно в топике 'General'")
#
#
# ###### STATE NAME
# @router.message(Form.project_category)
# async def cmd_add_project_category(message: Message, state: FSMContext) -> None:
#     await state.update_data(project_category=message.text)
#     data = await state.get_data()
#     await state.set_state(Form.project_name)
#     sent_message = (await message.reply('Введите название задачи',reply_markup=ReplyKeyboardRemove())).message_id
#     message_to_delete.append(message.message_id)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
#
# ####### STATE project_name
# @router.message(Form.project_name)
# async def cmd_add_project_name(message: Message, state: FSMContext) -> None:
#     await state.update_data(project_name=message.text)
#     await state.set_state(Form.username)
#     data = await state.get_data()
#
#     sent_message = (await message.reply('Введите username исполнителя')).message_id
#     message_to_delete.append(message.message_id)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
# ####### STATE username
# @router.message(Form.username)
# async def cmd_add_username(message: Message, state: FSMContext) -> None:
#     username = message.text.lower()
#
#     # Проверяем, содержит ли сообщение символ "@"; если нет, добавляем его
#     if not username.startswith('@'):
#         username = f'@{username}'
#
#     await state.update_data(username=username)
#     data = await state.get_data()
#     sent_message = (await message.reply('Добавьте описание к задаче')).message_id
#     await state.set_state(Form.project_description)
#     message_to_delete.append(message.message_id)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
#
# @router.message(Form.project_description)
# async def cmd_add_description(message: Message, state: FSMContext) -> None:
#     await state.update_data(project_description=message.text)
#     data = await state.get_data()
#     sent_message = (await message.reply('Выберите приоритет задачи', reply_markup=kb.priority_form_kb)).message_id
#     await state.set_state(Form.project_priority)
#     message_to_delete.append(message.message_id)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
# @router.message(Form.project_priority)
# async def cmd_add_project_priority(message: Message, state: FSMContext) -> None:
#     await state.update_data(project_priority=message.text)
#
#     await state.update_data(deadline_day='__')
#     locale.setlocale(locale.LC_TIME, "ru_RU")
#     current_month = datetime.datetime.now().month
#     current_year = datetime.datetime.now().year
#     current_month_name = datetime.datetime.now().strftime("%B")
#
#     # Получаем предыдущий месяц
#     previous_month = current_month - 1
#     if previous_month == 0:
#         previous_month = 12  # Если текущий месяц - январь, то предыдущим будет декабрь
#     else:
#         previous_year = current_year
#
#     last_day = calendar.monthrange(current_year, current_month)[1]
#     print(last_day)
#
#     next_month = current_month + 1
#     if next_month == 13:
#         next_month = 1  # Если текущий месяц - декабрь, то следующим будет январь
#         next_year = current_year + 1
#     else:
#         next_year = current_year
#     builder = InlineKeyboardBuilder()
#     builder.button(text='<', callback_data=CalendarCallback(action='previous_month', value=previous_month))
#     builder.button(text=f"{current_month_name}",
#                    callback_data=CalendarCallback(action="month_deadline", value=current_month))
#     builder.button(text='>', callback_data=CalendarCallback(action='next_month1', value=next_month))
#
#     await state.update_data(current_month=current_month, current_year=current_year)
#     data = await state.get_data()
#
#     for i in range(1, last_day):  # + 1):
#         is_current_day = i == datetime.datetime.now().day
#         day_text = f"✓ {i}" if is_current_day else str(i)
#         builder.button(text=day_text, callback_data=CalendarCallback(action="change", value=str(i)))
#
#     builder.adjust(3, 7, 7, 7, 7, 7, 3)
#     for i in range(6):
#         builder.button(text=' ', callback_data='-1-')
#     builder.button(text='<', callback_data=CalendarCallback(action='previous_year'))
#     builder.button(text=f"{current_year}", callback_data=CalendarCallback(action="year_deadline", value=current_year))
#     builder.button(text='>', callback_data=CalendarCallback(action='next_year'))
#     sent_message2 = (await message.answer(
#         "Выберите день:",
#         reply_markup=builder.as_markup(resize_keyboard=True)
#     )).message_id
#     sent_message = (await message.answer(
#         f"{data.get('deadline_day')}.{data.get('current_month')}.{data.get('current_year')}")).message_id
#     calendar_message.append(sent_message2)
#     data = await state.get_data()
#     await state.set_state(Form.deadline)
#     message_to_delete.append(message.message_id)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
# @router_calendar.callback_query(CalendarCallback.filter())
# async def previous_month(callback_query: types.CallbackQuery, callback_data: CalendarCallback, state: FSMContext):
#     action = callback_data.action
#     if action == 'previous_month':
#         current_state = await state.get_state()
#         data = await state.get_data()
#         current_month = data.get('current_month', datetime.datetime.now().month)
#         current_year = data.get('current_year', datetime.datetime.now().year)
#
#         previous_month = current_month - 1
#         if previous_month == 0:
#             previous_month = 12  # Если текущий месяц - январь, то предыдущим будет декабрь
#             previous_year = current_year - 1
#         else:
#             previous_year = current_year
#         print(f"{current_month} месяц был")
#         print(f"{previous_month} месяц стал")
#
#         last_day = calendar.monthrange(previous_year, previous_month)[1]
#
#         month_names = [
#             'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
#             'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
#         ]
#         previous_month_name = month_names[previous_month - 1]
#         builder = InlineKeyboardBuilder()
#         next_month = current_month + 1
#         if next_month == 13:
#             next_month = 1  # Если текущий месяц - декабрь, то следующим будет январь
#             next_year = current_year + 1
#         else:
#             next_year = current_year
#         next_month_name = datetime.date(next_year, next_month, 1).strftime("%B")
#         await state.update_data(current_month=previous_month, current_year=previous_year)
#         print(f"{data.get('current_month')} записан")
#
#         builder.button(text='<', callback_data=CalendarCallback(action='previous_month', value=previous_month))
#         builder.button(text=f"{previous_month_name}",
#                        callback_data=CalendarCallback(action="month_deadline", value=current_month))
#         builder.button(text='>', callback_data=CalendarCallback(action='next_month1', value=next_month))
#
#         for i in range(1, last_day + 1):
#             is_current_day = i == datetime.datetime.now().day
#             day_text = f"{i}" if is_current_day else str(i)
#             builder.button(text=day_text, callback_data=CalendarCallback(action="change", value=str(i)))
#
#         empty_buttons = 5 if last_day == 31 else 6 if last_day == 30 else 1 \
#             if last_day == 28 else 7 if last_day == 29 else 0
#         builder.adjust(3, 7, 7, 7, 7, 7, 3)
#         for i in range(empty_buttons):
#             builder.button(text=' ', callback_data='-1-')
#
#         builder.button(text='<', callback_data=CalendarCallback(action='previous_month'))
#         builder.button(text=f"{previous_year}",
#                        callback_data=CalendarCallback(action="year_deadline", value=current_year))
#         builder.button(text='>', callback_data='next_month1')
#
#         await callback_query.message.edit_reply_markup(reply_markup=builder.as_markup(resize_keyboard=True))
#
#         # Обновляем состояние
#         edited_text = f"{data.get('deadline_day')}.{previous_month:02d}.{previous_year}"
#         user_id = callback_query.from_user.id
#         for message_id in date_messages[user_id]:
#             print(message_id)
#             await bot.edit_message_text(text=edited_text, chat_id=callback_query.from_user.id, message_id=message_id)
#
#         print({data.get('current_month')})
#         print({data.get('current_year')})
#
#     if action == 'next_month1':
#         data = await state.get_data()
#         current_month = data.get('current_month', datetime.datetime.now().month)
#         current_year = data.get('current_year', datetime.datetime.now().year)
#
#         # Получаем следующий месяц и его имя на русском
#         next_month = current_month + 1
#         if next_month == 13:
#             next_month = 1  # Если текущий месяц - декабрь, то следующим будет январь
#             next_year = current_year + 1
#         else:
#             next_year = current_year
#
#         # Получаем имя следующего месяца на русском
#         month_names = [
#             'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
#             'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
#         ]
#         next_month_name = month_names[next_month - 1]
#
#         last_day = calendar.monthrange(next_year, next_month)[1]
#         await state.update_data(current_month=next_month, current_year=next_year)
#
#         builder = InlineKeyboardBuilder()
#         builder.button(text='<', callback_data=CalendarCallback(action='previous_month'))
#         builder.button(text=f"{next_month_name}",
#                        callback_data=CalendarCallback(action="year_deadline", value=current_year))
#         builder.button(text='>', callback_data=CalendarCallback(action='next_month1'))
#
#         for i in range(1, last_day + 1):
#             is_current_day = i == datetime.datetime.now().day
#             day_text = f" {i}" if is_current_day else str(i)
#             builder.button(text=day_text, callback_data=CalendarCallback(action="change", value=str(i)))
#
#         empty_buttons = 5 if last_day == 31 else 6 if last_day == 30 else 1\
#             if last_day == 28 else 7 if last_day == 29 else 0
#         builder.adjust(3, 7, 7, 7, 7, 7, 3)
#         for i in range(empty_buttons):
#             builder.button(text=' ', callback_data='-1-')
#
#         builder.button(text='<', callback_data=CalendarCallback(action='previous_month'))
#         builder.button(text=f"{next_year}",
#                        callback_data=CalendarCallback(action="year_deadline", value=current_year))
#         builder.button(text='>', callback_data='next_month1')
#
#         await callback_query.message.edit_reply_markup(reply_markup=builder.as_markup(resize_keyboard=True))
#
#         # Обновляем состояние
#         edited_text = f"{data.get('deadline_day')}.{next_month:02d}.{next_year}"
#         user_id = callback_query.from_user.id
#         for message_id in date_messages[user_id]:
#             print(message_id)
#             await bot.edit_message_text(text=edited_text, chat_id=callback_query.from_user.id, message_id=message_id)
#         print({data.get('current_month')})
#         print({data.get('current_year')})
#
#     if action == "change":
#         data = await state.get_data()
#         current_month = data.get('current_month', datetime.datetime.now().month)
#         current_year = data.get('current_year', datetime.datetime.now().year)
#         next_month = current_month + 1
#         if next_month == 13:
#             next_month = 1  # Если текущий месяц - декабрь, то следующим будет январь
#             next_year = current_year + 1
#         else:
#             next_year = current_year
#         user_id = callback_query.from_user.id
#         await state.update_data(deadline_day=callback_data.value)
#         data = await state.get_data()
#         edited_text = f"{data.get('deadline_day')}.{current_month:02d}.{next_year}"
#         await callback_query.answer()
#         for message_id in date_messages[user_id]:
#             print(message_id)
#             await bot.edit_message_text(text=edited_text, chat_id=callback_query.from_user.id, message_id=message_id)
#
#
# @router.message(Form.deadline)
# async def cmd_add_deadline(message: Message, state: FSMContext) -> None:
#     await state.update_data(deadline=message.text)
#     data = await state.get_data()
#     await state.set_state(Form.project_photo)
#     sent_message = (await message.reply('Прикрепите медиа к задаче')).message_id
#     message_to_delete.append(message.message_id)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
#
# @router.message(Form.project_photo, F.photo)
# async def cmd_add_photo_project(message: Message, state: FSMContext) -> None:
#     await state.update_data(photo=message.photo[0].file_id)
#     data = await state.get_data()
#     await state.set_state(Form.complete)
#     data = await state.get_data()
#     today = datetime.date.today()
#     formatted_today = today.strftime("%d.%m.%Y")
#     sent_message1 = (await message.answer('Давайте перепроверим данные:')).message_id
#     sent_message2 = (await message.answer_photo(photo=data.get('photo'),
#                                caption=f"Категория: <b>{data.get('project_category')}</b>\n\n"
#                                        f"Описание: <b>{data.get('project_description')}</b>\n\n"
#                                        f"Исполнитель: <b>{data.get('username')}</b>\n"
#                                        # f"Категория: <b>{data.get('project_category')}</b>\n"
#                                        # f"Ссылка на проект: <b>{data.get('project_link')}</b>\n"
#                                        f"Приоритет выполнения: <b>{data.get('project_priority')}</b>\n\n"
#                                        f"Дата создания проекта: <b>{formatted_today}</b>\n"  # Вставляем сегодняшнюю дату
#                                        f"Срок выполнения / выполнить до: <b>{data.get('deadline')}</b>", reply_markup=kb.form_kb,
#                                parse_mode='HTML')).message_id
#     message_to_delete.append(message.message_id)
#     message_to_delete.append(sent_message1)
#     print(message_to_delete)
#     for message_id in message_to_delete:
#         print(message_id)
#         await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
#     message_to_delete.clear()
#
#
# @router.callback_query(F.data == 'return_form')
# async def return_form(callback: CallbackQuery, state: FSMContext) -> None:
#     today = datetime.date.today()
#     formatted_today = today.strftime("%d.%m.%Y")
#     data = await state.get_data()
#     await callback.message.delete()
#     sent_message = (await callback.message.answer_photo(photo=data.get('photo'),
#                                         caption=
#                                        f"Категория: <b>{data.get('project_category')}</b>\n\n"
#                                        f"Описание: <b>{data.get('project_description')}</b>\n\n"
#                                        f"Исполнитель: <b>{data.get('username')}</b>\n"
#                                        # f"Категория: <b>{data.get('project_category')}</b>\n"
#                                        # f"Ссылка на проект: <b>{data.get('project_link')}</b>\n"
#                                        f"Приоритет выполнения: <b>{data.get('project_priority')}</b>\n\n"
#                                        f"Дата создания проекта: <b>{formatted_today}</b>\n"  # Вставляем сегодняшнюю дату
#                                        f"Срок выполнения / выполнить до: <b>{data.get('deadline')}</b>\n\n"
#                                        f"<b>Выберите пункт для редактирования:</b>", reply_markup=kb.return_form_kb, parse_mode='HTML')).message_id
#
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
#
# @router.callback_query(F.data == 'return_project_category')
# async def cmd_add_project_name(callback: CallbackQuery, state: FSMContext) -> None:
#     sent_message = (await callback.message.answer('Выберите категорию',reply_markup=kb.category_form_kb)).message_id
#     await state.set_state(Form.project_category_edit)
#
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
#
# @router.message(Form.project_category_edit)
# async def cmd_complete(message: Message, state: FSMContext) -> None:
#     await state.update_data(project_category=message.text)
#     data = await state.get_data()
#     today = datetime.date.today()
#     formatted_today = today.strftime("%d.%m.%Y")
#     sent_message1 = (await message.answer('Давайте перепроверим данные:',reply_markup=ReplyKeyboardRemove())).message_id
#     sent_message2 = (await message.answer_photo(photo=data.get('photo'),
#                                caption=f"Категория: <b>{data.get('project_category')}</b>\n\n"
#                                        f"Описание: <b>{data.get('project_description')}</b>\n\n"
#                                        f"Исполнитель: <b>{data.get('username')}</b>\n"
#                                        # f"Категория: <b>{data.get('project_category')}</b>\n"
#                                        # f"Ссылка на проект: <b>{data.get('project_link')}</b>\n"
#                                        f"Приоритет выполнения: <b>{data.get('project_priority')}</b>\n\n"
#                                        f"Дата создания проекта: <b>{formatted_today}</b>\n"  # Вставляем сегодняшнюю дату
#                                        f"Срок выполнения / выполнить до: <b>{data.get('deadline')}</b>" ,reply_markup=kb.form_kb,
#                                parse_mode='HTML')).message_id
#     message_to_delete.append(message.message_id)
#     for message_id in message_to_delete:
#         print(message_id)
#         await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
#     message_to_delete.clear()
#     message_to_delete.append(sent_message1)
#     # message_to_delete.append(sent_message2)
#     print(message_to_delete)
#
#
# @router.callback_query(F.data == 'return_project_name')
# async def cmd_add_project_name(callback: CallbackQuery, state: FSMContext) -> None:
#     sent_message = (await callback.message.answer('Введите название задачи',reply_markup=ReplyKeyboardRemove())).message_id
#     await state.set_state(Form.project_name_edit)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
#
# @router.message(Form.project_name_edit)
# async def cmd_complete(message: Message, state: FSMContext) -> None:
#     await state.update_data(project_name=message.text)
#     data = await state.get_data()
#     today = datetime.date.today()
#     formatted_today = today.strftime("%d.%m.%Y")
#     sent_message1 = (await message.answer('Давайте перепроверим данные:')).message_id
#     sent_message2 = (await message.answer_photo(photo=data.get('photo'),
#                                caption=f"Категория: <b>{data.get('project_category')}</b>\n\n"
#                                        f"Описание: <b>{data.get('project_description')}</b>\n\n"
#                                        f"Исполнитель: <b>{data.get('username')}</b>\n"
#                                        # f"Категория: <b>{data.get('project_category')}</b>\n"
#                                        # f"Ссылка на проект: <b>{data.get('project_link')}</b>\n"
#                                        f"Приоритет выполнения: <b>{data.get('project_priority')}</b>\n\n"
#                                        f"Дата создания проекта: <b>{formatted_today}</b>\n"  # Вставляем сегодняшнюю дату
#                                        f"Срок выполнения / выполнить до: <b>{data.get('deadline')}</b>" ,reply_markup=kb.form_kb,
#                                parse_mode='HTML')).message_id
#     message_to_delete.append(message.message_id)
#     for message_id in message_to_delete:
#         print(message_id)
#         await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
#     message_to_delete.clear()
#     message_to_delete.append(sent_message1)
#     message_to_delete.append(sent_message2)
#     print(message_to_delete)
#
#
# @router.callback_query(F.data == 'return_username')
# async def cmd_add_project_name(callback: CallbackQuery, state: FSMContext) -> None:
#     sent_message = (await callback.message.answer('Введите username исполнителя')).message_id
#     await state.set_state(Form.username_edit)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
#
# @router.message(Form.username_edit)
# async def cmd_complete(message: Message, state: FSMContext) -> None:
#     username = message.text.lower()
#     # Проверяем, содержит ли сообщение символ "@"; если нет, добавляем его
#     if not username.startswith('@'):
#         username = f'@{username}'
#         await state.update_data(username=username)
#     data = await state.get_data()
#     today = datetime.date.today()
#     formatted_today = today.strftime("%d.%m.%Y")
#     sent_message1 = (await message.answer('Давайте перепроверим данные:')).message_id
#     sent_message2 = (await message.answer_photo(photo=data.get('photo'),
#                                caption=f"Категория: <b>{data.get('project_category')}</b>\n\n"
#                                        f"Описание: <b>{data.get('project_description')}</b>\n\n"
#                                        f"Исполнитель: <b>{data.get('username')}</b>\n"
#                                        # f"Категория: <b>{data.get('project_category')}</b>\n"
#                                        # f"Ссылка на проект: <b>{data.get('project_link')}</b>\n"
#                                        f"Приоритет выполнения: <b>{data.get('project_priority')}</b>\n\n"
#                                        f"Дата создания проекта: <b>{formatted_today}</b>\n"  # Вставляем сегодняшнюю дату
#                                        f"Срок выполнения / выполнить до: <b>{data.get('deadline')}</b>" ,reply_markup=kb.form_kb,
#                                parse_mode='HTML'))
#     message_to_delete.append(message.message_id)
#     for message_id in message_to_delete:
#         print(message_id)
#         await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
#     message_to_delete.clear()
#     message_to_delete.append(sent_message1)
#     # message_to_delete.append(sent_message2)
#     print(message_to_delete)
#
#
# @router.callback_query(F.data == 'return_project_description')
# async def cmd_add_project_name(callback: CallbackQuery, state: FSMContext) -> None:
#     sent_message = (await callback.message.answer('Добавьте описание к задаче')).message_id
#     await state.set_state(Form.project_description_edit)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
#
# @router.message(Form.project_description_edit)
# async def cmd_complete(message: Message, state: FSMContext) -> None:
#     await state.update_data(project_description=message.text)
#     data = await state.get_data()
#     today = datetime.date.today()
#     formatted_today = today.strftime("%d.%m.%Y")
#     sent_message1 = (await message.answer('Давайте перепроверим данные:')).message_id
#     sent_message2 = (await message.answer_photo(photo=data.get('photo'),
#                                caption=f"Категория: <b>{data.get('project_category')}</b>\n\n"
#                                        f"Описание: <b>{data.get('project_description')}</b>\n\n"
#                                        f"Исполнитель: <b>{data.get('username')}</b>\n"
#                                        # f"Категория: <b>{data.get('project_category')}</b>\n"
#                                        # f"Ссылка на проект: <b>{data.get('project_link')}</b>\n"
#                                        f"Приоритет выполнения: <b>{data.get('project_priority')}</b>\n\n"
#                                        f"Дата создания проекта: <b>{formatted_today}</b>\n"  # Вставляем сегодняшнюю дату
#                                        f"Срок выполнения / выполнить до: <b>{data.get('deadline')}</b>" ,reply_markup=kb.form_kb,
#                                parse_mode='HTML')).message_id
#     message_to_delete.append(message.message_id)
#     for message_id in message_to_delete:
#         print(message_id)
#         await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
#     message_to_delete.clear()
#     message_to_delete.append(sent_message1)
#     # message_to_delete.append(sent_message2)
#     print(message_to_delete)
#
#
# @router.callback_query(F.data == 'return_project_priority')
# async def cmd_add_project_name(callback: CallbackQuery, state: FSMContext) -> None:
#     sent_message = (await callback.message.answer('Поставьте приоритет задачи',reply_markup=kb.priority_form_kb)).message_id
#     await state.set_state(Form.project_priority_edit)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
#
# @router.message(Form.project_priority_edit)
# async def cmd_complete(message: Message, state: FSMContext) -> None:
#     await state.update_data(project_priority=message.text)
#     data = await state.get_data()
#     today = datetime.date.today()
#     formatted_today = today.strftime("%d.%m.%Y")
#     sent_message1 = (await message.answer('Давайте перепроверим данные:', reply_markup=ReplyKeyboardRemove())).message_id
#     sent_message2 = (await message.answer_photo(photo=data.get('photo'),
#                                caption=f"Категория: <b>{data.get('project_category')}</b>\n\n"
#                                        f"Описание: <b>{data.get('project_description')}</b>\n\n"
#                                        f"Исполнитель: <b>{data.get('username')}</b>\n"
#                                        # f"Категория: <b>{data.get('project_category')}</b>\n"
#                                        # f"Ссылка на проект: <b>{data.get('project_link')}</b>\n"
#                                        f"Приоритет выполнения: <b>{data.get('project_priority')}</b>\n\n"
#                                        f"Дата создания проекта: <b>{formatted_today}</b>\n"  # Вставляем сегодняшнюю дату
#                                        f"Срок выполнения / выполнить до: <b>{data.get('deadline')}</b>" ,reply_markup=kb.form_kb,
#                                parse_mode='HTML')).message_id
#     message_to_delete.append(message.message_id)
#     for message_id in message_to_delete:
#         print(message_id)
#         await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
#     message_to_delete.clear()
#     message_to_delete.append(sent_message1)
#     # message_to_delete.append(sent_message2)
#     print(message_to_delete)
#
#
# @router.callback_query(F.data == 'return_deadline')
# async def cmd_add_project_name(callback: CallbackQuery, state: FSMContext) -> None:
#     sent_message = (await callback.message.answer('Срок выполнения / выполнить до:')).message_id
#     await state.set_state(Form.deadline_edit)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
#
# @router.message(Form.deadline_edit)
# async def cmd_complete(message: Message, state: FSMContext) -> None:
#     await state.update_data(deadline=message.text)
#     data = await state.get_data()
#     today = datetime.date.today()
#     formatted_today = today.strftime("%d.%m.%Y")
#     sent_message1 = (await message.answer('Давайте перепроверим данные:')).message_id
#     sent_message2 = (await message.answer_photo(photo=data.get('photo'),
#                                caption=f"Категория: <b>{data.get('project_category')}</b>\n\n"
#                                        f"Описание: <b>{data.get('project_description')}</b>\n\n"
#                                        f"Исполнитель: <b>{data.get('username')}</b>\n"
#                                        # f"Категория: <b>{data.get('project_category')}</b>\n"
#                                        # f"Ссылка на проект: <b>{data.get('project_link')}</b>\n"
#                                        f"Приоритет выполнения: <b>{data.get('project_priority')}</b>\n\n"
#                                        f"Дата создания проекта: <b>{formatted_today}</b>\n"  # Вставляем сегодняшнюю дату
#                                        f"Срок выполнения / выполнить до: <b>{data.get('deadline')}</b>" ,reply_markup=kb.form_kb,
#                                parse_mode='HTML')).message_id
#     message_to_delete.append(message.message_id)
#     for message_id in message_to_delete:
#         print(message_id)
#         await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
#     message_to_delete.clear()
#     message_to_delete.append(sent_message1)
#     # message_to_delete.append(sent_message2)
#     print(message_to_delete)
#
#
# @router.callback_query(F.data == 'return_project_photo')
# async def cmd_add_project_name(callback: CallbackQuery, state: FSMContext) -> None:
#     sent_message = (await callback.message.answer('Прикрепите медиа к задаче:')).message_id
#     await state.set_state(Form.project_photo_edit)
#     message_to_delete.append(sent_message)
#     print(message_to_delete)
#
# @router.message(Form.project_photo_edit)
# async def cmd_complete(message: Message, state: FSMContext) -> None:
#     await state.update_data(photo=message.photo[0].file_id)
#     data = await state.get_data()
#     today = datetime.date.today()
#     formatted_today = today.strftime("%d.%m.%Y")
#     sent_message1 = (await message.answer('Давайте перепроверим данные:')).message_id
#     sent_message2 = (await message.answer_photo(photo=data.get('photo'),
#                                caption=f"Категория: <b>{data.get('project_category')}</b>\n\n"
#                                        f"Описание: <b>{data.get('project_description')}</b>\n\n"
#                                        f"Исполнитель: <b>{data.get('username')}</b>\n"
#                                        # f"Категория: <b>{data.get('project_category')}</b>\n"
#                                        # f"Ссылка на проект: <b>{data.get('project_link')}</b>\n"
#                                        f"Приоритет выполнения: <b>{data.get('project_priority')}</b>\n\n"
#                                        f"Дата создания проекта: <b>{formatted_today}</b>\n"  # Вставляем сегодняшнюю дату
#                                        f"Срок выполнения / выполнить до: <b>{data.get('deadline')}</b>" ,reply_markup=kb.form_kb,
#                                parse_mode='HTML')).message_id
#     message_to_delete.append(message.message_id)
#     for message_id in message_to_delete:
#         print(message_id)
#         await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
#     message_to_delete.clear()
#     message_to_delete.append(sent_message1)
#     # message_to_delete.append(sent_message2)
#     print(message_to_delete)
#
# async def send_message_to_user(username, message, state, caption, reply_markup):
#     # Найти id пользователя по username в вашей базе данных
#     # Предположим, что у вас есть функция find_user_id_by_username(username)
#     user_id = db.find_user_id_by_username(username)
#     chat_id = db.find_user_id_by_username(username)
#     reply_markup = kb.main
#     id_group = -1001909951706
#     id_thread = 24
#     if user_id:
#         # Отправить сообщение пользователю по id
#         # data = await state.get_data
#         data = await state.get_data()
#         await bot.send_message(chat_id=user_id, text=message)
#         await bot.send_photo(photo=data.get('photo'),caption=caption,chat_id=user_id, parse_mode='HTML', reply_markup=reply_markup)
#     else:
#         print(f"Пользователь {username} не найден.")
#
#
# @router.callback_query(F.data == 'complete_form')
# async def complete_form(callback: CallbackQuery, state: FSMContext):
#     await add_project(state)  # Добавил проект в базу данных
#     data = await state.get_data()
#
#     # Здесь username берется из данных состояния
#     username = data.get('username', '')
#     today = datetime.date.today()
#     formatted_today = today.strftime("%d.%m.%Y")
#     db.update_active_projects(username)  # Увеличиваем active_projects у пользователя
#     await callback.message.delete()
#     await callback.message.answer("✅ Проект успешно добавлен",reply_markup=kb.main)
#     reply_markup = kb.main_kb
#     message = "🔔 У вас новая активная задача"
#     photo = data.get('photo')
#     caption = (f"Категория: <b>{data.get('project_category')}</b>\n\n"
#                f"Описание: <b>{data.get('project_description')}</b>\n\n"
#                f"Приоритет выполнения: <b>{data.get('project_priority')}</b>\n\n"
#                f"Дата создания: <b>{formatted_today}</b>\n"  # Вставляем сегодняшнюю дату
#                f"Срок выполнения / выполнить до: <b>{data.get('deadline')}</b>\n\n"
#                f"<b>Задача получена от: @{callback.from_user.username}</b> <b>[</b><code>{callback.from_user.id}</code><b>]</b> ❗️\n")
#     for message_id in message_to_delete:
#         print(message_id)
#         await bot.delete_message(chat_id=callback.from_user.id, message_id=message_id)
#     message_to_delete.clear()
#
#     await send_message_to_user(username, message, state, caption, reply_markup)
#     await state.clear()
