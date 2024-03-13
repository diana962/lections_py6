"""1) Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
"""
# class Auto:
#     def ride(self):
#         return('Riding on a ground')

# class Boat:
#     def swim(self):
#         return('floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj3 = Amphibian()
# print(obj3.ride())
# print(obj3.swim())

"""2) Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""

# class RadioMixin:
#     def __init__(self, name):
#         self.name = name
#     def play_music(self, name):
#         self.name = name
#         return(f'{self.name} playes')

# class Auto:
#     def ride(self):
#         return('Riding on a ground')

# class Boat:
#     def swim(self):
#         return('floating on water')

# class Amphibian(Auto, Boat, RadioMixin):
#     pass

# amphibian = Amphibian('')
# print(amphibian.ride())
# print(amphibian.swim())
# print(amphibian.play_music("Dancing with a stranger"))

"""3) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник."""

# from datetime import datetime 

# class Clock:
#     def time(self, time = datetime.now()):
#         self.time = time
#         return self.time

# class Alarm:
#     def on(self):
#         return ('Alarm in on')
#     def off(self):
#         return ('Alarm in off')

# class AlarmClock(Clock, Alarm):
#     def set_alarm(self, time):
#         super().time()
#         self.time = time
#         return {f'{self.on()}. Alarm clock is set on {self.time}'}
    
# obj = AlarmClock()
# print(obj.set_alarm(12))
# clock = Clock()
# print(clock.time())

"""4) Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""

class Coder:
    def __init__(self, experience, count_code_time = 0):
        self.exp = experience
        self.counts = count_code_time
    def get_info(self):
        pass
    #     return (f'Programmer has {self.exp} years')
    def coding(self):
        pass
    #     self.count += hour
    #     return (f'Programmer works {self.count} hours.')

class Backend(Coder):
    def __init__(self, experience, languages_backend):
        Coder.__init__(self, experience)
        self.languages_backend = languages_backend
    
    def count(self, time):
        self.counts += time
        return self.counts
    
class Frontend(Coder):
    def __init__(self, experience, languages_frontend):
        Coder.__init__(self, experience)
        self.languages_frontend = languages_frontend
    def count(self, time):
        self.counts += time
        return self.counts

class Fullstack(Frontend, Backend):
    def __init__(self, experiencef, experienceb, languages_backend, languages_frontend):
        Frontend.__init__(self, experiencef, languages_frontend)
        Backend.__init__(self, experienceb, languages_backend)
    
    def get_info(self):
        return f'Backend langguage : {self.languages_backend} and frontend langguage : {self.languages_frontend}'
    
    def count(self, back_time, front_time):
        print(Frontend.count(self, front_time))
        print(Backend.count(self, back_time))
    

# bolot = Fullstack(3, 5, 'Ruby')
# # print(temirlan.get_info())

# bolot = Fullstack(1, 360, 'Python')
# # bolot = Fullstack(1, 360, 'Ruby')
# print(bolot.get_info())
# print(bolot.languages_backend)
        
fb = Fullstack(10,10,'python', 'ruby')
# print(fb.count(10, 10))
print(fb.count(3, 4))

