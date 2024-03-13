from views import CreateMixin, ReadMixin

class SmartPhones(CreateMixin, ReadMixin):
    pass

smartphones = SmartPhones()
print(smartphones.post(title = 'Redmi Note 10', description = 'The best phone', qty = 10, price = 250))
print(smartphones.post(title = 'Iphone 15', description = 'The  phone', qty = 2, price = 1400))
print(smartphones.post(title = 'Samsung S23', description = 'The flip - flap phone', qty = 5, price = 1000))
print(smartphones.post(title = 'Huawei', description = 'The best phone', qty = 7, price = 360))
print(smartphones.post(title = 'Sony', description = 'The best phone', qty = 8, price = 250))


print()
print()
print()
print(smartphones.list())
print()
print(smartphones.detail(6))