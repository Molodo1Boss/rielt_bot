from classes import NMarketParser


if __name__ == "__main__":
    username = '79186779096'
    password = '425342R2r2'
    city_name = 'Крым'
    file_name = 'krim.html'
    save_path = '/home/aleksandr/PycharmProjects/Rielt_bot/pars_file'
    parser = NMarketParser(username=username, password=password, city_name=city_name, file_name=file_name,
                           save_path=save_path)

    parser.parse_nmarket()