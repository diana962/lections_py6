# dict() - Словарь -> упорядоченная коллекция элементов(python 3.7 -> ordered). 
# Каждый элемент внутри словаря хранится в виде пары
# --> {ключ: заключения}

# ассоциативный массив, hash table, object(js), structure == dictionary(py)

# ключами могут быть только неизменяемые типы данных и в словаре сохраняются только уникальные ключи, тогда как значениями могут выступать любые типы данных и любые значения 

# thisdict = { 
#     'brand': 'Ford',
#     'year': 1967,
#     'model': 'Mustang'
# }

# ls = ['Ford', 1967, 'Mustang']

# print(thisdict, type(thisdict))
# print(thisdict['brand'], [thisdict['model']])
# print(thisdict['year'])


# thisdict['motor'] = 'GTI Turbo' #--> добавил
# thisdict['model'] = 'fiesto' #--> заменил
# print(thisdict)

# ------------------------------------------------
# print(dir(dict))
# items, keys, values

user_info = {
    'first_name': 'John', 'last_name': 'Snow',
    'age': 24, 'email': 'bastard1123@gamil.com',
    'role': 'admin',
}

# ls = user_info.keys()
# ls1 = list(user_info.values())
# print(ls, '\n', ls1)

# ls3 = list(user_info.items())
# print(ls3)

# print('\nValues:')
# for value in user_info.values():
#     print(value)

# print('\nKeys: ')
# for key in user_info.keys():
#     print(key)

# print('\nItems: ')
# for key, value in user_info.items():
#     print(f'keys: {key}, values:{value}')

# изменение c update
# dict_ = {'name': 'Jack', 'age': 17}
# print(dict_)
# dict_['name'] = 'James'
# dict_['adress'] = 'Winterfell'
# print(dict_)
# dict_.update(age=24, adress = 'BlackCastle') #-> more than 1 argument 
# print(dict_)
# dict_.update({'name': 'john Snow'})
# dict_.update({'age': 24, 'adress' : 'Winterfell'})
# print(dict_)

# Словари записываются в фигурных скобках и нельзя забывать о  запятых между разными ключами и их значениями.
# Присваиваются значения с помощью :
# ------------------------------------------------------------------------

# dict_ = {1: 'Pizza', 2: 'Burger', 5: 'Steak'}
# print(dict_[3], '!!!')
# print(dict_.get(5))#, 'Not found!')) # index, value

# setdefault - работает также как и get, но если нет такого ключа, то создает новую пару из этого ключа.

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.setdefault(5, "Манты")) # добавить новое значение
# print(dict_)

# -------------------------------------------------------------------------
# создание - fromkeys
# ls = list(range(1, 10))
# new_dict = dict.fromkeys(ls, 'default')
# print(new_dict)

# -------------------------------------------------------------------------
# удаление элементов
# pop, popitem

# pop(<key>) - удаляет пару по ключу
# popitem() - удаляет послледнюю пару

# dict_ = {'name': 'Jonn', 'last_name' : 'Snow', 'age': 24}
# print(dict_)

# removed = dict_.pop('last_name')
# print(dict_)
# print(removed)
# print('---------------------')
# removed = dict_.popitem()  # вернул с ключом
# print(dict_)
# print(removed)

# ---------------------------------------------------------------------------------
# roles = {
#     1: 'Admin',
#     2: 'Customer',
#     3: 'Vendor',
# }

# users = {
#     55: {
#         'id': 55, 'role': roles[3], 'username': "Tirion",
#     },
#     2: {
#         'id': 2, 'role': roles[1], 'username': "John Snow",
#     },
#     4: {
#         'id': 3, 'role': roles[2], 'username': "Raychel",
#     },
# }
# print(users)

# product = {
#     'id': 1,
#     'title': 'Samsung Galaxy s23 Ultra',
#     'description': 'lorem ipsum',
#     'price': 1000
# }
# print(product) #12

# id_user = int(input('Vvedite id: '))
# if users[id_user]['role'] == roles[1]:
#     product['ddescription'] = input('Vvedite username: ')
# else:
#     print('You don\'t have a permission!')

# print()
# print(product)