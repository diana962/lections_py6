# Циклы - это конструкция, которая заставляет какой-то блок кода выполняться несколько раз.

# while <expression>:
#     <body>

# i = 0
# while i < 10:
#     i += 1
#     print(i)

# while smth := input('Vvedite chto to: '):
#     print(smth)


# while (smth := input('Vvedite chto to: ')) == 'ok':
#     print(smth)

# Все, что пустое или '0' дает нам False.
# := --> это моржовый оператор
# control + C --> останавливает код
# \ --> перенос кода
# Чтобы вытащить значение ключа или его значения из библиотеки, необходимо просто ввести: dict['name_key']
    
# i = 1
# while ((name1 := input('Enter a name: ')) != 'john') or \
#     ((name2 := input('Enter a name: ')) != 'raychel'):
#     print()

#     if i >= 5:
#         print('Cycle terminated.')
#         break # принудительная остановка
#     i +=1
# else:
#     print(f'You gugessed {name1}, {name2} right!')


# user = {'username': 'JohnnSnow', 'password': 'bastard123'}

# i = 3
# while password := input(f'{user["username"]} vvedite parol\': ') != user['password']:
#     i -= 1
#     if i == 0:
#         print('You\'re blocked.')
#         break
# else:
#     print(f'Welcome to our system, {user["username"]}!')

# ------------------------------------------------------------------------------------------

# for <variable> in <iterable object>:
#     <boby>

# ls = ['a', 'hello', 55, 66, 77, True]
# i = iter(ls)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# from random import randint 

# dict_ = {}
# for x in range(1, 21):
#     dict_.update({x: randint(1, 50)}) # Очень полезная штучка

# print(dict_)

# ls = ['Tirion', 'Bilal', 'Sansa', 'John', 'Jamie']

# for x in ls:
#     if x == 'Bilal':
#         continue
#     print(f'Hello Mr/Mrs {x}!')



# for x in ls:
#     if x.startswith('J'): # or x.endswith('e')
#         continue 
#     print(f'Hello Mr/Mrs {x}!')

