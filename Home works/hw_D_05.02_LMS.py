# 1) Создайте функцию, которая генерирует рандомное (случайно сгенерированное) число и выводит на окно терминала через команду print(). Далее создайте декоратор, который журналирует это событие. То есть функция декоратор должна писать в dict() предложение: «Функция …………… была запущена успешно», а ключом будет уникальный идентификатор (id).   (15 баллов)

# import requests
# from random import randint
# def decorator(func):
#     def wrapper(*args):
#         print(f'Функция "{func.__name__, func(*args)}" была запущена успешно')
#         # return(func(*args))
#     return wrapper

# @decorator
# def num(num = randint(1, 100)):
#     return num
# print(num())


# 2) Напишите функцию, которая принимает фразу, и возвращает его сокращенную форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest -- FYI и т.п. (10 баллов)

# def abbreviation(str = input('Enter phrase: ').upper().split(' ')):
#     ls = []
#     for letter in str:
#         ls.append(letter[0][0])
#     return (''.join(ls))
# print(abbreviation())

# 3) '''Напишите декоратор, который проверяет, что функция вызывается с определенными типами аргументов.''' (15 баллов)

def decor(func):
    def wrapper(*args, **kwargs):
        try: 
            print(func(*args, **kwargs))
        except:
            print('The argument and its type dont match.')
    return wrapper

@decor
def plus(x, y):
    return x + y
print(plus(1 , '3'))

# def type_check(excepted_type):
#     def decorator(func):
#         # print(excepted_type)
#         def wrapper(*args,**kwargs):
#             for arg in args:
#                 if not isinstance(arg,excepted_type):
#                     raise TypeError(f'Argument {arg} is not {func}')
#             res = func(*args,**kwargs)
#             print(f"Функция {func.name} было успешно запущена")
#             return res
#         return wrapper
#     return decorator

# @type_check(int)
# def int_num(*args):
#     list_ = []
#     for arg in args:
#         argus = arg * 2
#         list_.append(argus)
#     return list_
# print(int_num(5,5,5))

# 4) '''Создайте декоратор, который автоматически преобразует результат функции в другой тип данных,''' (15 баллов)

# def decorator(func):
#     def wrapper(*args):
#         print(type(func(*args)))
#         return(type(list(func(*args))))
#     return wrapper

# @decorator
# def words(str = input('Enter words: ')):
#     return str
#     # return(type(str)) #-> через декор выводил <class 'type'>, так как returnil type(str), a ne str
# print(words())

# 5) '''Реализуйте декоратор, который ограничивает максимальное количество вызовов функции.''' (20 баллов)

# def decor(func):
#     def wrapper(*args):
#         attempts = 10
#         while attempts:
#             print(f'the length: {func(input("Enter smth: "))}')
#             print(f'{attempts} attempts left')
#             attempts -= 1
#     return wrapper

# @decor
# def len_(a): 
#     return len(a)
# print(len_())

# 6) '''Напишите декоратор, который автоматически логирует исключения, возникающие внутри функции.''' (15 баллов)
# def decor(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#             print(f'Функция: {func(*args, **kwargs)} прошла успешно.')
#         except Exception as e:
#             print(f'Возникла ошибка: {e}')
#     return wrapper


# @decor
# def division(a, b):
#     return a / b
# print(division(1, 0))


# 7) '''Напишите декоратор, который ограничивает доступ к функции только определенным пользователям или ролям.''' (15 баллов) 

# def Decor(func):
#     def wrapped(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print({k: v for k, v in result.items() if v == 'admin'})
#     return wrapped

# @Decor
# def ls():
#     dict_= {}
#     while True:
#         user = input('Enter a name or "q" to quit: ') 
#         if user == "q":
#             break
#         else:
#             role = input('Enter admin or user: ')
#         dict_[user] = role
#     return dict_
# print(ls())



