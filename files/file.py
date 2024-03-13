# Работа с файлами
# Каретка - укзатель - курсор
# open("путь до файла")
# file = open("files.py") # относительный путь
# ~ working ->Desktop/PY6_/files/lectures

# path = '/Users/diana/Desktop/PY6_/files' # аболютный путь
# file = open(path, 'r')
# data = file.read()
# print(data, type(data))
# file.close()

# Режимы работы с файлами
# 1) r/r+/rb -> read = для чтения файлов
# 2) w/w+/wb -> write - для записи данных
# 3) a/a+ -> для добавления данных
# b, x

# file = open("files/test.txt", 'r')
# print(file.read())
# file.close()

# file = open("files/test.txt", 'r')
# print(file.readlines())
# file.close()


# --------------------------------------------------------------------------------
# контекстный менеджер
# with open('files/test.txt', 'r') as file:
#     print(file.readline())
#     print(file.readline())
#     print('!!!')
#     print(file.read())


# file.tell() - Возвращает ииндекс, где находится каретка(указатель)
# file.seek() - Возвращает курсор на индекс, который вы передали

# with open('files/test.txt', 'r') as file:
#     print(file.tell()) #0
#     data = file.read(20)
#     print(data, '!!')
#     print(file.tell())
#     file.seek(0)
#     data = file.read()
#     print(data, '!!')

# with open('files//text.txt', 'w') as file:
#     file.write('Hello, Diana\n')
#     file.write('Welcome home, my dear!\n')
#     file.write('Take off your clothes\n')
#     # file.seek(0)
#     data = ['Test 1 stroka\n', 'Test 2 stroka\n']
#     file.writelines(data)

# with open('files/text.txt', 'a+') as f:
#     f.write('\nJohn Snow is a King of North\n')
#     f.write('\nYou know nothing\n')
#     f.seek(0)
#     f.read()# если в a+ то он работает, с просто а не работает
#     print(f.read())

# --------------------------------------------------------------------
# from PIL import Image
# import pytesseract
# import re

# base_url = '/Users/diana/Desktop/PY6_/files/'
# def get_imei_codes(image_path: str):
#     string = pytesseract.image_to_string(image_path)
#     # print(string)
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)

# image_path = base_url + 'imei.jpg'
# get_imei_codes(image_path)

