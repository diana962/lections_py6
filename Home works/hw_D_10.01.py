# 1) Напишите программу, которая генерирует случайное число  от 1 до 100, а затем предлагает пользователю угадать это число. Программа должна предоставить подсказки о том, больше или меньше введенное число загаданного.
# “””
# from random import randint

# num = randint(1, 100)
# guess = int(input('Guess a number from 1 till 100: '))
# if guess == num:
#     print('You\'re lucky!')
# if guess >= num: 
#     print ('It\'s', guess/ num, 'times bigger, than expected.','Try again.')
# if guess <= num: 
#     print ('It\'s',num/guess,'times smaller. Try again.')
# “””

# 2)Напишите программу, которая преобразует температуру из градусов Цельсия в градусы Фаренгейта и наоборот. Позвольте пользователю выбирать тип преобразования.
# ”””
# tem = input('Is temperature of the room in Celsius (a) or Fahrenheit (b)? Enter a or b: ')

# if tem == 'a':
#     celsius = int(input('Enter celsius:  '))
#     resF =  celsius * 9/5 + 32
#     print("In Fahrenheit it will be:", resF)
# if tem == 'b':
#     fahrenheit = float(input('Enter fahrenheit:  '))
#     resC = (fahrenheit - 32) * 5/9
#     print('In Celsius it will be: ', resC)


# “””
# 3) Реализуйте программу, которая рассчитывает ежемесячные выплаты по ипотеке. Пользователь должен ввести сумму кредита, годовую процентную ставку и срок кредита. 
# # ”””
# sum = int(input('Enter summu kredita: ')) # 10_000
# proc = int(input('Gодовую процентную ставку: ')) # 20 procentov = 0.2, 10000 + 10000 * 0.2 / time (god)/ 12(month)
# proc1 = proc / 100 # 20 procentov = 0.2
# time = int(input('Na skoliko let:  ')) # 1
# '''
# # if time != 1:
# #     n = time
# #     print((sum + (sum * proc1))/ time/ 12 + (proc1 * n))
# '''
# print((sum + (sum * proc1))/ time/ 12 + (proc1 * time * 12))

# “””
# 4) Напишите программу, которая генерирует первые n чисел в последовательности Фибоначчи, где n вводится пользователем.
# “””
'''
factorial:
# n = int((input('Enter chislo: ')))
# res = 0
# for i in range(1, n+1):
#     res += i
# print(res)
'''
# n = int((input('Enter number of cycles: ')))
# num = 0
# formula = (num - 1) - (num - 2)
# print(formula)
# # res = 0
# for formula in range(0, n):
#     res == formula
#     print(res)

# Fn = Fn-1 + Fn-2

# # Losung von Sanzhar
# n = int((input('Enter number of cycles: ')))
# # n = 7
# # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
# default = [0, 1]
# if n <=2:
#     print(default)
# else:
#     i = 2
#     while i < n:
#         res = default[-1] + default[-2]
#         default.append(res)
#         i += 1
#     print(default)


# проводить столько циклов от нуля сколько user пожелает:
# a = n + (n+1) --> 0 + 1 = 1 --> 
# b = a + (a+1) --> 1 + 2 = 3 --> 
# c = b + (b+1) --> 3 + 4 = 7 --> 

# print('Последовательность Фибоначчи', a, b, c)

#Последовательность чисел Фибоначчи определяется формулой Fn = Fn-1 + Fn-2 . 
# То есть, следующее число получается как сумма двух предыдущих. 
# Первые два числа равны 1 , затем 2(1+1) , затем 3(1+2) , 5(2+3) 

# “””
# 5) Попросите пользователя ввести количество часов, а затем выведите эквивалентное количество минут.
# ”””
# time = float(input('Привет! Я преобразую часы в минуты. Введи колличестсво часов: '))
# min = time * 60
# print('колличестсво', time, 'часов равна', min, 'минутам')


# “””
# 6) Запросите у пользователя цену товара и количество единиц товара, а затем выведите общую стоимость.
# # ”””
# price = int(input('Введите цену товара в сомах: '))
# quantity = int(input('Введите количество единиц товара: '))
# print('Общая стоимость товара состовляет:', price * quantity, 'сом')

# ““”
# 7) Количество дней в годах: Введите возраст пользователя и выведите, сколько дней он прожил (учитывая невисокосные года).
# # ”””
age = int(input('Сколько вам лет? '))
today = int(input('Введите сегодняшнее число в формате DD.MM.YYYY : '))

day = int(input('Введите нынешний день (DD): '))
month = int(input('Введите нынешний месяц (MM): '))
year = int(input('Введите нынешний год (YYYY): '))

day_of_birthday = int(input('Введите день (DD) рождения: '))
month_of_birthday = int(input('Введите месяц (MM) рождения: '))
year_of_birthday = int(input('Введите год (YYYY) рождения: '))

raznitsa_d = day - day_of_birthday
raznitsa_m = (month - month_of_birthday) * 30 # неусовершенствовано
# 31 день в 6 месяцах, 30 дней в 5 месяцах и 28 дней в 1 месяце 

raznitsa_y = year - year_of_birthday
if  raznitsa_y >= 5: # каждый пятый год добавляется 1 день, то есть 20 лет -> 21/4 --> 5 дней
    dy = raznitsa_y * 365 + raznitsa_y // 4
else:
    raznitsa_y == 1825

overall = raznitsa_d + dy + raznitsa_m
print('Вы прожили', overall  , 'дней')
    
# “””
# 8) Попросите пользователя ввести количество дней, а затем выведите, сколько это недель и сколько дней осталось.

# day = int(input('Введите количество дней: '))
# x = 7
# print('Это приблизительно', day // x, 'недель', 'если быть точнее, то', round(day / x, 2), 'недель')

# “””
# 9) Extra. Создайте игру "Камень-ножницы-бумага" с компьютером. Пользователь вводит свой выбор, а программа генерирует случайный выбор компьютера.

# from random import randint
# vybor = int(input('Давай поиграем в игру "Камень-ножницы-бумага"! Выбери камень(1), ножницы (2), бумага (3): '))
# comp = randint(1,3)

# # Условия игры: 3>1, 2>3, 1>2, 1<3, 2<1, 3<2

# while comp == 1:
#     if vybor == 3:
#         comp <= vybor
#         print('You won!')
        
#     elif vybor == 2:
#         comp >= vybor
#         print('You lose!')
#     else: 
#         print("Ничья")
#     break

# while comp == 2:
#     if vybor == 3:
#         comp >= vybor
#         print(comp)
#         print('You won!')
#     elif vybor == 1:
#         comp <= vybor
#         print('You lose!')
#     else: 
#         print("Ничья")
#     break

# while comp == 3:
#     if vybor == 2:
#         comp <= vybor
#         print(comp)
#         print('You won!')
#     elif vybor == 1:
#         comp >= vybor
#         print('You lose!')
#     else: 
#         print("Ничья")
#     break

