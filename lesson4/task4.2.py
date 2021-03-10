# Задание 2. Курс Валюты
# Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
# Код валюты может быть в произвольном регистре.
# Функция должна возвращать результат числового типа, например float.
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
# http://www.cbr.ru/scripts/XML_daily.asp.
#
# Выведите на экран курсы для доллара и евро, используя написанную функцию.


import requests
r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp.')
print(r.status_code,r.content.decode('utf-8'))
# # Внутри созданного проекта создаем новый файл с названием main.py. После этого сразу же через терминал выполняем установку библиотек: requests, а также beautiful soup.
# #
# # pip install requests bs4
# # Библиотека requests позволяет обращаться к необходимому сайту и копировать всю его HTML разметку. Внутри HTML разметки выбрать нужные данные очень сложно, если использовать стандартные функции Python по типу: replace, join и прочих. Поэтому мы используем вторую библиотеку beautiful soup для быстрой и комфортной выборки необходимых данных из HTML.
# #
# #
# #
# # Далее нам необходимо прописать весь код для корректной работы нашей программы. Весь код показан ниже:
#
# import requests  # Модуль для обработки URL
# # import time  # Модуль для остановки программы
# # import smtplib  # Модуль для работы с почтой
# # Основной класс
# class Currency:
#     # Ссылка на нужную страницу
#     DOLLAR_RUB = 'http://www.cbr.ru/scripts/XML_daily.asp'
#     # Заголовки для передачи вместе с URL
#     # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#     current_converted_price = 0
#     # difference = 5  # Разница после которой будет отправлено сообщение на почту
#
#     def __init__(self):
#         # Установка курса валюты при создании объекта
#         self.current_converted_price = float(self.get_currency_rate().replace(",", "."))
#
#     # Метод для получения курса валюты
#     def get_currency_rate(self):
#         # Парсим всю страницу
#         full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
#
#         # Разбираем через BeautifulSoup
#         # soup = BeautifulSoup(full_page.content, 'html.parser')
#
#         # Получаем нужное для нас значение и возвращаем его
#         convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
#         return convert[0].text
#
#     # Проверка изменения валюты
#     def check_currency(self):
#         currency = float(self.get_currency_price().replace(",", "."))
#         if currency >= self.current_converted_price + self.difference:
#             print("Курс сильно вырос, может пора что-то делать?")
#             self.send_mail()
#         elif currency <= self.current_converted_price - self.difference:
#             print("Курс сильно упал, может пора что-то делать?")
#             self.send_mail()
#
#         print("Сейчас курс: 1 доллар = " + str(currency))
#         time.sleep(3)  # Засыпание программы на 3 секунды
#         self.check_currency()
#
#     # Отправка почты через SMTP
#     def send_mail(self):
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.ehlo()
#
#         server.login('ВАША ПОЧТА', 'ПАРОЛЬ')
#
#         subject = 'Currency mail'
#         body = 'Currency has been changed!'
#         message = f'Subject: {subject}\n{body}'
#
#         server.sendmail(
#             'От кого',
#             'Кому',
#             message
#         )
#         server.quit()
#
#
# # Создание объекта и вызов метода
# currency = Currency()
# currency.check_currency()
