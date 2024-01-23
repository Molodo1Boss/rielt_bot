from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton )


main_kb = [
    [KeyboardButton(text='🤝 Сотрудничество'),
     KeyboardButton(text='❓ Помощь')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True)


count_rooms_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Студия', callback_data='0_rent')],
    [InlineKeyboardButton(text='1', callback_data='1_rent'),
     InlineKeyboardButton(text='2', callback_data='2_rent')],
    [InlineKeyboardButton(text='3',  callback_data='3_rent'),
     InlineKeyboardButton(text='4',  callback_data='4_rent')],
    [InlineKeyboardButton(text='Любое количество', callback_data='any_count_rooms_rent')]

])


count_rooms_edit_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Студия', callback_data='0_edit_rent')],
    [InlineKeyboardButton(text='1', callback_data='1_edit_rent'),
     InlineKeyboardButton(text='2', callback_data='2_edit_rent')],
    [InlineKeyboardButton(text='3',  callback_data='3_edit_rent'),
     InlineKeyboardButton(text='4',  callback_data='4_edit_rent')],
    [InlineKeyboardButton(text='Любое количество', callback_data='any_count_rooms_edit_rent')]
])


raion_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Западный', callback_data='Zapadniy_rajon_rent'),
     InlineKeyboardButton(text='Карасунский', callback_data='Karasun_rajon_rent')],
    [InlineKeyboardButton(text='Прикубанский',  callback_data='Prikubanskiy_rajon_rent'),
     InlineKeyboardButton(text='Центральный',  callback_data='Central_rajon_rent')],
    [InlineKeyboardButton(text='Любой', callback_data='any_raion_rent')]
])


raion_edit_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Западный', callback_data='Zapadniy_rajon_edit_rent'),
     InlineKeyboardButton(text='Карасунский', callback_data='Karasun_rajon_edit_rent')],
    [InlineKeyboardButton(text='Прикубанский',  callback_data='Prikubanskiy_rajon_edit_rent'),
     InlineKeyboardButton(text='Центральный',  callback_data='Central_rajon_edit_rent')],
    [InlineKeyboardButton(text='Любой', callback_data='any_raion_edit_rent')]
])


edit_kvadrat_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Редактировать минимальную квадратуру', callback_data='red_min_kvadrat_rent')]
])


kvadrat_ot_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любая', callback_data='Any_kvadrat_ot_rent')]
])


kvadrat_ot_edit_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любая', callback_data='Any_kvadrat_ot_edit_rent')]
])


kvadrat_do_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любая', callback_data='Any_kvadrat_do_rent')]
])


kvadrat_do_edit_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любая', callback_data='Any_kvadrat_do_edit_rent')]
])


floor_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любой кроме перового', callback_data='not_first_floor_rent'),
     InlineKeyboardButton(text='Любой кроме последнего', callback_data='not_last_floor_rent')],
    [InlineKeyboardButton(text='Любой этаж', callback_data='Any_floor_rent')]

])


floor_edit_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любой кроме перового', callback_data='not_first_floor_edit_rent'),
     InlineKeyboardButton(text='Любой кроме последнего', callback_data='not_last_floor_edit_rent')],
    [InlineKeyboardButton(text='Любой этаж', callback_data='Any_floor_edit_rent')]

])


repair_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='С ремонтом', callback_data='With_repair_rent'),
     InlineKeyboardButton(text='Без ремонта', callback_data='Without_repair_rent')],
    [InlineKeyboardButton(text='Без разницы', callback_data='any_repair_rent')]

])


repair_edit_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='С ремонтом', callback_data='With_repair_edit_rent'),
     InlineKeyboardButton(text='Без ремонта', callback_data='Without_repair_edit_rent')],
    [InlineKeyboardButton(text='Без разницы', callback_data='any_repair_edit_rent')]

])


bath_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='bath_1_rent'),
     InlineKeyboardButton(text='2', callback_data='bath_2_rent')],
    [InlineKeyboardButton(text='Любое количество', callback_data='Any_count_bath_rent')]
])


bath_edit_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='bath_1_edit_rent'),
     InlineKeyboardButton(text='2', callback_data='bath_2_edit_rent')],
    [InlineKeyboardButton(text='Любое количество', callback_data='Any_count_bath_edit_rent')]
])


balcony_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Балкон', callback_data='balcony_type_rent'),
     InlineKeyboardButton(text='Лоджия', callback_data='loggia_type_rent')],
    [InlineKeyboardButton(text='Любой', callback_data='Any_balcony_type_rent')]
])


balcony_edit_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Балкон', callback_data='balcony_type_edit_rent'),
     InlineKeyboardButton(text='Лоджия', callback_data='loggia_type_edit_rent')],
    [InlineKeyboardButton(text='Любой', callback_data='Any_balcony_type_edit_rent')]
])


price_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Без ограничения', callback_data='any_price_rent')]
])


price_edit_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Без ограничения', callback_data='any_price_edit_rent')]
])


complete_buy_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🔎 Поиск', callback_data='complete_buy_search_rent'),
     InlineKeyboardButton(text='🔄 Редактировать', callback_data='edit_buy_search_rent')]
])


edit_buy_search_rent = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Район', callback_data='raion_edit_rent'),
     InlineKeyboardButton(text='Количество комнат', callback_data='count_rooms_edit_rent')],
    [InlineKeyboardButton(text='Площадь от',  callback_data='kvadrat_ot_edit_rent'),
     InlineKeyboardButton(text='Площадь до',  callback_data='kvadrat_do_edit_rent')],
    [InlineKeyboardButton(text='Этаж', callback_data='floor_edit_rent'),
     InlineKeyboardButton(text='Тип ремонта', callback_data='repair_edit_rent')],
    [InlineKeyboardButton(text='Количество санузлов', callback_data='bath_edit_rent'),
     InlineKeyboardButton(text='Тип балкона',  callback_data='balcony_edit_rent')],
    [InlineKeyboardButton(text='Бюджет',  callback_data='price_edit_rent')]
])