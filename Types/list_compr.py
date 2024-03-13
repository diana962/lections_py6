# list comprehensions - генераторы списков
# list comprehensions - упрощенный подход к созданию списков, которая задействует всегда цикл for, а также конструкцию if для определения того, что в итоге попадает в наш список.

# list -> 0 - 200 -> четные

# ls = list(range(0, 201, 2)) #-- то что я не использую
# print(ls)

# ls = []
# for i in range(0, 201):
#     if i % 2 == 0:
#         ls.append(i)
# print(ls)

# ls = [x for x in range(0, 201, 2 )]
# ls = [x for x in range(0, 201) if x % 2 == 0] #--> ввести в обыденность

# print(ls)
# ls = [x for x in range(0, 301) if x % 2 == 0 and x % 3 == 0] #--> ввести в обыденность
# print(ls)

# print([x for x in range(0, 301) if x % 2 == 0 and x % 3 == 0])


# ls = [x ** 2 for x in range(0, 101) if x % 2 == 0 and x ** 3 for x in range(0, 101) if x % 3 == 0]
# print(ls)

# ls = []
# for i in range(0, 101):
#     if i % 2 == 0:
#         ls.append(i ** 2)
#     elif i % 3 == 0:
#         ls.append(i ** 3)
# print(ls)

# ls = [x ** 2 if x % 2 == 0 else x ** 3 #-> очень непривычная запись
#     for x in range(0, 101)
#     if x % 2 == 0 or x % 3 == 0
# ]
# print(ls)

# -------------------------------------------------------------------------------------------------------
# newlist = [expression for item in iterable <if condition == True>]
# print([str(i * 2) for i in range(0, 11)])

# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# ls.extend(ls[0])
# ls.extend(ls[1])
# ls.extend(ls[2])
# ls.remove(ls[0])
# ls.remove(ls[0])
# ls.remove(ls[0])
# print(ls)

# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = []
# for x in ls:
#     for num in x:
#         res.append(num)
# print(res)

# res = [num for x in ls for num in x]
# print(res)

# -----------------------------------------------
# from datetime import datetime

# start = datetime.now() #11.41.35
# # print(start)
# ls = []
# for x in range(0, 100_000_000):
#     ls.append(x)
# finish = datetime.now() # 11.41.46

# print(finish - start)

# start = datetime.now() #11.41.35
# ls = [x for x in range(0, 100_000_000)] #--> в 4 раза быстрее работает
# finish = datetime.now() # 11.41.46

# print(finish - start)
