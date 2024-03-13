# Задание 1.
# Есть список 
# list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
# ls = []
# chisla = []
# def argument(list_1):
#     # print("аргументы: ", list_1)
#     for i in list_1:
#         if i == str(i):
#             ls.append(i.capitalize())
#             ls.sort()
#         else:
#             chisla.append(i)
#             chisla.sort(reverse = True)
#     return ls, chisla
# print(argument(list_1))


# def slojenie(chisla):
#     ls2 = []
#     float_sum = 0
#     for i in chisla:
#         if isinstance(i, float):
#             float_sum += i   
#     return float_sum
# print(slojenie(chisla))

# Задание 2.
# Сэндвичи: напишите функцию, которая получает первым аргументом размер сэндвича в виде строкового значения и список компонентов сэндвича.
# При вызове функции, функция должна выводить описание заказанного сэндвича например «Большой сэндвич со следующими ингредиентами: огурец, колбаса … » . Вызовите функцию три раза с разными количествами аргументов и разными размерами (Большой, средний, маленький)

# def sandwich(size, component):
#     print (size, 'has' ,component)
# sandwich(input('Enter size: '), input('Enter component: '))

# Задание 3.
# Напишите функцию для сохранения информации об автомобиле в словаре . Функция всегда должна возвращать производителя и название модели, но при этом она может получать произвольное количество именованных аргументов . Вызовите функцию с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет и комплектация) . 

# car = make_car(‘subaru’, ‘outback’, colour=’blue’, engine='V8') и возвращать строку" 
# Subaru Outback colour is blue, engine is V8


# def make_car(maker, model, **components):
#     car = {'maker': maker, 'model': model}
#     car.update(components)
#     return f"{car['maker']} {car['model']} colour is {car.get('colour', 'unknown')} engine is {car.get('engine', 'unknown')}"
# print(make_car('subaru', 'outback', colour = 'blue', engine = 'V8'))

# print(f"{name}, {model}, 'colour is', {colour}, 'engine is', {engine}")
# auto('tesla', tesla = 'Model X')

# Задача 4

# Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое в нём количество цифр и букв. Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.

# Реализовать в цикле while, для выхода пользователь должен ввести "выход"

# Пример:

# Введите текст: 100 лет в обед

# Какую цифру ищем? 0

# Какую букву ищем? л

# Количество цифр 0: 2

# Количество букв л: 1

# def count_letters(user = input('Enter "q", if you want to quit or entter smth to continue: ')): 
#     while True:
#         if user == 'q':
#             break
#         else:
#             chisla = input('Какую цифру ищем?') 
#             bukva = input('Какую букву ищем?')
#             count_c = 0
#             count_b = 0
#             for i in user:
#                 if i == chisla:
#                     count_c += 1
#                 elif i == bukva:
#                     count_b +=1
#             print(f'Количество букв ', count_b, 'Количество цифр', count_c)

# print(count_letters())

# Задача 5.

# Напишите функцию, которая в виде аргумента принимает словарь (данные с именами и должностями , где ключ это имя работника,  а значение его должность. Функция должна вернуть предложения, типа:  
# Работник Асан, занимает должность Директор

# dict_ = {"Asan" : "director"}

# def data(dict):
#     for keys, values in dict.items():
#         # print('Работник', keys, 'занимает должность', values)
#         return(f'Работник {keys} занимает должность {values}')

# print(data(dict_))

# Задача 6 (дополнительно)

# Напишите программу, которая будет суммировать все числа, введенные пользователем, игнорируя при этом нечисловой ввод. Выводите на экран текущую сумму чисел после каждого очередного ввода. Ввод пользователем значения, не являющегося числовым, должен приводить к появлению соответствующего предупреждения, после чего пользователю должно быть предложено ввести следующее число. Выход из программы будет осуществляться путем пропуска ввода. Удостоверьтесь, что ваша программа корректно обрабатывает целочисленные значения и числа с плавающей запятой. 

# def summa():
#     count = 0
#     while True:
#         user = (input('Enter a num: '))
        
#         if user.isalpha():
#             print('Ошибка, введите только числа')
#         elif user == '':
#             break
#         else:
            
#             count += float(user)
            
#             print(count)

# print(summa())