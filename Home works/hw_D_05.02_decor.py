# 1) '''Напишите декоратор, который проверяет, что функция вызывается с определенными типами аргументов.'''

# def decor(func):
#     def wrapper(*args, **kwargs):
#         try: 
#             print(func(*args, **kwargs))
#         except:
#             print('The argument and its type dont match.')
#     return wrapper

# @decor
# def plus(x, y):
#     return x + y
# print(plus(1 , '3'))

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

# 2) '''Создайте декоратор, который автоматически преобразует результат функции в другой тип данных,'''

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

# 3) '''Реализуйте декоратор, который ограничивает максимальное количество вызовов функции.'''

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


# 4) '''Напишите декоратор, который автоматически логирует исключения, возникающие внутри функции.'''

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

# 5) '''Создайте декоратор, который выполняет аутентификацию пользователя перед вызовом функции.'''

# def Decor(func):
#     def wrapper(*args):
#         print('wrapper works on it\'s own')
    
#     return wrapper

# @Decor
# def name(str):
#     return(str)
# print(name('Diku'))



# 6) '''Реализуйте декоратор, который изменяет значение возвращаемого результата функции, например, умножая его на определенный коэффициент.'''

# #

# 7) '''Напишите декоратор, который ограничивает доступ к функции только определенным пользователям или ролям.'''


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

# 8) '''Создайте декоратор, который преобразует аргументы функции в определенный формат перед её выполнением, например, в строку в верхнем регистре.'''

# #

# 9) '''Напишите декоратор, который устанавливает максимальное время выполнения функции и завершает её, если оно превышено.'''

# #

# 10) '''Напишите декоратор, который ограничивает доступ к функции только в определенное время суток.'''



# 11) Напишите декоратор, который перехватывает определенные исключения, возникающие в функции, и преобразует их в другие исключения или обрабатывает особым образом.





# 7) '''Напишите декоратор, который ограничивает доступ к функции только
#  определенным пользователям или ролям.'''
# users = [
#     {'name':'Nasty','roles':'moderator'},
#     {'name':'Anton','roles':'admin'},
#     {'name':'Stark','roles':'user'},
#     {'name':'Tony','roles':'admin'},
# ]
# def user_roles(user_name):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             user = next((u for u in users if u['name'] == user_name),None) 
#             #проверяет есть ли вользователь в словаре и если есть он выводит его в переменную
            
#             if 'roles' in user:
#                 required_roles = user['roles']
#                 if required_roles in user['roles'] and required_roles in ('admin','moderator'):
#                     return func(*args,**kwargs)
#                 else:
#                     raise PermissionError(f"User '{user_name}' doesn't have to permission")
#             else:
#                 raise ValueError(f"User '{user_name}' not found in the user list")
#         return wrapper
#     return decorator

# @user_roles('Anton')
# def admin_func():
#     return f'hello world'
# print(admin_func())

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         try:
#             res = func(*args)
#             if float(res):
#                 print(f'Function is worked yeaaahh')
#                 return res
#             else:
#                 raise ValueError
#         except ValueError:
#             f'GG error blyat'

#     return wrapper
# @decorator
# def test_xt(a='5.2'):
#     return a
# print(test_xt())

# def except_log(func):
#     """Декоратор, записывающий все исключения в файл log"""
#     import traceback
#     from datetime import datetime

#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             with open("log.txt", "a") as f:
#                 timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#                 message = f"{timestamp}\n\n{traceback.format_exc()}"
#                 f.write(message + "\n\n")

#     return wrapper


# @except_log
# def raise_exception():
#     """Функция, которая может бросить исключение"""
#     1 / 0

# raise_exception()  
# with open("log.txt", "r") as f:
#     for x in f:
#         print(x)
