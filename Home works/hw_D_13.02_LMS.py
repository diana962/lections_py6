"""
1) В текстовом файле посчитать количество строк, а также для каждой
отдельной строки определить количество в ней символов и слов.
# """
# with open('txt.txt', 'w+') as file:
#     file.write('Hello, my world\nWelcome home!')
#     file.seek(0)
#     lines = file.readlines()
#     # print(lines)

#     length = len(lines)

#     for i, line in enumerate(lines, 1):
#         line = line.strip()
#         # print(line)
#         symbol = len(line.strip())
#         words = len(line.strip().split()) 

#         print(f'количество строк: {length}, количество в ней символов и слов: {symbol} and {words}')
"""
2) Создайте файл nums.txt, содержащий несколько чисел, записанных через
пробел. Напишите программу, которая подсчитывает и выводит на экран
общую сумму чисел, хранящихся в этом файле.
# """
# count = 0
# with open('nums.txt', 'w+') as file: 
#     file.write('1 2 3 4 5 6 7 8')
#     file.seek(0)
#     for line in file:
#         # print(line)
#         num = line.split()
#         # print(num)
#         for i in num:
#             try:
#                 count += int(i)
#             except:
#                 print(f"{num}' не число.")
#     print("Сумма чисел:", count)

"""
3) Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем
записать их произведение в файл output.txt.
"""
# with open('input.txt', 'w+') as file: 
#     file.write('1 2 3 4 5 6 7 8 9 10 11 12')
#     file.seek(0)
#     first_10 = file.readline().split()[:10]
#     print(first_10)
#     x = 1
#     for i in first_10:
#         z = int(i)
#         x *= z
#     # print(x)
#     with open('output.txt', 'w+') as output_file:
#         output_file.write(str(x))
        


"""
4) В файле записаны в целые числа. Найти максимальное и минимальное
число и записать в другой файл.
"""
# with open('num.txt', 'w+') as file: 
#     file.write('1 2 3 4 5 6 7 8 9 10 11 12')
#     file.seek(0)
#     lines = file.readline().strip().split()
#     print(lines)
#     result = []
#     for i in lines:
#         if i.isdigit:
#             result.append(int(i))
#     # print(min(result), max(result))

#     with open('output.txt', 'w+') as another_file:
#         another_file.write(str(min(result), max(result)))

"""
5) В файле записаны в столбик целые числа. Отсортировать их по
возрастанию суммы цифр и записать в другой файл.
"""

# with open('num.txt', 'w+') as file: 
#     file.write('16 2 37 4 5 61 7 8 9 10 11 12')
#     file.seek(0)
#     lines = file.readline().strip().split()
#     print(lines)
#     result = []
#     for i in lines:
#         if i.isdigit:
#             result.append(int(i))
#     # print(sorted(result))

#     with open('output.txt', 'w+') as another_file:
#         another_file.write(str(sorted(result)))


# 6) Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым: Вечерело Жужжали мухи Светил фонарик Кипела вода в чайнике Венера зажглась на небе Деревья шумели Тучи разошлись Листва зеленела

# with open('article.txt', 'w+') as file:
#     file.write('Вечерело\nЖужжали мухи\nСветил фонарик\nКипела вода в чайнике\nВенера зажглась на небе\nДеревья шумели\nТучи разошлись\nЛиства зеленела')
#     # file.seek(0)
#     # data = file.readline()
#     # data1 = file.read()
#     # print(data)

# def read_last(lines_num = int(input('Enter amount of lines you want to see: ')), file = input('Enter a file name: ')):
#     if lines_num < 0:
#         raise ValueError('Enter positive numbers')
#     else:
#         with open(file, 'r') as f:
#             all = f.readlines()
#             for line in all[-lines_num:]:
#                 print(line.strip())
# print(read_last())

# 7) Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
# Проход по все каталогам и файлам в определенной директории можно осуществить при помощи функции walk() модуля os.

# import os
# def print_docs(directory):
#     for root, dirs, files in os.walk(directory):
#         print(f"Directory: {root}")
#         for file in files:
#             print(f" - File: {file}")
# print(print_docs('/Users/diana/Desktop/PY6_/files'))

# 8) Документ «article.txt» содержит следующий текст: Вечерело Жужжали мухи Светил фонарик Кипела вода в чайнике Венера зажглась на небе Деревья шумели Тучи разошлись Листва зеленела Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).


# with open('article.txt', 'w+') as file:
#     file.write('Вечерело Жужжали мухи Светил фонарик Кипела вода в чайнике Венера зажглась на небе Деревья шумели Тучи разошлись Листва зеленела')

# def longest_words(file):
#     with open(file, 'r') as f:
#         all = f.readline().strip().split()
#         result = []
#         maxx = len(max(all, key=len))
#         # print(maxx)
#         for i in all:
#             if len(i) == maxx:
#                 result.append(i)   
#     return(result)
# print(longest_words('article.txt'))


# 9) Требуется создать csv-файл «rows_300.csv» со следующими столбцами: – № - номер по порядку (от 1 до 300); – Секунда – текущая секунда на вашем ПК; – Микросекунда – текущая миллисекунда на часах. На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
# import time
# def get_time():
#     current_time = time.time()
#     seconds = int(current_time)
#     microseconds = int((current_time - seconds) * 1000)
#     return seconds, microseconds
# print(get_time())

# import csv
# with open('rows_300.csv', 'w') as file:
#     fieldname = ['№', 'Sekunde', 'Mikrosekunde']
#     writer = csv.DictWriter(file, fieldname)
#     writer.writerow({
#         '№': '№', 
#         'Sekunde': 'Sekunde',
#         'Mikrosekunde': 'Mikrosekunde'})
#     with open('rows_300.csv', 'a') as file:
#         fieldname = ['№', 'Sekunde', 'Mikrosekunde']
#         writer = csv.DictWriter(file, fieldname)
#         for count in range(1, 301):
#             seconds, microseconds = get_time()
#             writer.writerow({
#                 '№': count, 
#                 'Sekunde': seconds,
#                 'Mikrosekunde': microseconds
#             })
#             time.sleep = 0.1

'''
# 10) При помощи библиотеки Pillow в директории circles (создайте ее во время выполнения функции) нарисуйте и сохраните 100 кругов радиусом 300 пикселей случайных цветов в формате jpg на белом фоне (каждый круг - отдельный файл). Для этого напишите функцию circles_generator(num_of_circles=100).
# В первую очередь требуется установка модуля Pillow: pip install Pillow 
# Осталось только случайным образом генерировать цвета в палитре RGB и воспользоваться классами Image, ImageDraw из установленной библиотеки. Чтобы нарисовать круг, нужно применить метод ellipse() и задать координаты точек, соответствующие квадрату.
'''

# 11) Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
# наименование товара;
# количество товара (целое число);
# цена (в рублях) товара за 1 шт. (целое число).
# Напишите программу, подсчитывающую общую стоимость заказа.
# with open('prices.txt', 'w+') as file:
#     file.write('Apple\t3\t140000 \nSamsung\t1\t57000\nRedmi\t10\t30000')

# def itog(file):
#     cost = 0
#     with open(file, 'r') as f:
#         for line in f:
#             colona = line.strip().split('\t')
#             kol = int(colona[1])
#             price = int(colona[2])
#             cost += kol * price
#     return cost

# print(itog('prices.txt'))



# 12) Словарь из csv. Имеется файл data.csv, содержащий информацию в csv-формате. Напишите функцию read_csv() для чтения данных из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей. Функция read_csv() не должна принимать аргументов.

# dict_ = {'students': 'grades'}

# import csv
# with open('data.csv', 'w+') as file:
#     fieldname = ['key', 'value']
#     writer = csv.DictWriter(file, fieldname)
#     writer.writerow({
#         'key': 'Key',
#         'value': 'Value'})

# with open('data.csv', 'a') as file:
#     fieldname = ['key', 'value']
#     writer = csv.DictWriter(file, fieldname)
#     writer.writerow({
#         'key': dict_.keys(),
#         'value': dict_['students']})

# def read_csv(file):
#     with open(file, 'r') as file:
#         return(file.read())
# print(read_csv('data.csv'))

# 13) Запрещенные слова
# Напишите программу, которая получает на вход строку с названием текстового файла, и выводит на экран содержимое этого файла, заменяя все запрещенные слова звездочками * (количество дочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
# Формат ввода
# Строка текста с именем существующего текстового файла, в котором необходимо заменить запрещенные слова звездочками.
# Формат вывода
# Текст, отредактированный в соответствии с условием задачи.
# Пример ввода вывода
# Предположим, что forbidden_words.txt содержит следующие запрещенные слова:
# hello email python the exam wor is
# А текст файла, подлежащего цензуре, выглядит так:
# Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!
# Тогда программа должна вывести отредактированный текст в таком виде:
# *, *ld! **  * programming language of * future. My * .... **  awesome!!!!


# def censored(file=input("Введите имя файла с запрещенными словами: "), text = input("Введите имя текстового файла: ").lower()):
#     with open(file, 'r') as f:
#         forbidden_words = f.read().split()
#     for word in forbidden_words:
#         text = text.replace(word, '*' * len(word))
#     censored_text = ''
#     i = 0
#     for symbol in text:
#         if symbol.isalpha():
#             if text[i].isalpha():
#                 if text[i] == symbol.lower():
#                     censored_text += '*'
#                 else:
#                     censored_text += symbol
#                 i += 1
#             else:
#                 censored_text += symbol
#         else:
#             censored_text += symbol
#     return censored_text

# 14) В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов

# with open('students.txt', 'w+') as file:
#     file.write('Adina 2\n Burul 4\n Aigerim 3')

# def students_with_low_grades(file):
#     with open(file, 'r') as f:
#         for line in f:
#             name, grade = line.strip().split()
#             if int(grade) < 3:
#                 print(name)

# students_with_low_grades('students.txt')



# 15) Выведите в обратном порядке содержимое всего файла полностью. Для этого считайте файл целиком при помощи метода read().
# Примеры
# входные данные:
# Beautiful is better than ugly. 
# Explicit is better than implicit. 
# Simple is better than complex.
# Complex is better than complicated.

# выходные данные:
# .detacilpmoc naht retteb si xelpmoC 
# .xelpmoc naht retteb si elpmiS 
# .ticilpmi naht retteb si ticilpxE 
# .ylgu naht retteb si lufituaeB

# with open('article.txt', 'w+') as file:
#     file.write('Beautiful is better than ugly. \nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.')

# def reversed(file):
#      with open(file, 'r') as f:
#         all = f.readlines()
#         for line in all:
#             print(line[::-1].strip())
# print(reversed('article.txt'))