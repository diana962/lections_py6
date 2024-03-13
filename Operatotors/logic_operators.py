# Операторы сравнения
# Услоовные операторы
# Логические операторы


# операторы сравнения
#  <, >, ==(равно), != (не равно), <=, >=
# 1 > 7 --> False
# 7 < 9 --> True

# print('ABC1234124' > 'abc123') # Он сравнивает по ASCll

# 1 2 4 8 16 32 64 128 256 512 1024 2048
# 0  0  1 1  0   1 # справа на лево
# 44 --> 101100
# 15 --> 1111
# 20 --> 10100

# a = 'A'
# b = 'b'
# print(ord(a), ord(b)) # функция
# num = 65
# print(chr(num)) # обратная функция

# Условные оператторы
# if
# elif
# else

# if <condition>:
#     <body if> # сработает, если в conditon if придет True
# [elif] <confition>: # а если:
#     <body elif>
# [else]:
#     <body else> # сработает, если во всех стоящих условиях пришло False

# string = input('Enter smth: ').lower()

# if string == 'hello':
#     print('Hello, It\'s me, I was wonderung if after all these you\'d like like to meet!')
# elif string == 'John Snow':
#     print('Welcome back, John Snow! The king of North!')
# elif string == 'abra-kadabra':
#     print('Sim salamon kadabra!')
# else:
#     print('No match found.')

# print('Registration Form: ')
# email = input('Enter ypur mail: ')
##if '@' not in email:
##     raise ValueError('Email is invalid!')
# password = input('Enter the password: ')
# if len(password) < 8:
#     raise ValueError('Too short! At least 8 symbols!')
# elif password.isdigit():
#     raise ValueError('Invalid Password! Only digits!')
# elif password.isalpha():
#     raise ValueError('Invalid Password! Only alphabet!')

# password2 = input('Enter the password confirmation: ')

# if password != password2:
#     raise ValueError("Passwords did\'t match!")

# print(f'Sucessfully registered! Hello Mr/Mrs {email}@gmail.com!') #-> с @gmail.com

# index = email.find('@') #  или email.index('@')
# print(f'Sucessfully registered! Hello Mr/Mrs {email[:index]}!')#-> без @gmail.com
'''
Узнала индекс последней буквы,введенной пользоваелем:
last_value = email[-1]
index = email.find(last_value)
print(last_value)
print(index)
'''

# age = input('Enter your age: ')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid value for age!')

# if age < 18:
#     print(f'Access denied! come again after {18-age} year')
# else:
#     print('You\'re welcome!')

# Логические операторы
# and 
# or
# not

# money = 1000000
# status = 'base'

# if money > 1000000 and status == 'premium':
#     print('You\'re president of our club!')
# elif money > 1000000 or status == 'premium':
#     print('You\'re minister of our club!')
# else:
#     print('You\'re honorable member of our club!')