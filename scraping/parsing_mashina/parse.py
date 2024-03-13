from bs4 import BeautifulSoup 
import requests
import csv
import pprint

# # url = 'https://www.mashina.kg/'
# # def parsing_data(url):
# #     response = requests.get(url)
# #     print(response, type(response))
# #     print()
# #     print(dir(response))

# # parsing_data(url)

# # <Response [200]> <class 'requests.models.Response'>
# # ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

url = 'https://www.mashina.kg/search/all/'

def parsing_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    container = soup.find('div', class_ = 'table-view-list')
    print(container)
    cars = container.find_all('div', class_ = 'list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_ = 'name').text.strip()
        try:
            img = car.find('img', class_ = 'lazy-image-attr').get('src')
        except Exception as e:
            img = f'No image, {e}!'
        print(img)
        price = car.find('div', class_ = 'block price').find('strong').text
        print(price)
        description = ''.join(car.find('div', class_='block info-wrapper item-info-wrapper').text.split())
        print(description)
        data = {'title': name, 'description': description, 'price': price, 'img': img}
        result.append(data)
    return result
pprint.pprint(parsing_data(url))


# def get_last_page(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     pages = soup.find_all('a', class_= 'page-link')[-1]
#     return int(pages.get('data-page'))



def prepare_csv():
    with open('cars.csv', 'w') as file:
        fieldname = ['№', 'name', 'decription', 'price', 'img']
        writer = csv.DictWriter(file, fieldname)
        writer.writerow({
            '№': '№',
            'name': 'Name',
            'decription': 'Decription',
            'price': 'Price: ',
            'img': 'Image URL' #
        })
# prepare_csv()

def write_to_csv(data: list):
    with open('cars.csv', 'a') as file:
        global count
        fieldname = ['№', 'name', 'decription', 'price', 'img']
        writer = csv.DictWriter(file, fieldname)
        for car in data:
            writer.writerow ({
            '№': count,
            'name': car['title'],
            'decription': car['description'],
            'price': car['price'],
            'img': car['img'] 
            })
            count +=1
# write_to_csv(parsing_data(url))

# data = parsing_data(url)
# write_to_csv(data)

# count = 1
# url = f'https://www.mashina.kg/search/all/?page=1'
# last_page = get_last_page(url)
# print(last_page)
# prepare_csv()

# i = 1
# while i <= 1:#last_page:
#     page_url = f'https://www.mashina.kg/search/all/?page={i}'
#     data = parsing_data(url)
#     write_to_csv(data)
#     print(f'Спарсили {i}/{last_page} pages!')
#     i+=1


# P.s.: 1. read a documentation of beautifulsoup4 and 2. SELENIUM - parsing