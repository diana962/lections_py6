# области видимости и пространства имен(scopes)
# технология, которая определяет контекст имени в рамках которого мы можем ее использовать.

# a = 5
# def func():
#     print(a) # a = 5
#     b = 10
#     print(b)

# func()
# print(b) #-> не сработает, так как b находится внутри фунции, что ограничивает ее видимость.

# built-ins (встроенная область видимости) - print(), len()
# global(глобальная) - область одной функции
# <enclosed> (замкнутая(нелокальная, non local))
# local(локальная) -> область внутри одной функции

# a = 5 # global
# print(len('Hello')) # built in
# def hello(): # global
#     a = 'Hello' # local
#     print(a, 'local, inside in func!')

# hello()
# print(a, 'global') # 10 

# LEGB - local enclosed global built-in # последовательность поиска имен
# ----------------------------------------------------------------------------------------------
# enclosed
# замкнутое пространство имен - локальное пространство, у которого есть внутреннее (локальное) вложенное пространство

# x = 'global'
# print(x, '1') # в первую очередь

# def enclosed():
#     x = 'enclosed'

#     def local():
#         x = 'local'
#         print(x, '3')
#     # local() -> зависит от метоположения
#     print(x, '2') # во вторую очередь
#     local() # в третью очередь
#     print(x, '4') # в четвертую очередь
# enclosed() # если закоментить local вообще не появится
# print(x, '5') # в послюднюю очередь


# var = 0
# def increment(): # LEGB
#     global var
#     var = var + 1
#     if var < 15:
#         increment() #-> zaprintit 15

# increment()
# increment() #-> повтор def
# increment()
# increment() #-> повтор def
# print(var) # 14 + 4

# global - позволяет изменять значение глобальной переменной внутри локальной области
# nonlocal - позволяет изменять значение нелокальной переменной, находясь внутри локальной области

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num +=1
#         return num
#     return increment

# c_steps = counter()
# for _ in range(1, 10000):
#     c_steps() #-> можно косвенно призывать фунцию: c_steps->counter()->def counter()->increrment-> num +=1
# print(c_steps(), 'steps')

# c_jumps = counter()
# print(c_jumps(), 'jump')
# print(c_jumps(), 'jumps')
# print(c_jumps(), 'jumps')
