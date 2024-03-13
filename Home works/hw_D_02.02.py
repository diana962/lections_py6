"""Функции задания"""

# 1
# Создать функцию, которая будет принимать 3 числа в качестве аргументов, функция должна возвращать сумму первых двух чисел разделеную на третье число
# нужно реализовать проверку на то, что третье число не является нулем, если это ноль, то просто возвратить результат сложения первого и второго числа

# def num(a = float(input('Enter a number: ')), b = float(input('Enter a number: ')), c = float(input('Enter a number: '))):
#   try:
#     return (a + b) / c
#   except ZeroDivisionError:
#     print('Not possible!')
#     return(f'The sum of numbers: {a + b}')

# print(num())


# 2
# Создать функцию, которая принимает в качестве аргумента список со строками и в каком регистре нужно вернуть данные, строки могут быть записаны в любом регистре, задача: на основе выбора регистра, возвращать либо список со строками в верхнем регистре, либо в нижнем регистре
# Например: func(["hEllo", "wORld"], "lower") -> ["hello", "world"]

# def func(txt_or_list = input('Enter smth: '), reg = input('Enter register (low/ up): ')):
#     if reg == 'low':
#         return(f'{txt_or_list} -> {txt_or_list.lower()}')
#     else:
#         return(f'{txt_or_list} -> {txt_or_list.upper()}')
# print(func())

# Создать функцию, которая будет принимать в качестве аргумента строку, а затем говорить сколько в ней и каких символов, результать вернуть в виде объекта
# Например: 'Hello' -> {'H': 1, 'e': 1, 'l': 2, 'o': 1}

# def func(ls = input('Enter smth: ')):
#     dict_ = dict()
#     for i in ls:
#         dict_[i] = ls.count(i)
#     return f'"{ls}" -> {dict_}'
# print(func())

# Создать калькулятор используя функции, должны быть доступны операции(+, -, /, *), также должна быть функция-менеджер, которая будет принимать 2 числа и операцию, а затем вызывать нужную функцию и возвращать результат

# def calculator():
#   while True:
#     start = input('Добро пожаловать в калькулятор. Чтобы продолжить нажмите "return", а чтобы завершить введите "q"')
#     if start == 'q':
#         print('Калькулятор завершен.')
#         break
#     elif start == ' ':
#         print('Нет ничего приятнее, чем знание о твоих знаниях!')
#     else:
#         num = float(input('Enter a number: '))
#         num2 = float(input('Enter a number: '))
#         # функция-менеджер
#         str = int(input('I\'m your assistant. What do you want to do? Choose: \n 1: если вы хотите найти сумму \n 2: если вы хотите найти разность \n 3: если вы хотите найти произведение \n 4: если вы хотите найти деление \n'))
#         if str == 1:
#             print(num + num2)
#         elif str == 2:
#             print(num - num2)
#         elif str == 3:
#             print(num * num2)
#         elif str == 4:
#             if num2 == 0:
#                 print('На ноль делить нельзя! ')
#             else:
#                 print(num / num2)

# print(calculator())


# Создайте функцию, которая будет рассылать сообщения пользователям, сообщая о акции в магазине компьютерной техники, отправлять сообщения нужно только тем людям, которые тем или иным образом относятся к IT-сфере

# def sms():
#     for _ in users:
#         if 'IT' in _['work']:
#             z = _['name']
#             print(f'Dear, {z}. We have fresh news for you!')
            
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]
# print(sms())

# Создать функцию, которая будет принимать в качестве аргумента 2 строки, 1-я строка должна быть следующего вида -> '1200m', вторая строка состоит из величины, в которую необходимо преобразовать данные -> 'km', 'cm', 'mm', задача: реализовать логику, которая будет принимать например строку вида '2000m', и строку в которую нужно преобразовать величину например 'km', вывод должен быть '2km'

# def turner(weg = input('Enter a way to convert: '), vel = input('In what to convert (km/cm/mm): ')):
#     ls = []
#     ls1 = []
#     for i in weg:
#       if i.isdigit():
#         ls.append(i)
#       else:
#          ls1.append(i)
#     chislo = int(''.join(ls))
#     entered_velichina = ''.join(ls1)

#     return(f'{chislo / 1000} km' if vel == "km" else (f'{chislo * 100} cm' if vel == "cm" else (f'{chislo * 1000} mm' if vel == "mm" else 'no')))
# print(turner())

# Создать функцию, которая будет рассчитывать расход топлива автомобиля, будет принимать 2 аргумента 1-й сколько всего километров проехали, второй сколько понадобилось топлива на это, затем функция должна рассчитать сколько ушло топлива на 100 км и вернуть результат вида: 'На 100км было расходовано 10л горючего'

# def expences():
#     try:
#         way = int(input('Enter a distance in km: '))
#         fuel = int(input('How much fuel did you fill in liter? '))
#         return (f'На 100км было расходовано {round((fuel / way) * 100, 2)}л горючего')
#     except:
#         print('Enter only digits!')
# print(expences())

# Расчет премии сотрудникам
# salary- это заработная плата в месяц, overTime- количество часов, которое сотрудник взял сверхурочно, задача: создать функцию, которая будет добавлять к основной зарплате сверхурочное время(1час=200$), функция должна принимать список со словарями и возвращать также список, но уже с измененными данными пример: [{'name': 'Jack', 'salary': 10000, 'overTime': 4}] -> [{'name': 'Jack', 'salary': 10800}]

# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]
# def money(ls):
#     for i in ls:
#         i['salary'] = i['salary'] + i['overTime']* 200
#         i.popitem()
#     print(ls)
#     ## print((ls)[0], (ls)[1], (ls)[2], (ls)[3], (ls)[4], sep = '\n')
#     for x in ls:
#        print(f'{i in ls} -> {x}')
      
# print(money(employees))

# Создать функцию, которая в качестве аргумента будет принимать список со строками и числами, задача, отсортировать числа в отдельный список, а строки в отдельный и распечатать оба списка

# def sorting(list):
#     ls1 = []
#     ls2 = []
#     for i in list:
#         if isinstance(i, int): 
#           ls1.append(i)
#         else:
#            ls2.append(i)
#     return (f' Это лист с числами {ls1}, а это лист с со словами {ls2}')
        
# print(sorting([1, 2, 'str']))


# Создайте функцию, которая будет в качестве аргумента принимать список такого вида как указан выше, и будет возвращать отсортированный список (сортировать по убыванию оценок, используйте sort())

# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# def filtered(list_):
#   list_.sort(key = lambda x: x['marks'], reverse=True)
#   return list_

# print(filtered(students))

11
# Создайте функцию, которая будет принимать строку, а затем будет смотреть на все товары и возвращать только те, у которых в названии есть данная строка (учесть, что название может быть полным, а может быть частичным)
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]
# def filtered(str = input('Enter a product you want to buy: ').title()):
#     for i in products:
#       if str in i['title']:
#         return(i)
# print(filtered())

# str = input('Enter a product you want to buy: ').title()
# comprehension_list = [i for i in products if str in i['title']]
# print(comprehension_list)

12
# Используя из предыдущей задачи список с товарами, реализовать фильтрацию по категориям, функция должна в качестве аргумента принимать строку с категорией и возвращать список, в котором будут только те товары, у которых категория полностью совпадает с переданной

# def choice(str = input('Enter a category: ')):
#     for i in products:
#       if str in i['category']:
#         return(i)
# print(choice())
    
# str = input('Enter a category: ')
# comprehension_list = [i for i in products if str in i['category']]
# print(comprehension_list)

13
# Создать счетчик расходов, есть некая переменная, которая будет хранить данные о вашем балансе, создать две функции, первая будет записывать расходы, вторая просто пополнять баланс, первая функция: ее основная задача получать 2 аргумента на что потрачено и сколько потрачено, дальше формировать словарь типа: {'target': 'Products', 'spend': 400}, затем сохранять эти данные в список и соответственно вычитать из баланса сумму трат, вторая функция просто получает в качестве аргумента сумму, которую нужно добавить на баланс, также необходимо реализовать проверку, достаточно ли средств на балансе для совершения расходов

# data = 1000
# def expences(target = input('What did you purchase? '), spend = int(input('How much does it cost? '))):
#     dict_ = {target: spend}
#     a = int(input('Enter your income: '))
#     print(f'You had ${data+a} on your accout.')
#     if (data+a - dict_[target]) < 0:
#         return(f'You have not ${abs(data+a - dict_[target])} to buy it.')
#     else:
#       return (f'The current amount on your account: ${data+a - dict_[target]}')
# print(expences())    

# while True:
#     balance_user= 10200
#     def replenish_balance():
#         global balance_user
#         user_replenish = input('Вы хотите пополнить баланс,если да то напишите число для пополнения:')
#         if user_replenish == 'q':
#             return
#         elif user_replenish == 'Все':
#             return exit()
#         else:
#             user_replenish = int(user_replenish)
#             balance_user += user_replenish
#             print(balance_user)
#     def targets_spent():
#         global balance_user
#         target_data = input('Введите на что вы потратили: ')
#         spend_data = int(input('Сколько вы потратили: '))
#         if balance_user < spend_data:
#             print('Закончились деньги ты бомж')
#             return exit()
#         products_data = {}
#         products_data['target'] = target_data
#         products_data['spend'] = spend_data
#         ls_data_spent = []
#         ls_data_spent.append(products_data['spend'])
#         for num in ls_data_spent:
#             balance_user -= num
#             print(balance_user)
#         return 
#     replenish_balance()
#     targets_spent()
    
14
# Дан пустой список, необходимо использовать его в качестве базы данных для словарей типа {title: 'str', price: num, category: 'str'}, задача реализовать полный CRUD(create(должна быть возможность создавать данные, в нашем случае объекты), read(возможность получения/чтения данных), update(изменение данных(можно использовать индекс)), delete(удаление данных(можно использовать индекс))), за каждое действие должна отвечать отдельная функция

# database = []

# def create_item(title: str, price: int, category: str):
#     item = {'title': title, 'price': price, 'category': category}
#     database.append(item)

# def read_items():
#     return database

# def update_item(index, title=None, price=None, category=None):
#     if index < len(database):
#         item = database[index]
#         if title:
#             item['title'] = title
#         if price:
#             item['price'] = price
#         if category:
#             item['category'] = category
#         return True
#     else:
#         return False

# def delete_item(index):
#     if index < len(database):
#         del database[index]
#         return True
#     else:
#         return False

# create_item('Book', 10, 'Education')
# create_item('Phone', 500, 'Electronics')
# create_item('Shirt', 20, 'Clothing')

# print("Созданные элементы:")
# print(read_items())

# update_item(1, price=600) 
# print("\nОбновленные элементы:")
# print(read_items())

# delete_item(0)  
# print("\nЭлементы после удаления:")
# print(read_items())



"""Comprehensions extra"""
8

# list1 = [44,54,64,74,104]
# # Создайте новый list2, прибавив к каждому числу 6
# list2 = [i + 6 for i in list1]
# print(list2)

9
"""Из списка
list1 = [2, 4, 6, 8, 10, 12, 14]
Создайте новый, внеся туда только те числа квадрат которых больше 50
"""
# list1 = [2, 4, 6, 8, 10, 12, 14]
# list2 = [i**2 for i in list1 if i**2 > 50]
# print(list2)

10
"""
Из сторки string = "happy birthday!"
Создайте список list_, внесите туда все символы из строки кроме пробела и '!'
 
Вывод:
['h', 'a', 'p', 'p', 'y', 'b', 'i', 'r', 't', 'h', 'd', 'a', 'y']
"""
# string = "happy birthday!"
# list_ = [i for i in string if i != ' ' and i !='!']
# print(list_)

11
"""
Дан словарь:
dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
Используйте его чтобы создать список, из значений внутренних словарей

Вывод:
[3, 45, 23, 9, 12, 89]
"""
# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list1 = [num for x in dict_.values() for num in x.values()]
# print(list1)

# #print(dict_['a']['d'], dict_['a']['e'])
12
"""
Из списка:
list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
Создайте словарь, занесите только те имена, длина которых больше 4.
Ключами будут имена, а значениями их длины, возведенные  
в квадрат. 

Вывод:
{'george': 36, 'ringo': 25, 'patty': 25, 'cynthia': 49, 'linda': 25}
"""
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# dict_ = {name: len(name) ** 2 for name in list_name if len(name) > 4}
# print(dict_)

13
"""
Дан словарь
dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
Пройдитесь по словарю и добавьте в список только те ключи, значение, которых
в диапазоне от 200 до 5000, добавленные в список ключи должны быть в верхнем регистре.
Нужно использовать comprehension.
"""
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# new_dict = {name.upper(): chislo for name, chislo in dict_.items() if chislo in range(200, 5001)}
# print(new_dict)

14
"""
Дан словарь:
dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
Создайте словарь dict2:
- Ключи должны быть те же, что и в первом словаре, но каждый символ 'i' замените на ''
- Значением должно быть количество повторений символа 'i' в этом ключе

Вывод:
{'Sedan': 0, 'SUV': 0, 'Pckup': 1, 'Mvan': 2, 'Vann': 0, 'Sem': 1, 'Bcycle': 1, 'Motorcycle': 0}
"""
# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {name.replace(i, ''): len(name) - len(name.replace(i, '')) for name in dict1 for i in name if i=='i'}
# print(dict2)

# dict3 = {name.replace('i', ''): name.count('i') for name in dict1.keys()}
# print(dict3)

15
"""
Из списка 
list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
Создайте новый list2, не добавляя все пустые значения(0, None, [], {}, '') 

Вывод:
[1, 2, 3, 'a', 'abc', 23, [1, 2, 3, 4], {'a': 1, 'b': 2}, 'drf']
"""

# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = [i for i in list1 if i not in [0, None, [], {}, '']]
# print(list2)

16
"""
Дан список SPL_Patrons. Каждый его подсписок содержит две части информации
о посетителях библиотеки:
- имя посетителя
- количество книг, которые они одолжили за последний год
Используйте list comprehension, 
чтобы создать список readers имен меценатов, 
которые в прошлом году одолжили более 100 книг

Вывод:
['Kim Tremblay', 'Jessica Smith', 'Alex Roy', 'Sarah Khan', 'Samuel Lee', 'Ayesha Qureshi']
"""

# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

# readers = [i[0] for i in SPL_Patrons for x in i if isinstance(x, int) and x > 100]
# print(readers)

17
"""
Из предыдущего списка SPL_Patrons:
предположим, что посетитель экономит в среднем 11,95 доллара, 
одалживая книгу вместо того, чтобы покупать ее. 
Используйте list comprehension, чтобы создать список saved_amount 
сэкономленной суммы для каждого клиента


Вывод:
[1601.3, 501.9, 2569.25, 1804.45, 1254.75, 2629.0, 286.79, 2378.05, 669.19, 824.55]
"""
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

# saved_amount = [round(i[1] * 11.95, 2) for i in SPL_Patrons]
# print(saved_amount)

18
"""
Используйте comprehensions для создания списка из списков, 
где каждый подсписок состоит из имени пирата и стоимости 
его / ее награбленных мешков с зерном 
(рассчитайте стоимость зерна, предположим, 
что средняя рыночная стоимость мешка зерна составляет 42 доллара, 
но включите только тех пиратов, которые любят попугаев)

Вывод:
[['Tractor Jack', 42000], ['Prairie Lily', 10290], ['Red River Rosie', 14700], ['Assiniboine Sally', 26040], ['Thresher Tom', 6300]]
"""

# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]

# papagei_pirates = [[pirat_data[0], pirat_data[1] * 42] for pirat_data in prairie_pirates if pirat_data[-1] == True]
# print(papagei_pirates)

19
"""
По данному ниже словарю, пройдитесь циклом
- Найдите сумму лайков всех пользователей, рейтинг которых выше 3
используйте list comprehension
"""

# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }
# ls = [dict_[person]['likes'] for person in dict_ if dict_[person]['rating'] > 3]
# print(sum(ls))


20
"""
Используя приведенный словарь dict_, создайте список из id, 
которые хранятся под ключом comments. Берите только те комментарии, 
количество которых больше 3


Вывод:
[1, 2, 3, 4, 5, 6]
"""
# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }


# ls = [num['id'] for comments in dict_.values() for num in comments['comments'] if len(comments['comments']) > 3]
# print(ls)