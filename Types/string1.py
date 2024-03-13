# 'String - Строки'
# 'Hello my name is John Snow'

# str1 = '''
# I\'m John Snow.
# I\'m King of North!
# '''
# print(str1)

# Строки - набор последовательных символов, которые мы используем для хранения и представления текстовой информации. 

# Индексация в строке
# name = 'John'
#         # J = 0 = -4
#         # o = 1 = -3
#         # h = 2 = -2
#         # n = 3 = -1
# print(name)
# print(name[1], name[3])
# print(name[ -1]) # -1 всегда последний символ, а 0 всегда первый

# срезы по индексам
# [start: end: <step>]

# str1 = 'birthday'
# print(str1[0:5], str1[::2])
# print(str1)
# print(str1[0:5])  # пятерка в данном случае не включена, так как квадратные скобки так и работают.
# print(str1[5:8])

# print(str1[:5])  до 5
# print(str1[5:]) от 5 

# text = 'hello world! My name is John Snow and I am a king of north!'
# print(text[:13])
# print(text[:13:2]) # :2 step в данном случае вырезвет каждый второй символ.
# print(text[::2])
# print(text[::-1]) # отрицательные значения берут начало в конце.
# print(text[::-2])

# Конкатенация строк(соединение
# a = 'Hello'
# b = 'World'
# c = ' '
# res = a + c + b
# res = a + ' ' + b
# print(res)
# print(a + '\t' + b)

# экранирование - способ записи символов в строку, которые невозможно ввести с клавиатуры, 
# либо же записи спец символов, которые имеют функционал в питоне.

#  \n --> перенос строки 
#  \t --> горизонтальная табуляция
#  \v --> вертикальная табуляция
#  \' --> апостроф

# str1 = '\tHello world!\n\v\tHello John!\n \'\\'
# print(str1)

# Форматирование строк ==> Интерполяция
# 1. с помощью %
# 2. с использовнаием .format()
# 3. интерполяция(преобразование строк) f - stroki

# 1) Пример с помощью %
# name = input('enter first name: ')
# last_name =input('enter last name: ')
# str1 = 'Hello mr/mrs %s %s' %(name, last_name) # 
# print(str1)

# 2) .format()
# name = input('enter first name: ')
# last_name =input('enter last name: ')
# club = 'Kipish'
# print('Welcome in the club, {}, mr/mrs {} {}!'.format(club, name, last_name))

# # f - строки
# name = input('enter first name: ')
# last_name =input('enter last name: ')
# print(f'hello mr/mrs {name} {last_name}! Welcome to the party!')

# Умножение строк (дублирование)
# str1 = 'Codify'
# print(str1 * 3)