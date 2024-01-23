from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton)

city_rostov_region = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Краснодар', callback_data='Krasnodar_city')],
     [InlineKeyboardButton(text='Все города', callback_data='all_city_krasnodar')]
])


raion_rostov = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='Zapadniy_rajon'),
     InlineKeyboardButton(text='2', callback_data='Karasun_rajon')],
    [InlineKeyboardButton(text='3',  callback_data='Prikubanskiy_rajon'),
     InlineKeyboardButton(text='4',  callback_data='Central_rajon')],
    [InlineKeyboardButton(text='5', callback_data='any_raion')]
])