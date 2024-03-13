# Задача: Разработка иерархии классов для университета

# Вы проектируете систему для университета. Ваша задача — создать классы для различных типов людей в университете.

# 1) Базовый класс Person: Этот класс должен содержать общие атрибуты, такие как name (имя), age (возраст), и id (идентификационный номер). Также включите метод show_details(), который выводит информацию о человеке.

# 2) Класс Student: Наследует от Person. Добавляет специфические атрибуты, такие как student_id и courses (список курсов, на которые записан студент). Переопределите метод show_details() для вывода дополнительной информации специфичной для студента.

# 3) Класс Professor: Также наследует от Person. Вводит дополнительные атрибуты, например, employee_id, department (кафедра) и research_area (область исследований). Переопределите метод show_details(), чтобы он отображал информацию, специфичную для профессора.

# 4) Класс Administrator: Наследует от Person. Включает дополнительные атрибуты, такие как role (роль в университете) и department. Метод show_details() должен быть переопределен, чтобы отображать информацию, относящуюся к администраторам.

class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    def show_details(self):
        return (f'{self.name}: {self.id} \n{self.age} years old')

class Student(Person):
    def __init__(self, name, age, student_id, courses):
        super().__init__(self, name, age)
        self.student_id = student_id
        self.courses = courses
    def show_details(self):
        a = super().show_details()
        return [a] + [self.student_id] + [self.courses]
    
aida = Student('Kanat', 22, 10869, 'Math')
print(aida.show_details())
