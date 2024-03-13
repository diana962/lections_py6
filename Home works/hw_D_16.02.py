# 1.
# Вам дан список со словарями, сериализуйте этот список в json-строку

# import json
# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status' : True,
#     'wife': False,
#     'children': None
# }
# print(dict_, type(dict_))
# a = json.dumps(dict_)
# print(a, type(a))

# 2.
# Вам дана json-строка, десериализуйте ее. 
# Выведите названия тех продуктов, рейтинг которых больше 4

# import json
# produkt = {
#     "banana": 5,
#     "apple": 5,
#     "pulm": 4,
#     "mango": 3
# }
# a = json.dumps(produkt)
# b = json.loads(a)
# for i in b:
#     if b[i] > 4:
#         print(i)
# print(b, type(b))

# 3.
# Вам дан файл db.json. Десериализуйте данные с него. 
# Добавьте в каждый продукт новую пару ("description":"..."). 
# Запишите измененные данные в файл new_db.json

# dict_ = {
#     "name": "Ivan",
#     "age": 30,
#     "city": "Moscow"
# }
# import json
# with open('db.json', 'w') as file:
#     json.dump(dict_, file, indent =4)
# with open('db.json', 'r') as file:
#     data = json.load(file)
#     print(data)
# data["description"] = "Russian"
# print(data)
# with open('new_db.json', 'w') as file:
#     json.dump(data, file, indent=4)

# #4
# with open('new_db.json', 'r') as file:
#     data = json.load(file)
# data.pop("city")
# with open('newdb.json', 'w') as file:
#     json.dump(data, file, indent = 4)

# 5.
# Напишите функцию, которая будет запрашивать id, title, description, price, rating и добавлять этот продукт в new_db.json
# import json

# def operation_json(id = input('ID: '), 
#                    title = input('Title: '), 
#                    description = input('Description: '), 
#                    price = input('Price: '), 
#                    rating = input('Rating: ')):    
    
#     dict_ = {
#         "id": id,
#         'title': title,
#         "description": description,
#         "price": price,
#         "rating": rating
#     }

#     with open('new_db.json', 'r') as file:
#         try:
#             data = json.load(file)
#             data = list(data)
#             with open('new_db.json', 'w') as file:
#                 data.append(dict_)
#                 json.dump(data, file, indent=4)
#                 print('Запись добавлена!')

#         except json.decoder.JSONDecodeError:
#             print('Файл пустой!')
#             with open('new_db.json', 'w') as file:
#                 data = [dict_]
#                 json.dump(data, file, indent=4)
# operation_json()
# # ------------------------------------------------
# with open('new_db.json','r') as file:
#     data = json.load(file)
#     data.append({'id': input('ID: '),'title':input('Title: '),'description':input('description: '),'price': input('price: '),
#                  'rating': input('rating: ')})
# with open('new_db.json','w') as new_file:
#     json.dump(data,new_file)

# 6.
# Напишите функцию, которая будет принимать id продукта
# если такого продукта нет в new_db.json, функция выводит ошибку
# если такой продукт есть, то запрашивается id, title, description, price, rating и продукт должен обновиться в new_db.json

# --> done in #5

# 7.
# Напишите функцию, которая будет вытаскивать все продукты из new_db.json и выводить отсортированный список с продуктами по рейтингу (в порядке убывания)

# import json
# produkt = {
#     "banana": 5,
#     "apple": 5,
#     "pulm": 4,
#     "mango": None
# }
# with open('new_db.json', 'w+') as file:
#     a = json.dump(produkt, file)
# with open('new_db.json', 'r') as file:
#     json_data = file.read()
# def conventor(file):
#     a = json.loads(json_data)
#     return type(a)
# print(conventor('new_db.json'))

# 8.
# Напишите функцию, которая принимает часть названия и выводит список из всех продуктов из new_db.json в названиях которых будет находится эта часть названия

# import json
# def halbname(file):
#     title = input('Enter a name: ')
#     with open(file, 'r') as file:
#         data = json.load(file)
#         products = [i for i in data if title in i]
#         return products

# print(halbname('new_db.json'))

# 9.
# Напишите функцию, которая принимает цену и выводит список из всех продуктов из new_db.json цена которых больше или равна заданной
# import json

# def filtered(num):
#     with open('new_db.json', 'r') as f:
#         data = json.load(f)

#     res = []
#     for name, price in data.items():
#         if price >= num:
#             res.append(name)

#     return res
# print(filtered(2))

# 10.
# Напишите функцию, которая принимает список из продуктов
# эти продукты должны будут добавиться в new_db.json
# если продукт с таким же id уже есть в new_db.json, то он не добавляется
# import json
# with open('list_of_products.json', 'w') as file:
#     json.dump(["banana", "apple", "plum", "mango"], file)

# def adding(smth = list(input('Enter:').split(","))):
#     with open('list_of_products.json', 'r') as file:
#         data = json.load(file)
#     for i in smth:
#         if i in data:
#             print('This produkt exist.')
#         else:
#             data.append(i)
#             print('Added')
#     with open('list_of_new_products.json', 'w') as file:
#         json.dump(data, file)
# adding()


"""Объявите словарь

a = {'a': 1, 'b': 2, 'c': 1}

удалите один из элементов, не используя методы словаря
"""
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# a = list(dict_)
# a.remove('a')
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# delete = 'a'
# if delete in a:
#     del a[delete]
# print(a) 

#3
"""Объявите словарь

a = {'a': 1, 'b': 2, 'c': 1}

выведите всего его элементы специальным методом и распечатайте результат. 
Результат в терминале, должен быть такой:

dict_items([('a', 1), ('b', 2), ('c', 3)])
"""
# a = {'a': 1, 'b': 2, 'c': 1}
# print(list(zip(a.keys(), a.values())))

#4
"""
Дан словарь. Распечатайте максимальное значение в словаре

a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}

Вывод:
56
"""
# a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# maximum = 0
# for v in a.values():
#     if maximum < v:
#         maximum = v
# print(maximum)
#5
"""
Дан словарь. Распечатайте минимальное значение в словаре

a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}

Вывод:
21
# """
# a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# maximum = 100
# for v in a.values():
#     if maximum > v:
#         maximum = v
# print(maximum)

# a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# min_ = min(a.values())
# print(min_)

#6
"""Создайте словарь a с числовыми значениями. 
Создайте новый словарь b, такой же как словарь а, 
но все нечетные значения замените на 1.

Пример: Ввод -> 
a = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
Вывод -> 
b = {'a': 1, 'b': 4, 'c': 1, 'd': 1,  'e': 6}
"""
# a = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# b = {}
# for k, v in a.items():
#     if v % 2 != 0:
#         b[k] = 1
#     else:
#         b[k] = v
# print(b)


#7
"""Дан словарь, оставьте все элементы с пустыми значениями, остальные удалите

a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

Вывод:

{'a': None, 'd': None}
# """
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {k: v for k, v in a.items() if v is None}
# print(b)

# try:
#     for k, i in a.items():
#         if i != None:
#             a.pop(k)
#         print(a)
# except:
#     print('error')




#8
"""Дан словарь a, где ключами будут цены товаров, а значениями их названия, 
затем пройдитесь циклом по нему и поменяйте все ключи элементов, 
возведя их в квадрат, новые элементы запишите в словарь b

Ввод:
a = {25: 'apple', 26: 'orange', 27: 'banana'} 
b = {}


Вывод:
{625: 'apple', 676: 'orange', 729: 'banana'}
"""
# a = {25: 'apple', 26: 'orange', 27: 'banana'} 
# b = {k**2:v for k, v in a.items()}
# print(b)

#9
"""Дан список. Создайте словарь а, ключами которого будут строки из списка,
а значениями их длины

list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
a = {}

Вывод:
{'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
"""
# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# a = {k:len(k) for k in list_}
# print(a)

#10
"""Из предыдущего словаря а, достаньте ключ, значение которого является 
максимальным

a = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}

Вывод:
'Bootcamp'
# """
# a = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# for k, v in a.items():
#     if v == max(a.values()):
#         print(k)

'===============MEDIUM================'
#1
"""Дан словарь a, где ключи - числа от 1 до 5 и значения те же самые числа.
Создайте словарь b, у которого ключи такие же как в первом словаре, 
а значения эти же числа, возведенные в куб


a = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
b = {}

Вывод:
{'1': 1, '2': 8, '3': 27, '4': 64, '5': 125}
"""
# a = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
# b = {k: v**3 for k, v in a.items()}
# print(b)


#2
"""Дан словарь а, значениями, которого являются словари,
измените словарь 'а' таким образом, чтобы значения внутреннего словаря стали 
внешними значениями

a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}

Вывод:
{'a': 32, 'b': 36, 'c': 37, 'd': 21}
"""
# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# b = {k: b for k, v in a.items() for b in v.values()}
# print(b)

#3
"""Дан словарь dict1. Создайте словарь dict2, с ключами как в 
словаре dict1, а значениями пусть будут произведение чисел внутренних словарей 

dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
dict2 = {}

Вывод:
{'a': 4, 'b': 8, 'c': 27}
"""
dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {k: b for k, v in dict1.items() for b in v.values()} 
# print(dict2)
from functools import reduce
res = []
for i in dict1.values():
    print(list(reduce(lambda x, y: x*y, i.values())))
print(res)

# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {outer_key: 1 for outer_key in dict1}  
# for outer_key, inner_dict in dict1.items():
#     product = 1
#     for value in inner_dict.values():
#         product *= value
#     dict2[outer_key] = product
# print(dict2)


#4
"""Дан список, состоящий из строк и чисел. Создайте словарь, ключами которого
будут строки из списка, а значениями числа

list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
a = {}
Вывод:
{'hello': 23, 'world': 56, 'Makers': 928, 'word': 456, 'bootcamp': 223, 'coding': 89}

"""
# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']

# a = {}

# for element in range(len(list_)-1):
#     if isinstance(list_[element],str) and isinstance(list_[element + 1],int):
#         a[list_[element]] = list_[element+1]
# print(a)
#5
"""Дан словарь dict_. Отсортируйте словарь по значениям в порядке увеличения.
Новые элементы занесите в словарь sorted_dict

dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = {}

Вывод:
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
"""
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# sorted_keys = sorted(dict_, key=dict_.get)
# for key in sorted_keys:
#     sorted_dict[key] = dict_[key]
# print(sorted_dict)

#6
"""Дан словарь dict_. Отсортируйте словарь по значениям в порядке уменьшения.
Новые элементы занесите в словарь sorted_dict

dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = {}

Вывод:
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
"""
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# sorted_keys = sorted(dict_, key=dict_.get, reverse = True)
# for key in sorted_keys:
#     sorted_dict[key] = dict_[key]
# print(sorted_dict)
#7
"""Дан словарь. С помощью переменной x проверьте есть ли такой ключ в словаре.
Если есть, напечатайте строку 'Key is present in the dictionary', если нет -
'Key is not present in the dictionary'

dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
x = input()
"""
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# x = input('num: ')
# print('Key is present in the dictionary' if x == dict_.keys() else 'Key is not present in the dictionary')

'==================HARD===================='
#1
"""Даны 3 словаря. Объедините эти словари в 4

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4 = {}

Вывод:
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# dic4 = {zip(dic1, dic2, dic3)}
# dic4 = {**dic1, **dic2, **dic3}
# print(dic4)
#2
"""Даны два списка одинаковой длины. 
Необходимо создать из них словарь таким образом, 
чтобы элементы первого списка были ключами, 
а элементы второго — соответственно значениями нашего словаря


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
a = {}

Вывод:
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}
"""
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# a = {k: v for k, v in zip(list1, list2)}
# print(a)


#3
"""Дан словарь. Найдите сумму значений словаря, который хранится под ключом 'vars',
используя значение словаря, под ключом 'math'

dict_ = {
    'math': {
        'sum': sum
    },
    'vars': {
        'a': 5,
        'b': 20,
        'c': 50
    }
}

Вывод: 
75
"""
# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }
# func = dict_['math']['sum'] 
# vars_ = dict_['vars'].values()
# print(func(vars_))
