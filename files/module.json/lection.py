# JSON - Java Script Object Notation
# единый текстовый формат, был сооздан для хранения и передачи данных между сервисами, проектами
# <filename>.json #файл в формате JSON

# js object == {key: value}
# JSON =={key: value}
# PY Dict == {key: value}

# Процессы Сериализации и Десериализации данных(конвертация)

# Сериализация (запись данных в JSON) - Это перевод из Python в JSON формат
# dump - записывает данные в файл формата JSON
# dumps (s from str) - записывает данные в ТЕКСТ формата JSON

# Десериализация(чтение даныых из JSON) - это процесс перевода из JSON в PY dict

# load - функция, которая считывавет данные из файла JSON
# loads - функция, которая считывавет данные из ТЕКСТА JSON

# ---------------------------------------------------------------------------------------
# Процесс сериализации
# import json
# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status' : True,
#     'wife': False,
#     'children': None
# }
# print(dict_, type(dict_))

# json_text = json.dumps(dict_)
# print()
# print(json_text, type(json_text))


# import json
# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status' : True,
#     'wife': False,
#     'children': None
# }
# print(dict_, type(dict_))

# with open('new.json', 'w') as file: #--> крутая вещь
#     json.dump(dict_, file, indent =4)

# -------------------------------------------------------------------------------
# Процесс десериализации

# import json
# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data, type(json_data))
# dict_ = json.loads(json_data)
# print()
# print(dict_, type(dict_))

# ---------------------------------
# import json
# with open('new.json', 'r') as file:
#     dict_ = json.load(file)
#     print(dict_, type(dict_))

