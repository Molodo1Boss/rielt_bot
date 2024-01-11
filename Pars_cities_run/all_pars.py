from classes import NMarketParser

if __name__ == "__main__":
    cities = ['Ростов-на-Дону', 'Владимир', 'Москва', 'Санкт-Петербург']

    username = '79186779096'
    password = '425342R2r2'
    save_path = '/pars_file'

    for city_name in cities:
        file_name = f'{city_name.lower()}.html'
        parser = NMarketParser(username=username, password=password, city_name=city_name, file_name=file_name,
                               save_path=save_path)

        parser.parse_nmarket()

