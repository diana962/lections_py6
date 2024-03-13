"""Функции задания"""

# 1
# Создать функцию, которая будет принимать 3 числа в качестве аргументов, функция должна возвращать сумму первых двух чисел разделеную на третье число
# нужно реализовать проверку на то, что третье число не является нулем, если это ноль, то просто возвратить результат сложения первого и второго числа
def calculate_and_divide(a = 1, b = 2, c = 0):return (a + b) / c if c != 0 else a + b
# 2
# Создать фуункцию, которая принимает в качестве аргумента список со строками и в каком регистре нужно вернуть данные, строки могут быть записаны в любом регистре, задача: на основе выбора регистра, возвращать либо список со строками в верхнем регистре, либо в нижнем регистре
# Например: func(,  -> ["hello", "world"]
def change_case(strings = ["hEllo", "wORld"], case_type="lower"):return [s.lower() for s in strings] if case_type == "lower" else [s.upper() for s in strings] if case_type == "upper" else strings
3
# Создать функцию, которая будет принимать в качестве аргумента строку, а затем говорить сколько в ней и каких символов, результать вернуть в виде объекта
# Например: 'Hello' -> {'H': 1, 'e': 1, 'l': 2, 'o': 1}
def count_characters(input_str = 'Hello'):return {char: input_str.count(char) for char in set(input_str)}
4
# Создать калькулятор используя функции, должны быть доступны операции(+, -, /, *), также должна быть функция-менеджер, которая будет принимать 2 числа и операцию, а затем вызывать нужную функцию и возвращать результат
def calculator_manager(a = 5, b = 5, operation = '*'):
    def add(x, y):return x + y
    def subtract(x, y):return x - y
    def multiply(x, y):return x * y
    def divide(x, y): return x / y if y != 0 else "Cannot divide by zero."
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    return print(operations[operation](a, b) if operation in operations else "Invalid operation.")
calculator_manager()
5
# Создайте функцию, которая будет рассылать сообщения пользователям, сообщая о акции в магазине компьютерной техники, отправлять сообщения нужно только тем людям, которые тем или иным образом относятся к IT-сфере
users = [
  { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
  { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
  { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
  { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
  { 'name': 'Hel\'ga', 'age': 35, 'work': 'IT-HR' }
]
def send_promotional_messages(users):return f"Sending promotional messages to: {', '.join(it_professionals:=[user['name'] for user in users if 'IT' in user['work'].upper()])}"

6
# Создать функцию, которая будет принимать в качестве аргумента 2 строки, 1-я строка должна быть следующего вида -> '1200m', вторая строка состоит из величины, в которую необходимо преобразовать данные -> 'km', 'cm', 'mm', задача: реализовать логику, которая будет принимать например строку вида '2000m', и строку в которую нужно преобразовать величину например 'km', вывод должен быть '2km'
def convert_measurement(value_str, target_unit):
    units = {'m': 1, 'km': 0.001, 'cm': 100, 'mm': 1000}

    try:
        value = int(value_str[:-1])
        conversion_factor = units.get(target_unit, 1)
        result = value * conversion_factor
        return f"{result}{target_unit}"
    except ValueError:
        return "Invalid input."

# Examples of usage
print(calculate_and_divide(10, 5, 2))
print(change_case(["hEllo", "wORld"], "lower"))
print(count_characters('Hello'))
print(calculator_manager(10, 5, '+'))
print(send_promotional_messages(users))
print(convert_measurement('1200m', 'km'))


7
# Создать функцию, которая будет рассчитывать расход топлива автомобиля, будет принимать 2 аргумента 1-й сколько всего километров проехали, второй сколько понадобилось топлива на это, затем функция должна рассчитать сколько ушло топлива на 100 км и вернуть результат вида: 'На 100км было расходовано 10л горючего'
def calculate_fuel_consumption(kilometers = 300, fuel_used = 30):print(f'На 100км было расходовано {((fuel_used / kilometers) * 100 ):.2f}л горючего') 



8
# Расчет премии сотрудникам
# salary- это заработная плата в месяц, overTime- количество часов, которое сотрудник взял сверхурочно, задача: создать функцию, которая будет добавлять к основной зарплате сверхурочное время(1час=200$), функция должна принимать список со словарями и возвращать также список, но уже с измененными данными пример: [{'name': 'Jack', 'salary': 10000, 'overTime': 4}] -> [{'name': 'Jack', 'salary': 10800}]

employees = [
  {'name': 'Jack', 'salary': 10000, 'overTime': 4},
  {'name': 'Tom', 'salary': 15000, 'overTime': 3},
  {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
  {'name': 'Helen', 'salary': 25000, 'overTime': 2},
  {'name': 'Peter', 'salary': 30000, 'overTime': 7}
]

def calculate_bonus(employees = employees):return print(updated_employees:= [{'name': emp['name'], 'salary': emp['salary'] + emp['overTime'] * 200} for emp in employees])


9
# Создать функцию, которая в качестве аргумента будет принимать список со строками и числами, задача, отсортировать числа в отдельный список, а строки в отдельный и распечатать оба списка

def sort_strings_and_numbers(input_list = [10, 'apple', 5, 'banana', 3.14, 'orange', 7]): print("Отсортированные числа:", sorted((item for item in input_list if isinstance(item, (int, float)))), "\nОтсортированные строки:", sorted((item for item in input_list if isinstance(item, str))))





10
# Создайте функцию, которая будет в качестве аргумента принимать список такого вида как указан выше, и будет возвращать отсортированный список (сортировать по убыванию оценок, используйте sort())
students = [
  {'student': 'Jack', 'marks': 43},
  {'student': 'Tom', 'marks': 92}, 
  {'student': 'Helen', 'marks': 85}, 
  {'student': 'Peter', 'marks': 58},
  {'student': 'Jessica', 'marks': 78}
]

def sort_students_by_marks(student_list):
    sorted_students = sorted(student_list, key=lambda x: x['marks'], reverse=True)
    return sorted_students

sorted_students_list = sort_students_by_marks(students)
print("Отсортированный список студентов по убыванию оценок:")
print(sorted_students_list)

11
# Создайте функцию, которая будет принимать строку, а затем будет смотреть на все товары и возвращать только те, у которых в названии есть данная строка (учесть, что название может быть полным, а может быть частичным)
products = [
  {
    'title': 'Samsung S10', 
    'price': 800, 
    'count': 6, 
    'category': 'samsung'},
  {
    'title': 'iPhone 13 Pro', 
    'price': 1200, 
    'count': 9, 
    'category': 'apple'},
  {
    'title': 'Xiaomi Mi 10', 
    'price': 500, 
    'count': 2, 
    'category': 'xiaomi'},
  {
    'title': 'Samsung S9', 
    'price': 600, 
    'count': 4, 
    'category': 'samsung'},
  {
    'title': 'iPhone 11', 
    'price': 850, 
    'count': 1, 
    'category': 'apple'}
]

def filter_products_by_title(products, search_string):
    filtered_products = [product for product in products if search_string.lower() in product['title'].lower()]
    return filtered_products

search_result = filter_products_by_title(products, 'Samsung')
print("Товары с названием, содержащим 'Samsung':")
print(search_result)

12
# Используя из предыдущей задачи список с товарами, реализовать фильтрацию по категориям, функция должна в качестве аргумента принимать строку с категорией и возвращать список, в котором будут только те товары, у которых категория полностью совпадает с переданной
class ExpenseTracker:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.expenses = []

    def record_expense(self, target, amount):
        if amount > self.balance:
            print("Ошибка: Недостаточно средств на балансе.")
            return

        expense_data = {'target': target, 'spend': amount}
        self.expenses.append(expense_data)
        self.balance -= amount
        print(f"Расход на {target} в размере {amount} успешно записан. Остаток на балансе: {self.balance}")

    def add_income(self, amount):
        self.balance += amount
        print(f"Баланс успешно пополнен на {amount}. Текущий баланс: {self.balance}")

    def filter_expenses_by_category(self, category):
        filtered_expenses = [expense for expense in self.expenses if expense.get('category') == category]
        return filtered_expenses

tracker = ExpenseTracker(initial_balance=1000)

tracker.record_expense('Продукты', 200)
tracker.record_expense('Развлечения', 50)
tracker.record_expense('Техника', 500)

filtered_expenses = tracker.filter_expenses_by_category('Продукты')
print(f"Товары в категории 'Продукты': {filtered_expenses}")


13
# Создать счетчик расходов, есть некая переменная, которая будет хранить данные о вашем балансе, создать две функции, первая будет записывать расходы, вторая просто пополнять баланс, первая функция: ее основная задача получать 2 аргумента на что потрачено и сколько потрачено, дальше формировать словарь типа: {'target': 'Products', 'spend': 400}, затем сохранять эти данные в список и соответственно вычитать из баланса сумму трат, вторая функция просто получает в качестве аргумента сумму, которую нужно добавить на баланс, также необходимо реализовать проверку, достаточно ли средств на балансе для совершения расходов

class ExpenseTracker:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.expenses = []

    def record_expense(self, target, amount):
        if amount > self.balance:
            print("Ошибка: Недостаточно средств на балансе.")
            return

        expense_data = {'target': target, 'spend': amount}
        self.expenses.append(expense_data)
        self.balance -= amount
        print(f"Расход на {target} в размере {amount} успешно записан. Остаток на балансе: {self.balance}")

    def add_income(self, amount):
        self.balance += amount
        print(f"Баланс успешно пополнен на {amount}. Текущий баланс: {self.balance}")

tracker = ExpenseTracker(initial_balance=1000)

tracker.record_expense('Продукты', 200)
tracker.record_expense('Развлечения', 50)

tracker.add_income(300)
tracker.record_expense('Техника', 500)

14
# Дан пустой список, необходимо использовать его в качестве базы данных для словарей типа {title: 'str', price: num, category: 'str'}, задача реализовать полный CRUD(create(должна быть возможность создавать данные, в нашем случае объекты), read(возможность получения/чтения данных), update(изменение данных(можно использовать индекс)), delete(удаление данных(можно использовать индекс))), за каждое действие должна отвечать отдельная функция
# database = 

class Manager:
    database = []

    @classmethod
    def create_record(cls, title, price=0.0, category='Uncategorized'):
        record = {'title': title, 'price': price, 'category': category}
        cls.database.append(record)
        return record

    @classmethod
    def read_records(cls, index=None):
        if index is not None:
            return cls.database[index] if 0 <= index < len(cls.database) else None
        return cls.database

    @classmethod
    def update_record(cls, index, title=None, price=None, category=None):
        if 0 <= index < len(cls.database):
            record = cls.database[index]
            record.update({'title': title, 'price': price, 'category': category})
            return record
        return None

    @classmethod
    def delete_record(cls, index):
        if 0 <= index < len(cls.database):
            return cls.database.pop(index)
        return None


Manager.create_record('Product1', 10.99, 'Electronics')
Manager.create_record('Product2', 20.49, 'Clothing')

print("Before update:")
print(Manager.read_records())

Manager.update_record(0, price=15.99)

print("\nAfter update:")
print(Manager.read_records())

Manager.delete_record(1)

print("\nAfter delete:")
print(Manager.read_records())



"""Comprehensions extra"""
8
"""
Из списка 
Создайте новый list2, прибавив к каждому числу 6
"""
list1 = [44,54,64,74,104]
list2 = []
for x in list1:
    list2.append(x+6)
print(list2)


9
"""Из списка
Создайте новый, внеся туда только те числа квадрат которых больше 50
"""
task_9_list = [2, 4, 6, 8, 10, 12, 14]
list_9 = [x for x in task_9_list if x**2 > 50]
print(list_9)



10
"""
Из сторки string = "happy birthday!"
Создайте список list_, внесите туда все символы из строки кроме пробела и '!'
 
Вывод:
['h', 'a', 'p', 'p', 'y', 'b', 'i', 'r', 't', 'h', 'd', 'a', 'y']
"""
my_string = "happy birthday!"

list_ = [i for i in my_string if i.isalpha()]
print(list_)

11
"""
Дан словарь:
Используйте его чтобы создать список, из значений внутренних словарей

Вывод:
[3, 45, 23, 9, 12, 89]
"""
dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
new_list = [i for key, value in dict_.items() for x, i in value.items()]
print(new_list)
12
"""
Из списка:
Создайте словарь, занесите только те имена, длина которых больше 4.
Ключами будут имена, а значениями их длины, возведенные  
в квадрат. 

Вывод:
{'george': 36, 'ringo': 25, 'patty': 25, 'cynthia': 49, 'linda': 25}
"""
list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude']
new_dict = {name: len(name) ** 2 for name in list_name if len(name) > 4}
print(new_dict)
13
"""
Дан словарь
Пройдитесь по словарю и добавьте в список только те ключи, значение, которых
в диапазоне от 200 до 5000, добавленные в список ключи должны быть в верхнем регистре.
Нужно использовать comprehension.
"""
some_dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
some_List_ = [f'{x.capitalize()} : {y}' for x, y in some_dict_.items() if 5000 > y > 200]
print(some_List_)

14
"""
Дан словарь:
Создайте словарь dict2:
- Ключи должны быть те же, что и в первом словаре, но каждый символ 'i' замените на ''
- Значением должно быть количество повторений символа 'i' в этом ключе

Вывод:
{'Sedan': 0, 'SUV': 0, 'Pckup': 1, 'Mvan': 2, 'Vann': 0, 'Sem': 1, 'Bcycle': 1, 'Motorcycle': 0}
"""
dict__123 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
dict__1234 = {name.replace('i', ''): name.count('i') for name in dict__123}
print(dict__1234)
15
"""
Из списка 
Создайте новый list2, не добавляя все пустые значения(0, None, [], {}, '') 

Вывод:
[1, 2, 3, 'a', 'abc', 23, [1, 2, 3, 4], {'a': 1, 'b': 2}, 'drf']
"""
list1_14524 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
list123393 = [z for z in list1_14524 if z]
print(list123393)

16
"""
Дан список SPL_Patrons. Каждый его подсписок содержит две части информации
о посетителях библиотеки:
- имя посетителя
- количество книг, которые они одолжили за последний год
Используйте list comprehension, 
чтобы создать список readers имен меценатов, 
которые в прошлом году одолжили более 100 книг

Вывод:
['Kim Tremblay', 'Jessica Smith', 'Alex Roy', 'Sarah Khan', 'Samuel Lee', 'Ayesha Qureshi']
"""
print(new_list48591:= [i[0] for i in [['Kim Tremblay', 134],['Emily Wilson', 42],['Jessica Smith', 215],['Alex Roy', 151],['Sarah Khan', 105],['Samuel Lee', 220],['William Brown', 24],['Ayesha Qureshi', 199],['David Martin', 56],['Ajeet Patel',69]] if i[1] > 100])
17
"""
Из предыдущего списка SPL_Patrons:
предположим, что посетитель экономит в среднем 11,95 доллара, 
одалживая книгу вместо того, чтобы покупать ее. 
Используйте list comprehension, чтобы создать список saved_amount 
сэкономленной суммы для каждого клиента

Вывод:
[1601.3, 501.9, 2569.25, 1804.45, 1254.75, 2629.0, 286.79, 2378.05, 669.19, 824.55]
"""
print(saved_amount:= [x[1] * 11.95 for x in [['Kim Tremblay', 134],['Emily Wilson', 42],['Jessica Smith', 215],['Alex Roy', 151],['Sarah Khan', 105],['Samuel Lee', 220],['William Brown', 24],['Ayesha Qureshi', 199],['David Martin', 56],['Ajeet Patel',69]] ])
18
"""
Используйте comprehensions для создания списка из списков, 
где каждый подсписок состоит из имени пирата и стоимости 
его / ее награбленных мешков с зерном 
(рассчитайте стоимость зерна, предположим, 
что средняя рыночная стоимость мешка зерна составляет 42 доллара, 
но включите только тех пиратов, которые любят попугаев)

Вывод:
[['Tractor Jack', 42000], ['Prairie Lily', 10290], ['Red River Rosie', 14700], ['Assiniboine Sally', 26040], ['Thresher Tom', 6300]]
"""
prairie_pirates = [
['Tractor Jack', 1000, True],
['Plowshare Pete', 950, False],
['Prairie Lily', 245, True],
['Red River Rosie', 350, True],
['Mad Athabasca McArthur', 842, False],
['Assiniboine Sally', 620, True],
['Thresher Tom', 150, True],
['Cranky Canola Carl', 499, False]
]
print(rice_amount:= [[x[0], x[1]*42] for x in  prairie_pirates if x[2] == True])


19
"""
По данному ниже словарю, пройдитесь циклом
- Найдите сумму лайков всех пользователей, рейтинг которых выше 3
используйте list comprehension

Вывод:
57
"""
dict_ = {
    'Sasha': {
        'likes': 23,
        'comments': 2,
        'rating': 4
    },
    'Aliya': {
        'likes': 34,
        'comments': 5,
        'rating': 5
    },
    'Dasha': {
        'likes': 15,
        'comments': 3,
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': 2,
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': 7,
        'rating': 2
    }
}

print(some_complihension:= sum(v["likes"] for k, v in dict_.items()if v['rating'] > 3))

20
"""
Используя приведенный словарь dict_, создайте список из id, 
которые хранятся под ключом comments. Берите только те комментарии, 
количество которых больше 3
"""
dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}

"""
Вывод:
[1, 2, 3, 4, 5, 6]
"""
print(comment_ids:= [comment['id'] for user_data in dict_.values() for comment in user_data['comments'] if len(user_data['comments']) > 3])


