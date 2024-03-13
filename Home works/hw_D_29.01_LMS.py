# Задача 1: Валидация пароля

# Пользователь хочет установить пароль для своей учетной записи. Пароль должен соответствовать следующим критериям:

# password = input('Enter a possible password: ')

# # big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# # small = 'abcdefghijklmnopqrstuvwxyz'
# # digit = '1234567890'
# # symbols = '!@#$%^&*()_-+=<>?/'

# if len(password) < 8:
#     raise ValueError('Password cannot be longer than 8 symbols.')
# elif not any(char.isupper() for char in password):
#     raise ValueError('Password must have at least one capital letter.')
# elif not any(char.islower() for char in password):
#     raise ValueError('Password must have at least one строчную letter.')
# elif not any(char.isdigit() for char in password):
#     raise ValueError('Password must have at least one digit.')
# elif not any(char in '!@#$%^&*()_-+=<>?/' for char in password):
#     raise ValueError('Password must have at least one специальный символ из множества: !@#$%^&*()_-+=<>?/')


# password2 = input('Enter a password again: ') 
# if password2 != password:
#     print('Password is wrong')
# else:
#     print('Password accepted.')

# Задача 2: Обработка ошибок при работе с элементами списка:

# ls = [1, 2, 3, 4, 5, 6, 7]

# try:
#     # print(ls.index(8))
#     ## print(ls[8])
#     ### for x in ls:
#         ###print(x/0)
# except ValueError:
#     print('not in list')
# except IndexError:
#     print('list index out of range')
# except ZeroDivisionError:
    # print('division by zero not possible')

# Задача 3: Поиск значения в словаре с обработкой исключения:

# Создайте словарь с данными (например, словарь с именами и возрастами людей). Затем запросите у пользователя имя и попробуйте найти возраст этой персоны в словаре. Обработайте исключение, если имя не найдено.

# dict_ = {
#     'Diana': 21,
#     'Aika': 20,
#     'Ayana': 21
# }

# try:
#     user = input('Enter a name: ')
#     if user in dict_:
#         print(f'Age of {user} is', dict_[user])
#     else:
#         raise KeyError
# except:
#     print('такого человека я не знаю')

