# ФУНКЦИЯ полиморфизм -> len(): __len__
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

#Полиформизм способность функции (метода) использоваться с объектами различных классов
#Широко распрастраненное определение: "один интерфейс - много реализаций"
#list.pop
#set.pop
#dict.pop 

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f'I am {self.name}'

# class Dog(Animal):
#     def speak(self):
#         return super().speak() + ' woof!'

# class Cat(Animal):
#     def speak(self):
#         return super().speak() + ' meow!'

# def test_polymorphism():
#     dog = Dog('Bobby')
#     cat = Cat('Whiskers')
    
#     assert dog.speak() == 'I am Bobby woof!'
#     assert cat.speak() == 'I am Whiskers meow!'
#     return dog.speak(), cat.speak()


# print(test_polymorphism())

# class Cat:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f'Its a car. Cats name is {self.name},age: {self.age}')
    
#     def make_sound(self):
#         print('meow meow')

# class Dog:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f'Its a dog. Dogs name is {self.name},age: {self.age}')
    
#     def make_sound(self):
#         print('woof woof')

# cat = Cat('Garfild' , 5)
# dog = Dog('PLuto' , 10)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()

# cat.make_sound()
# dog.make_sound()

# from abc import ABC,abstractmethod

# class Shape(ABC):
#     def __init__(self,name) -> None:
#         self.name = name
    
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def fact(self):
#         pass

# class Square(Shape):
#     def __init__(self, length) -> None:
#         super(Square,self).__init__('kvadrat')
#         self.length = length
    
#     def area(self):
#         return self.length **2

#     def fact(self):
#         return 'У КВАДРАТА ВСЕ СТОРОНЫ РАВНЫ'
    
# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius
    
#     def area(self):
#         from math import pi
#         return pi * self.radius **2
    
#     def fact(self):
#         return 'krug'
# a = Square(5)
# b = Circle(5)
# print(a.area())
# print(b.area())

#mixins
# Миксины классы которые используются для наследования и передачи дочерним классам опеределнный
# методов но от них не создаются обьекты 
# для чего

# 1 вы хотите предоставить множество доп методов  для классов 
# 2 вы хотите использовать один конкретный метод во множестве разных классов

# class EngineMixin:
#     def start_engine(self):
#         print(f'Started engine')
    

# class RadioMixin:
#     def play_road(self):
#         print(f'music is playing')

# class Plane(EngineMixin):
#     pass

# class Smartphone(RadioMixin):
#     pass

# class Train(EngineMixin,RadioMixin):
#     pass

# plane_1 = Plane()
# plane_1.start_engine()
# phone_1 = Smartphone()
# train_1 = Train()

# class FlyMixin:
#     def fly(self):
#         print('I can fly!')

# class WalkMixin:
#     def walk(self):
#         print('I can walk!')

# class SwimMixin:
#     def swim(self):
#         print('I can swim!')


# class Human(WalkMixin, SwimMixin):
#     name = 'human'

#     def talk():
#         print('I can talk!')

# class Fish(SwimMixin):
#     name = 'fish'

# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'flying fish'

# class Duck(SwimMixin, WalkMixin, FlyMixin):
#     name = 'duck'

# obj = Human()
# obj.walk()
# obj.swim()
