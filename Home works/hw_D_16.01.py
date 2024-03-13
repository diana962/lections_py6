# 1) Создайте словарь тремя возможными способами.
# """
# # писать код здесь

# dict = {
#     '': '',
#     '': ''
# }
# dict1 = dict([(1 , ''), ("", 2)])
# dict2 = dict.fromkeys('default')
# print(type(dict), type(dict2), type(dict1))

# my_dict = {}
# my_dict['ключ1'] = 'значение1'
# my_dict['ключ2'] = 'значение2'
# my_dict['ключ3'] = 'значение3'
# print(my_dict)

# my_dict = dict(ключ1='значение1', ключ2='значение2', ключ3='значение3')
# print(my_dict)

# keys = ['ключ1', 'ключ2', 'ключ3']
# values = ['значение1', 'значение2', 'значение3']

# my_dict = dict.fromkeys(keys, None)
# print(my_dict)

# keys = ['ключ1', 'ключ2', 'ключ3']
# values = ['значение1', 'значение2', 'значение3']

# my_dict = {k: v for k, v in zip(keys, values)}

# keys = ['ключ1', 'ключ2', 'ключ3']
# values = ['значение1', 'значение2', 'значение3']

# my_dict = {}
# my_dict.update(zip(keys, values))


# """
# 2) Объявите словарь, удалите один из элементов и распечатайте удалённый элемент.
# """

# my_dict = dict(ключ1='значение1', ключ2='значение2', ключ3='значение3')
# print(my_dict)
# removed = my_dict.popitem() 
# print(my_dict)
# print(removed)

# """
# 3) Объявите словарь, добавьте в него новую пару - "ключ: значение" и распечатайте.
# """
# my_dict = dict(ключ1 ='значение1', ключ2 = 'значение2', ключ3 = 'значение3')
# print(my_dict)
# my_dict.setdefault(4, "значение4")
# print(my_dict)
                    

# """
# 4) Объявите словарь, удалите все его элементы и распечатайте.
# """
# my_dict = dict(ключ1 ='значение1', ключ2 = 'значение2', ключ3 = 'значение3')
# print(my_dict)

# my_dict.pop('ключ1')
# my_dict.pop('ключ2')
# my_dict.popitem()
# print(my_dict)

# my_dict.clear()
# print(my_dict)

# """
# 5) Дан словарь, выведите все его ключи.
# """
# dict = {
#     '1': 'no',
#     '0': 'yes'
# }
# ls = dict.keys()
# print(ls)

# """
# 6)  Объявите словарь, сделайте его копию и распечатайте 
# dict = {
#     '1': 'no',
#     '0': 'yes'
# }
# dict_ = (dict)
# print(dict_)

# dict.copy()
# print(dict)

# """
# 7) Это меню вашего ресторана (ключ -- название блюда, значение -- стоимость):
# • menu = {'Pad Thai': 200, 'Tom Yam': 170, 'Chicken Teriyaki': 250}
# • Добавьте в меню новое блюдо 'Fried Rice' и установите стоимость 150
# • Вы решили, что 'Tom Yam' слишком дешевый. Установите новую цену для него: 195
# • Ваш повар отвратительно готовит 'Pad Thai', поэтому хотите удалить это блюдо.
# • Самостоятельно найдите оператор, который удаляет пару “ключ”:”значение”, и удалите 'Pad Thai' из меню.
# • Выведите оставшиеся блюда
# """
# menu = {'Pad Thai': 200, 'Tom Yam': 170, 'Chicken Teriyaki': 250}
# menu.setdefault('Fried Rice', 150)
# print(menu)
# menu.update({'Tom Yam': '195'})
# print(menu)
# menu.
# menu.pop('Pad Thai')
# print(menu)


# """
# 8) Дан словарь, состоящий из элементов типа: слово-синоним. Все слова в словаре различны. Выведите синоним для последнего слова.
# Пример : {‘hello’: ‘hi’, ‘good’: ‘nice’, ‘price’: ‘cost’} --> cost
# """
# dict_ = {
#     'hello': 'hi', 'good': 'nice', 'price': 'cost'
#     }
# dict_.update({'price': 'value'})
# print(dict_)

# """
# 9) Создайте три словаря где будут собраны характеристики некоторых животных, затем выведите краткое описание животных.
# Пример : dog = {‘name’: ‘Lucky’, ‘age’: 5, 'eyes': 'blue' } --> This is a dog. His name is Lucky. It has blue eyes. Lucky is 2 years old. 
# """
# info = {
#     'dog': {'name': 'Lucky', 'age': 5, 'eyes': 'blue' }, #--> This is a dog. c Lucky. It has blue eyes. Lucky is 2 years old. 
#     'cat': {'name': 'Sary', 'age': 7, 'eyes': 'grey' },
#     'bird': {'name': 'Leyla Lewellyn', 'age': 15, 'eyes': 'green' }
# }
# print('This is a dog. His name is', info['dog']['name'], 'It has' , info['dog']['eyes'], 'eyes.', info['dog']['name'], 'is', info['dog']['age'], 'old.')
# print('This is a cat. His name is', info['cat']['name'], 'It has' , info['cat']['eyes'], 'eyes.', info['cat']['name'], 'is', info['cat']['age'], 'old.')
# print('This is a bird. His name is', info['bird']['name'], 'It has' , info['bird']['eyes'], 'eyes.', info['bird']['name'], 'is', info['bird']['age'], 'old.')


# """
# 10) Создайте словарь в котором будет содержаться информация о факультетах и учениках, ключом будет факультет, а значением список с несколькими учениками. 
# Используйте одно имя из списка, который является значением у словаря, для выведения утверждения об этом ученике.
# Пример : {'Civil Engineering': ['Thomas', 'Benjamin', 'Franklin'], 'Psycology': ['Joe', 'Chedwick', 'Helena']}
# --> This is Franklin. He studies Civil Engineering. 
# """
# dict_ = {'Civil Engineering': ['Thomas', 'Benjamin', 'Franklin'], 'Psycology': ['Joe', 'Chedwick', 'Helena']}
# for k, v in dict_.items(): #--> создаем две переменные для key and value
#     for student in v:
#         print('This is', student, '. He studies', k)

# 1) Создайте список изпользуя циклы.
# """
# ls = [0]
# x = input('Enter: ')

# while:
#     ls.append
#     print(x)
# """
# 2) Дан список из чисел, запишите чётные числа в один лист а нечётные в другой лист и выведите результат.
# """
# ls = [1, 2, 3, 4]
# print(ls[::2])
# print(ls[1::2])

# """
# 3) Напишите программу, которая найдет факториал введенного числа.
# """
# n = int((input('Enter chislo: ')))
# res = 0
# for i in range(1, n+1):
#     res += i
# print(res)
# """
# 4) Напишите программу, которая будет находить наибольшую цифру натурального
# числа. Натуральное число вводится с клавиатуры. Найти его наибольшую цифру.

# """
# n1 = int((input('Enter chislo: ')))
# n2 = int((input('Enter chislo: ')))

# if n1 < n2:
#     print('наибольшaya цифрa', n2)
# else:
#     print('наибольшaya цифрa', n1)
# """
# 5) Вам дан список из чисел. Напишите программу в котором вам необходимо найти факториал каждого
# числа и записать в новый список.
# """
# ls = [1, 4, 8]
# ls1 = []

# for x in ls: #--> x это каждый элемент в списке по очереди
#     res = 0 #--> суть факториалов, факториалы начинаются с 0 и постепенно увеличиваются.
#     for i in range(1, x+1): #--> + последующее число, ???
#         res += i
#     ls1.append(res) # --> добавляет все значения в новый список
# print(ls1)
# """
# 6) Вам дан список из чисел. Напишите скрипт в котором она запишет в новый список.
# """
# ls = [1, 2, 3, 4]
# ls1 = []
# for x in ls:
#     ls1.append(x)
# print(ls1)

# 7) Создайте пустой список. Напишите программу которая должна 
# записывать в ваш список числа от 0 до 10 включительно.
# """
# ls = []
# for x in range(0, 11): 
#     ls.append(x)
# print(ls)

# """
# 8) Вам дан список целых чисел. Напишите программу
# которая выводит все элементы которые меньше 7.
# """
# ls = [1, 2, 3, 4, 77]
# ls1 = []
# for x in ls:
#     if x > 7:
#         ls1.append(x)
# print(ls1)
