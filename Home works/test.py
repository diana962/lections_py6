# import random

# ls = {'Watch Toples on YouTube': 0, 'Read books': 0, 'Scroll Instagram': 0}
# rounds = 1000000 #or 1_000_000
# i = 1

# while i <rounds:
#     chislo = random.randint(1, 3) #1, 2, 3
#     if chislo == 1:
#         ls ['Watch Toples on YouTube'] +=1
#     elif chislo ==2:
#         ls['Read books'] +=1
#     else:
#         ls ['Scroll Instagram'] +=1
#     print(i)
#     i = i +1

# print (ls)


# def min1(sequence):
#     start_for_min = sequence[0]
#     for i in sequence[1:]:
#         if start_for_min < i:
#             start_for_min == i
#             return start_for_min
        
# print(min1([1, 2, 7, 9]))

# def min1(sequence):
#     return sorted(sequence)[0]
# print(min1([2, 2, 7]))

# def is_polindrom(word = 'Hello'): # zdec 'hello' chisto po default, a tak po suti zdec pusto
#     return word == word[::-1]

# print(is_polindrom('Level'.upper())) # True: polindrom
# print(is_polindrom()) # False: not polindrom

# new = lambda word = 'hello': word == word[::-1]
# print(new('level'))


# def show_words(func, words):
#     for i in words:
#         print(func(i))

# show_words(len, ['rain', 'snow'])
# show_words(lambda word: word.upper(), ['rain', 'snow'])

# number = list(range(1, 16))
# print(number)

# #функция filter
# filtered = list(filter(lambda num: num>9, number)) #filter expects 2 arguments
# print(filtered)

# #функция map
# mapped = tuple(map(lambda num: num - 3, number)) # Функция lambda применяется списке number: что -> kak-> где
# print(mapped)

# # отличие filter and map в том, что map производит что либо с каждым элементом.

# lambda arbeitet auch mit list comprehension
# pifagor = lambda num: [i * num for i in range(1, 11)] # lambda передает в сыром ввиде, а чтобы этого избежать ее превращаем в переменную.
# print(pifagor(int(input('enter num (for me: its type is str): '))))

# Работа с файлами
# file.txt-> название.формат,'w' - write, encoding for those whos computer refuses to work
# file = open('file.txt', 'w', encoding='utf-8')
# file.write('Bish, KGZ')
# file.close()

# 'w' - write
# 'a' - add
# 'x' - проверка на название файла. Не создаст файл, если такое имя существует,то создаст. Обеспечение сохранности данных от утери.
# 'r' - rea

# with open('file.txt', 'x') as file: # new way to create a file or change smth in file
#     file.write('\nвторая строка')

# with open('file.txt', 'r') as file: # new way to create a file or change smth in file
#     for i in file.read():
#         print(i, end='')
    # print(file.readlines())
    # print(file.read())