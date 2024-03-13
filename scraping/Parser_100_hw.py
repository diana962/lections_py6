# from bs4 import BeautifulSoup 
# from selenium import webdriver as wd
# import requests
# import csv
# import pprint
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time
# from webdriver_manager.chrome import ChromeDriverManager


# chromedriver_path = '/usr/bin/chromedriver'
# service = Service()
# options = wd.ChromeOptions()
# options.headless = False  # Установите True, если не нужно открывать окно браузера
# browser = wd.Chrome()

# url = 'https://global.wildberries.ru/catalog?category=9492'
# browser.get(url)

# # browser.implicity_wait(10)
# time.sleep(20)
# product_info = browser.find_elements(By.CLASS_NAME, 'card__link')
# print(product_info)
# result = []
# for product in product_info:
#     title = product.find_element(By.CLASS_NAME, 'b-card__info-row').text
#     price = product.find_element(By.CLASS_NAME, 'price__lower').text
#     img = product.find_element(By.CLASS_NAME, 'main-img').get_attribute('src')
#     print(img)
#     data = {'title': title, 'price': price, 'img': img}
#     result.append(data)
# # pprint.pprint(result)
# browser.quit()

# def excelviewer():
#     with open('WB.csv', 'w') as file:
#         colone = ['#', 'name', 'price', 'img']
#         writer = csv.DictWriter(file, colone)
#         writer.writerow({'#': '№', 'name': 'Name', 'price': 'Price', 'img': 'Image'})
# excelviewer()


# count = 1
# def writer(data):
#     with open('WB.csv', 'a') as file:
#         global count
#         colone = ['#', 'name', 'price', 'img']
#         writer = csv.DictWriter(file, colone)
#         for product in data:
#             writer.writerow({'#': count, 'name': product['title'], 'price': product['price'], 'img': product['img']})
#             count +=1
# writer(result)



# Техническое задание

# Необходимо вытянуть данные с сайта
# url = 'https://global.wildberries.ru/catalog?category=9492';
# Парсинг сайтов – это новый метод ввода данных, который не требует повторного
# ввода или копипастинга. Такого рода программное обеспечение ищет информацию под
# контролем пользователя или автоматически, выбирая новые или обновленные данные
# и сохраняя их в таком виде, чтобы у пользователя был к ним быстрый доступ.
# Что нужно сделать?
# 1) Спарсить наименование товара;
# 2) Спарсить цену товара;
# 4) Спарсить линк картинки этого товара

# Полезные ссылки:

# 3) https://leftjoin.ru/all/parsim-dannye-kataloga-sayta-ispolzuya-beautiful-soup-i-selenium/
# 4) https://www.dataquest.io/blog/web-scraping-tutorial-python/
# 5) https://devman.org/encyclopedia/modules/bs4-tutorial/
# 6) https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html
# 7) https://www.youtube.com/watch?v=ykjBVT57r68
# 8) https://www.youtube.com/watch?v=3hgkiDAaSQs
# 9) https://habr.com/ru/companies/selectel/articles/754674/


