# # # 1 задача:
# # # Напишите программу, которая симулирует игру лото с одной картой. Начните с генерирования списка их всех возможных номеров выпадения (от В1 до О 75). После этого перемешайте номера в хаотичном порядке, воспользовавщись функцией shuffle из модуля random. Вытаскивайте по одному номеру из списка и зачеркивайте номера, пока карточка не окажется выигравшей. Приведите 1000 симуляций и выведите на экран минимальное, максимальное и среднее количество извлечений номеров, требующееся для выигрыша.

# # dict_ = {
# #     'B': '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75',
# #     'I': '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75',
# #     'N': '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75',
# #     'G': '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75',
# #     'O': '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75',
# # }

# # from random import shuffle

# # paket = []
# # for x in dict_:
# #     for i in dict_.values():
# #         ls_i = i.split(', ')
# #         for y in ls_i:
# #             paket.append(x+y)
# #         break
# # shuffle(paket)
# # # print(paket)

# # # Создать билет 
# # jackpot_b = []
# # jackpot_i = []
# # jackpot_n = []
# # jackpot_g = []
# # jackpot_o = []
# # for i in paket:
# #     if i.startswith('B') :
# #         jackpot_b.append(i)  
# #     if i.startswith('I') :
# #         jackpot_i.append(i)  
# #     if i.startswith('N') :
# #         jackpot_n.append(i)  
# #     if i.startswith('G') :
# #         jackpot_g.append(i)  
# #     if i.startswith('O') :
# #         jackpot_o.append(i)  
# # # print(jackpot)

# # import random
# # five_b = random.sample(jackpot_b, 5)
# # five_i = random.sample(jackpot_i, 5)
# # five_n = random.sample(jackpot_n, 5)
# # five_g = random.sample(jackpot_g, 5)
# # five_o = random.sample(jackpot_o, 5)
# # ### print(' '.join(five_b))

# # ls = [five_i, five_b, five_g, five_o, five_n] #----> горизонтальная линия

# # for x in ls:
# #     print(x) #----> мой сгенерированный эстетичный билет
# # # print(ls) 

# # # v1 = [five_i[0], five_b[0], five_g[0], five_o[0], five_b[0]]
# # # print(v1)

# # v2 = []
# # for i in range(5):
# #     for x in ls:
# #         v2.append(x[i])
# #         # if i.index(x) == 0:
# #         #     v2.append(x)
# #         # if i.index(x) == 1:
# #         #     v2.append(x)
# #         # if i.index(x) == 2:
# #         #     v2.append(x)
# #         # if i.index(x) == 3:
# #         #     v2.append(x)
# #         # if i.index(x) == 4:
# #         #     v2.append(x)
# # # print(v2)
# # sublists = [v2[i:i+5] for i in range(0, len(v2), 5)] #---->  вертельная линия
# # # print(sublists) 



    

# # ls1 = [ls[0][0],ls[1][1], ls[2][2],ls[3][3],ls[4][4]] #----> первая диагональ
# # # print(ls1)
# # ls2 = [ls[0][-1],ls[1][-2],ls[2][-3],ls[3][-4],ls[4][-5]] #---->  вторая диагональ
# # # print(ls2)

# # winning_slot = five_i, five_b, five_g, five_o, five_n, ls1, ls2
# # # print(winning_slot)


# # num_simulations = 1000
# # count = []
# # while num_simulations > 0:
# #     count = 0
# #     for comb in winning_slot:
# #         if all(i in paket for i in comb):
# #             count += 1          
# #     num_simulations -= 1

# # print(count)



# from random import shuffle

# res = []
# for _ in range(1000):
#     bilet = [['b7',  'b54', 'b64', 'b12', 'b13'],
#              ['i5',  'i6',  'i8',  'i9',  'i10'],
#              ['n11', 'n12', 'n13', 'n14', 'n15'],
#              ['g16', 'g6',  'g29', 'g41', 'g54'],
#              ['o16', 'o17', 'o36', 'o41', 'o54']]

#     # мешок из которого достаем рандомный номер билета
#     meshok = [x + str(i) for i in range(1, 76) for x in 'bingo']
#     shuffle(meshok)

#     # количество извлечений номеров
#     draw = 0

#     # Создаем два списка с диагоналями
#     diagonals = [[], []]
#     i = 0
#     i2 = -1
#     for row in bilet:
#         diagonals[0].append(row[i])
#         diagonals[1].append(row[i2])
#         i += 1
#         i2 -= 1
#     print(diagonals)

#     flag = True
#     while flag:
#         number = meshok.pop()
#         draw += 1

#         # Проверка выигрыша по горизонтали
#         for row in bilet:
#             if number in row:
#                 row[row.index(number)] = 'X'
#                 if all(cell == 'X' for cell in row):
#                     flag = False

#         # Проверка по вертикали
#         for i in range(5):
#             column = [row[i] for row in bilet]
#             if all(cell == 'X' for cell in column):
#                 flag = False

#         # Проверка по диагонали
#         for diagonal in diagonals:
#             if number in diagonal:
#                 diagonal[diagonal.index(number)] = 'X'
#                 if all(cell == 'X' for cell in diagonal):
#                     flag = False
#     res.append(draw)
#     draw = 0

# print(f'Максимальное количество вытаскиваний номеров из мешка равно {max(res)}\nМинимальное количество вытаскиваний номеров из мешка равно {min(res)}')


# # # import random
# # # applicants = ['jjk', 'pop', 'icon']
# # # print (random.sample(applicants, 2)) #--> 2 указывает на колличество выбранных претендентов
 

# # # 2 задача:

# # #     Азбука Морзе зашифровывает буквы и цифры при помощи точек и тире.
# # #     В данном упражнении вам необходимо написать программу, в которой
# # #     соответствие символов из азбуки Морзе будет храниться в виде словаря.
# # #     В табл. 6.3 приведена та часть азбуки, которая вам понадобится при ре-
# # #     шении этого задания.
# # #     В основной программе вам необходимо запросить у пользователя стро-
# # #     ку. После этого программа должна преобразовать его в соответствующую
# # #     последовательность точек и тире, вставляя пробелы между отдельными120  Упражнения
# # #     символами. Символы, не представленные в таблице, можно игнорировать.
# # #     Например, сообщение Hello, World! может быть представлено следующей
# # #     последовательностью: .... . .–.. .–.. ––– .–– ––– .–. .–.. –..
# # #     Таблица 6.3. Азбука Морзе

# # # dict_ = {
# # #     'A': '.-', 
# # #     'B': '-...', 
# # #     'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
# # #     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
# # #     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
# # #     'Y': '-.--', 'Z': '--..',
# # #     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
# # #     '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
# # # }

# # # user = input('Enter a sentence: ').upper()
# # # ls = []
# # # for i in list(user):
# # #     print(i)
# # #     if i == ',' or i == '?':
# # #         continue
# # #     for k,v in dict_.items():
# # #         if i == k:
# # #             ls.append(v)
# # # print(' '.join(ls))