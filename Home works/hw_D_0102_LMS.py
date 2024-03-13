# 1) Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра.
# def kol(text = input('Enter a text: ')):
#     try: 
#         count = 0
#         count1 = 0
#         for i in text:
#             if i.isupper():
#                 count +=1
#             elif i.islower():
#                 count1 +=1
#     except:
#         print('Enter a number!')
#     print(f'Колличество больших букв: {count}, Колличество строчных: {count1}')
# print(kol())

# 2) Напишите функцию, которая принимает число n и генерирует словарь, чьи ключи состоят из чисел от 1 до n, а их значения -- куб ключей. Пример: передано число 5. В результате должны получить словарь {1: 1, 2: 8, 3: 27, 4: 64}
# def k():
#     while True:
#         n = int(input('Enter a number: '))
#         dict_ = {}
#         for n in range(1, n+1):
#             n **3
#             # print(n**3)
#             dict_.setdefault(n, n**3)
#         print(dict_)

# print(k())

# 3) Напишите функцию sum_range(start, end), которая суммирует все целые числа
#     от значения «start» до величины «end» включительно. Если пользователь задаст
#     первое число большее чем второе, просто поменяйте их местами.

# def sum_range(start = int(input('Enter number: ')), end = int(input('Enter number: '))): # 3 return 6):
#     sum = 0
#     if start > end:
#         all = list(range(end, start + 1))
#         sorted(all)
#         for i in all:
#             sum += i 
#         return(sum)
#     else: 
#         all = list(range(start, end + 1))
#         for i in all:
#             sum += i 
#         return(sum)


# print(sum_range())