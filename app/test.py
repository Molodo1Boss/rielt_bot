from aiogram import Router, F, Bot, Dispatcher
from dotenv import load_dotenv
import os
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import types
from typing import Optional
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
import datetime
import calendar
import locale


router_calendar = Router()
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher()


class Test(StatesGroup):
    deadline_day = State()
    deadline_mounth = State()
    deadline_year = State()
    previous_mounth = State()
    previous_month = State()
    current_month = State()
    current_year = State()


class RegionCallback(CallbackData, prefix="region"):
    action: str
    value: Optional[int] = None

class CalendarCallback(CallbackData, prefix="calendar"):
    action: str
    value: Optional[int] = None

date_messages = {}
calendar_message = []

@router_calendar.message(F.text == '/test23')
async def reply_builder1(message: types.Message, state: FSMContext):
    button1 = 123
    button2 = 321
    builder = InlineKeyboardBuilder()
    builder.button(text='1', callback_data=RegionCallback(action='test1', value=button2))
    builder.button(text=f"123", callback_data=RegionCallback(action="test2",
                                                                                value=button1))
    builder.button(text='2', callback_data=RegionCallback(action='test3', value=button2))
    await message.answer(f'Test', reply_markup=builder.as_markup(resize_keyboard=True))




@router_calendar.message(F.text == '/test24')
async def reply_builder(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id not in date_messages:
        date_messages[user_id] = []

    locale.setlocale(locale.LC_TIME, "ru_RU")
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    current_month_name = datetime.datetime.now().strftime("%B")

    # Получаем предыдущий месяц
    previous_month = current_month - 1

    if previous_month == 0:
        previous_month = 12  # Если текущий месяц - январь, то предыдущим будет декабрь
    else:
        previous_year = current_year

    last_day = calendar.monthrange(current_year, current_month)[1]
    print(last_day)

    next_month = current_month + 1
    if next_month == 13:
        next_month = 1  # Если текущий месяц - декабрь, то следующим будет январь
        next_year = current_year + 1
    else:
        next_year = current_year
    builder = InlineKeyboardBuilder()
    builder.button(text='<', callback_data=CalendarCallback(action='previous_month', value=previous_month))
    builder.button(text=f"{current_month_name}", callback_data=CalendarCallback(action="month_deadline",
                                                                                value=current_month))
    builder.button(text='>', callback_data=CalendarCallback(action='next_month1', value=next_month))

    await state.update_data(current_month=current_month, current_year=current_year)
    data = await state.get_data()

    for i in range(1, last_day + 1):
        is_current_day = i == datetime.datetime.now().day
        day_text = f"✓ {i}" if is_current_day else str(i)
        builder.button(text=day_text, callback_data=CalendarCallback(action="change", value=str(i)))

    builder.adjust(3, 7, 7, 7, 7, 7, 3)
    for i in range(6):
        builder.button(text=' ', callback_data='-1-')
    builder.button(text='<', callback_data=CalendarCallback(action='previous_year'))
    builder.button(text=f"{current_year}", callback_data=CalendarCallback(action="year_deadline", value=current_year))
    builder.button(text='>', callback_data=CalendarCallback(action='next_year'))
    sent_message2 = (await message.answer(
        "Выберите день:",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )).message_id
    sent_message1 = (await message.answer(f"{data.get('deadline_day')}.{data.get('current_month')}.{data.get('current_year')}")).message_id
    calendar_message.append(sent_message2)

    # Добавляем идентификаторы сообщений для данного пользователя
    date_messages[user_id].append(sent_message1)


@router_calendar.callback_query(CalendarCallback.filter())
async def previous_month(callback_query: types.CallbackQuery, callback_data: CalendarCallback, state: FSMContext):
    action = callback_data.action
    if action == 'previous_month':
        current_state = await state.get_state()
        data = await state.get_data()
        current_month = data.get('current_month', datetime.datetime.now().month)
        current_year = data.get('current_year', datetime.datetime.now().year)

        previous_month = current_month - 1
        if previous_month == 0:
            previous_month = 12  # Если текущий месяц - январь, то предыдущим будет декабрь
            previous_year = current_year - 1
        else:
            previous_year = current_year
        print(f"{current_month} месяц был")
        print(f"{previous_month} месяц стал")

        last_day = calendar.monthrange(previous_year, previous_month)[1]

        month_names = [
            'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
            'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
        ]
        previous_month_name = month_names[previous_month - 1]
        builder = InlineKeyboardBuilder()
        next_month = current_month + 1
        if next_month == 13:
            next_month = 1  # Если текущий месяц - декабрь, то следующим будет январь
            next_year = current_year + 1
        else:
            next_year = current_year
        next_month_name = datetime.date(next_year, next_month, 1).strftime("%B")
        await state.update_data(current_month=previous_month, current_year=previous_year)
        print(f"{data.get('current_month')} записан")

        builder.button(text='<', callback_data=CalendarCallback(action='previous_month', value=previous_month))
        builder.button(text=f"{previous_month_name}",
                       callback_data=CalendarCallback(action="month_deadline", value=current_month))
        builder.button(text='>', callback_data=CalendarCallback(action='next_month1', value=next_month))

        for i in range(1, last_day + 1):
            is_current_day = i == datetime.datetime.now().day
            day_text = f"{i}" if is_current_day else str(i)
            builder.button(text=day_text, callback_data=CalendarCallback(action="change", value=str(i)))

        empty_buttons = 5 if last_day == 31 else 6 if last_day == 30 else 1 if last_day == 28 else 0
        builder.adjust(3, 7, 7, 7, 7, 7, 3)
        for i in range(empty_buttons):
            builder.button(text=' ', callback_data='-1-')

        builder.button(text='<', callback_data=CalendarCallback(action='previous_month'))
        builder.button(text=f"{previous_year}",
                       callback_data=CalendarCallback(action="year_deadline", value=current_year))
        builder.button(text='>', callback_data='next_month1')

        await callback_query.message.edit_reply_markup(reply_markup=builder.as_markup(resize_keyboard=True))

        # Обновляем состояние
        edited_text = f"{data.get('deadline_day')}.{previous_month:02d}.{previous_year}"
        user_id = callback_query.from_user.id
        for message_id in date_messages[user_id]:
            print(message_id)
            await bot.edit_message_text(text=edited_text, chat_id=callback_query.from_user.id, message_id=message_id)

        print({data.get('current_month')})
        print({data.get('current_year')})

    if action == 'next_month1':
        data = await state.get_data()
        current_month = data.get('current_month', datetime.datetime.now().month)
        current_year = data.get('current_year', datetime.datetime.now().year)

        # Получаем следующий месяц и его имя на русском
        next_month = current_month + 1
        if next_month == 13:
            next_month = 1  # Если текущий месяц - декабрь, то следующим будет январь
            next_year = current_year + 1
        else:
            next_year = current_year

        # Получаем имя следующего месяца на русском
        month_names = [
            'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
            'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
        ]
        next_month_name = month_names[next_month - 1]

        last_day = calendar.monthrange(next_year, next_month)[1]
        await state.update_data(current_month=next_month, current_year=next_year)

        builder = InlineKeyboardBuilder()
        builder.button(text='<', callback_data=CalendarCallback(action='previous_month'))
        builder.button(text=f"{next_month_name}",
                       callback_data=CalendarCallback(action="year_deadline", value=current_year))
        builder.button(text='>', callback_data=CalendarCallback(action='next_month1'))

        for i in range(1, last_day + 1):
            is_current_day = i == datetime.datetime.now().day
            day_text = f" {i}" if is_current_day else str(i)
            builder.button(text=day_text, callback_data=CalendarCallback(action="change", value=str(i)))

        empty_buttons = 5 if last_day == 31 else 6 if last_day == 30 else 1\
            if last_day == 28 else 7 if last_day == 29 else 0
        builder.adjust(3, 7, 7, 7, 7, 7, 3)
        for i in range(empty_buttons):
            builder.button(text=' ', callback_data='-1-')

        builder.button(text='<', callback_data=CalendarCallback(action='previous_month'))
        builder.button(text=f"{next_year}",
                       callback_data=CalendarCallback(action="year_deadline", value=current_year))
        builder.button(text='>', callback_data='next_month1')

        await callback_query.message.edit_reply_markup(reply_markup=builder.as_markup(resize_keyboard=True))

        # Обновляем состояние
        edited_text = f"{data.get('deadline_day')}.{next_month:02d}.{next_year}"
        user_id = callback_query.from_user.id
        for message_id in date_messages[user_id]:
            print(message_id)
            await bot.edit_message_text(text=edited_text, chat_id=callback_query.from_user.id, message_id=message_id)
        print({data.get('current_month')})
        print({data.get('current_year')})

    if action == "change":
        data = await state.get_data()
        current_month = data.get('current_month', datetime.datetime.now().month)
        current_year = data.get('current_year', datetime.datetime.now().year)
        next_month = current_month + 1
        if next_month == 13:
            next_month = 1  # Если текущий месяц - декабрь, то следующим будет январь
            next_year = current_year + 1
        else:
            next_year = current_year
        user_id = callback_query.from_user.id
        await state.update_data(deadline_day=callback_data.value)
        data = await state.get_data()
        edited_text = f"{data.get('deadline_day')}.{data.get('current_month')}.{next_year}"
        await callback_query.answer()
        for message_id in date_messages[user_id]:
            print(message_id)
            await bot.edit_message_text(text=edited_text, chat_id=callback_query.from_user.id, message_id=message_id)



