"""

1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.

"""

# class Class1:
#     def __init__(self, person):
#         self.person = person
#     def go(self):
#         print('Go')
#     def walk(self):
#         print('walk')

# class Class2(Class1):
#     def __init__(self):
#         super().go()
#         super().walk()
#     def say(self):
#         print('Say')
#     def roar(self):
#         print('roar')

# obj = Class2()
# print('Alia')


"""

2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.

"""
# class A:
#     def method1(self):
#         print("Основной функционал")

# class B(A):
#     def __init__(self):
#         super().method1
#         print('Дополнительный функционал')

# obj = B()
# print(obj.method1())


"""

3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:

append, который будет принимать строку и добавлять её в конец исходной

pop, который удаляет из строки последний элемент и возвращает его.

Пример:

# example = MyString('String')

# example.append('hello')

# print(example) -> 'Stringhello'

# print(example.pop()) -> 'o'

# print(example) -> 'Stringhell'

"""
# class MyString:
#     def __init__(self, str):
#         self.str = str
#     def append_(self, word):
#         self.str += word
#         return self.str
#     def pop_(self):
#         return self.str[-1]
#     def __str__(self):
#         return self.str

# example = MyString('String')

# example.append_('hello')

# print(example) #-> 'Stringhello'

# print(example.pop_()) #-> 'o'

# print(example) #-> 'Stringhell'

"""

4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.

"""
# class MyDict(dict):
#     def find(self, num):
#         try:
#             return MyDict(self)[num]
#         except:
#             return('Are you kidding?')

# print(MyDict({'1': 'bir', '2': 'eki'}).find(5))
"""

5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.

Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.

"""

# class Person:
#     def __init__(self, name, desc):
#         self.name = name
#         self.desc = desc
#     def display(self):
#         return (f'{self.name}: {self.desc}')
    
# class Student(Person):
#     def __init__(self, name, desc, major):
#         super().__init__(name, desc)
#         self.major = major
#     def display_student(self):
#         show = super().display()
#         # a = [show] +[self.major]
#         return f'{show} {self.major}' 

# obj2 = Student('Alihan', 'Good', 'Engineer')
# print(obj2.display_student())

"""

6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.

"""
# list_ = ['mama', 'papa', 'Nurs', 'Nurba']
# class ContactList(list):
#     def search_by_name(self, name):
#         self.name = name
#         if self.name in list:
#             return('Found')
#         else:
#             return('Not found')

# obj = ContactList(['mama', 'papa', 'Nurs', 'Nurba'])
# # print(obj.search_by_name('mama'))
# print(obj)

"""

7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery по умолчанию

должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.

У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.


Создайте два дочерних класса от Smartphone - Iphone и Samsung.

У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от какого телефона оно было выслано.

А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.

Создайте объекты от данных классов и примените все методы.

"""
# class Smartphone:
#     def __init__(self, name, color, memory, battery = 0):
#         self.n = name
#         self.c = color
#         self.m = memory
#         self.b = battery
#     def charge(self, percent):
#         self.b +=percent
#         return (f'After charge: {self.b}')
#     def __str__(self):
#         return (f'{self.n}: {self.m}, {self.b}')
    
# class Iphone(Smartphone):
#     def __init__(self, color, memory, battery, ios):
#         super().__init__('Iphone', color, memory, battery)
#         self.ios = ios
#     def send_imessage(self):
#         return ('Hi')
    
# from datetime import datetime
# class Samsung(Smartphone):
#     def __init__(self, color, memory, battery, android):
#         super().__init__('Samsung', color, memory, battery)
#         self.android = android
#     def show_time(self):
#         return datetime.now()

# iphone = Iphone('black space', '128GB', 86, 17.2)
# print(iphone.send_imessage())
# print(iphone.charge(14))
# print(iphone)

# galaxy = Samsung('black space', '64GB', 69, 14)
# print(galaxy.show_time())
 

"""

8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и formula - полное произношение заклинания.
У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.

Переопределите у класса метод str, чтобы он выдавал вам название, формулу и описание вместе, к примеру:
Открытие замков: Alohomora
позволяет магу попасть в любую комнату, способно открыть любую закрытую замочную скважину.

Наследуя от класса Spell создайте три заклинания,переопределяя в них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы

"""
# class Spell:
#     def __init__(self, name, formula):
#         self.name = name
#         self.formula = formula
#     def get_description(self, desc):
#         self.desc = desc
#         return 'added'
#     def execute(self):
#         return 'shot'
#     def __str__(self):
#         return f'{self.name}: {self.formula} \n{self.desc}'

# ala = Spell('Alohomora', 'Открытие замков')
# ala.get_description('Pозволяет магу попасть в любую комнату, способно открыть любую закрытую замочную скважину.')
# # print(ala)

# class Patronum(Spell):
#     def __init__(self, formula):
#         super(). __init__('Patronum', formula)

# patr = Patronum('magia')
# patr.get_description('kills')
# print(patr)

"""

9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. Переопределите init таким образом, чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.

Создайте исключение от этого класса с сообщением:

"ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"
Напишите функцию проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом CustomError:
Traceback (most recent call last):

  File "inheritance.py", line 121, in <module>

    check_letters(a)

  File "inheritance.py", line 117, in check_letters

    raise capitals_error

main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ
"""
# class CustomError(Exception):
#     def __init__(self, sms):
#         self.sms = sms
#     def check_letters(self):
#         if any([i.islower() for i in self.sms]):
#             raise CustomError(self)
#         else:
#             return 'Done'
        
# obj = CustomError('MjM')
# print(obj.check_letters())

"""

10. Создайте класс Character с помощью которого можно создавать героев для игры. Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная power_list, в которой хранится словарь:

power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
Класс должен иметь методы:

give_weapon - выбирает случайное оружие из списка
give_role - выбирает случайную роль из списка, к примеру: ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:

char1.give_powers('ловкость', 5)

увеличит ловкость вашего героя.

Создайте три разных дочерних класса от класса Character - Elf, Orc, DragonBorn,

дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя init от Character. Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character.
"""
# import random
# from random import choice

# class Character:
#     def __init__(self, name, power_list = {'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }):
#         self.name = name
#         self.power_list = power_list
#     def give_weapon(self):
#         print('No weapon')
#     def give_role(self):
#         roles = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#         return choice(roles)
#     def give_powers(self, kraft, num):
#         self.kraft = kraft
#         self.num = num
#         if self.kraft in self.power_list:
#             self.power_list[self.kraft] += self.num
#             return self.power_list
#         else:
#             return (f'{self.kraft} does not exist')

# class Elf(Character):
#     def __init__(self, name, bow_skill):
#         super().__init__(name)
#         self.bow_skill = bow_skill

#     def elf_special_ability(self):
#         return "Скрытность и ловкость эльфов помогают избегать врагов."

# elf_character = Elf("Muchachas", 8)
# print(f"{elf_character.name} получил оружие: {elf_character.give_weapon()}")
# print(f"{elf_character.name} выбрал роль: {elf_character.give_role()}")
# elf_character.give_powers('ловкость', 5)
# print(f"{elf_character.name} улучшил свою ловкость: {elf_character.power_list['ловкость']}")
# print(elf_character.elf_special_ability())

# class Orc(Character):
#     def __init__(self, name, brute_strength):
#         super().__init__(name)
#         self.brute_strength = brute_strength

#     def orc_special_ability(self):
#         return "Силовые характеристики орков делают их мощными в ближнем бою."

# orc_character = Orc("Громмаш", 10)
# print(f"{orc_character.name} получил оружие: {orc_character.give_weapon()}")
# print(f"{orc_character.name} выбрал роль: {orc_character.give_role()}")
# orc_character.give_powers('сила', 8)
# print(f"{orc_character.name} улучшил свою силу: {orc_character.power_list['сила']}")
# print(orc_character.orc_special_ability())

# class DragonBorn(Character):
#     def __init__(self, name, breath_weapon):
#         super().__init__(name)
#         self.breath_weapon = breath_weapon

#     def dragonborn_special_ability(self):
#         return "Дыхание дракона придает драконорожденным уникальное оружие."
    
# dragonborn_character = DragonBorn("Сапфир", "Огненное дыхание")
# print(f"{dragonborn_character.name} получил оружие: {dragonborn_character.give_weapon()}")
# print(f"{dragonborn_character.name} выбрал роль: {dragonborn_character.give_role()}")
# dragonborn_character.give_powers('интеллект', 7)
# print(f"{dragonborn_character.name} улучшил свой интеллект: {dragonborn_character.power_list['интеллект']}")
# print(dragonborn_character.dragonborn_special_ability())