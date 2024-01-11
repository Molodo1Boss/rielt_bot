from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
import time

def open_city_tab(driver, city_name):
    time.sleep(3)

    try:
        # Нажимаем на кнопку выбора города
        button_city = driver.find_element(By.CLASS_NAME, "nm-location-btn__text")
        driver.execute_script("arguments[0].click();", button_city)
        print('Открыт список городов')

        # Ждем появления списка городов
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "nm-location__list")))

        # Ищем город в списке и кликаем на него
        city_element = driver.find_element(By.XPATH, f"//button[contains(@class, 'nm-location__link') and contains(text(), '{city_name}')]")
        driver.execute_script("arguments[0].click();", city_element)
        print(f'Выбран город: {city_name}')
    except NoSuchElementException:
        print(f'Элемент для города {city_name} не найден')


def save_html_to_file(html_content, file_path="file.html", overwrite=False):
    mode = 'a+' if overwrite else 'w'
    with open(file_path, mode, encoding="utf-8") as file:
        try:
            file.seek(0, 2)
            file.write(html_content)
        except Exception as e:
            print(f'Ошибка при записи в файл: {str(e)}')


def pars_nmarket_msc():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')  # Добавляем опцию для headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://auth.nmarket.pro/Account/Login?errorId'
               '=CfDJ8PJK9gY43RtApKh3q2Ywc6sZOVGhvzWfrqyDKAcOQTvhMchEClsSEvRIXcTab0'
        'gpgeS9BA_uZGbLFxJDENUbk3EQnum2MPaGcLE65G_OCXqtSaPf__1onhpGiDTbA9VArFiMGQse-1AIX7mPCd9jHDff2gmU'
               '-kD5dJBv2WAbtcvQS'
        'mqpt2l-Pvrp8H-_RqxkRNSxhh7WbekgdczZ9imSn75oBZchSeqoP9IWRKab8KHqZLmEARU8uW6tUO2OohQ23SlVxwRK5L3Pi4QcPr'
        'LPcKxSdbMXw2qf6ppT4nLRjsiLHeHDYIQw1EOlRR7V00IAZ3IAqH4ql8QVeVFFPgzT7pc')
    print('Загрузка страницы авторизации')

    # Ожидание появления полей ввода логина и пароля
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'login-input')))

    # Поиск полей для логина и пароля
    login = driver.find_element(By.XPATH, "//input[@id='login-input']")
    password = driver.find_element(By.XPATH, "//input[@id='mat-input-1']")

    # Ввод логина и пароля
    login.send_keys('79186779096')
    print('Авторизация...')
    password.send_keys('425342R2r2')

    # Поиск кнопки логина и нажатие на кнопку
    login_btn = driver.find_element(By.XPATH, "//button[@id='login_username_click']")
    login_btn.click()

    try:
        print(f'Ожидаю появления рекламы...')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                        "//div[@class='popmechanic-close']")))
        print(f'Реклама появилась. Жду 3 секунды...')
        time.sleep(3)


        # Проверка, какая реклама появилась
        if EC.presence_of_element_located((By.XPATH, "//div[@class='popmechanic-close']")):
            # Поиск кнопки закрытия рекламы и нажатие на кнопку
            close_btn = driver.find_element(By.XPATH, "//div[@class='popmechanic-close']")
            time.sleep(3)
            close_btn.click()
            print(f'Закрыл рекламу с классом "popmechanic-close"')

    except TimeoutException:
        print(f'Реклама не появилась в течение 10 секунд')

    cookies = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,
                                                                              'analytics_cookies_consent')))
    cookies.click()
    print(f'Принял просмотр cookie')

    # Поиск кнопки для перехода на вкладку ресейл квартир
    print(f'Перехожу во вкладку "Ресейл"')
    resale_btn = driver.find_element(By.XPATH, "//html/body/nm-general-header/div/div/ul/li[3]/a")
    time.sleep(3)
    resale_btn.click()

    try:
        print(f'Ожидаю появления рекламы...')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                        ((By.XPATH, "//div[@class='popmechanic-close']")))
        print(f'Реклама появилась. Жду 3 секунды...')
        close_btn = driver.find_element(By.XPATH, "//div[@class='popmechanic-close']")
        time.sleep(3)
        close_btn.click()
        print(f'Закрыл рекламу, начинаю парсинг')
    except TimeoutException:
        print(f'Реклама в ресейле не появилась в течение 10 секунд, перехожу к следующему шагу')

    button_reg = driver.find_element(By.CLASS_NAME, "nm-location-btn__text")
    driver.execute_script("arguments[0].click();", button_reg)
    time.sleep(3)
    open_city_tab(driver, 'Москва')

    try:
        print(f'Ожидаю появления рекламы...')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                        "//div[@class='popmechanic-close']")))
        print(f'Реклама появилась. Жду 3 секунды...')
        time.sleep(3)

        # Проверка, какая реклама появилась
        if EC.presence_of_element_located((By.XPATH, "//div[@class='popmechanic-close']")):
            # Поиск кнопки закрытия рекламы и нажатие на кнопку
            close_btn = driver.find_element(By.XPATH, "//div[@class='popmechanic-close']")
            time.sleep(3)
            close_btn.click()
            print(f'Закрыл рекламу с классом "popmechanic-close"')

    except TimeoutException:
        print(f'Реклама не появилась в течение 10 секунд')

    page_number = 1
    card_number = 1

    clean = 'Начало парсинга:'
    file_path = "file.html"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(clean)
        print("vladimir.html очищен для записи новых данных")
        file.close()

    while True:
        try:
            # Переходим на следующую страницу, если не первая страница
            if page_number > 1:
                button = driver.find_element(By.CLASS_NAME, "card-pagination__btn_next")
                driver.execute_script("arguments[0].click();", button)
                print(f"\rВыполнен переход на страницу № {page_number}, ожидание загрузки")

                # Ждем, пока новая страница полностью загрузится
                (WebDriverWait(driver, 30).
                 until(EC.presence_of_element_located((
                    By.XPATH, "//div[@class='catalog-table-cell catalog-table-cell_photo ng-star-inserted']"
                              "/div[@class='catalog-table-cell__photo-wrapper ng-star-inserted']"))))
                time.sleep(3)  # Дополнительное время на загрузку элементов

            # Получаем список окон перед началом цикла
            original_windows = driver.window_handles

            # Обновляем список элементов на текущей странице
            elements = (driver.find_elements
                        (By.XPATH,
                         ".//div[@class='catalog-table-cell catalog-table-cell_photo ng-star-inserted']"
                         "/div[@class='catalog-table-cell__photo-wrapper ng-star-inserted']"))

            # Перебираем все элементы и открываем их в новых вкладках
            for element in elements:
                # Кликаем по элементу
                time.sleep(3)
                element.click()

                # Ждем, пока новое окно не будет доступно
                WebDriverWait(driver, 10).until(
                    lambda driver: set(driver.window_handles) - set(original_windows)
                )

                # Получаем новое окно (последняя открытая вкладка)
                new_window = [window for window in driver.window_handles if window not in original_windows][0]
                driver.switch_to.window(new_window)

                # Ждем загрузки новой страницы
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                "//div[@class='object-body__main']")))

                # Дополнительное ожидание после загрузки страницы
                time.sleep(3)

                # Получаем HTML страницы
                html_content = driver.page_source

                # Сохраняем HTML в файл
                save_html_to_file(html_content, file_path=file_path, overwrite=True)
                print(html_content)

                # Закрываем вкладку
                driver.close()

                # Переключаемся обратно на первоначальные вкладки
                driver.switch_to.window(original_windows[0])

                print(f'Сохранено объявление № {card_number}')
                card_number += 1

            page_number += 1  # Увеличиваем номер страницы

        except (NoSuchElementException, TimeoutException):
            print('Объявления на странице закончились.')
            break  # Выход из цикла, если объявления закончились

        except ElementClickInterceptedException:
            print(f'Ошибка: Не удалось кликнуть на элемент. Попробуйте другую стратегию.')
            continue  # Продолжаем с следующим элементом

    print("Сохранение завершено. Файл закрыт.")
    driver.quit()


    time.sleep(150)
    driver.quit()


pars_nmarket_msc()
