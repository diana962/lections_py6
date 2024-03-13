# Создайте класс мобильного телефона. Определите атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

class Telephone:
    def __init__(self, imei, battery, info_oc):
        self.imei = imei
        self.battery = battery
        self.info = info_oc
        while self.battery:
            if self.battery in range(0, 101):
                print(f'The battery right now is {self.battery}')
                break
            else:
                raise ValueError('The battery cannot be over 100 percent')
    
    def internet(self, data = 0.5):
        self.battery -= data
        print(f'After: {self.battery}')
    
    def music(self, data = 5):
        while self.battery:
            if self.battery >= 5:
                self.battery -= data
                print(f'After: {self.battery}')
                break
            else:
                raise ValueError('Charge your Phone.')
    
    def video(self, data = 7):
        while self.battery:
            if self.battery <= 0:
                raise ValueError('Charge your Phone.')
            if self.battery < 10:
                print(f'{self.battery} is not enough. Please charge your phone.')
                break
            else:
                self.battery -= data
                print(f'After: {self.battery}')
                break
    
    def charge(self, percent):
        self.percent = percent
        possible = round(100 - self.battery)
        while True:
            if self.percent in range(0, possible + 1):
                print(f'After charge: {self.battery + self.percent}')
                break
            else:
                raise ValueError('It can be charged until 100 percent only.')
        

obj = Telephone(12345, 30, 'IOS')
obj.internet()
obj.video()
obj.music()
obj.video()
obj.internet()
obj.charge(10)
obj.video()
obj.music()