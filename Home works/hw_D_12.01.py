"""Задача 1: Индексация и Срезы
Создайте переменную sentence co значением "Привет мир! Меня зовут Python."
Выведите первый и последний символы строки, используя индексацию.
Выведите подстроку, включающую слово "мир", используя срез.
Разверните строку, используя срез.
Выведите каждый второй символ строки."""

# sentence = 'Привет мир! Меня зовут Python.'
# print(sentence.find(sentence[0]), sentence.find(sentence[-1]))

# first = sentence[0] # найти начало 0 и конец предложения -1
# last = sentence[-1]
# print(first, last)
# print(sentence.find(first), sentence.find(last))

# print(sentence[7:10])
# print(sentence[:7], sentence[10:])
# print(sentence[::2])


"""Задача 2: Конкатенация строк
Примите от пользователя first_name и last_name и присвойте им ваше имя и фамилию.
Сконкатенируйте эти строки, чтобы получить полное имя.
Создайте строку greeting c приветствием и используйте конкатенацию, чтобы добавить полное имя.
Добавьте пробел между именем и фамилией, используя конкатенацию.
Создайте строку age c вашим возрастом и конкатенируйте её c предыдущими данными."""

# first_name = input('Enter vorname: ')
# last_name = input('Enter surname: ')
# print(f'Your name is {first_name}, your surname is {last_name}.')
# print(first_name + last_name)

# greeting = 'Добро пожаловать, '
# print(greeting + first_name + ' ' + last_name)

# print(first_name, '\t', last_name)

# age = int(input('Enter age: '))
# print(f'Your name is {first_name}, your surname is {last_name}, your age is {age}.')



"""Задача 3: Методы строк
Создайте строку text co значением "Программирование на Python - это увлекательно!".
Используйте встроенный метод , чтобы заменить слово "Python" на "JavaScript".
Уберите пробелы в начале и конце строки, используя встроенный метод .
Проверьте, состоит ли строка только из букв.
Выведите индекс первого вхождения буквы "a" в строке."""

# text = "     Программирование на Python - это увлекательно!     "
# print(text.replace('Python', 'JavaScript'))
# print(text.lstrip(), '\n' , text.rstrip())
# print(text.isalpha()) # проверила, не состоит
# print(text.replace(' ','').isalpha())
# print(text.index('а'))


"""Задача 4: Форматирование строк
Запросите у пользователя ввод имени и фамилии. Выведите приветствие, используя форматирование %.
Снова запросите у пользователя ввод имени и фамилии. Выведите приветствие, используя метод .format.
Попросите пользователя ввести имя и фамилию. Выведите приветствие с использованием f-строки."""

# first_name = input('Enter vorname: ')
# last_name = input('Enter surname: ')
# print('Your name is %s, your surname is %s.' %(first_name, last_name))
# print('Your name is {}, your surname is {}.'.format(first_name, last_name))
# print(f'Your name is {first_name}, your surname is {last_name}.')

"""Задача 5: Дополнительные методы
Создайте строку sentence со значением "Строки - это базовый тип данных в Python.".
Подсчитайте сколько раз слово "Python" встречается в строке.
Разделить строку на слова и сохраните результат в списке.
Снова используйте созданный список слов и объедините слова обратно в строку, разделяя их запятой.
Примените метод swapcase к строке и выведите результат"""

# sentence = "Строки - это базовый тип данных в Python."
# print(sentence.count('Python'))
# print(sentence.split(' '))
# print(','.join(sentence.split(' ')))

# print(sentence.swapcase())