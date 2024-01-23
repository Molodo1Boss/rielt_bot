# test.py
'''

ТЕСТОВЫЙ ФАЙЛ, ЗДЕСЬ КОД ЗАПИСИ ДАННЫХ В БД ИЗ JSON ФАЙЛОВ

'''
import json
import os
import asyncio
from database.database_manager import AsyncDatabaseManager

async def main():
    db_manager = AsyncDatabaseManager(loop=asyncio.get_event_loop(), host='localhost', user='nmarket', password='10021999', database='your_database')

    await db_manager.connect()

    await db_manager.create_telegram_users_table()

    async def create_table_from_json(json_file_path, db_manager, clear_table=True):
        table_name = os.path.splitext(os.path.basename(json_file_path))[0]
        table_name = table_name.replace(' ', '_').replace('-', '_')

        if clear_table:
            await db_manager.clear_real_estate_table(table_name)

        await db_manager.create_real_estate_table(table_name)

        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        for entry in data:
            await db_manager.insert_real_estate_data(table_name, {
                'city': entry.get('City', ''),
                'offer_id': entry.get('ID', ''),
                'image_1': entry.get('Изображение 1', ''),
                'image_2': entry.get('Изображение 2', ''),
                'image_3': entry.get('Изображение 3', ''),
                'image_4': entry.get('Изображение 4', ''),
                'image_5': entry.get('Изображение 5', ''),
                'image_6': entry.get('Изображение 6', ''),
                'address': entry.get('Адрес', ''),
                'floor': entry.get('Этаж', ''),
                'total_area': entry.get('Общая площадь', ''),
                'kitchen_area': entry.get('Площадь кухни', ''),
                'rooms': entry.get('Количество комнат', ''),
                'balcony': entry.get('Балкон', ''),
                'bathroom': entry.get('Санузел', ''),
                'repair_type': entry.get('Тип ремонта', ''),
                'house_type': entry.get('Тип дома', ''),
                'elevator': entry.get('Лифт', ''),
                'total_price': entry.get('Полная стоимость', ''),
                'price_per_square_meter': entry.get('Стоимость м²', ''),
                'contract': entry.get('Договор', ''),
                'deal_type': entry.get('Тип сделки', ''),
                'maternity_capital': entry.get('Материнский капитал', ''),
                'agent': entry.get('Агент', ''),
                'description': entry.get('Описание', '')
            })

    directory_path = '/home/aleksandr/PycharmProjects/Rielt_bot/pars_result/'
    json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]

    for json_file in json_files:
        await create_table_from_json(os.path.join(directory_path, json_file), db_manager, clear_table=True)

    await db_manager.disconnect()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
