# Напишите класс Subscriber, у которого есть переменные экземпляра:
# firstname
# lastname
# Сделайте так, чтобы метод __repr__ возвращал firstname + lastname

# Напишите класс Provider, у которого есть:
# переменный экземпляра name -- название провайдера
# переменный экземпляра subscribers -- список, в котором будут храниться экземпляры класса Subscriber
# переменный экземпляра payments -- словарь, ключём которого является экземпляр класса Subscriber, значением является сумма (вещественное число)
# метод register_payment, который принимает экземпляр класса Subscriber, и сумму, затем проверяет, есть ли такой экземпляр Subscriber в списке subscribers. 
# Если есть, записывает экземпляр в словарь payments в качестве ключа, а сумму в качестве значения
# Если нет, выкидывает (raise) ошибку ValueError

# Напишите класс Terminal, у которого есть
# переменная экземпляра amount = 0
# переменная экземпляра providers = [ ]
# Регистрировать провайдера через метод register, который принимает экземпляр класса Provider и добавляет в providers
# Принимать деньги в счет провайдера (pay), который принимает экземпляр класса Provider, экземпляр класса Subscriber и сумму (вещественное число). Внутри метода должен вызываться метод register_payment экземпляра класса Provider. register_payment успешно сработал, то в переменую amount нужно добавить сумму.

class Subscriber:
    def __init__(self, first_name, last_name):
        self.name = first_name + ' ' + last_name
    
    def __repr__(self):
        return self.name
    
# obj = Subscriber('Di', 'T')
# print(obj)

class Provider:
    def __init__(self, name, subscribers = [], payments ={}):
        self.name = name
        self.subscribers = subscribers
        self.payments = payments
    
    def register_payment(self, subscriber, amount):
        if subscriber in self.subscribers:
            self.payments[subscriber] = amount
        else:
            raise ValueError("Not found")

class Terminal:
    def __init__(self, amount = 0, providers = []):
        self.amount = amount
        self.providers = providers

    def register(self, provider):
        self.providers.append(provider)

    def pay(self, provider, subscriber, amount):
        provider.register_payment(subscriber, amount)
        self.amount += amount

terminal = Terminal()
provider = Provider("Di")
subscriber = Subscriber('Nurba', 'T')

terminal.register(provider)
provider.subscribers.append(subscriber)

terminal.pay(provider, subscriber, 1500)
print('Terminal: ', terminal.amount, '$')  
print('Payments: ', provider.payments)  