# Тем кто закончил все задания

"""1)На вход программе подается строка текста – название футбольной команды. Напишите программу, которая повторяет ее на экране со словами « - чемпион!» (без кавычек).
Подсказка: используйте print() и input()
"""
# name = input('Enter name of football team: ') 
# print(name, 'Champion!!!')

# Необходимо всегда сохранять имена файлов с правильным расширением (.py), а иначе она не запустится.

"""
2) Напишите несколько строк кода, выводящих на экран ваше имя и почто-
вый адрес. Адрес напишите в формате, принятом в вашей стране. Ника-
кого ввода от пользователя ваша первая программа принимать не будет,
только вывод на экран и больше ничего.
"""
# name = 'Diana'
# email = 'blablabla@gmail.com'
# print((name +'\n'), email)

"""
3) Напишите программу, запрашивающую у пользователя его имя. В ответ
на ввод на экране должно появиться приветствие с обращением по имени,
введенному с клавиатуры ранее.
Пример вывода: Привет, Джон!
Можете использовать 'end'
"""
# name = input('Hi! What\'s your name?')
# print('Nice to meet you,', name)

"""
4)Напишите программу, запрашивающую у пользователя длину и ширину
комнаты. После ввода значений должен быть произведен расчет площади
комнаты и выведен на экран. Длина и ширина комнаты должны вводиться
в формате числа с плавающей запятой. Дополните ввод и вывод единицами
измерения, принятыми в вашей стране. Это могут быть футы или метры.
"""

# l = float(input('Enter lenght of the room: '))
# b = float(input('Enter bright of the room: '))
# s = l * b
# print('Area of the room is', str(s), 'm2')

"""
5)Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель.

Пример ввода: 
—>
Привет
Джон
Сноу

Вывод:
Привет—>Джон—>Сноу

"""
# sep = '-->'
# name = input('Enter a name: ')
# surname = input('Enter surname: ')
# print('Hi', sep, name, sep, surname, sep, 'bye')
