# zip(iterables) - она соединяет каждый элемент итерируемых обьектов между собой в тип данных tuple и возвращает итератор

# ls1 = [1,2,3]
# ls2 = [100, 200, 300, 123]
# ls3 = ['Hello', 'world', 'John']
# result = zip(ls1, ls2, ls3)
# print(result)
# for x in result:
#     print(x)
# ----------------------------------
# all(), any()

# all(iterable) - возвращает True, если все элементы итерируемого обьекта истина, иначе False

# ls = [[1, 2], -5, 'stroka', 1]
# print(all(ls))

# ip1 = '10.255.12.155'
# ip2 = '10.255.1y.123'

# result = all(x.isdigit() for x in ip1.split('.'))
# print(result)
# result2 = all(x.isdigit() for x in ip2.split('.'))
# print(result2)

# any - возвращает True, если хотя бы один элемент истина.

# ls = [0, 0, '', None, [], 1]
# print(any(ls))

# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']
# command = input('Enter a command: ')
# if any(x in command for x in ignore):
#     raise Exception('You don\'t have permmissions!')

# print('ok')

# Анонимные функции - lambda(обычные функции тольок без названия)
# lambda функции могут принимать сколько угодно аргументов, но всегда возвращают одно выражение

# def sum_of_args(a, b):
#     return a + b

# print(sum_of_args(6, 5))

# func = lambda a, b: a+b
# print(func(15, 5))

# def myFunc(n):
#     def result(num):
#         return num * n
#     return result

# myDoubler = myFunc(2) #-> n = 2
# myTripler = myFunc(3) #-> n = 3

# print(myDoubler(50)) #-> num = 50
# print(myDoubler(76))
# print(myDoubler(150))

# print(myTripler(55)) #-> num = 55

# def myFunc(n):
#     return lambda num: num * n

# res= myFunc(4)
# print(res(10))

# dict_ = {'John': 1000000, 'Jamie': 100, 'Din': 10000, 'Anvar': 500, 'Sam': 100000}
# res = sorted(dict_.items()) #-> он отсортировал по алфавиту
# print(res)

# res = sorted(dict_.items(), key = lambda x: x[1], reverse = True) #-> он отсортировал по значениям
# print(res)

# enumerate - она пронумеровывает кадждый элемент внутри iterable, ее собствееным индексом

# ls = ['hello', 'world', 'Din', 'Sam', 'Winchesters']
# res = list(enumerate(ls, 1)) # -> по default begins with index 0: enumerate(ls)
# print(res)

# for i, x in enumerate(ls):
#     print(f'Index: {i}, Element: {x}')

#------------------------------------------------
# map(function, iterable) ->  применяет функцию, которую мы передаем ко всем элементам iterable

# ls = ['one', 'two', 'three', 'Anvar-King']
# res = list(map(str.upper, ls))
# print(res)

# map, zip нужно оборачивать во что то.

# names = ['John', 'Din', 'SUltan', 'Anvar', 'Sam']

# res = list(map(lambda name: f'Hello {name}', names)) #-> names нужен для тандема с map
# print(res)

# dict_ = {1: 2, 3: 4, 5: 6}
# # for i in dict_:
# #     dict_[i] = str(i)
# # print(dict_)

# res = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print(res)

#-------------------------------------------------------------
#filter(function, iterable) -> применяет ко всем элементам iterable функуию, которую ы передали и возвращает итератор с теми же элементами ддля которых функция вернула True

# ls = ['one', 'two', '', 'list', '100', '12', 'din']
# res = list(filter(str.isdigit, ls)) # or ''.isdigit
# print(res)

# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)
# print(res)

# ls = ['john', 'codify', 'aibek', 'ono', 'bootcamp', 'Kyrgyzstan', 'mountains'] 
# res = list(filter(lambda x: len(x) > 5, ls))
# print(res)

# ls =[
#     {'name': 'Python', 'point': 10}, 
#     {'name': 'C++', 'point': 6},
#     {'name': 'JS', 'point': 8},
#     {'name': 'Java', 'point': 3},
#     {'name': 'C#', 'point': 9},
# ]

# res = list(filter(lambda dict_: dict_['point'] > 8, ls))
# print(res)

# users = [
#     {'username': 'Din', 'comments': ['I love you', 'so gorgeous']},
#     {'username': 'Raychel', 'comments': []},
#     {'username': 'Steven', 'comments': ['Bischkek', 'Python']},
#     {'username': 'Sam', 'comments': []},
#     {'username': 'Kira', 'comments': ['The best post']}
# ]

# res = list(filter(lambda dict_: len(dict_['comments']) > 0, users))
# print(res)

# active_users = list(filter(lambda obj: obj['comments'], users))
# inactive_users = list(filter(lambda obj: not obj['comments'], users))
# print(active_users)
# print(inactive_users)

#-------------------------------------------
# names = ['Raychel', 'Sultan', 'Aigerim', 'John', 'Kira', 'Bob']

# res = list(map(lambda x: f'Hello Mr/Mrs {x}', filter(lambda x: len(x)> 5, names)))
# print(res)

#--------------------------------------------
# Функция Reduce () принимает функцию и последовательность и возвращает одно значение, рассчитанное следующим образом:
# 1. Первоначально функция вызывается с первыми двумя элементами из последовательности, и результат возвращается.
# 2. Затем функция вызывается снова с результатом, полученным на шаге 1, и следующим значением в последовательности. Этот процесс повторяется до тех пор, пока в последовательности не закончатся элементы.

# from functools import reduce

# ls = [1, 2, 3, 4, 5]
# sum_ = reduce(lambda x, y: x + y, ls)
# res = reduce(lambda a, b: a * b, ls)
# print(sum_, res)

#----------------------------------------------

# from itertools import repeat
# from random import choices, shuffle
# from string import ascii_letters, digits
# from statistics import mean #-> среднее значение

# symbols = '_()$!%+-@#'

# (for x in repeat(lambda x: x, 15):
#     print(x)) -> just for explanation of repeat

# q_pass = int(input('Enter a length of password: '))
# result = {
#     f(choices(ascii_letters, k = 10), 
#       choices(digits, k = 4),
#       choices(symbols, k= 2))
#     for f in repeat(lambda a, d, s: ''.join(set(a + d + s)), q_pass)
#     }

# print(result)
# print(f'Quantity of passwords: {len(result)}')
# dlina = [len(x) for x in result]
# print(f'Average len: {mean(dlina)}')
