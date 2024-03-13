# def sum_of_args(a, b, c: int = 5, d: int = 3): # параметры
#     return a + b + c + d

# result = sum_of_args(1, 2, 3, 4) # аргументы
# print(result)
# print(sum_of_args(0, 0))

# result = sum_of_args("1", "2", "c", "d") # аргументы - > Конкатенация происходит при строках
# print(result)

#--------------------------------------------------------------------------------------------------
# позиционные и именовые аргументы

# def printParams(a, b, c):
#     print(a, "is stored in param a")
#     print(b, "is stored in param b")
#     print(c, "is stored in param c")

# printParams(5, 10, 15)
# print()
# printParams(a = 5, b = 10, c = 15)

# def sum_of_args(a, b, c, d):
#         return a + b + c + d
# print(sum_of_args(5, 10, 15, 20)) # arguments/ позиционные аргументы
# print(sum_of_args(a = 5, c = 20, b = 10, d = 15)) #keyword and keybord arguments (именованные арргументы)
# print(sum_of_args(5, 10, d = 20, c = 15))

# -----------------------------------------------------------------------------------------------------
#  оператор *
# a = [1, [2, 3]]
# b = [4, 5, 6]
# c = [*a, *b]
# print(c)
# print([*a, *a])
# -----------------------------------------------------------------------------------------------------
# *args, **kwargs
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)

# func(1, 2, 3, 4, 5, a = 1, b =2, c= 3)


# def printScores(student, *scores): #*args = *scores
#     print(f'Name of sudent: {student}')
#     # print(scores)
#     print(f' AVG: {sum(scores) / len(scores)}')
#     # for x in scores:
#     #     print(f'Scores: {x}')

# printScores('John Snow', 100, 90, 80, 95, 94)

# def printPetNames(owner, **pets): #{"key": "value"}
#     print(f'Owner name: {owner}')
#     # print(pets)
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}', *name)
#         else:
#             print(f'{pet}: {name}')

# printPetNames('John Snow', dog = 'Pluto', cat = 'Garfild', fish = ["Nemo", "Dori", "Simba"], turtle = "Leonardo")


# def get_some_data(a, b, *args, **kwargs):
#     print('параметры a и b:', a, b)
#     print("аргументы: ", args)
#     print('именованные аргументы: ', kwargs)

# get_some_data(1, 2, 3, 4, 5, lang = "Python", car = "subaru")

# -----------------------------------------------------------------------------------------------------
# import string as s
# from random import choice, shuffle

# def generate_random_str(len_):
#     # print(s.ascii_letters, s.digits, s.punctuation)
#     symbols = s.ascii_letters + s.digits
#     res = [choice(symbols) for _ in range(1, len_)] + [choice(s.punctuation)]
#     shuffle(res)
#     print("".join(res))
#     return "".join(res) #-> в принте не выдает None

# generate_random_str(15)
# generate_random_str(20)
# generate_random_str(5)

