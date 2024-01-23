import subprocess
import os
import json
from database.database_manager import DatabaseManager
from Pars_cities_run.classes import NMarketParser
import time
import concurrent.futures



def run_parser(city):
    username = '79186779096'
    password = '425342R2r2'
    file_name = f'{city}.html'
    save_path = '/home/aleksandr/PycharmProjects/Rielt_bot/pars_file'
    db_manager = DatabaseManager(host='localhost', user='nmarket', password='10021999', database='your_database')
    parser = NMarketParser(username=username, password=password,
                           city_name=city, file_name=file_name, save_path=save_path,db_manager=db_manager)

    print(f'Начинаю парсинг для города: {city}')
    start_time = time.time()  # Засекаем время начала парсинга
    parser.clear_file()
    parser.parse_nmarket()
    end_time = time.time()  # Засекаем время завершения парсинга
    elapsed_time = end_time - start_time
    print(f'Парсинг для города {city} завершен. Время выполнения: {elapsed_time:.2f} сек.\n')


if __name__ == "__main__":
    cities = [
        'Москва',
        'Санкт-Петербург',
        'Владимир',
        'Воронеж',
        'Дальний Восток',
        'Екатеринбург',
        'Ижевск',
        'Казань',
        'Калининград',
        'Киров',
        'Краснодар',
        'Крым',
        'Липецк',
        'Нижний Новгород',
        'Новосибирск',
        'Пенза',
        'Пермь',
        'Ростов-на-Дону',
        'Самара',
        'Уфа',
        'Челябинск',
        'Черноморское побережье'
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Получаем итератор по завершенным задачам
        futures = [executor.submit(run_parser, city) for city in cities]
        for future in concurrent.futures.as_completed(futures):
            # Получаем результаты, если нужно
            result = future.result()


def run_scrapy_script(spider_name, output_directory):
    # Переходим в директорию проекта Scrapy
    project_directory = "/home/aleksandr/PycharmProjects/Rielt_bot/nmarket_pars/"
    os.chdir(project_directory)

    # Формируем команды
    command1 = "scrapy crawl {spider_name} -o {output_directory}results.json".format(
        spider_name=spider_name,
        output_directory=output_directory
    )

    try:
        # Запускаем команды
        subprocess.run(command1, shell=True, check=True)
        print(f"Spider '{spider_name}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running spider '{spider_name}': {e}")


if __name__ == "__main__":
    spider_name = "nmarket_parsing"
    output_directory = "/home/aleksandr/PycharmProjects/Rielt_bot/pars_result/"

    run_scrapy_script(spider_name, output_directory)


db_manager = DatabaseManager(host='localhost', user='nmarket', password='10021999', database='your_database')

db_manager.create_telegram_users_table()


def create_table_from_json(json_file_path, db_manager, clear_table=True):
    table_name = os.path.splitext(os.path.basename(json_file_path))[0]
    table_name = table_name.replace(' ', '_').replace('-', '_')

    # Очистка таблицы перед записью новых данных (если clear_table=True)
    if clear_table:
        db_manager.clear_real_estate_table(table_name)

    db_manager.create_real_estate_table(table_name)

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    for entry in data:
        db_manager.insert_real_estate_data(table_name, {
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

db_manager = DatabaseManager(host='localhost', user='nmarket', password='10021999', database='your_database')

for json_file in json_files:
    create_table_from_json(os.path.join(directory_path, json_file), db_manager, clear_table=True)

db_manager.close_connection()


