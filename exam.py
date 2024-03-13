# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: легкая)
# Вы должны спарсить сайт https://www.kivano.kg/mobilnye-telefony. Как результат вы должны получить:
# 1. Наименование всех телефонов
# 2. Цену каждого продукта(в KGS)
# 3. И ссылка к фотографии
# 4. Все это записать в CSV файл
# Дополнительно(по желанию):
# 1. Ваш парсинг скрипт должен выполняться каждые 60 минут


from bs4 import BeautifulSoup 
import requests
import csv
import pprint

# url = 'https://www.kivano.kg/mobilnye-telefony'

# def parsing_data(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     container = soup.find('div', class_ = 'product-index product-index oh')
#     gadjets = container.find_all('div', class_ = 'item product_listbox oh')
#     result = []
#     for tel in gadjets:
#         name = tel.find('div', class_ = 'listbox_title oh').text.strip()
#         price = tel.find('div', class_ = 'listbox_price text-center').find('strong').text
#         try:
#             img = tel.find('img').get('src') #img = car.find('img').get('src')
#         except Exception as e:
#             img = f'No image, {e}!'
#         data = {'title': name, 'price': price, 'img': img}
#         result.append(data)
#     return result
# pprint.pprint(parsing_data(url))

# def excel():
#     with open('gadjets.csv', 'w') as file:
#         fieldname = ['№', 'name', 'price', 'img']
#         writer = csv.DictWriter(file, fieldname)
#         writer.writerow({
#             '№': '№',
#             'name': 'Name',
#             'price': 'Price: ',
#             'img': 'Image URL' 
#         })
# excel()

# count = 1
# def write_csv(data: list):
#     with open('gadjets.csv', 'a') as file:
#         global count
#         fieldname = ['№', 'name', 'price', 'img']
#         writer = csv.DictWriter(file, fieldname)
#         for telefon in data:
#             writer.writerow ({
#             '№': count,
#             'name': telefon['title'],
#             'price': telefon['price'],
#             'img': telefon['img'] 
#             })
#             count +=1
# write_csv(parsing_data(url))

# def get_last_page(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     pages = soup.find('li', class_= 'last').text
#     return int(pages)
# # print(get_last_page(url))


# url = f'https://www.kivano.kg/mobilnye-telefony'
# last_page = get_last_page(url)
# print(last_page)

# i = 1
# while i <= last_page :#last_page:
#     page_url = f'https://www.kivano.kg/mobilnye-telefony?page={i}'
#     data = parsing_data(url)
#     write_csv(data)
#     print(f'Спарсили {i}/{last_page} pages!')
#     i+=1


# # ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: средняя)
# # ● Спарсить kolesa.kz, категорию: 1.Название всех моделей.
# # 2.Цену всех моделей 3.Изображение всех моделей 4.Краткое описание всех моделей 5.Записать все в csv файл

# url = 'https://kolesa.kz/cars/audi/'

# def parsing_data(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup)
#     container = soup.find('div', class_ = 'a-list')
#     # print(container)
#     cars = container.find_all('div', class_ = 'a-list__item') 
#     # print(cars)
#     result = []
#     for car in cars:
#         try:
#             name = car.find('h5', class_ = 'a-card__title').text # a-card__link
#         except Exception as e:
#             name = f'No name, {e}!'
#         # print(name)
#         try:
#             price = car.find('span', class_ = 'a-card__price').text.strip()
#         except Exception as e:
#             price = f'No price, {e}!'
#         # print(price)
#         try:
#             img = car.find('img').get('src')
#         except Exception as e:
#             img = f'No image, {e}!'
#         # print(img)
#         try:
#             description = car.find('p', class_='a-card__description').text.strip()
#         except Exception as e:
#             description = f'No image, {e}!'
#         # print(description)
#         data = {'title': name, 'description': description, 'price': price, 'img': img}
#         result.append(data)
#     return result
# print(parsing_data(url))


# def prepare_csv():
#     with open('audi.csv', 'w') as file:
#         fieldname = ['№', 'name', 'decription', 'price', 'img']
#         writer = csv.DictWriter(file, fieldname)
#         writer.writerow({
#             '№': '№',
#             'name': 'Name',
#             'decription': 'Decription',
#             'price': 'Price: ',
#             'img': 'Image URL' 
#         })
# prepare_csv()

# count = 1
# def write_to_csv(data: list):
#     with open('audi.csv', 'a') as file:
#         global count
#         fieldname = ['№', 'name', 'decription', 'price', 'img']
#         writer = csv.DictWriter(file, fieldname)
#         for car in data:
#             writer.writerow ({
#             '№': count,
#             'name': car['title'],
#             'decription': car['description'],
#             'price': car['price'],
#             'img': car['img'] 
#             })
#             count +=1
# write_to_csv(parsing_data(url))

# i = 1
# while i <= 7:
#     page_url = f'https://kolesa.kz/cars/audi/?page={i}'
#     data = parsing_data(url)
#     write_to_csv(data)
#     print(f'Спарсили {i} pages!')
#     i+=1


# # ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: тяжелая)
# # 1. При нажатии на кнопку start, телеграмм бот должен зайти на сайт KaktusMedia (https://kaktus.media/) и спарсить категорию “Все новости”
# # 2. При вводе текста должны выйти первые 20 заголовков статей с нумерацией. Должна быть возможность выбрать новости по нумерации или id (по желанию)
# # 3. После выбора новости по нумерации, телеграмм бот должен отправить сообщение в виде “some title news you can see Description of this news
# # and Photo” и пользователь отправит текст (либо нажмет кнопку) Description, то бот должен отправить описание именно текущего поста, также аналогично с Photo.
# # 4. При нажатии на кнопку «Quit» бот должен отправить сообщение “До свидания“


# url = 'https://kaktus.media/?lable=8&date=2024-02-15&order=time'
# count = 0
# def parsing_data(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     container = soup.find('div', class_ = 'Tag--articles')
#     news = container.find_all('div', class_ = 'Tag--article')
#     result = []
#     for i in news:
#         global count
#         name = i.find('a', class_ = 'ArticleItem--name').text.strip()
#         time = i.find('div', class_ = 'ArticleItem--time').text.strip()
#         try:
#             img = i.find('a', class_ = 'ArticleItem--image').find('img').get('src')
#         except Exception as e:
#             img = f'No image, {e}!'
#         data = {'count': count,'title': name, 'time': time, 'img': img}
#         result.append(data)
#         count += 1
#     return result
# # pprint.pprint(parsing_data(url))

# def prepare_csv():
#     with open('news.csv', 'w') as file:
#         fieldname = ['№', 'name', 'time', 'img']
#         writer = csv.DictWriter(file, fieldname)
#         writer.writerow({
#             '№': '№',
#             'time': 'Time',
#             'name': 'Name',
#             'img': 'Image URL' 
#         })
# prepare_csv()

# count = 1
# def write_to_csv(data: list):
#     with open('news.csv', 'a') as file:
#         global count
#         fieldname = ['№', 'name', 'time', 'img']
#         writer = csv.DictWriter(file, fieldname)
#         for car in data:
#             writer.writerow ({
#             '№': count,
#             'time': car['time'],
#             'name': car['title'],
#             'img': car['img'] 
#             })
#             count +=1
# write_to_csv(parsing_data(url))

# import telebot
# from telebot import types
# import random

# data_base = parsing_data(url)

# token = '6677420796:AAF6PUyrrCtueEY8-VZFlwCI8HglAhQ9EwQ'
# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id,'Здравствуйте!\nВведите "/kaktus"')
    

# @bot.message_handler(commands=['kaktus'])
# def button_message(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for i in data_base:
#         bot.send_photo(message.chat.id, i['img'], caption=f"№{i['count']} {i['title']}")
#     bot.send_message(message.chat.id,'Введите номер',reply_markup=markup)

# @bot.message_handler(content_types='text')
# def message_reply(message):
#     try:
#         for x in data_base:
#             if message.text == str(x['count']):
#                 global id
#                 id = x
#                 markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#                 photo_b=types.KeyboardButton("Photo")
#                 quit_b = types.KeyboardButton("Quit")
#                 markup.add(photo_b)
#                 markup.add(quit_b)
#                 bot.send_message(message.chat.id,'Вы выбрали:')
#                 bot.send_photo(message.chat.id, id['img'], caption=f"№{id['count']} {id['title']}")
#                 bot.send_message(message.chat.id,'Deistvie', reply_markup=markup)
#                 bot.send_message(message.chat.id,'после получения результата, ты можешь продолжить поиск по номерам')
#                 break
#     except TypeError:
#         bot.send_photo(message.chat.id, 'https://risovach.ru/upload/2021/06/mem/da-kto-takoy_273422635_orig_.jpg', caption="Новостей пока нет )':")
#     if message.text=="Description":
#         try:
#             bot.send_message(message.chat.id,id['desc'])
#         except telebot.apihelper.ApiTelegramException:
#             i = 0
#             while i < len(id['desc']):
#                 bot.send_message(message.chat.id,f"{id['desc'][i:i+1000:]}")
#                 i += 1000

#         markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

#     elif message.text == 'Photo':
#         bot.send_photo(message.chat.id, id['img'], caption=f"№{id['count']} Источник:{id['link']}")

#     elif message.text == 'Quit':
#         bot.send_message(message.chat.id,"':")
#         bot.stop_bot()
#         print('STOP_BOT!')


#     elif message.text.lower() == 'test':
#         bot.send_message(message.chat.id,"""OK\n\n/start    /kaktus""")


# bot.polling()