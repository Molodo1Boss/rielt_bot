from classes import NMarketParser
import concurrent.futures
import time
import subprocess

def run_parser(city):
    username = '79186779096'
    password = '425342R2r2'
    file_name = f'{city}.html'
    save_path = '/home/aleksandr/PycharmProjects/Rielt_bot/pars_file'

    parser = NMarketParser(username=username, password=password, city_name=city, file_name=file_name, save_path=save_path)

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
        executor.map(run_parser, cities)


def run_scrapy_script(spider_name, output_directory):
    command = f"scrapy crawl {spider_name} -o {output_directory}"

    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Spider '{spider_name}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running spider '{spider_name}': {e}")


if __name__ == "__main__":
    spider_name = "nmarket_parsing"
    output_directory = "/home/aleksandr/PycharmProjects/Rielt_bot/pars_result/"

    run_scrapy_script(spider_name, output_directory)
