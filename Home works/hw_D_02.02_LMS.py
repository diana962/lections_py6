# 1) Часы и минуты в секунды: Напишите функцию, которая принимает целочисленные значения часов и минут, конвертирует эти значения в секунды, а затем суммирует их и возвращает в качестве результата.
# def time_(hour = int(input('Enter amount of hours: ')), min = int(input('Enter amount of minutes: '))):
#     return (f' Amount of {(hour * 60 + min) * 60} seconds')

# print(time_())

# 2) Возраст в дни: Напишите функцию, которая принимает возраст (количество лет) и преобразует это значение в количество дней.
# def days(age = int(input('Сколько вам лет: '))):
#     return age * 365
# print(days())

# age = int(input('Сколько вам лет? '))
# today = int(input('Введите сегодняшнее число в формате DD.MM.YYYY : '))

# day = int(input('Введите нынешний день (DD): '))
# month = int(input('Введите нынешний месяц (MM): '))
# year = int(input('Введите нынешний год (YYYY): '))

# day_of_birthday = int(input('Введите день (DD) рождения: '))
# month_of_birthday = int(input('Введите месяц (MM) рождения: '))
# year_of_birthday = int(input('Введите год (YYYY) рождения: '))

# raznitsa_d = day - day_of_birthday
# raznitsa_m = (month - month_of_birthday) * 30 # неусовершенствовано
# # 31 день в 6 месяцах, 30 дней в 5 месяцах и 28 дней в 1 месяце 

# raznitsa_y = year - year_of_birthday
# if  raznitsa_y >= 5: # каждый пятый год добавляется 1 день, то есть 20 лет -> 21/4 --> 5 дней
#     dy = raznitsa_y * 365 + raznitsa_y // 4
# else:
#     raznitsa_y == 1825

# overall = raznitsa_d + dy + raznitsa_m
# print('Вы прожили', overall  , 'дней')


# 3) Сколько ног на ферме: Для решения этой задачи необходимо написать функцию, которая посчитает количество ног у всех животных на ферме. На ферме живут курочки, коровки, и свинки. Зная количество животных каждого вида, посчитайте, сколько всего ног у всех животных на ферме.

# def legs_farm():
#     chicken = int(input('Введите количество куриц: '))
#     cow = int(input('Введите количество коров: '))
#     pepa = int(input('Введите количество свиней: '))
#     chicken_leg = 2
#     cow_leg = 4
#     pepa_leg = 4
#     sum_legs = 0
#     sum_legs = (chicken * chicken_leg)+(cow * cow_leg)+(pepa * pepa_leg)
#     return print(sum_legs)
# legs_farm()