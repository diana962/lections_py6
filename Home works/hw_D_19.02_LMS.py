# Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .

# Добавьте атрибут horsepower, который равен 85.

# Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с

# Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.

# Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto

# class Auto:
#     def __init__(self, brand, year, color, horsepower = 85):
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.horsepower = horsepower
#         self.add_horsepower()
#     def get_auto(self):
#         print(f'BRAND: {self.brand}, YEAR: {self.year}, COLOR: {self.color}, HORSEPOWER: {self.horsepower}')
#     def get_year(self):
#         print(f'YEAR: {self.year}')
#     def add_horsepower(self):
#         if self.brand in ('Mers, BMW, Poshe'):
#             self.horsepower += 40
#         else:
#             self.horsepower += 20

    
# auto1 = Auto('Tesla', 2017, 'black') 
# auto1.get_auto()
# # auto1.get_year()
# auto2 = Auto('BMW', 2017, 'black')
# auto2.get_auto()

# Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

# Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода для каждого студента.

# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def get_student(self):
#         print(f'NAME: {self.name}, AGE: {self.age}, COURSE: {self.course}')
    
#     def get_birth_year(self):
#         birth = 2024 - int(self.age)
#         print(f'{self.name} is {birth} years old')

# stud1 = Student('Anarbek', '21', 'Python')
# stud2 = Student('Bolot', '22', 'Literature')

# stud1.get_student()
# stud1.get_birth_year()
# stud2.get_student()