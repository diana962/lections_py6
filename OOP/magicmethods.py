# magic methods - магические методы
# dunder methods (double underscore) -> __init__
# служебные методы

# Магия(фишка) заключается в том, что эти методы запускаются без прямого обращения к ним, определенные методы могут отвечать за определенные операторы.

# Магические методы сравнения
# __eq__(self, other) -> 5 == 8
                        #  5__eq__(8)
# __ne__ -> !=
# __lt__ -> <
# __gt__ -> >
# __le__ -> <=
# __ge__ -> >=

# print('15' > 'ABC') # ASCII

# class Word(str):
#     def __new__(cls, obj): # cls - отсылка к самому классу Word 
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)
    
#     def __init__(self, obj) -> None:
#         super().__init__()
#         self.obj = obj
#     def __gt__(self, other): # obj - gt - obj2
#         print('gt worked')
#         print(self, '----', other)
#         if len(self) > len(other):
#             return self
#         elif len(self) < len(other):
#             return other
#         else:
#             return 'eq'
#     def __lt__(self, other) -> bool:
#         return len(self) < len(other)
#     def __eq__(self, other) -> bool:
#         return len(self) == len(other)


# obj = Word('      Hello World   ')
# obj2 = Word('Cod i fy trto')

# print(obj > obj2)
# print(obj < obj2)
# print(obj == obj2)

# --------------------------------------------
#  + - / * // % **


# + (__add__) - method
# * (__mul__) - operator
# / (__truediv__) - division
# // (__floordiv__) - floor division
# % (__mod__) - modulo
# ** (__pow__) - power
# << (__lshift__) - left shift
# >> (__rshift__) - right shift 
# & (__and__) - bitwise AND
# | (__or__) - bit


# class Number:
#     def __new__(cls, *args, **kwargs):
#         # print(cls, '!!!')
#         number = abs(args[0]) # number = abs(args) -> TypeError: bad operand type for abs(): 'tuple'
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance #-> intstance = self, instance = other
    
#     def __add__(self, other):
#         res = self.number + other.number
#         print(f'Result: {self.number} + {other.number} = {res}')
#         return res

# value1 = Number(-117)
# value2 = Number(53)
# res = value1 + value2
# print(5+5)

#  -------------------------------------------
# from random import choice

# class Dog:
#     def sound(self):
#         print('Bark!')

# class Cat:
#     def sound(self):
#         print('Meow meow')

# class Horse:
#     def sound(self):
#         print('Ihoho')

# class Pet:
#     def __new__(cls):
#         pet = choice([Dog, Cat, Horse])
#         self = super().__new__(pet)
#         print(f'I\'m {type(self).__name__}') # -> type(self) -> Class , __name__ -> name of this Class
#         return self
#     def __init__(self):
#         print('Pet never was called')

# pet = Pet()
# pet.sound()

#  -------------------------------------------

# MUST KNOW!!! Что такое синглтон? Написать сиинглтон.
# SINGLETON

# class Singleton:
#     _instance = None # -> После первого раза ссылка обьекта сохраняется(Not None) и все последующие будут под ним.

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __str__(self) -> str:
#         return str(id(self))
    
# a = Singleton()
# b = Singleton()
# print(a, b)
# print(a is b)
# obj = Singleton()
# obj2 = Singleton()
# print(obj, obj2)

#  -------------------------------------------
# from itertools import repeat
# from random import choice, randint

# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []
#     def add_coin(self, coin):
#         self.total += coin
#         self.coins.append(coin)
#     def  __len__(self):
#         return len(self.coins)
#     def __getitem__(self, index):
#         return self.coins[index - 1]


# obj = Kopilka() # -> Here is leer
# print(obj.coins)
# print(obj.total)
# print(len(obj)) # ohne def __len__(self) funktioniert nicht-> TypeError: object of type 'Kopilka' has no len()
# # print(len(Kopilka)) # -> Sowieso funktioniert nicht: TypeError: object of type 'type' has no len()

# for f in repeat(choice, randint(89, 156)):
#     obj.add_coin(f([1, 3, 5, 10]))

# # obj.add_coin(10)
# # obj.add_coin(5)
# # obj.add_coin(3)


# print(obj.coins)
# print(obj.total)
# print(len(obj))

# print(obj[0])
# print(obj[1])