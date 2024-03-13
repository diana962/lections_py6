# (deactivate) and (. venv/bin/activate) #pip install -r requirement.txt
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service # он у меня и без него работает
from datetime import datetime
# from utils import get_html_selenium
from utils import get_page_html_selenium, get_deps_html_selenium
from multiprocessing import Pool


base_url = 'https://kenesh.kg/ru' # Не забудь в конце /
deputs_url = base_url + '/deputies/' # Перед deputies не стваится /, но здесь поменяли

def get_soup(html): 
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_personal_link(soup):
    container = soup.find('div', class_= 'section-body')
    items = container.find_all('div', class_ = 'card-body')
    # print(items)
    links = [base_url + x.find('a').get('href') for x in items]
    return links

# html = get_html_selenium(deputs_url)
# soup = get_soup(html)
# # print(len(soup.find_all('h5', class_= 'card-title')), soup.find_all('h5', class_= 'card-title'))
# print(get_personal_link(soup))

def get_all_page_links(pages):
    res = []
    for i in range(1,9):
        html = pages[i]
        soup = get_soup(html)
        urls = get_personal_link(soup)
        res.extend(urls)
    return res

# all_pages = get_page_html_selenium(deputs_url)
# # print(get_all_page_links(all_pages))
# links = get_all_page_links(all_pages)
# # print(links, len(links))

def get_dept_data(link):
    html = get_deps_html_selenium(link)
    soup = get_soup(html)
    name = soup.find('h5', class_ = 'card-title').text
    info_divs = soup.find_all('div', class_ = 'card-subtitle d-flex')
    info = ' '.join(x.text for x in info_divs)
    bio = soup.find('article', class_ = 'clearfix').text.strip().replace('Powered by Froala Editor', '')
    img = soup.find('img', class_ ='card-img-top').get('src').replace('', '%20')
    write_to_csv(name, info, bio, img, link)


def prepare_csv():
    with open('deputy.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(['FIO:', 'Info:', 'Bio:', 'Image:', 'Link to page: '])
prepare_csv()


def write_to_csv(name, info, bio, img, url):
    with open('deputy.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([name, info, bio, img, url])
        print(f'{name} - parsed!')

# print(get_dept_data())

def main():
    prepare_csv()
    print('In Progress...')
    all_pages = get_page_html_selenium(deputs_url)
    links = get_all_page_links(all_pages)

    # for link in links: # последовательно
    #     get_dept_data(link)
    # paralelnno
    with Pool(8) as pool:
        pool.map(get_dept_data, links)

if __name__ == '__main__':
    start = datetime.now()
    main()
    finish = datetime.now()
    print({finish - start}) #seconds=353 #119 #116 #103

