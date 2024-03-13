# Инкапсуляция:
# 1. Языыковая конструкция, которая помогает связать данные с методами для их обработки и управления (связь между данными и методами которые управляют ими) (класс - капсула)
# 2. Механизм сокрытия, при помощи которого можно ограничитьдоступ одного компонента программы к другому

# Инкапсуляция как связь
# class Phone:
#     number = '+9955555555'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')
#         print(f'Мой номер: {Phone.number}')

# my_phone = Phone()
# my_phone.print_number()

# Инкапсуляция как метод сокрытия данных:
# 3 уровня сокрытия данных в питоне:
    # 1. Публичный (public) - number, print_number
    # 2. Защищенный (_protected) - _number
    # 3. Приватный (_private) - _number

# class Car:
#     _country = 'Germany'
#     motor = 'GT Line'

#     def __init(self) -> None:
#         self.marka = 'BMW' # public
#         self._model = 'I8' # protector
#         self.color = 'Red' # private

# obj = Car()
# print(dir(obj))
# print(obj.marka)
# print(obj._country, obj._model)
# print(obj._Car__color,obj._Car__motor)

# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 17

#     def call(self):
#         print(f'{self._caller} звонит вам')
#         questions = input('Взять трубку (yes/no): ')
#         if questions.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('Сбросили трубку!')

#     def __turn_on(self):
#         print('Ало!')
#         print(f'Count of calls with {self._caller}: {self.__count_of_calls}')

#     def __increment_calls(self):
#         self.__count_of_calls += 1


# john = Phone()
# print(john.username)
# john.call()
# john.call()
# john.call()
# john.call()
# john.call()

# class Person:
#     def __init(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def display_info(self):
#         print(f'My name is {self.name} and I\'m {self.age} years old!')

# obj = Person('John', 18)
# obj.display_info()
# obj.name = [1,2,3,4]
# obj.age = -25
# obj.display_info()

# ---------------------------------------------------------------------------------

# getter & setter
# они нужны чтобы избежать прямого обращения к сокрытым атрибутам
# при этом можно добавить логику валидации (проверки) данных которые будут установлены в атрибут

# class Person:
#     def __init__(self, name, age) -> None:
#         self.__name = name
#         self.__age = age
    
#     def display_info(self):
#         print(f'My name is {self.__name} and I\'m {self.__age} years old!')

#     # getter
#     def name(self): return self.__name #-> сделал его публичным
#     def age(self): return self.__age

#     # setter
#     def set_name(self, name):
#         if not isinstance(name, int):
#             print('Name must be str object!')
#         else:
#             self.__name = name

#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age <150:
#             print('Invalid value for age')
#         else:
#             self.__age = age

# obj = Person('John', 18)
# obj.display_info()
# obj.set_name(55)
# obj.set_age(-18)
# obj.display_info()
# obj.set_name('jamie')
# obj.set_age(26)
# obj.display_info()

# class Car:
#     def __init__(self, make, model, year, odometer = 0, fuel = 70):
#         self.make = make
#         self.model = model
#         self.year = year
#         self._odometer = odometer
#         self._fuel = fuel
    
#     @property
#     def odometer(self):
#         return self._odometer
    
#     def __add_distance(self, new_vall):
#         self._odometer += new_vall

#     def __subtruct_fuel(self, new_vall):
#         self._fuel = self._fuel - new_vall


#     def drive(self, km):
#         if km * 10  > self._fuel:
#             raise  ValueError("Not enough fuel! Please, fill up the tank.")
#         else:
#             print("Let's drive!")
#             self.__add_distance(km)
#             self.__subtruct_fuel(km * 10)


