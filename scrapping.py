from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
from openpyxl import Workbook


def scrape_devkg(keywords=[], start_page=1):
    url = 'https://devkg.com'
    jobs_url = 'https://devkg.com/ru/jobs?page='
    vacancies = {}

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    print(' . . . Начинаем поиск . . . ')
    with webdriver.Chrome(options=chrome_options) as driver:
        error_count = 0
        while error_count < 3:
            try:
                driver.get(f'{jobs_url}{start_page}')
                html_code = driver.page_source
                soup = BeautifulSoup(html_code, 'lxml')
                jobs = soup.find_all('article', class_='item')
                link_archived_found = False

                for job in jobs:
                    if job.find('a', class_='link archived'):
                        link_archived_found = True
                        break

                    job_url = url + job.find('a', class_='link').get('href')
                    position = job.find('div', class_='jobs-item-field position').get_text(strip=True).replace(
                        'Должность', '')

                    if not keywords or any(keyword.lower() in position.lower() for keyword in keywords):
                        company = job.find('div', class_='jobs-item-field company').get_text(strip=True).replace(
                            'Компания', '')
                        salary = job.find('div', class_='jobs-item-field price').get_text(strip=True).replace('Оклад',
                                                                                                              '')
                        job_type = job.find('div', class_='jobs-item-field type').get_text(strip=True).replace('Тип',
                                                                                                               '')
                        driver.get(job_url)
                        information = BeautifulSoup(driver.page_source, 'lxml').find('section',
                                                                                     class_='information')
                        description = information.find('div', class_='text').get_text(strip=True)[17:]
                        contacts = [contact.text for contact in information.find_all('div', class_='type')[1:]]
                        vacancies[job_url] = {'position': position, 'company': company, 'salary': salary,
                                              'type': job_type, 'description': description, 'contacts': contacts}

                if link_archived_found:
                    break
                else:
                    print(f' . . . Пройдена страница №{start_page} . . . ')
                    start_page += 1
                    error_count = 0

            except Exception as e:
                error_count += 1
                print(f'Ошибка при парсинге страницы. Попытка {error_count}/3.')
                if error_count == 3:
                    print('Достигнуто максимальное количество попыток. Прекращение парсинга.')
                    break

    print(f' . . . Найдено {len(vacancies)} вакансий . . . ')
    return vacancies


def save_vacancies_to_excel(vacancies):
    print(' . . . Начинаю запись . . . ')
    current_datetime = datetime.now()
    filename_with_datetime = current_datetime.strftime("DevKG - вакансии (%H:%M:%S, %d.%m.%Y).xlsx")
    wb = Workbook()
    ws = wb.active
    ws.title = "Вакансии"
    ws.append(["Должность", "Компания", "Описание", "Контакты", "Зарплата", "Тип", "Ссылка"])

    for vacancy_url, vacancy_info in vacancies.items():
        if not all(key in vacancy_info for key in ['position', 'company', 'description', 'salary', 'type', 'contacts']):
            print(f"Ошибка: Некорректные данные для вакансии по ссылке: {vacancy_url}")
            continue

        if not all(vacancy_info[key] for key in ['position', 'company', 'description', 'salary', 'type', 'contacts']):
            print(f"Ошибка: Некорректные данные для вакансии по ссылке: {vacancy_url}")
            continue

        contacts = "| ".join(vacancy_info.get('contacts', []))
        ws.append(
            [vacancy_info.get(key, '') for key in ['position', 'company', 'description']] +
            [contacts, vacancy_info.get('salary', ''), vacancy_info.get('type', ''), vacancy_url])

    wb.save(filename_with_datetime)
    print(f' . . . Данные сохранены в файл: {filename_with_datetime} . . . ')


save_vacancies_to_excel(scrape_devkg(keywords=['python']))
