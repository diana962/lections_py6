#  Типы данных числа int float
#  = => оператор присваивания

# num = 5 
# print (num) # 5
# num = 79
# print (num) # 79
# num +=1 # num = num + 1
# print (num) # 80
# num -= 5
# print (num)

# abc - нижний регистр
# ABC - верхний регистр

# PEP8
# tomorrow_day = '11.01.2024' Snack case
# tomorrowDay = '11.01.2024' Camel case

# +
# num1 = 5
# num2 = 15
# result = num1 + num2
# print (result)

# -
# num1 = int(input('enter the num1: ')) # то, что в скабках имеет приоритет
# num2 = int(input('enter the num2: '))
# print (num2, '-', num1, '=', num2 - num1)

# *
# num1 = int(input('enter the num1: ')) # то, что в скабках имеет приоритет
# num2 = int(input('enter the num2: '))
# print (num2, '*', num1, '=', num2 * num1)

# /and // and %
# / обычное деление
# // деление без остатка
# % модульное деление (получение остатка от деления)

# num1 = 8
# num2 = 3
# print ('/', num1 / num2)
# print ('//', num1 // num2)
# print ('%',  num1 % num2)

# ** и pow-> возведение в степень 

# print(5**2)
# print(17**55)

# ** 0.5
# print(144 ** 0.5) # квадратный корень
# print(144 ** (1/2)) # квадратный корень

# res = 5 * (15 + 5)
# print(res)

# pow - возведение в степень
# pow(num1, num2, <mod>) # <mod> не обязательное условие = modulnoe delenie
# print(pow(5, 2)) # 5 ** 2
# print(pow(5, 2, 2)) # 5 ** 2 % 2

# a = 6
# b = 3
# res = pow(a, b, 50)
# print(res)

# abs() - абсолютное значение числа -> abs(-5) -> 5
                                         #|-5| -> 5

# a = abs(-16)
# b = abs(15)
# c = abs(-2.5)
# print(a, b, c) 

# round() - округление числа с плавающей точной
# a = 5.47 # если 5.47, то 5, если 5.57, то 6
# print(round(a))

# b =7.389980
# print(round(b, 2)) # 2 это двве цифры после запятой, то есть сотая.

# divmod(a, b) - она выводит два числа, первое число- это результат целого деления (//), а второе число- это модульное деление чисел a и b
# Простыми словами: целое число и ее остаток, но это не дробная часть

# print(22 / 5) #4.4
# print(divmod(22, 5)) #4, 2

# num.py or math

# import math

# a = 5
# print(round(math.sqrt(5), 1))
      
# Множественное присваивание 

# a = 'moloko'
# b = 'voda'
# c = None

# c = b
# b = a
# a = c
# print(a, b)

# a = 'moloko'
# b = 'voda'
# a, b = b, a
# print(a, b)

# num1, num2, num3 = input('num1: '), input('num2: '), input('num3: ')
# print(num1)
# print(num2)
# print(num3)

# from math import pi
# r = int(input('Vvedoite radius: '))
# resP = 2 * r * pi
# resS = r ** 2 * pi
# print ('S okrujnosti: ', round(resS, 2))
# print ('P okrujnosti: ', round(resP, 2))

# from random import randint

# num = randint(1, 10)
# i = 0
# while i < 3:
#     guess = int(input('Guess a number: '))
#     if guess == num: 
#         print('You won!')
#         i = 3
#     i += 1
# print(num)


# from random import uniform 
# for x in range(1,100):
#     num = round(uniform(1,10), 1)
#     print(num)