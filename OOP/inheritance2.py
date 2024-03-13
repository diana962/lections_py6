# class Employee:
#     bonus = 1.5

#     def __init__(self, first_name, last_name, salary):
#         self.name = f'{first_name} {last_name}'
#         self.salary = salary

#     def get_info(self):
#         return f'FIO: {self.name}, \nSalary: {self.salary}'
    
#     def increase(self):
#         self.salary *= self.bonus
    
#     def __str__(self) -> str:
#         return self.get_info()
    
# class Manager(Employee):
#     def __init__(self, first_name, last_name, salary, devs = []):
#         super().__init__(first_name, last_name, salary)
#         self.devs = devs
    
#     def add_devs(self, developer):
#         self.devs.append(developer)
    
#     def show_devs(self):
#         return [x.get_info() for x in self.devs]

# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, language):
#         super().__init__(first_name, last_name, salary)
#         self.lang = language

#     def get_info(self):
#         info = super().get_info()
#         info += f', Programming Languages: {self.lang}'
#         return info

# dev1 = Developer('John', 'Snow', 1500, 'Python')
# dev2 = Developer('Steve', 'Jobs', 3000, 'C++')
# dev3 = Developer('Lary', 'Page', 1200, 'JS')
# dev4 = Developer('Tirion', 'lanister', 2000, 'JS')

# man1 = Manager('jamie', 'Lanister', 4000, [dev2, dev1])
# man2 = Manager('William', 'Kan', 15)

# print(f'Manager {man1}, has {man1.show_devs()} developers')
# print(f'Manager {man2}, has {man2.show_devs()} developers')

# man1.add_devs(dev3)
# man2.add_devs(dev3)
# man2.add_devs(dev4)

# dev3.increase()
# dev4.increase()
# man2.increase()

# print('After: ')
# print(f'Manager {man1} has {man1.show_devs()} developers!')
# print(f'Manager {man2} has {man2.show_devs()} developers!')

# ---------------------------------------------------------------------------
# Множественное наследование - это когда класс наследуется от двух или более классов

# class Auto:
#     def play_music_at_station(self):
#         print('Music playes!')

#     def ride(self):
#         print('We are riding on the ground')

# class Plane:
#     def play_music_at_station(self):
#         print('Ed Sheeran')

#     def fly(self):
#         print('We are flying')

# class FutureAuto(Plane, Auto):
#     pass

# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()
# obj.play_music_at_station()

# -------------------------
# Проблема ромба - когда поиск шел в родительский класс прежде чем искать у соседнего общего потомка(решена с помощью MRO)
# MRO(Method Resolution Order) - механизм для корректного поиска родительских методов. Был создан для решения ппроблемы ромба, которая появилась после введения object в пайтон. Поиск идет таким образом, что если у родительских классов есть общий предок, то идет поиск в ширину

# class Zero:
#     def say(self):
#         print('class Zero')

# class First(Zero):
#     # def say(self):
#     #     print('class First')
#     pass

# class Second(Zero):
#     def say(self):
#         print('class Second')

# class MyClass(First, Second):
#     def say(self):
#         super().say()
#         print('My class')

# obj = MyClass()
# obj.say()
# print(MyClass.mro()) # [<class '__main__.MyClass'>, <class '__main__.First'>, <class '__main__.Second'>, <class '__main__.Zero'>, <class 'object'>]