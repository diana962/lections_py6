# 1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
# # """
# class Circle:
#     color = 'blue'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def show_info(self):
#         print(f'area: {Circle.pi * 2 * self.radius}, {self.color}')

# krug = Circle(2)
# krug.show_info()
# krug.color = 'red'
# krug.show_info()

# """
# 2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
# """
# class Song:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
#     def show_title(self):
#         print(f'{self.name}')
#     def show_author(self):
#         print(f'{self.author}')
#     def show_year(self):
#         print(f'{self.year}')

# song1 = Song('Save your tears', 'Weeknd', '2018')
# song1.show_author()

# """
# 3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
# """
# class Taxi:
#     def __init__(self, name, price, price_per_km, km):
#         self.name = name
#         self.price = int(price)
#         self.price_per_km = int(price_per_km)
#         self.way = int(km)
#     def show_price(self):
#         print(f'Price of {self.name}: {self.price + (self.price_per_km *self.way)} som')
        

# namba = Taxi('Namba', '55', '22', '15')
# namba.show_price()

# """
# 4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
# Затем объявите экземляр класса и вызовите метод.
# """

# class Telefon_Book:
#     def __init__(self, first_name, last_name, number):
#         self.name = first_name + " "+ last_name
#         self.number = number
#     def show(self):
#         print(f'Контакт: {self.name}, телефон: {self.number}')

# ivan = Telefon_Book('Ivan', 'Petrov', '+996555777888')
# ivan.show()

# """
# 5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
# """
# # писать код здесь

# class Salary:
#     steuer = 0.08
#     def __init__(self, salary, expirience_in_year):
#         self.salary = int(salary)
#         self.expirience = int(expirience_in_year)
#     def show(self):
#         print(f'сумму вашего налога is: {self.salary * Salary.steuer * self.expirience * 12}')

# ivan = Salary('25000', '10')
# ivan.show()


# Создайте класс Soda принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
# class Soda:
#     def __init__(self, topping = 0):
#         self.topping = topping
#     def show_my_drink(self):
#         if self.topping:
#             print(f'Газировка c {self.topping}')
#         else:
#             print("«Обычная газировка»")

# cola = Soda()
# cola.show_my_drink()

# Создайте класс Student. При создании его экземпляра, мы должны записать имя и фамилию студента в соответствующие переменные объекта. В классе должны быть:
#  1 переменная объекта books = [ ]
#  2 переменная объекта “knowledge” со значением по умолчанию 0
#  3 метод read_book, который принимает название книги, добавляет книгу в books, добавляет 100 баллов в knowledge
#  4 метод do_homework, который при вызове добавляет 10 баллов в knowledge
#  5 Создайте экземпляры, вызовите методы.

# class Student:
#     def __init__(self, first_name, last_name, books: list, knowledge = 0):
#         self.name = first_name + " " + last_name
#         self.books = books
#         self.knowledge = knowledge
#     def read_book(self, book):
#         self.books.append(book)
#         self.knowledge +=100
#     def do_homework(self):
#         self.knowledge +=10
#     def show(self):
#         print(f'{self.name}: {self.books}, {self.knowledge}')

# sasha = Student('s', 'Petrova', ['100 years of Solitude', 'If we were villains'])
# print(sasha.knowledge)
# sasha.read_book('Forest')
# sasha.do_homework
# print(sasha.knowledge)
# print(sasha.show())

# 6. Создайте класс имеющий атрибут "дата рождения" и автоматически просчитываемый возраст по входящей дате рождения. Используйте модуль time/datetime 

from datetime import datetime

class Person:
    def __init__(self, birth_date):
        self.birth_date = birth_date

    @property
    def age(self):
        today = datetime.today()
        birth_date = datetime.strptime(self.birth_date, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
diana = Person("2002-06-09")
print("Возраст:", diana.age)


# Задание 2: Класс "Студент"

# Задача: Определите класс Студент с атрибутами имя и оценки (список оценок). Добавьте методы для добавления оценки к списку оценок и метод для расчета среднего балла.

# Пример использования:

# студент = Студент("Иван")
# студент.добавить_оценку(5)
# студент.добавить_оценку(4)
# print(студент.расчет_среднего()) -> 4.5

# class Student:
#     def __init__(self, name, grade: list):
#         self.name = name
#         self.grade = int(grade)
#     def grades(self, grade1):
#         ls = [self.grade]
#         ls.append(grade1)
#         return(f'AVG: {sum(ls)/ len(ls)})')
    
# diku = Student('Diku', 5)
# print(diku.grades(3))
# print(diku.grades(5))

# Задание 1: Класс "Комната" и "Дом"
# Цель: Практика в создании взаимодействующих объектов и управлении ими.

# Задача: Создайте класс Комната с атрибутами название, ширина и длина. Добавьте метод, который вычисляет площадь комнаты. Затем создайте класс Дом, который содержит список комнат. В классе Дом должны быть методы для добавления комнаты и вычисления общей площади дома.

# class Room:
#     def __init__(self, name, bright, length):
#         self.name = name
#         self.bright = bright
#         self.length = length
#     def area(self):
#         return(f'{self.bright * self.length}')
    
# class House:
#     def __init__(self):
#         self.rooms = []

#     def add_room(self, room):
#         self.rooms.append(room)

#     def total_area(self):
#         total = 0
#         for room in self.rooms:
#             total += int(room.area())
#         return total

# kitchen = Room("kitchen", 3, 4)
# bedroom = Room("bedroom", 5, 6)
# # print(kitchen.area())
# # print(bedroom.area())

# house = House()
# house.add_room(kitchen)
# house.add_room(bedroom)
# print(f'Area of house: {house.total_area()} m^2') 

# Задание 3: Класс "Библиотека" и "Книга"
# Цель: Работа с коллекциями объектов и их методами.

# Задача: Расширьте класс Книга из предыдущего задания, добавив атрибут количество. Создайте класс Библиотека, который будет содержать список книг. В классе Библиотека реализуйте методы для добавления книги (с учетом уже существующих тайтлов), удаления книги по названию, и поиска книг по автору.

# class Books:
#     def __init__(self, title, author, amount = 1):
#         self.title = title
#         self.author = author
#         self.amount = amount
#     def show_books(self):
#         print(f'Info of book: {self.title} ({self.author}), {self.amount}')

# class Library:
#     def __init__(self, list_of_books = []):
#         self.list_of_books = list_of_books
#     def add_book(self, book):
#         self.list_of_books.append(book)
#     def delete_book(self, title):
#         for book in self.list_of_books:
#             if book.title == title:
#                 if book.amount > 1:
#                     book.amount -= 1
#                 else:
#                     self.list_of_books.remove(book)
#     def search_by_author(self, author):
#         for book in self.list_of_books:
#             if book.author == author:
#                 print(f'{book} is found')
#     def __str__(self):
#         return f'Info of library: {self.list_of_books}'

# book1 = Books('War and Peace', 'Tolstoi')
# book2 = Books('Selection', 'Kira Kass', 3)
# book3 = Books('King', 'Kira Kass', 3)
# # book1.show_books()

# library1 = Library()
# library1.add_book(book1)
# library1.add_book(book2)
# library1.add_book(book3)
# library1.delete_book('War and Peace')
# print(library1)

# print(library1.search_by_author('Kira Kass'))



# Задание 4: Класс "Магазин" и "Продукт"
# Цель: Изучение принципов инкапсуляции и взаимодействия объектов.

# Задача: Создайте класс Продукт с атрибутами название, цена и категория. Затем создайте класс Магазин, который будет содержать список продуктов. В Магазине реализуйте методы для добавления продукта, удаления продукта по названию, и метод, который выводит список продуктов определенной категории.

# class Product:
#     def __init__(self, title, price, category):
#         self.title = title
#         self.price = price
#         self.category = category

# class Shop:
#     list_of_products = []
#     def add(self, product = []):
#         self.list_of_products.append(product)
#     def delete_product(self, title):
#         for product in self.list_of_products:
#             if product.title == title:
#                 self.list_of_products.remove(product)
#     def same(self, category):
#         res = []
#         for product in self.list_of_products:
#             if product.category == category:
#                 res.append(product)
#         print(f'Same category: {res}')
#     def __str__(self):
#         return f'In Basket: {self.list_of_products}'

# ban = Product('banana', 120, 'fruit')
# ban1 = Product('apple', 100, 'fruit')
# ban2 = Product('cucumber', 150, 'vegetable')

# shop = Shop()
# # shop.add([ban, ban2, ban1])
# shop.add(ban)
# shop.add(ban1)
# shop.add(ban2)
# # print(shop)

# # shop.delete_product('banana')
# # print(shop)

# shop.same('fruit')
# print(shop)


# Задание 5: Класс "Пользователь" и "УчетнаяЗапись"
# Цель: Глубокое понимание взаимодействия классов и управления состоянием.

# Задача: Создайте класс Пользователь с атрибутами имя, фамилия и email. Создайте класс УчетнаяЗапись, который будет содержать пользователя, логин, пароль и баланс. В классе УчетнаяЗапись реализуйте методы для изменения пароля, пополнения баланса и совершения платежа, проверяя достаточность средств на балансе.

# class User:
#     def __init__(self, name, last_name, email):
#         self.name = name
#         self.last_name = last_name
#         self.email = email

# class Account:
#     def __init__(self, user, username, password, balance=0):
#         self.user = user
#         self.username = username
#         self.password = password
#         self.balance = balance

#     def new_password(self, new):
#         self.password = new

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Balance: {self.balance}")

#     def pay(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"Remained: {self.balance}")
#         else:
#             print("Go make money!")

#     def __str__(self):
#         return f"Account of {self.user}, username: {self.username}, balance: {self.balance}"

# user1 = User('Karina', 'Saimon', 'bla-bla@gmail.com')
# account1 = Account(user1, 'KS', 'Karina11')
# print(account1)

# account1.new_password('12345678')
# account1.deposit(2500)
# account1.pay(50)
# account1.deposit(350)
# print(account1)
