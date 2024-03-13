# class Student:
#     uni = 'MIT'

#     def __init__(self, name) ->None:
#         self.name = name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_work = False
    
#     def add_points(self,points):
#         self.knowledge += points
#         if self.knowledge > 500 and not self.is_ready_work:
#             self.is_ready_work = True
#             print(f'{self.name} gets 500 points and ready to work')

#     def read_book(self, book_name):
#         self.add_points(50)
#         self.books.append(book_name)

#     def do_projects(self):
#         self.add_points(100)
    
#     def learn_lang(self, language, percent):
#         if percent not in range(70, 101):
#             print('INvalid')
#         else:
#             self.languages[language] = percent
#             self.add_points(percent)
    
# st1 = Student('John Snow')
# # st2 = Student('Din Winchester')
# # print(st1.name)
# # print(st2.name)

# # print(f'Before study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}')
# # print(f'Ready to work: {st1.is_ready_work}')

# st1.read_book('Grokaem Algoritmy')
# st1.read_book('Martin Eden')
# st1.read_book('algoritmi and data structures')

# st1.do_projects()
# st1.do_projects()

# st1.learn_lang('Python', 60)
# st1.learn_lang('JS', 90)
# st1.learn_lang('Python', 90)

# st1.do_projects()
# print(f'After study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_work}')

# ----------------------------------------------------------------
# class Car:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model
#     def show_info(self):
#         return f'{self.brand} -> {self.model}'
    
#     def __str__(self) -> str: #-> dabei man keine show_info Funktion braucht
#         return f'{self.brand} -> {self.model}'
    
# obj = Car('BMW', '8 series')
# print(obj) #-> BMW -> 8 series dank fuer def __str__(self):
# print(obj.brand)
# print(obj.show_info())

# obj2 = Car('Mercedes', 'Sprint')
# print(obj2)
# # obj2() ->TypeError: 'Car' object is not callable
# ----------------------------------------------------------------
# class Soda:
#     def __init__(self, ingredient = None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None
#     def __str__(self) ->str:
#         return'Normal one' if not self.ingredient else f'Soda is {self.ingredient}'
# a = Soda(1234)
# b = Soda(True)
# print(a,b)
# dushes = Soda('Pears')
# print(dushes)


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

# ------------------------------------------------------------------
# import random
# class Sniper:
#     health = 100
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self)-> str:
#         return self.name
    
#     def shoot(self, other):
#         other.health -=20
#         print(f'Attacked {self}')
#         print(f'Bei {other} ist nur {other.health} geblieben')

# sniper1 = Sniper('John Snow')
# sniper2 = Sniper('Din Winchester')

# print(sniper1)
# print(sniper2)

# while sniper1.health and sniper2.health:
#     choice = random.randint(1,2)
#     sniper1.shoot(sniper2) if choice == 1 else sniper2.shoot(sniper1)
#     print()

# print(f'{sniper1 if sniper1.health else sniper2} hat gewonnen.')