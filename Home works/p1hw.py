name = ['yes', 'no']
name.append('')
name[0] = 'no' # Замена на позиции 0, любая позиция
name.insert(2, 'hell yeah')
del name [0] # Удаление значения позиции 0, любая позиция
name.pop() # Удаление значения с позиции -1 или с желаемой позиции(x). Сохранение значения: popped_name = name.pop()
print(name)

# Типичная задача из области программирования — перебрать все элементы списка и выполнить с каждым элементом одну и ту же операцию.
# В ситуациях, требующих применения одного действия к каждому элементу списка, можно воспользоваться циклами for.
cars = ['honda', 'yamaha', 'suzuki', 'ducati']
for car in cars:
    print(car.title())

# first_name = 'nursultan'
# last_name = 'berdiev'
# full_name = first_name +" " + last_name 
# print(full_name)

# full_name = 'nursultan berdiev'
# print(full_name.title()) #Точка (.) после name в конструкции name.title() приказывает Python применить метод title() к переменной name.
# print(full_name.upper()) 
# print(full_name.lower())

# bicycles = ['trek', 	'cannondale', 	'redline', 	'specialized']
# print(bicycles[0])

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# ['honda', 'yamaha', 'suzuki']
# motorcycles[0] = 'ducati'
# print(motorcycles)
# ['ducati', 'yamaha', 'suzuki']

# #Простейший способ добавления новых элементов в список — присоединение элемента в конец списка. Используя список из предыдущего примера, добавим новый элемент 'ducati':
# motorcycles.append('ducati')
# print(motorcycles)
# ['honda', 'yamaha', 'suzuki', 'ducati']

# #Метод append() упрощает динамическое построение списков. Например, вы можете начать с пустого списка и добавлять в него элементы серией команд append().
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

# #Метод insert() позволяет добавить новый элемент в произвольную позицию списка. Для этого следует указать индекс и значение нового элемента.
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)
# ['ducati', 'honda', 'yamaha', 'suzuki']

# #Если вам известна позиция элемента, который должен быть удален из списка, воспользуйтесь командой del.
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# ['honda', 'yamaha', 'suzuki']
# del motorcycles[0]
# print(motorcycles)
# ['yamaha', 'suzuki']

# #Метод pop() удаляет последний элемент из списка, но позволяет работать с ним после удаления. Удалим мотоцикл из списка:
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# ['honda', 'yamaha', 'suzuki']
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# ['honda', 'yamaha']
# print(popped_motorcycle)
# suzuki
