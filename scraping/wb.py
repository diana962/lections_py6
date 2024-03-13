import csv
import requests
from bs4 import BeautifulSoup
# from selenium import webdriver as wd
import pprint
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-javascript")

# time.sleep(5)
def get_html_selenium(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    
    html = driver.page_source
    driver.quit() 
    return html

url = "https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki?sort=popular&page=1"
html_content = get_html_selenium(url)

def laptops_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # print(soup.text)
    container = soup.find('div', class_ = 'product-card-list')
    print(container)
    laptops = soup.find_all('div', class_ = 'product-card__wrapper')#.get('product-card__link j-card-link j-open-full-product-card')

    result = []
    for lp in laptops:
        name = lp.find('h2', class_ = 'product-card__brand-wrap').text
        price = lp.find('ins', class_ = 'price__lower-price').text # 'div', class_= 'product-card__middle-wrap'
        img = lp.find('img', class_ = 'j-thumbnail').get('src')
        data = {'title': name, 'price': price, 'img': img}
        result.append(data)
    return result

pprint.pprint(laptops_data(html_content))
database = laptops_data(html_content)

def excelviewer():
    with open('WB1.csv', 'w') as file:
        colone = ['#', 'name', 'price', 'img']
        writer = csv.DictWriter(file, colone)
        writer.writerow({'#': '№', 'name': 'Name', 'price': 'Price', 'img': 'Image URL'})
excelviewer()
print(excelviewer())


count = 1
def writer(data):
    with open('WB1.csv', 'a') as file:
        global count
        colone = ['#', 'name', 'price', 'img']
        writer = csv.DictWriter(file, colone)
        writer.writeheader()
        for lp in data:
            writer.writerow({'#': count, 'name': lp['title'], 'price': lp['price'], 'img': lp['img']})
            count +=1
print(writer(database))


# url = 'https://global.wildberries.ru/catalog?category=9492'
# i = 1
# while i < 10:#last_page:
#     page_url = f'https://global.wildberries.ru/catalog?category=9492&page={i}'
#     html_content = get_html_selenium(page_url)
#     data = laptops_data(html_content)
#     writer(data)
#     print(f'Спарсили {i} pages!')
#     i+=1