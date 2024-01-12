from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
import os


class NMarketParser:
    def __init__(self, username, password, city_name, file_name, save_path):
        self.username = username
        self.password = password
        self.city_name = city_name
        self.file_name = file_name
        self.save_path = save_path
        self.driver = None

    def clear_file(self):
        file_path = os.path.join(self.save_path, self.file_name)

        try:
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write('')  # Просто очистим содержимое файла
            print(f'Файл {self.file_name} успешно очищен.')

        except Exception as e:
            print(f'Ошибка при очистке файла: {str(e)}. Город {self.city_name}')

    def initialize_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get('https://auth.nmarket.pro/Account/Login?errorId=CfDJ8PJK9gY43RtApKh3q2Ywc6sZOVGhvzWfrqyDKAcOQTvhMchEClsSEvRIXcTab0'
                        'gpgeS9BA_uZGbLFxJDENUbk3EQnum2MPaGcLE65G_OCXqtSaPf__1onhpGiDTbA9VArFiMGQse-1AIX7mPCd9jHDff2gmU'
                        '-kD5dJBv2WAbtcvQS'
                        'mqpt2l-Pvrp8H-_RqxkRNSxhh7WbekgdczZ9imSn75oBZchSeqoP9IWRKab8KHqZLmEARU8uW6tUO2OohQ23SlVxwRK5L3Pi4QcPr'
                        'LPcKxSdbMXw2qf6ppT4nLRjsiLHeHDYIQw1EOlRR7V00IAZ3IAqH4ql8QVeVFFPgzT7pc')
        print('Загрузка страницы авторизации')

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'login-input')))
        login = self.driver.find_element(By.XPATH, "//input[@id='login-input']")
        password = self.driver.find_element(By.XPATH, "//input[@id='mat-input-1']")

        login.send_keys(self.username)
        print(f'Авторизация.... Город {self.city_name}')
        password.send_keys(self.password)
        login_btn = self.driver.find_element(By.XPATH, "//button[@id='login_username_click']")
        login_btn.click()

    def close_advertisement(self):
        try:
            print(f'Ожидаю появления рекламы... Город {self.city_name}')
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='popmechanic-close']")))
            print(f'Реклама появилась. Жду 3 секунды... Город {self.city_name}')
            time.sleep(3)
            if EC.presence_of_element_located((By.XPATH, "//div[@class='popmechanic-close']")):
                close_btn = self.driver.find_element(By.XPATH, "//div[@class='popmechanic-close']")
                time.sleep(3)
                close_btn.click()
                print(f'Закрыл рекламу с классом "popmechanic-close". Город {self.city_name}')

        except TimeoutException:
            print(f'Реклама не появилась в течение 10 секунд. Город {self.city_name}')

    def accept_cookies(self):
        try:
            cookies = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'analytics_cookies_consent')))
            cookies.click()
            print(f'Принял просмотр cookie. Город {self.city_name}')

        except TimeoutException:
            print(f'Не удалось найти кнопку принятия cookie в течение 10 секунд. Город {self.city_name}')

    def navigate_to_resale_tab(self):
        print(f'Перехожу во вкладку "Ресейл". Город {self.city_name}')
        resale_btn = self.driver.find_element(By.XPATH, "//html/body/nm-general-header/div/div/ul/li[3]/a")
        self.driver.execute_script("arguments[0].click();", resale_btn)

    def open_city_tab(self):
        time.sleep(1)
        try:
            button_city = self.driver.find_element(By.CLASS_NAME, "nm-location-btn__text")
            self.driver.execute_script("arguments[0].click();", button_city)
            print(f'Открыт список городов. Город {self.city_name}')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "nm-location__list")))
            city_element = self.driver.find_element(By.XPATH,
                                                    f"//button[contains(@class, 'nm-location__link') and contains(text(), '{self.city_name}')]")
            self.driver.execute_script("arguments[0].click();", city_element)
            print(f'Выбран город: {self.city_name}')
            self.driver.refresh()
        except NoSuchElementException:
            print(f'Элемент для города {self.city_name} не найден')

    def save_html_to_file(self, html_content):
        file_path = os.path.join(self.save_path, self.file_name)

        with open(file_path, 'a', encoding="utf-8") as file:
            try:
                file.write(html_content + '\n\n')  # Добавим пустые строки между объявлениями
            except Exception as e:
                print(f'Ошибка при записи в файл: {str(e)}')

    def click_and_wait(self, element):
        original_windows = self.driver.window_handles
        element.click()

        # Ждем, пока появится новое окно или загрузится страница объявления
        WebDriverWait(self.driver, 10).until(
            lambda driver: set(driver.window_handles) - set(original_windows) or
                           EC.presence_of_element_located((By.XPATH, "//div[@class='object-body__main']"))
        )

        new_windows = set(self.driver.window_handles) - set(original_windows)
        if new_windows:
            new_window = new_windows.pop()
            self.driver.switch_to.window(new_window)

            WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='object-body__main']"))
            )

        else:
            WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='object-body__main']"))
            )

        new_windows = set(self.driver.window_handles) - set(original_windows)
        if new_windows:
            new_window = new_windows.pop()
            self.driver.switch_to.window(new_window)
            WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='object-body__main']"))
            )

    def parse_page(self):
        page_number = 1
        card_number = 1

        while True:
            try:
                if page_number > 1:
                    button = self.driver.find_element(By.CLASS_NAME, "card-pagination__btn_next")
                    self.driver.execute_script("arguments[0].click();", button)
                    print(f"\rВыполнен переход на страницу № {page_number}, ожидание загрузки. Город {self.city_name}")

                    WebDriverWait(self.driver, 300).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        "//div[@class='catalog-table-cell catalog-table-cell_photo ng-star-inserted']"
                                                        "/div[@class='catalog-table-cell__photo-wrapper ng-star-inserted']")))
                    time.sleep(3)

                original_windows = self.driver.window_handles
                elements = self.driver.find_elements(
                    By.XPATH,
                    ".//div[@class='catalog-table-cell catalog-table-cell_photo ng-star-inserted']"
                    "/div[@class='catalog-table-cell__photo-wrapper ng-star-inserted']")

                for element in elements:
                    time.sleep(3)
                    self.click_and_wait(element)

                    WebDriverWait(self.driver, 10).until(
                        lambda driver: set(self.driver.window_handles) - set(original_windows)
                    )

                    new_window = [window for window in self.driver.window_handles if window not in original_windows][0]
                    self.driver.switch_to.window(new_window)

                    WebDriverWait(self.driver, 50).until(
                        EC.presence_of_element_located((By.XPATH, "//div[@class='object-body__main']"))
                    )

                    html_content = self.driver.page_source
                    self.save_html_to_file(html_content)

                    self.driver.close()
                    self.driver.switch_to.window(original_windows[0])

                    print(f'Сохранено объявление № {card_number} на странице {page_number}. Город {self.city_name}')
                    card_number += 1

                page_number += 1

            except (NoSuchElementException, TimeoutException):
                print(f'Объявления на странице закончились. Город {self.city_name}')
                break

            except ElementClickInterceptedException:
                print(f'Ошибка: Не удалось кликнуть на элемент. Попробуйте другую стратегию. Город {self.city_name}')
                continue

            print(f"Сохранение завершено. Файл закрыт. Город {self.city_name}")

        print(f"Сохранение завершено. Файл закрыт. Город {self.city_name}")

    def parse_nmarket(self):
        try:
            self.initialize_driver()
            self.login()
            self.close_advertisement()
            self.accept_cookies()
            self.navigate_to_resale_tab()
            self.open_city_tab()
            self.close_advertisement()
            self.parse_page()

        finally:
            if self.driver:
                self.driver.quit()


if __name__ == "__main__":
    username = '79186779096'
    password = '425342R2r2'
    city_name = 'Москва'
    file_name = 'msc123123.html'
    save_path = '/home/aleksandr/PycharmProjects/Rielt_bot/Pars_cities_run'
    parser = NMarketParser(username=username, password=password, city_name=city_name, file_name=file_name,
                           save_path=save_path)
    parser.clear_file()
    parser.parse_nmarket()
