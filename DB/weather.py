from bs4 import BeautifulSoup 
import requests
import pprint
import csv

url = 'https://yandex.ru/pogoda/bishkek?lat=42.875969&lon=74.603698'

def parsing_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_='temp forecast-briefly__temp forecast-briefly__temp_day')
    if container:
        daytime = container.find('span', class_='temp__value temp__value_with-unit').text
        print(daytime)
    else:
        return "Data not found."
    container1 = soup.find('div', class_='temp forecast-briefly__temp forecast-briefly__temp_night')
    if container1:
        nighttime = container1.find('span', class_='temp__value temp__value_with-unit').text
        print(nighttime)
    else:
        return "Data2 not found."
print(parsing_data(url))


def prepare_csv():
    with open('weather.csv', 'w') as file:
        fieldname = ['tem_hi', 'tem_lo']
        writer = csv.DictWriter(file, fieldname)
        writer.writerow({
            'tem_hi': 'HIGH tem',
            'tem_lo': 'LOW tem' #
        })
prepare_csv()


def write_to_csv(daytime, nighttime):
    with open('weather.csv', 'a') as file:
        fieldname = ['tem_hi', 'tem_lo']
        writer = csv.DictWriter(file, fieldname)
        writer.writerow ({
        'tem_hi': daytime,
        'tem_lo': nighttime
        })
write_to_csv(parsing_data(url))


