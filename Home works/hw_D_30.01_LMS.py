# Задача 1. Сумма чисел (10 баллов)

# Напишите функцию summa_n, которая принимает одно целое положительное число N и выводит сумму всех чисел от 1 до N включительно. 

# Реализуйте через цикл while, для выхода из цикла пользователь должен ввести "выход" (5 баллов)


# def summa_n():
#     while True:
#         a = input('Введите одно целое положительное число или нажмите "q", чтобы выйти: ')
#         if a == "q":
#             break
#         elif a.isdigit() == True:
#             a = int(a)
#             ls = list(range(0, a + 1))
#             print (f'Я знаю, что сумма чисел от 1 до {a} равна {sum(ls)}')
#         else:
#             print('Введите только одно целое положительное число')
#             continue
# # return мостанавливает работу while
# summa_n()

# Задача 2. Функция в функции (15 баллов)

# Асан проходит специальный тест по программированию. У него всё шло хорошо, пока он не наткнулся на тему «Функции». Задание звучит так:
# def test(num = input('Number: '))-> int:
#     if num.startswith('-') or num.isdigit() == True:
#         num = int(num)
#         if num > 0:
#             def positive():
#                 print('positive')
#             positive()    
#         else:
#             def negative():
#                 return ('negative')
#             negative()
#     else: 
#         return('Not number')
# print(test())

# Задача 3. Площади (15 баллов)

# Муниципалитет хочет построить необычный парк в одном из районов города. Власти остановились на трёх вариантах: 
# изображение на карте в виде круга, прямоугольника или треугольника. Однако им также нужно понять, какую площадь будет занимать тот или иной вариант при разных значениях.

# Напишите программу, которая в зависимости от выбора пользователя вычисляет площадь круга, прямоугольника или треугольника. Для вычисления площади каждой фигуры должна быть написана отдельная функция. (Формулы нахождения площадей попробуйте найти в интернете)))

# from math import sqrt, pi
# def area(r = int(input('Enter radius круга: ')))-> int:
#     return pi * r**2
# def areaP(a = int(input('Enter одну сторону прямоугольника: ')), b = int(input('Enter другую сторону прямоугольника: ')))-> int:
#     return a * b
# def areaT(a = int(input('Enter одну сторону треугольника: ')), b = int(input('Enter другую сторону треугольника: ')), c = int(input('Enter third сторону треугольника: ')))->int:
#     return sqrt((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c))

# print(area())
# print(areaP())
# print(areaT())

# Задача 4. Число наоборот (15 баллов)

# Пример:
# Реализовать через цикл while, соответственно для выхода из цикла, пользователь должен будет ввести 0 и вывести сообщение "Программа завершена!" (5 баллов)
# Дополнительно: добейтесь такого вывода чисел, в начале которых идут нули

# def naoborot(user = input('Enter a number: ')) -> str:
#     while True:
#         if user == '0':
#             print('Программа завершена!')
#             break
#         else:
#             user = user[::-1]
#             break
#     return user
# print(naoborot())


# Задача 5. Копейки (20 баллов)

# На одном складе нашли старые кассовые аппараты, в которых, как выяснилось, до сих пор остались лежать копейки разного достоинства. Даже однокопеечные есть! Все найденные копейки собрали в кучу и закинули в специальное устройство, которое сканирует все монеты и в результате выдаёт, сколько всё это будет в рублях.

# Напишите функцию, которая будет считать количество мелких монеток достоинством в 1, 5, 10 и 50 копеек. Функция должна выводить общую сумму.


# Пример:

# Монет по 1 копейке: 3

# Монет по 5 копеек: 6

# Монет по 10 копеек: 7

# Монет по 50 копеек: 2

# Всего у нас 2.03 рубля

# def sum_of_args(a, b, c, d):
# def sum_of_args(a = int(input('Монет по 1 копейке: ')), b = int(input('Монет по 5 копейке: ')) * 5, c = int(input('Монет по 10 копейке: ')) * 10, d = int(input('Монет по 50 копейке: ')) * 50):
#     print(f'Всего у нас {(a + b + c + d)/100} рубля')
# sum_of_args()

# Задава 6. Калькулятор (продолжение) (15 баллов)

# Реализуйте калькулятор из прошлого д/з через функцию
# def plus(num1 = float(input('Enter a number: ')), num2 = float(input('Enter a number: '))):
#     return num1 + num2
# print(plus())
# def minus(num1 = float(input('Enter a number: ')), num2 = float(input('Enter a number: '))):
#     return num1 - num2
# print(minus())
# def proiz(num1 = float(input('Enter a number: ')), num2 = float(input('Enter a number: '))):
#     return (num1 * num2)
# print(proiz())
# def delen(num1 = float(input('Enter a number: ')), num2 = float(input('Enter a number: '))):
#     if num2 != 0:
#         return num1 / num2
#     else:
#         return ("На ноль делить нельзя! ")
# print(delen())