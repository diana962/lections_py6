# 1) Палиндром:

# Напишите программу, которая проверяет, является ли введенная пользователем строка палиндромом (читается одинаково с начала и с конца, игнорируя пробелы, регистр букв).

# name = input("Программа проверяет, является ли введенная Вами строка палиндромом. Введите слово: ")
# name = 'mom'
# name = name.upper()
# if name == name[::-1]:
#     print(f'Слово {name} является полиндромом. ')

# else:
#     print(f'Слово {name} НЕ является полиндромом.')

# 2) Подсчет слов:

# Программа должна принимать текст и слово. Напишите программу, которая подсчитывает количество слов в этом предложении.
# text = 'Напишите программу, которая подсчитывает количество слов в этом предложении.'
# one = text.split()
# print(f'В предложении "{text}" насчитывается', len(one), 'слов.' + '\n')

# name = input("Программа должна принимать текст и слово. Она подсчитывает количество слов в предложении. Введите текст: ")
# print('В вашем предложении насчитывается', len(name.split()), 'слов.')

# 3) Генерация пароля:

# Напишите программу, которая генерирует случайный пароль заданной длины. Пароль должен содержать как буквы, так и цифры.

# import random
# import string

# password_length = 16
# all = string.ascii_letters + string.digits
# password = ''.join(random.choice(all) for _ in range(password_length))
# print(password)


# 4) Поиск повторяющихся символов:

# Напишите программу, которая проверяет, есть ли в веденной строке повторяющиеся символы.
# text = 'Goggle'
# repeated = set([symbol for symbol in text if text.count(symbol) >1])
# print('In Text the symbol', repeated, 'was repeated.')



# 5) Подсчет гласных и согласных:

# Введите строку, а затем напишите программу, которая подсчитывает количество гласных и согласных букв в ней.

# text = 'Gojo Satoru'

# soglasnye = 0
# glasnye = 0

# for bukvy in text:
#     if bukvy in set('aeiouy'):
#         glasnye += 1
#     else:
#         soglasnye +=1

# print("Количество гласных равно:", glasnye, '\n', "Количество согласных равно:", soglasnye)
        