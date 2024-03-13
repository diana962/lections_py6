# Анотация свойств (@property(getter seter))

# class Person:
#     __name = 'John'
#     __age = 22

#     @property
#     def name(self):
#         """The name property (getter)"""
#         print(self.__name)
    
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             print('Invalid value')
#         else:
#             print(f'Setter: {value}')
#             self.__name = value
    
#     @property
#     def age(self):
#         print(self.__age)
    
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or value not in range(0, 150):
#             print('Invalid Value for age')
#         else:
#             self.__age = value


# obj = Person()
# obj.name #-> here you dont need to use () in the end, because of @property 
# obj.name  = 'Din'
# obj.name
# obj.age
# obj.age = 30
# obj.age
# obj.age = -3
# obj.age = 208
# obj.age = 'fg'
# obj.age


# -----------------------------------------------------------------------------------

# read, write, delete

# class Circle:
#     def __init__(self, radius) -> None:
#         self._radius = radius
    
#     def _get_radius(self):
#         print('Getter, _get_radius')
#         return self._radius
    
#     def _set_radius(self, value):
#         print('setter, _set_radius')
#         if not isinstance(value, (int, float)):
#             print('Invalid Value')
#         else:
#             self._radius = value
    
#     def _del_radius(self):
#         print('deleter, _del_radius')
#         answer = input('Are you sure(yes/no)?')
#         if answer.lower().strip() == 'yes':
#             del self._radius
#             print('Deleted')
#         else:
#             print('Not deleted.')
    
#     radius = property(fget = _get_radius, fset = _set_radius, fdel = _del_radius, doc = 'radius property') # -> NEW NEW NEW not as decorator but as function

# obj = Circle(5)
# print(obj.radius)
# obj.radius = 7.5
# print(obj.radius)
# del obj.radius
# print(obj.radius)

# ------------------------------------------------------------------
# read - only

# class CoordinateWriteError(Exception):
#     pass

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     @property
#     def x(self):
#         print(self.__x)
    
#     @property
#     def y(self):
#         print(self.__y)
    
#     @x.setter
#     def x(self, value):
#         raise ConnectionAbortedError('x - Coordinate is to read only')
    
#     @y.setter
#     def y(self, value):
#         raise ConnectionAbortedError('y - Coordinate is to read only')
    
# obj = Point(42.123445, -123.58790)
# obj.x
# obj.y
# # obj.x = 55


# -------------------------------------------------------------------------------

# write - only
# import hashlib, os

# class User:
#     def __init__(self, username, password):
#         self.__password  = password
#         self.usernmae = username
    
#     @property
#     def password(self):
#         raise AttributeError('Password is invalid!')
    
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str) or len(value) < 8:
#             raise ValueError('Invalid value for password')
#         salt = os.urandom(32)
#         self.__password = hashlib.pbkdf2_hmac('sha256', value.encode('utf - 8'), salt, 100_000)

# # sha256 -> name of hash that already exists
# # 100_000 -> amount of times from where comp chooses only one

# john = User('JohnSnow', 'secret_key')
# print(john.password)
# john.password = 'JohnSnowTheBest'
# print(john._User__password) -> зпхэширован