# Принципы ООП
# 1. нааследование
# 2. Инкапсуляция
# 3. Полиморофизм

# 4. Абстракция
# 5. Композиция
# 6. Агрегация
# ----------------------------------

# Наследование 
# позволяет принимать родительские меттоды и атрибуты дочернему классу

# Родительсккий класс
# Дочерний класс
# ----------------------------------

# class Animal:
#     def print_info(self):
#         print('I am an Animal!')

# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass

# lion = Lion()
# lion.print_info()
# print(dir(lion))

# ------------------------------------

# class Animal:
#     def say(self):
#         print(f'This animals name is {self.name}: {self.golos}')
#     def eat(self):
#         print(f'{self.name} eats {self.meal}')

# class Lion(Animal):
#     name = 'lion'
#     golos = 'roar'
#     meal = 'meat'
#     griva = True

#     def info(self):
#         print(f'{self.name} griva: {self.griva}')

# class Dog(Animal):
#     name = 'dog'
#     golos = 'bark'
#     meal = 'meat'

# class Koala(Animal):
#     name = 'Koala'
#     golos = '---'
#     meal = 'Evkalid'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# simba.info()
# print()
# ------------------------------------

# class Person:
#     def info(self):
#         print('I am from Bish')

# class Student(Person):
#     def info(self):
#         super().info() # функция super возможна при использовании метода
#         print('I study at Manas university')

# obj = Student()
# obj.info()
# ------------------------------------

# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#     def get_info(self):
#         return {'brand': self.brand, 'model': self.model, 'price': self.price}

# class Acer(Laptop):
#     def __init__(self, model, price, year, videocard):
#         super().__init__('Acer', model, price)
#         self.vc = videocard
#         self.year = year

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['videocard'] = self.vc
#         return repr

# class Apple(Laptop):
#     def __init__(self, model, price, displey, year):
#         super().__init__('Macbook', model, price)
#         self.displey = displey
#         self.year = year

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['displey'] = self.displey
#         return repr
    
# mac = Apple('Pro', 1500, 14, 2020)
# print(mac.get_info())

# mac = Acer('Swift', 600, 'Nvidia', 2019)
# print(mac.get_info())