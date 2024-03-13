from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time
import pprint
import lxml
# Укажите путь к драйверу Chrome
# chromedriver_path = '/usr/bin/chromedriver'  # Замените на ваш путь к chromedriver
# service = Service()

# Настройки для WebDriver
# options = webdriver.ChromeOptions()
# chrome_options = webdriver.ChromeOptions()
# options.headless = False # Установите True, если не нужно открывать окно браузера

# Переход на страницу
url = 'https://lalafo.kg/kyrgyzstan/transport'
def get_html_selenium(url):
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    # Получить HTML-код после выполнения JavaScript
    html = browser.page_source

    # Закрыть браузер
    browser.quit()

    return html
# print(get_html_selenium(url))

def transport_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    product_blocks = soup.find_all('article', class_='ad-tile-horizontal')
    # print(product_blocks)
    result = []
    for block in product_blocks:
        try: 
            product_card_desc = block.find('p', class_='LFSubHeading size-14 weight-700').text
        except (AttributeError, TypeError):
            product_card_desc = "Image not found"

        try:
            product_price = block.find('p', class_='LFSubHeading size-14 weight-700 ad-tile-price ad-tile-price__national-price').text
        except (AttributeError, TypeError):
            product_price = "Price not found"

        try:
            # product_card_img = block.find('data-src', class_='').get('src')
            img_tag = block.find('picture').find('img')
            photo_url = img_tag.get('data-src') or img_tag.get('src')
        except (AttributeError, TypeError):
            photo_url = "Image not found"


        data = {
            'desc': product_card_desc,
            'img': photo_url,
            'price': product_price,
            # 'discount': product_price_discount,
            # 'reviews': product_card_reviews,
            # 'rating': product_card_rating,
        }
        result.append(data)

    return result
print(transport_data(get_html_selenium(url)))


def excel():
    with open('lalafo.csv', 'w') as file:
        fieldname = ['#', 'desc', 'img','price']
        writer = csv.DictWriter(file, fieldname)
        writer.writerow({
            '#': '№', 'desc':'Desc','img':'Img','price':'Price'
            })
excel()
def write_csv(result):
    count = 1
    with open('lalafo.csv', 'a') as file:
        fieldnames = ['#', 'desc','img','price']
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        for transport in result:
            writer.writerow({
                '#': count,
                'desc':transport['desc'],
                'img':transport['img'],
                'price':transport['price']
            })
            count +=1

i = 1


while i <= 1:  # last_page:
    page_url = f'https://lalafo.kg/kyrgyzstan/transport?page={i}'
    html = get_html_selenium(page_url)
    data = transport_data(html)
    # excel()
    write_csv(data)
    print(f'Спарсили {i} pages!')
    i += 1