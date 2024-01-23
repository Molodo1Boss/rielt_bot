import os
import json
import aiomysql
import mysql.connector
from aiomysql import create_pool, Pool


import os
import json
import mysql.connector


'''
ОБЫЧНЫЙ КЛАСС ДЛЯ РАБОТЫ С БД
'''


class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_real_estate_table(self, table_name):
        # Создаем таблицу для объявлений
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city TEXT NOT NULL,
                offer_id VARCHAR(255) NOT NULL,  -- Указываем явно длину ключа
                image_1 VARCHAR(255),
                image_2 VARCHAR(255),
                image_3 VARCHAR(255),
                image_4 VARCHAR(255),
                image_5 VARCHAR(255),
                image_6 VARCHAR(255),
                address VARCHAR(255),
                floor VARCHAR(255),
                total_area VARCHAR(255),
                kitchen_area VARCHAR(255),
                rooms VARCHAR(255),
                balcony VARCHAR(255),
                bathroom VARCHAR(255),
                repair_type VARCHAR(255),
                house_type VARCHAR(255),
                elevator VARCHAR(255),
                total_price VARCHAR(255),
                price_per_square_meter VARCHAR(255),
                contract VARCHAR(255),
                deal_type VARCHAR(255),
                maternity_capital VARCHAR(255),
                agent VARCHAR(255),
                description TEXT,
                UNIQUE KEY unique_offer_id (offer_id(255))  -- Указываем явно длину ключа
            );
        ''')
        self.conn.commit()

    def clear_real_estate_table(self, table_name):
        # Очищаем таблицу real_estate
        self.cursor.execute(f'DELETE FROM {table_name};')
        self.conn.commit()

    def create_telegram_users_table(self):
        # Создаем таблицу для пользователей Telegram
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS telegram_users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                username VARCHAR(255),
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                chat_id INT NOT NULL,
                UNIQUE KEY unique_user_id (user_id, chat_id)
            );
        ''')
        self.conn.commit()

    def insert_real_estate_data(self, table_name, data):
        # Вставляем данные в базу данных
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, list(data.values()))
        self.conn.commit()

    def insert_user_data(self, user_data):
        # Вставляем данные о пользователе в таблицу
        self.cursor.execute('''
            INSERT INTO telegram_users (user_id, username, first_name, last_name, chat_id)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE username = VALUES(username), first_name = VALUES(first_name), last_name = VALUES(last_name)
        ''', (
            user_data.get('id'),
            user_data.get('username'),
            user_data.get('first_name'),
            user_data.get('last_name'),
            user_data.get('chat_id')
        ))
        self.conn.commit()

    def close_connection(self):
        # Закрываем соединение с базой данных
        self.conn.close()

    def create_table_from_json(self, json_filename):

        table_name = os.path.splitext(json_filename)[0]
        self.create_real_estate_table(table_name)

"""
ЗАКОМЕНТИРОВАННЫЙ ФРАГМНЕТ, ЧЕРНОВИК СТАРОГО КОДА ПРИ ПОПЫТКИ НАПИСАНИЯ АСИНХРОННОГО ПОДХОДА
"""


# class BaseDatabaseManager:
#     def create_real_estate_table(self, table_name):
#         raise NotImplementedError
#
#     def clear_real_estate_table(self, table_name):
#         raise NotImplementedError
#
#     def create_telegram_users_table(self):
#         raise NotImplementedError
#
#     def insert_real_estate_data(self, table_name, data):
#         raise NotImplementedError
#
#     def insert_user_data(self, user_data):
#         raise NotImplementedError
#
#     def close_connection(self):
#         raise NotImplementedError
#
#     def create_table_from_json(self, json_filename, batch_size=10):
#         raise NotImplementedError


'''
АСИНХРОННЫЙ КЛАСС ДЛЯ РАБОТЫ С БД
'''


class AsyncDatabaseManager:
    def __init__(self, loop, host, user, password, database):
        self.loop = loop
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.pool = None

    def is_pool_created(self):
        return self.pool is not None

    async def create_pool(self) -> Pool:
        self.pool = await create_pool(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.database
        )
        return self.pool

    async def initialize(self):
        if self.pool is None:
            raise Exception("Ошибка: pool не инициализирован.")
        # Дополнительная инициализация, если необходимо

    async def connect(self):
        if self.pool is None:
            raise Exception("Ошибка: pool не инициализирован.")
        await self.pool.acquire()

    async def close(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()

    async def create_real_estate_table(self, table_name):
        # Создание таблицы недвижимости
        query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city TEXT NOT NULL,
                offer_id VARCHAR(255) NOT NULL,
                image_1 VARCHAR(255),
                image_2 VARCHAR(255),
                image_3 VARCHAR(255),
                image_4 VARCHAR(255),
                image_5 VARCHAR(255),
                image_6 VARCHAR(255),
                address VARCHAR(255),
                floor VARCHAR(255),
                total_area VARCHAR(255),
                kitchen_area VARCHAR(255),
                rooms VARCHAR(255),
                balcony VARCHAR(255),
                bathroom VARCHAR(255),
                repair_type VARCHAR(255),
                house_type VARCHAR(255),
                elevator VARCHAR(255),
                total_price VARCHAR(255),
                price_per_square_meter VARCHAR(255),
                contract VARCHAR(255),
                deal_type VARCHAR(255),
                maternity_capital VARCHAR(255),
                agent VARCHAR(255),
                description TEXT,
                UNIQUE KEY unique_offer_id (offer_id(255))
            ) ENGINE=InnoDB;
        '''
        await self.execute(query)
        await self.commit()

    async def clear_real_estate_table(self, table_name):
        # Очистка таблицы недвижимости
        query = f'DELETE FROM {table_name};'
        await self.execute(query)
        await self.commit()

    async def create_telegram_users_table(self):
        # Создание таблицы пользователей телеграм
        query = '''
            CREATE TABLE IF NOT EXISTS telegram_users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                username VARCHAR(255),
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                chat_id INT NOT NULL,
                UNIQUE KEY unique_user_id (user_id, chat_id)
            );
        '''
        await self.execute(query)
        await self.commit()

    async def insert_real_estate_data(self, table_name, data):
        # Вставка данных недвижимости
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        try:
            await self.execute(query, *list(data.values()))
            await self.commit()
        except Exception as e:
            print(f"Error during insertion: {e}")
            await self.rollback()

    async def insert_user_data(self, user_data):
        # Вставка данных пользователя телеграм
        query = '''
            INSERT INTO telegram_users (user_id, username, first_name, last_name, chat_id)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE username = VALUES(username), first_name = VALUES(first_name), last_name = VALUES(last_name)
        '''
        await self.execute(query, (
            user_data.get('id'),
            user_data.get('username'),
            user_data.get('first_name'),
            user_data.get('last_name'),
            user_data.get('chat_id')
        ))
        await self.commit()

    async def create_table_from_json(self, json_filename, batch_size=10):
        # Создание таблицы из JSON
        table_name = os.path.splitext(json_filename)[0]
        await self.create_real_estate_table(table_name)

        with open(json_filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            for entry in batch:
                await self.insert_real_estate_data(table_name, {
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

        print(f"Inserted {len(data)} rows into {table_name}")

