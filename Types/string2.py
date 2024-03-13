# text = 'The more you learn, the more you earn.'
# len() - возвращает длину строки, считая каждый ее символ.
# len_text = len(text) #38
# print(text, len_text)
# print(text[::-1])

# text = 'The more you learn, the more you earn.'
# count_e = 0
# i = 0
# while i < len(text):
#     symbol = text[i]
#     if symbol == 'e' or symbol == 'E':
#         count_e +=1
#     i += 1 # инкремент i = i + 1

# print(f'Symbol E is found: {count_e} times!')

# 1) Custom len codeZ
# text = 'The more you learn, the more you earn.'
# i = 0
# while text[i:]:
#     i +=1
#     print(i)

# 2) Custom len code
# text = 'The more you learn, the more you earn.'
# count_e = 0
# i = 0
# c = 0
# while text[i:]:
#     i +=1
#     c +=1
#     print(c)

# --------------------------------------------------------------------------------
# Методы строк - dir()

# print(dir('a'))

# text = ''''capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill' '''
# print(text.count(''))


# count(value, index) - считает кол-во вхождений value в нашу строку
# text = 'hello ooooooo'
# print(text.count('o'))
# print(text.count('h', 5))
# print(text.count('hello'))

# replace(old, new, [count]) - меняет в строке pld символ на new, заменит count раз, если передает число.
# text = 'ha ha ha ha'
# res = text.replace('a', 'e', 2)
# print(text)
# print(f'Result after replace: {res}')


# strip() - Убирает пробельные символы в начале и в конце строки
# rstrip - right side, lstrip - left side

# a = '   Hello   '
# print(a, len(a), sep='->')
# res = a.strip()
# print(res, len(res), sep='->')
# print(a.lstrip(), '1')


# isalpha - состоит ли наша строка из символов алфавита
# txt = 'Hello world'
# print(txt.isalpha()) # из за наличия пробела выводит False

# res = txt.replace(' ', '') # длинный код
# res = (res, res.isalpha())
# print(res, res.isalpha())

# print(('Hello world'.replace(' ','')).isalpha()) # кратко


# isdigit - проверяет
# isnumeric - состоит ли наша строка  из чисел
# isdecimal - полностью из чисел

# num = input('Write number: ')
# print(f'Is it a number?: {num.isdigit()}')


# num = input('vvedote chislo: ')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} * 5 = {num * 5}')
# else:
#     print('Vy vveli ne chislo!: ')

# split(separator) - дробит (разделяет) строку на несколько частей по разделителю, все части сохраняются в типе лист.

# text = 'Let me speak in English! '
# res = text.split('e')
# print(text)
# print(res)
# print(text.split())

# a = '#hello#life#love#work#bischkek'
# print(a)
# print(a[1:].split('#')) #Можно вставлять радиус диапозона через [:].split('')

# 'connector'.join(list) -  соедииняяет no connector строки, котоорые были в list
# ls = ['Anvar', 'John', 'Jamie', 'Osmon']
# print(ls)
# res = '-'.join(ls) # 'определяет по какому знаку соединять' 
# print(res)

# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр


# text = ' Helo world, John snow'
# print(f'Original: {text}')
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

# index(value) - выводит индекс значения value внутри строки

# text = 'Hello John snow'
# print(text.index('o'))
# print(text.index('John'))
# print(text.index('o', 5))
# print(text.index('a')) # Выводит ошибку, когда не находит

# find(value) - делает то же самое, что и index, но если не нашел value, то вернется -1.
# text = 'Hello John snow'
# print(text.index('o'))
# print(text.index('John'))
# print(text.index('o', 5))
# print(text.find('a')) # Выводит -1, когда не находит