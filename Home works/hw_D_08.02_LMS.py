# 1) Умножение соответствующих элементов двух списков: Используйте map и lambda, чтобы умножить соответствующие элементы двух списков.

# ls = [1, 2, 4]
# ls1 = [2, 6, 8]
# # Ouput: res = [2, 12, 32]
# res = list(map(lambda x, y: x * y, ls, ls1))
# print(res)

# 2) Проверка, что в строке есть хотя бы одна гласная буква: Используйте any и lambda, чтобы проверить, что в строке есть хотя бы одна гласная буква.

# str = 'Di911'
# glasnye = 'aeiouy'
# if any(lambda x: x in str for x in glasnye):
#     print('Here is glasnye here')
# else:
#     print('No glasnye')

# 3) Фильтрация слов с определенной длиной: Используйте filter и lambda для фильтрации слов в списке строк, имеющих заданную длину.

# ls = ['hallo', 'how are you?', 'Sam', 'Essen']
# res = list(filter(lambda x: len(x)> 5, ls))
# print(res)

# 4) Проверка, что все элементы списка больше нуля: Используйте all и map, чтобы проверить, что все элементы в списке больше нуля.

# ls = [0, 1, 3, -6]
# res = all(map(lambda x: x > 0, ls))
# print(res)

# 5) Сумма квадратов четных чисел: Напишите программу, которая с использованием map и reduce находит сумму квадратов четных чисел в списке.

# from functools import reduce

# ls = [4, 1, 3, -6]
# # print(list(map(lambda x: x%2==0, ls)))
# res = reduce(lambda a, b: a + b, list(map(lambda x: x**2 if x%2 ==0 else x, ls))); print(res)