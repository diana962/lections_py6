# """
# 1) Дан список 
# list_ = [1, 2, 3, 4] #Выведите сумму всех этих чисел.
# # """
# print(sum(list_))
# """
# 2) Дан списка из чисел. Проверьте, что все числа больше трёх.
# # """
# list_ = [2, 6, 5, 4]
# res = list(map(lambda i: i>3, list_))
# print(res)

# """
# 3) Даны список из чисел. Проверьте, что в нём есть отрицательные числа.
# """
# ls = [-3, 6, 7, 9]
# res = any(x for x in ls if x < 0)
# print(res)

# """
# 4) Дан список, состоящий из числами. Создайте новый список, состоящий из квадратов этих чисел.
# """
# ls = [-3, 6, 7, 9]
# print([x**2 for x in ls ])
# """
# 5) Дан список с числами. Отфильтруйте этот список, оставив только чётные числа.
# """
# ls = [-3, 6, 7, 9]
# res = list(filter(lambda x: x%2 == 0, ls))
# print(res)
# """
# 6) Дан список, со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов.
# """
# ls = ['one', 'two', 'thirteen']
# res = list(filter(lambda x: len(x) > 7, ls))
# print(res)

# """
# 7) Дан список list_ = [5, 6, 7, 8]. Выведите произведение всех этих чисел.
# """
# from functools import reduce
# list_ = [5, 6, 7, 8]
# res = reduce(lambda a, b: a * b, list_)
# print(res)
# """
# 8. Дан список, с числами. Посчитате количество чётных и нечётных чисел в этом списке.
# """
# ls = [-3, 6, 7, 9]
# res = len([i for i in ls if i%2 == 0])
# res1 = len([i for i in ls if i%2 != 0])
# print(res, res1)
# """
# 9) Дан список list_ = [-1, 2, 3, 0, 5, -3, 7,]. Если число в списке меньше 0, замените его на False, если больше, то на True .
# """
# list_ = [-1, 2, 3, 0, 5, 3, 7]
# res = list(map(lambda i: i >= 0, list_))
# print(res)

# """
# 10) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
# """
# from functools import reduce

# name = ['Aidar', 'Samat', 'Bai', 'Bek']
# res = reduce(lambda x, y: x if len(x) > len(y) else y, name)
# print(res)

