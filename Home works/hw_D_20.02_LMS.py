"""
1. Создайте класс BankAccount, в конструкторе которого определена переменная
экземпляра класса balance = 0. Определите метод withdraw с параметром amount,
который будет отнимать сумму от баланса и возвращать текущий баланс. Также
добавьте метод deposit, который также имеет параметр amount и соответсвенно
добавляет сумму к балансу, возвращает баланс.
"""
# class BankAccount:
#     balance = 0
#     def __init__(self, balance = 0):
        # self.balance = balance
#     def withdraw(self, amount):
#         self.balance -= amount
#     def deposit(self, amount):
#         self.balance += amount

# money = BankAccount(2000)
# print(money.balance)

# money.withdraw(50)
# print(money.balance)
# money.deposit(550)
# print(money.balance)

"""
2. Вам дан такой код:

winner1 = Nobel("Литература", 1971, "Пабло Неруда")
print(winner1.category, winner1.year, winner1.winner)
print(winner1.get_year())

winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
print(winner2.category, winner2.year, winner2.winner)
print(winner2.get_year())

который выводит в терминал такие значения:

Литература 1971 Пабло Неруда
выиграл 50 лет назад

Литература 1994 Кэндзабуро Оэ
выиграл 27 лет назад

Напишите класс Nobel и метод класса get_year() таким образом, чтобы данный вам код вывел указанные значения в терминале. Даты внутри класса не хардкодить.
"""
# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#     def get_year(self):
#         return (f'выиграл {2024 -int(self.year)} лет назад')
#     def __str__(self):
#         return(f'{self.category} {self.year} {self.winner}')


# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())

"""
3. Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:
- пароль должен быть минимум 8 символов, но меньше 15
- пароль должен содержать цифры
- пароль должен содержать буквы
- пароль должен содержать хотя бы один из символов:
    '@', '#', '&', '$', '%', '!', '~', '*'

если одно из условий не выполнено, выводите кастомное исключение, 
если же все условия выполнены метод validate должен возвращать строку: 'Ваш пароль сохранен'.

Также переопределите метод str, чтобы при попытке распечатать
сам пароль, вам выдавалась строка из звездочек,
к примеру пароль - 'joe@123456'
в терминале выйдет - ******
"""
# class Password:
#     def __init__(self, password):
#         self.password = password
#     def validate(self):
#         if len(self.password) < 8:
#             raise ValueError('Password cannot be longer than 8 symbols.')
#         elif not any(char.isupper() for char in self.password):
#             raise ValueError('Password must have at least one capital letter.')
#         elif not any(char.islower() for char in self.password):
#             raise ValueError('Password must have at least one строчную letter.')
#         elif not any(char.isdigit() for char in self.password):
#             raise ValueError('Password must have at least one digit.')
#         elif not any(char in '!@#$%^&*()_-+=<>?/' for char in self.password):
#             raise ValueError('Password must have at least one специальный символ из множества: !@#$%^&*()_-+=<>?/')
#         else:
#             return('Good password!')

# password = Password('12345Qwe!')
# print(password.validate())
"""
4. Создайте класс Math, экземпляром которого должно быть число.
У классa Math должно быть 3 метода:
- get_factorial - выводит факториал числа
- get_sum - выводит сумму цифр числа
- get_mul_table - выводит таблицу умножения для числа до 10. 
Создайте экземпляр класса и примените к нему все методы. 
"""
# class Math:
#     def __init__(self, number):
#         self.num = number
#     def _str__(self):
#         return str(self.num)
#     def get_factorial(self):
#         factorial = 1
#         for i in range(1, self.num + 1):
#             factorial *= i
#         return factorial
#     def get_tab(self):
#         i = int(self.num)
#         for i in range(0, 11):
#             print(f'{self.num} x {i} = {self.num * i}')
#     def get_sum(self):
#         num_str = str(self.num)
#         return sum(int(digit) for digit in num_str)
    
# num = Math(6)
# print("Factorial:", num.get_factorial())
# print("Sum of digits:", num.get_sum())
# print(num.get_tab())

"""
5. Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д)

У класса есть метод give_priority который записывает вашу задачу в список(переменная класса) с ключом в виде числа, 
приоритет который вы даете вашей задаче -
к примеру {3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

У класса должен быть метод list_of_tasks, который выдает вам список отсортированных задач 
по приоритету:
[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]

"""

# class ToDo:
#     def __init__(self, str_todos = {}):
#         self.str_todos = str_todos
#     def __str__(self):
#         return (self.str_todos)
#     def give_priority(self, task, number):
#         self.str_todos[number] = task
#     def list_of_tasks(self):
#         res = sorted(self.str_todos.items())
#         return(res)

# todos = ToDo()
# print(todos.give_priority('сходить в кино', 3))
# print(todos.give_priority('сделать домашку', 1))
# print(todos.give_priority('выгулять собаку', 2))
# print(todos.list_of_tasks())