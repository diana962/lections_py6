
# 1.
# Вам дан список со словарями, сериализуйте этот список в json-строку
# import json

# list_of_dicts = [
#     {"ключ1": "значение1", "ключ2": "значение2"},
#     {"ключ3": "значение3", "ключ4": "значение4"},
    
# ]
# json_strings = json.dumps(list_of_dicts)
# print(json_strings)
# 2.
# Вам дана json-строка, десериализуйте ее. 
# Выведите названия тех продуктов, рейтинг которых больше 4
# json_data =[
#     {"product": "Продукт1", "rating": 3.5},
#     {"product": "Продукт2", "rating": 4.2},
#     {"product": "Продукт3", "rating": 5.0},
    
# ]

# high_rated_products = [item['product'] for item in json_data if item['rating'] > 4]
# print(high_rated_products)

# 3.
# Вам дан файл db.json. Десериализуйте данные с него. 
# Добавьте в каждый продукт новую пару ("description":"..."). 
# Запишите измененные данные в файл new_db.json
# with open('db.json','r') as file:
#     data = json.load(file)
#     print(data)



# for product in data:
#     product['description'] = 'тОВАР ГИБРИД'


# with open('new_db.json','w') as new_file:
#     json.dump(data,new_file)


# # 4.
# Удалите из файла new-db.json продукт с id 3.
# with open('new_db.json','r') as file:
#     data = json.load(file)

# product_to_remove = "Продукт3"


# data =[item for item  in data if item["product"] != product_to_remove]

# with open('new_db.json','w') as new_file:
#     json.dump(data,new_file)


    
# 5.
# Напишите функцию, которая будет запрашивать id,
#  title, description, price, rating и добавлять этот продукт в new_db.json
# with open('new_db.json','r') as file:
#     data = json.load(file)
#     data.append({'id':input('id'),'title':'Product4','description':'bmw','price':123412,
#                  'rating':4.1})
# with open('new_db.json','w') as new_file:
#     json.dump(data,new_file)


# 6.
# Напишите функцию, которая будет принимать id продукта
# если такого продукта нет в new_db.json, функция выводит ошибку
# если такой продукт есть, то запрашивается id, title, description, price, rating и продукт должен обновиться в new_db.json
# def id_product(id):
#     try:
#         with open('new_db.json','r') as file:
#             data = json.load(file)
#             for product in data:
#                 if product['id'] == id:
#                     new_id = int(input("Введите новый id: "))
#                     new_title = input("Введите новый title: ")
#                     new_description = input("Введите новое description: ")
#                     new_price = float(input("Введите новый price: "))
#                     new_rating = float(input("Введите новый rating: "))

                    
#                     product["id"] = new_id
#                     product["title"] = new_title
#                     product["description"] = new_description
#                     product["price"] = new_price
#                     product["rating"] = new_rating
               
#                     with open('new_db.json','w') as new_file:
#                         json.dump(data,new_file)
                    
#                     print(f"Продукт с id {id} успешно обновлен в new_db.json")
#                     return
#         print(f"Продукт с id {id} не найден в данных.")
#     except FileNotFoundError:
#         print("Файл new_db.json не найден.")
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")

# id_product(1)

# 7.
# Напишите функцию, которая будет вытаскивать все
#  продукты из new_db.json и выводить отсортированн
# ый список с продуктами по рейтингу (в порядке убывания)
# def all_products():
#     with open('new_db.json', 'r') as file:
#         data = json.load(file)
        
#         sorted_products = sorted(data , key=lambda x: x['rating'], reverse=True)

#         for product in sorted_products:
#             print(product)
# all_products()
# 8.
# Напишите функцию, которая принимает часть названия и выводит список 
# из всех продуктов из new_db.json в названиях которых будет находится эта часть названия
# def name_product():
#     with open('new_db.json', 'r') as file:
#         data = json.load(file)
#         for product in data:
#             # print(product)
#             if "Продукт" in product['product'] :
#                 print(product)

# name_product()
# 9.
# Напишите функцию, которая принимает цену и выводит список из всех продуктов 
# из new_db.json цена которых больше или равна заданной

# def price_product(cost):
#     with open('new_db.json', 'r') as file:
#         data = json.load(file)
#         for product in data:
#             # print(product)
#             print(product['price'])
#             if cost <= product['price'] :
#                 print(product)

#         with open('new_db.json','w') as new_file:
#             json.dump(data,new_file, indent=4)


# price_product(152)

# 10.
# Напишите функцию, которая принимает список из продуктов
# эти продукты должны будут добавиться в new_db.json
# если продукт с таким же id уже есть в new_db.json, то он не добавляется
# def dict_id(dict):
#     with open('new_db.json','r') as file:
#         data = json.load(file)

#     existing_ids = {product['id'] for product in data}
#     new_product_id =  dict.get('id')

#     if new_product_id in existing_ids:
#         print(f'Такой айди уже есть')
#     else:
#         temp_data = data.copy()
#         temp_data.append(dict)
#         with open('new_db.json','w') as new_file:
#             json.dump(temp_data,new_file, indent=4)

# dict_id({'id':4,'title':'Mazeratti','rating':15})
    



"""Объявите словарь

a = {'a': 1, 'b': 2, 'c': 1}

удалите один из элементов, не используя методы словаря
"""
# a = {'a': 1, 'b': 2, 'c': 1}
# remove = 'a'
# delete = {key: value for key,value in a.items() if key != remove}
# print(delete)



#3
"""Объявите словарь

a = {'a': 1, 'b': 2, 'c': 1}

выведите всего его элементы специальным методом и распечатайте результат. 
Результат в терминале, должен быть такой:

dict_items([('a', 1), ('b', 2), ('c', 3)])
"""
# from pprint import pprint
# a = {'a': 1, 'b': 2, 'c': 1}

# pprint(list(str(a)))





#4
"""
Дан словарь. Распечатайте максимальное значение в словаре

a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}

Вывод:
56
"""
# a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(max(map(lambda x: x[1],a.items())))


#5
"""
Дан словарь. Распечатайте минимальное значение в словаре

a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}

Вывод:
21
"""
# a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(min(map(lambda x: x[1],a.items())))



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
# b = print(dict(map(lambda x : (x[0],x[1]) if x[1] % 2 == 0 else (x[0],1) ,a.items())))





#7
"""Дан словарь, оставьте все элементы с пустыми значениями, остальные удалите

a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}


Вывод:

{'a': None, 'd': None}
"""

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

# b = {key:x for key,x in a.items() if x == None}
# print(b)




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

# b = {key**2:x for key,x in a.items() }
# print(b)



#9
"""Дан список. Создайте словарь а, ключами которого будут строки из списка,
а значениями их длины

list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
a = {}

Вывод:
{'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# """
# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']

# print(dict(map(lambda x : (x,len(x)),list_)))


#10
"""Из предыдущего словаря а, достаньте ключ, значение которого является 
максимальным

a = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}

Вывод:
'Bootcamp'
"""
# a = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# print(max(a, key=lambda x: a[x]))






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
# b = {key: value**3 for key,value in a.items()}
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
# print({outer_key : inner_value for outer_key, inner_dict in a.items() for inner_key , inner_value in inner_dict.items()})



#3
"""Дан словарь dict1. Создайте словарь dict2, с ключами как в 
словаре dict1, а значениями пусть будут произведение чисел внутренних словарей 

dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
dict2 = {}

Вывод:
{'a': 4, 'b': 8, 'c': 27}
"""
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for key, inner_dict in dict1.items():
#     product = 1
#     for inner_value in inner_dict.values():
#         product *= inner_value
#     dict2[key] = product

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
dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = dict(sorted(dict_.items(),key=lambda x : x[1],reverse=False))

print(sorted_dict)



#6
"""Дан словарь dict_. Отсортируйте словарь по значениям в порядке уменьшения.
Новые элементы занесите в словарь sorted_dict

dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = {}

Вывод:
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
"""
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = dict(sorted(dict_.items(),key=lambda x : x[1],reverse=True))

# print(sorted_dict)


#7
"""Дан словарь. С помощью переменной x проверьте есть ли такой ключ в словаре.
Если есть, напечатайте строку 'Key is present in the dictionary', если нет -
'Key is not present in the dictionary'

dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
x = input()
"""
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# x = input()

# if int(x) in dict_ :
#     print('Key is present in the dictionary')
# else:
#     print('Key is not present in the dictionary')
    




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
# dic4 = {}

# for key, value in dic1.items():
#     dic4[key] = value

# for key, value in dic2.items():
#     dic4[key] = value

# for key, value in dic3.items():
#     dic4[key] = value

# print(dic4)


"""Даны два списка одинаковой длины. 
Необходимо создать из них словарь таким образом, 
чтобы элементы первого списка были ключами, 
а элементы второго — соответственно значениями нашего словаря


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
a = {}

Вывод:
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}
# """
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# a = dict(map(lambda x,y: (x,y),list1,list2))
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

# for category, values in dict_.items():
#     if category == 'math':
#         sum_function = values['sum']
#     elif category == 'vars':
#         sum1 = sum(values.values())

# print(sum1)        