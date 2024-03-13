# ООП - обьектно-ориентированное программирование
# Класс - это описание того, как должен выгдялить обьект, то есть в классе мы описываем какими своцйствами (даанымим) и поведением(функциями) долден обдладать обьект.

# Обьект - это некая сущность, которую мы создаем от класса, у обьектна есть состояние свойств(данные)

# атрибуты - обычные пеерменные внутри класса

# методв - функции внутри класса
# ----------------------------------------------------------------------------------

# class Human:
#     age = 0 # атрибут класса

#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + ' '+ last_name # атрибут метода
#         self.job = job
#         self.citizen = citizenship
    
#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Citizen: {self.citizen}'

# john = Human('John', 'Snow', 'King of North', 'Northener')
# anvar = Human('Anvar', 'Lanister', 'Programmer', 'Kyrgyz')

# # print(john, anvar, type(anvar))
# # print()
# # print(dir(john))

# # print(john.show_info()) # -> self.methode()
# # john.age = 24 # -> updated data -> self.attribute = new value
# # john.job = 'King of Westeros' # -> updated data
# # print(john.show_info())
# # ----------------------------------------------------------------------------------

# class Dog:
#     #атрибуты класса
#     age = 0
#     ears = True

#     def __init__(self, name: str, color: str) -> None:
#         "Инициализатор именно здесь создаются атрибуты обьекта"
#         # self - ссылка на обьект, который создается 
#         self.name = name
#         self.color = color
    
#     def bark(self):
#         print(f'{self.name} лает!')

#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, color: {self.color}, ears: {self.ears}')

# rex = Dog('Rex', 'black')
# pluto = Dog('Pluto', 'brown')
# aktosh = Dog('Aktosh', 'gray')

# print(rex.show_info())

# rex.age = 2
# pluto.age = 7
# aktosh.age = 1
# aktosh.ears = False

# print(aktosh.show_info())
# rex.show_info()
# pluto.show_info()

# rex.bark()
# pluto.bark()
# aktosh.bark()
# ----------------------------------------------------------------------------------

class Human:
    def __init__(self, name) -> None:
        self.name = name
        self.hunger = 100

    def walk(self):
        print(f'{self.name} walking around!')
        self.hunger +=30
    
    def work(self):
        print(f'{self.name} works! Criminal!')
        self.hunger +=50
    
    def eat(self, meal, finish = True):
        print(f'{self.name} eats {meal}!')
        self.hunger -=60 if finish else 30
    
    def info(self):
        print(f'{self.name} -> {self.hunger}')

obj = Human('Raychel')
obj.info()
obj.eat('Kruassan')
obj.eat('Kasha', finish = False)
obj.info()
obj.walk()
obj.work()
obj.eat('Plov')
obj.walk()
obj.info()
