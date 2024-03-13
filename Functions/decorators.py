# Декоратор - это функция, которая позволяет без изменения кода функции расширить функционал этой функции.
# API (Application Programming Interface)

# Функция высшего порядка - это функция, которая принимает другую функцию. Например: декоратор.

import requests
from time import time

def timeCheck(func):
    def wrapper():
        start = time()
        func()
        finish = time()
        print(f'Time to get result: {round(finish - start, 2)}')
    return wrapper

@timeCheck # -> обязательно начинать с собачкой, it's wrapped
def printCars():
    car = input('Enter a car model: ')
    api_url = f'https://api.api-ninjas.com/v1/cars?model={car}'
    response = requests.get(api_url, headers={'X-Api-Key': 'fMvF8LTzSEKonJ8R7LWhEw==GYSkLGG2n8xytyiF'})
    if response.status_code == 200: #-> код для быстрой проверки. существует множество кодов.
        print(response.text)
    else: 
        print(f'Error: {response.status_code}\n{response.text}')
    return

@timeCheck
def printUser():
    api_url = 'https://randomuser.me/api/'
    response = requests.get(api_url)
    if response.status_code == 200:
        print(response.text)
    else: 
        print(f'Error: {response.status_code}\n{response.text}')
    return

# # printUser()

printCars()
# print()
# print()
printUser()

# def decorator(func):
#     def wrapper():
#         print('decorator worked!')
#         print(f'{func.__name__} была вызванана!')
#         print() #-> just to get otstup
#         func()
#     return wrapper

# @decorator
# def get_name():
#     print(f'Owner name is John Snow!')
# get_name()


# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвала {func.__name__}()\nона приняла args: {args}, kwargs: {kwargs}')
#         res = func(*args, **kwargs)
#         print(f'Trace: вызвала {func.__name__}()\nона вернула {res}')
#         return res
#     return wrapper

# @trace
# def printAddress(name, adress):
#     return f'Name: {name} -> address: {adress}'
# @trace
# def getHello(name, last_name, coountry):
#     return f'Hello {name} {last_name} from {coountry}'

# print(printAddress('Din Winchester', 'Kansas'))
# print(getHello('Sam', last_name='Winchester', coountry='USA'))


# def boldText(func):
#     def wrapper(*args, **kwargs):
#         res = '<bold>' + func(*args, **kwargs) + '</bold>'
#         return res
#     return wrapper

# def iText(func):
#     def wrapper(*args, **kwargs):
#         res = '<i>' + func(*args, **kwargs) + '</i>'
#         return res
#     return wrapper

# @iText
# @boldText
# def get_name():
#     name = input('Enter a name: ')
#     return name

# print(get_name())
