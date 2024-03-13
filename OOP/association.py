# Ассоциация - принцип ООП, в котором два класса связаны друг с другом. Связь обозначает то что внутри одного объекта будет существовать другой объект от другого класса

# агрегация - слабая связь
# композиция - сильная связь

class Battery:
    _power = 100
    
    def charge(self):
        if self._power < 100:
            self._power = 100

# class Iphone:
#     def init(self, color) -> None:
#         self.color = color
#         self.battery = Battery()
#         # когда мы создаем внутри класса объект от другого класса - композиция

# a = Iphone('white')
# print(a.battery._power)
# a.battery._power -= 50
# print(a.battery._power)
# a.battery.charge()
# print(a.battery._power)
# del a
# при удалении iphone вместе с ним удаляется батарейка

class Nokia:
    def init(self, color, battery) -> None:
        self.color = color
        self.battery = battery
        # когда объект создается из вне класса и передается внутрь - агрегация

battery = Battery()
nokia1 = Nokia('gray', battery)

print(nokia1.battery._power)
del nokia1

nokia2 = Nokia('black', battery)
# при удалении объекта Nokia, батарейка остается