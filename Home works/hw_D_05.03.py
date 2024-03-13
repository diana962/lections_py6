"""
1. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
"""
# class MyList(list):
#     # def __getitem__(self, index):
#     #     return super().__getitem__(index-1)
#     def __new__(cls, list):
#         instance = super().__new__(cls)
#         # instance.insert(0, 0)
#         return instance

#     # # def index(self, instance):
#     # #     for i in instance:
#     # #         return instance.index(i-1)
        
# x = MyList([1,2,3,4,5])
# print(x) #-> [1, 2, 3, 4, 5]
# print(x[2])
# print(x[3])
"""
2. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
Также в методе new напишите условие для удаления
пробелов и пустых строк в созданных словах.
"""
# class Word(str):
#     def __new__(cls, obj): # cls - отсылка к самому классу Word 
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)
    
#     def __init__(self, obj) -> None:
#         super().__init__()
#         self.obj = obj
#     def __gt__(self, other): # obj - gt - obj2
#         if len(self) > len(other):
#             return self
#         elif len(self) < len(other):
#             return other
#         else:
#             return 'eq'
#     def __lt__(self, other):
#         return len(self) < len(other)
#     def __eq__(self, other):
#         return len(self) == len(other)
    
# word1 = Word('Diana')
# word2 = Word('Nurbolot')

# print(word1 > word2)
# print(word1 < word2)
# print(word1 == word2)


"""
3. Создайте класс BankAccount, представляющий банковский счет. Реализуйте магические методы init, str, add и sub, чтобы поддерживать инициализацию счета, вывод информации о счете и операции пополнения и снятия средств.
"""

# class BankAccount:
#     def __init__(self, money) -> None:
#         self.money = money
#     def __str__(self) -> str:
#         return (f'On your account: {self.money}')
#     def __add__(self, coins):
#         self.money +=coins
#         return (f'On your account: {self.money}')
#     def __sub__(self, coins):
#         self.money -= coins
#         return (f'On your account: {self.money}')

# cash = BankAccount(1200)
# print(cash)
# print(cash + 200)
# print(cash - 1100)


# Класс Vector3D 
# Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z). 
# Обязательно должны быть реализованы методы:  
# – сложение векторов оператором + (метод add), 
# – вычитание векторов оператором - (метод sub), 
# – скалярное произведение оператором * (метод mul), 
# – умножение на скаляр оператором * (метод mul), 
# – векторное произведение оператором @ (метод matmul). 
# Пример  
# v1 = Vector3D(4, 1, 2) 
# v1.display() 
# v2 = Vector3D() 
# v2.read() 
# v3 = Vector3D(1, 2, 3)