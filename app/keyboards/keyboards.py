from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.types import  WebAppInfo



main_kb = [
    [KeyboardButton(text='🤝 Сотрудничество'),
     KeyboardButton(text='❓ Помощь')]
]


main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True)


start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Новостройки', callback_data='new_apt'),
     InlineKeyboardButton(text='Ресейл', callback_data='resale_apt')],
])


inquiry = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Аренда', callback_data='rent_apt'),
     InlineKeyboardButton(text='Покупка', callback_data='buy_apt')],
    [InlineKeyboardButton(text='Добавить проект',  callback_data='add_apt_from_client')]
])


region = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Москва', callback_data='Moscow_region'),
     InlineKeyboardButton(text='Санкт-Петербург', callback_data='Saint_Petersburg_region')],
    [InlineKeyboardButton(text='Краснодар', callback_data='Krasnodar_region'),
     InlineKeyboardButton(text='Ростов-на-Дону', callback_data='Rostov_on_Don_region')],
    [InlineKeyboardButton(text='Черноморское побережье', callback_data='Black_Sea_Coast_region'),
     InlineKeyboardButton(text='Крым', callback_data='Crimea_region')],
    [InlineKeyboardButton(text='Калининград', callback_data='Kaliningrad_region'),
     InlineKeyboardButton(text='Казань', callback_data='Kazan_region')],
    [InlineKeyboardButton(text='Ижевск', callback_data='Izhevsk_region'),
     InlineKeyboardButton(text='Екатеринбург', callback_data='Ekaterinburg_region')],
    [InlineKeyboardButton(text='Владимир', callback_data='Vladimir_region'),
     InlineKeyboardButton(text='Киров', callback_data='Kirov_region')],
    [InlineKeyboardButton(text='Липецк', callback_data='Lipetsk_region'),
     InlineKeyboardButton(text='Нижний Новгород', callback_data='Nizhny_Novgorod_region')],
    [InlineKeyboardButton(text='Новосибирск', callback_data='Novosibirsk_region'),
     InlineKeyboardButton(text='Пенза', callback_data='Penza_region')],
    [InlineKeyboardButton(text='Пермь', callback_data='Perm_region'),
     InlineKeyboardButton(text='Воронеж', callback_data='Voronezh_region')],
    [InlineKeyboardButton(text='Самара', callback_data='Samara_region'),
     InlineKeyboardButton(text='Уфа', callback_data='Ufa_region')],
    [InlineKeyboardButton(text='Челябинск', callback_data='Chelyabinsk_region'),
     InlineKeyboardButton(text='Дальний Восток', callback_data='Far_East_region')],
])


count_rooms = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Студия', callback_data='0')],
    [InlineKeyboardButton(text='1', callback_data='1'),
     InlineKeyboardButton(text='2', callback_data='2')],
    [InlineKeyboardButton(text='3',  callback_data='3'),
     InlineKeyboardButton(text='4',  callback_data='4')],
    [InlineKeyboardButton(text='Любое количество', callback_data='any_count_rooms')]
])


count_rooms_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Студия', callback_data='0_edit')],
    [InlineKeyboardButton(text='1', callback_data='1_edit'),
     InlineKeyboardButton(text='2', callback_data='2_edit')],
    [InlineKeyboardButton(text='3',  callback_data='3_edit'),
     InlineKeyboardButton(text='4',  callback_data='4_edit')],
    [InlineKeyboardButton(text='Любое количество', callback_data='any_count_rooms_edit')]
])


raion_krd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Западный', callback_data='Zapadniy_rajon'),
     InlineKeyboardButton(text='Карасунский', callback_data='Karasun_rajon')],
    [InlineKeyboardButton(text='Прикубанский',  callback_data='Prikubanskiy_rajon'),
     InlineKeyboardButton(text='Центральный',  callback_data='Central_rajon')],
    [InlineKeyboardButton(text='Любой', callback_data='any_raion')]
])


raion_rnd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Западный', callback_data='Zapadniy_rajon'),
     InlineKeyboardButton(text='Карасунский', callback_data='Karasun_rajon')],
    [InlineKeyboardButton(text='Прикубанский',  callback_data='Prikubanskiy_rajon'),
     InlineKeyboardButton(text='Центральный',  callback_data='Central_rajon')],
    [InlineKeyboardButton(text='Любой', callback_data='any_raion')]
])


raion_msc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Западный', callback_data='Zapadniy_rajon'),
     InlineKeyboardButton(text='Карасунский', callback_data='Karasun_rajon')],
    [InlineKeyboardButton(text='Прикубанский',  callback_data='Prikubanskiy_rajon'),
     InlineKeyboardButton(text='Центральный',  callback_data='Central_rajon')],
    [InlineKeyboardButton(text='Любой', callback_data='any_raion')]
])


raion_spb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Западный', callback_data='Zapadniy_rajon'),
     InlineKeyboardButton(text='Карасунский', callback_data='Karasun_rajon')],
    [InlineKeyboardButton(text='Прикубанский',  callback_data='Prikubanskiy_rajon'),
     InlineKeyboardButton(text='Центральный',  callback_data='Central_rajon')],
    [InlineKeyboardButton(text='Любой', callback_data='any_raion')]
])


raion_krim = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Западный', callback_data='Zapadniy_rajon'),
     InlineKeyboardButton(text='Карасунский', callback_data='Karasun_rajon')],
    [InlineKeyboardButton(text='Прикубанский',  callback_data='Prikubanskiy_rajon'),
     InlineKeyboardButton(text='Центральный',  callback_data='Central_rajon')],
    [InlineKeyboardButton(text='Любой', callback_data='any_raion')]
])


raion_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Западный', callback_data='Zapadniy_rajon_edit'),
     InlineKeyboardButton(text='Карасунский', callback_data='Karasun_rajon_edit')],
    [InlineKeyboardButton(text='Прикубанский',  callback_data='Prikubanskiy_rajon_edit'),
     InlineKeyboardButton(text='Центральный',  callback_data='Central_rajon_edit')],
    [InlineKeyboardButton(text='Любой', callback_data='any_raion_edit')]
])


edit_kvadrat = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Редактировать минимальную квадратуру', callback_data='red_min_kvadrat')]
])


kvadrat_ot = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любая', callback_data='Any_kvadrat_ot')]
])


kvadrat_ot_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любая', callback_data='Any_kvadrat_ot_edit')]
])


kvadrat_do = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любая', callback_data='Any_kvadrat_do')]
])


kvadrat_do_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любая', callback_data='Any_kvadrat_do_edit')]
])


floor = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любой кроме перового', callback_data='not_first_floor'),
     InlineKeyboardButton(text='Любой кроме последнего', callback_data='not_last_floor')],
    [InlineKeyboardButton(text='Любой этаж', callback_data='Any_floor')]
])


floor_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Любой кроме перового', callback_data='not_first_floor_edit'),
     InlineKeyboardButton(text='Любой кроме последнего', callback_data='not_last_floor_edit')],
    [InlineKeyboardButton(text='Любой этаж', callback_data='Any_floor_edit')]
])


repair = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='С ремонтом собственника', callback_data='With_repair_from_user'),
     InlineKeyboardButton(text='Без ремонта', callback_data='Without_repair')],
    [InlineKeyboardButton(text='Без разницы', callback_data='any_repair')]
])


repair_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='С ремонтом', callback_data='With_repair_edit'),
     InlineKeyboardButton(text='Без ремонта', callback_data='Without_repair_edit')],
    [InlineKeyboardButton(text='Без разницы', callback_data='any_repair_edit')]
])


bath = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Cовмещенный', callback_data='with'),
     InlineKeyboardButton(text='Раздельный', callback_data='without')],
    [InlineKeyboardButton(text='Без разницы', callback_data='Any_count_bath')]
])


bath_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='bath_1_edit'),
     InlineKeyboardButton(text='2', callback_data='bath_2_edit')],
    [InlineKeyboardButton(text='Любое количество', callback_data='Any_count_bath_edit')]
])


balcony = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Есть', callback_data='balcony_have'),
     InlineKeyboardButton(text='Отсутствует', callback_data='balcony_none')],
    [InlineKeyboardButton(text='Без разницы', callback_data='Any_balcony_type')]
])


balcony_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Балкон', callback_data='balcony_type_edit'),
     InlineKeyboardButton(text='Лоджия', callback_data='loggia_type_edit')],
    [InlineKeyboardButton(text='Любой', callback_data='Any_balcony_type_edit')]
])


price = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Без ограничения', callback_data='any_price')]
])

keyboard_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️', callback_data='back_show_more'),
     InlineKeyboardButton(text="Показать 10", callback_data="show_more"),
     InlineKeyboardButton(text="➡️", callback_data="next_show_more")],
    [InlineKeyboardButton(text='Сохранить избранное', callback_data='save_show_more')]
])

tiktok = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Открыть тик ток", web_app=WebAppInfo(url="https://www.tiktok.com/"))]
])

price_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Без ограничения', callback_data='any_price_edit')]
])


complete_buy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🔎 Поиск', callback_data='complete_buy_search'),
     InlineKeyboardButton(text='🔄 Редактировать', callback_data='edit_buy_search')]
])


edit_buy_search = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Район', callback_data='raion_edit'),
     InlineKeyboardButton(text='Количество комнат', callback_data='count_rooms_edit')],
    [InlineKeyboardButton(text='Площадь от',  callback_data='kvadrat_ot_edit'),
     InlineKeyboardButton(text='Площадь до',  callback_data='kvadrat_do_edit')],
    [InlineKeyboardButton(text='Этаж', callback_data='floor_edit'),
     InlineKeyboardButton(text='Тип ремонта', callback_data='repair_edit')],
    [InlineKeyboardButton(text='Количество санузлов', callback_data='bath_edit'),
     InlineKeyboardButton(text='Тип балкона',  callback_data='balcony_edit')],
    [InlineKeyboardButton(text='Бюджет',  callback_data='price_edit')]
])