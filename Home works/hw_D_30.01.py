# 1) Напишите функцию -- чат-бот, который 
# Всегда отвечает “Конечно!” на любой вопрос
# Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
# Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же духе!” Если вызвал функцию, но ничего не передал.
# В любых других случаях, отвечает “ну и что

# ”"""
# def chatbot(user = input('Enter smth: ')):
#     while True:
#         if user == user.upper():
#             print('Успокойся')
#             break
#         if user == '':
#             print('Как классно, когда ты молчишь. Продолжай в том же духе!')
#             break
#         if user.endswith("?"):
#             print('Конечно!')
#             break
#         else:
#             print('ну и что?')
#             break

# print(chatbot())

# """
# 2) Напишите функцию, которая принимает слово и возвращает True, если слово изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False
# """

# """
# 3) Подсчет букв:
# Напишите функцию, которая принимает строку и возвращает словарь, в котором ключами являются буквы, а значениями — количество их вхождений в строку. Регистр букв не должен учитываться.
# """
# def l(user = input('Enter smth: ')):
#     return {user: len(user)}
# print(l())
# """
# 4) Поиск подстроки:
# Напишите функцию, которая принимает две строки и возвращает True, если вторая строка является подстрокой первой.
# """
# def task(str = input('enter smth: '), str1 = input('enter smth: ')):
#     if str in str1:
#         return True
#     else:
#         print('None')

# print(task())
# """
# 5) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано. 
# Например: “Money, money, money, it’s always sunny, in the richmen’s world”. 
# money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.
# """
# def ch(ls = "Money, money, money, it’s always sunny, in the richmen’s world") -> dict:
#     dict_ = dict()
#     for i in set(ls.lower().split(' ')):
#         dict_[i] = ls.lower().count(i)
#     return dict_
# print(ch())

# """
# 6) Напишите функцию, которая принимает строку и выводит количество гласных, согласных букв и остальных символов. Используйте только кириллические символы
# """
# def text(txt = 'Привет'.upper()):
#     soglasnye = 0
#     glasnye = 0
#     for bukvy in txt:
#         if bukvy in set('А, И, О, У, Ы, Э, Е, Ё, Ю, Я'):
#             glasnye += 1
#         else:
#             soglasnye +=1
#     return soglasnye, glasnye

# print(text())

# """
# 7) Вам дан список из нескольких имён в нижнем регистре. Напишите функцию которая записывает начинает первую букву имени в верхнем регистре и сохраните в новом списке.
# """
# def pre(ls = ['anvar', 'katja', 'bolot']):
#     ls1 = []
#     for i in ls:
#         ls1.append(i.capitalize())
#     return ls1

# """
# 8) Вам дан список из целых чисел. Напишите функцию, в которой Вам необходимо найти факториал каждого из чисел и записать в новый список.
# """
# def factorial(ls = [1, 3, 4]):
#     ls1 = []
#     for i in ls:
#         res = 0
#         for i in range(1, i+1):
#             res += i
#         ls1.append(res)
#     return ls1

# print(factorial())
# """
# 9) Вам дан список из чисел. Напишите функцию, которая вернёт новый список из квадратов этих чисел.
# """
# def q(ls = [1, 3, 4]):
#     ls1 = []
#     for i in ls:
#         ls1.append(i ** 2)
#     return ls1

# print(q())

# # 10) Напишите функцию average, которая принимает список чисел и возвращает их среднее значение, НЕ используя встроенные функции sum и len
# def average(user = input('Enter numbers:'))->int:
#     list(user)
#     summa = 0
#     for x in list(user.split(',')):
#         x = int(x)
#         summa += x
#     count = 0
#     for i in list(user.split(',')):
#         count +=1
#     return summa/count

# print(average())
