# 1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
# """
# # писать код здесь

# """
# 2)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World". Затем создайте класс B, который будет наследоваться от класса A. Создайте экземпляр от класса B, и через него вызовите метод method1.
# """
# # писать код здесь

# """
# 3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. Затем определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, с помощью которого Вы будете получать значение скорости.
# """
# # писать код здесь

# """
# 4)Перепишите класс Car из предыдущего задания.
# Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, для того чтобы можно было работать с данным классом следующим образом:

# car = Car()
# car.speed = 120
# print(car.speed)
# """
# # писать код здесь

# """
# 5. Создайте класс Car. Пропишите в init параметры make, model, year, odometer, fuel.
# Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70.
# Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте,
# хватит ли вам бензина из расчета того, что машина расходует 10 л / 100 км (1л - 10 км) . Если
# его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению
# одометра, но не напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью приватного
# метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не Let’s drive!”. Если же бензина не
# хватит, то распечатайте “Let’s drive!”. Если же бензина не Need more fuel, please, fill more!”
# """
# # писать код здесь
# """










# Написать платформу для прослушивания музыки
# 1) Класс Пользователь с юзернеймом, возраст, эл. почтой и подпиской(по дефолту - Без подписки, если подписка не оформлена, то с каждым прослушиванием появялется реклама, спам), плейлист(по дефолту - пустой список). Можно дополнительно еще пароль сделать, с валидацией, вся информация должна быть приватной.
# Нужно провалидировать все данные(почту на наличие @, пароль, возраст)

# - Метод для оформления подписки, для добавления в пейлист песни, 
# - метод для прослушивания песни, 
# - метод который прослушивает весь плейлист по очередно

# 2) Класс жанр в названием

# 3) Класс музыка с названием, автором, жанром, длительностью

# 4) Класс работник, который наследуется от Пользователя, но у него есть доп атрибут - роль (например админ), и платформа где он работает

# 5) Класс платформа для прослушивания музыки, например - Spotify, у которого должны быть списки песен, жанры, список пользователей с полпиской и без

# - методы для  просмотра всех песен,
# - методы для просмотра песен по определенному жанру,
# - метод для оформления подписки у пользователя, если
# - метод для поиска песни по названию
# - метод для добавления определенной песни в плейлист пользователя
# - метод удаления, добавления песни, жанра из списка Платформы, которую может сделать только админ этой платформы
# - метод блокировки, удаления пользователя, если это потребуется


















# Основные Концепции:
# 1) Абстракция: Создать абстрактный класс Транспортное Средство, который будет базовым для всех типов транспорта.
# 2) Наследование: Разработать классы Грузовик, Легковой Автомобиль и Мотоцикл, наследующие от Транспортное Средство.
# 3) Полиморфизм: Реализовать методы, такие как двигаться, загружать и разгружать, которые будут работать по-разному для разных типов транспортных средств.
# 4) Миксины: Включить миксин, например GPSМиксин, который добавляет функциональность GPS в транспортные средства.
# Задачи:
# Абстрактный Класс Транспортное Средство:

# Определите атрибуты, общие для всех транспортных средств (например, марка, модель, год выпуска).
# Определите абстрактные методы двигаться, загружать и разгружать.
# Классы Грузовик, Легковой Автомобиль и Мотоцикл:

# Наследуйте эти классы от Транспортное Средство.
# Реализуйте методы двигаться, загружать и разгружать по-своему для каждого типа транспорта.
# Миксин GPSМиксин:

# Добавьте методы для отслеживания местоположения транспорта.
# Интегрируйте этот миксин с классами транспортных средств.
# Тестирование:

# Создайте несколько экземпляров каждого типа транспортного средства.
# Продемонстрируйте полиморфизм, вызывая общие методы на разных объектах.
# Покажите работу GPS-функциональности.
# Это задание позволит студентам практиковаться в применении концепций ООП в Python, а также познакомит их с реальной ситуацией, где эти практики могут быть полезны.

# Написать платформу для прослушивания музыки
# 1) Класс Пользователь с юзернеймом, возраст, эл. почтой и подпиской(по дефолту - Без подписки, если подписка не оформлена, то с каждым прослушиванием появялется реклама, спам), плейлист(по дефолту - пустой список). Можно дополнительно еще пароль сделать, с валидацией, вся информация должна быть приватной.
# Нужно провалидировать все данные(почту на наличие @, пароль, возраст)

# - Метод для оформления подписки, для добавления в пейлист песни, 
# - метод для прослушивания песни, 
# - метод который прослушивает весь плейлист по очередно

# 2) Класс жанр в названием

# 3) Класс музыка с названием, автором, жанром, длительностью

# 4) Класс работник, который наследуется от Пользователя, но у него есть доп атрибут - роль (например админ), и платформа где он работает

# 5) Класс платформа для прослушивания музыки, например - Spotify, у которого должны быть списки песен, жанры, список пользователей с полпиской и без

# - методы для  просмотра всех песен,
# - методы для просмотра песен по определенному жанру,
# - метод для оформления подписки у пользователя, если
# - метод для поиска песни по названию
# - метод для добавления определенной песни в плейлист пользователя
# - метод удаления, добавления песни, жанра из списка Платформы, которую может сделать только админ этой платформы
# - метод блокировки, удаления пользователя, если это потребуется