# Обработка исключений
# Операторы try...except

# Ошибки Errors - синтакс ошибки, связанные с кодом
    # SyntaxError
    # IndentationError # ошибки с пробелом/ отступом
    # TabError

# Исключения Exceptions --> связаны с неправильными данными, которые передаются в код, операции.
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# BaseException # прородитель всех исключений


# try:
#     num1 = int(input('num : '))
#     num2 = int(input('num : '))
#     print(f'{num1} / {num2} = {num1 / num2}')
# except: 
#     print('invalid Values!')


# print('DIANAAAAAAAAAAAAAAAAAAAAA')


# try:
#     num1 = int(input('num1 : '))
#     num2 = int(input('num2 : '))
#     print(f'{num1} / {num2} = {num1 / num2}')
# except ValueError: 
#     print('Wrong! ')
# except ZeroDivisionError: # or except:
#     print('не дели на ноль')
# default 'except:' must be last 

# print('благодларя try...except код работает дальше, уведомив комментами в принте!')

# Если действие находится за гранью try except, то код выведет ошибку.

# ------------------------------------------------------------------------------------------

# try:
#     <body> # код с веротным исключением
# except:
#     <body except> сработает только, если ошибка в try
# else:
#     <body> сработает только, если нет ошибки в try
# finally:
#     <body> сработатет в любом случае


# dict_ = {1: 'bir', 2: 'two', 3: 'three'}

# try:
#     key = int(input('Enter s key: '))
#     print(dict_[key])
# except ValueError: #-> сработал так как вводится может только int
#     print('Invalid value for key!')
# except KeyError:
#     print('Key does not exist')
# else:
#     print('No errors!')
# finally:
#     print('The end!')


# --------------------------------------------------------------------------------------

# отображение ошибки
# 1. import sys

# import sys
# ls = [1,2,3,4,5]

# try:
#     index = int(input('Index: '))
#     print(ls[index])
# except:
#     print(f'oops, we catched{sys.exc_info()} error!')

# # 2. Exception as <name>
    
# ls = [1,2,3,4,5]
# while True:
#     try:
#         index = int(input(':'))
#         print(ls[index])
#     except Exception as name:
#         print(f'oops, we catched{name.__class__} error!')