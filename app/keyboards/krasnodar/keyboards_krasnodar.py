from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton)

city_krasnodar_region = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Краснодар', callback_data='Zapadniy_rajon')],
     [InlineKeyboardButton(text='Все города', callback_data='Karasun_rajon')]
])


raion_krd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Западный', callback_data='Zapadniy_rajon'),
     InlineKeyboardButton(text='Карасунский', callback_data='Karasun_rajon')],
    [InlineKeyboardButton(text='Прикубанский',  callback_data='Prikubanskiy_rajon'),
     InlineKeyboardButton(text='Центральный',  callback_data='Central_rajon')],
    [InlineKeyboardButton(text='Любой', callback_data='any_raion')]
])