# Задача 1: "Dollar"
# Цель: Создать функцию dollarize, преобразующую числа в долларовый формат, и класс MoneyFmt для управления денежными суммами.
# Описание:
# Функция dollarize должна принимать дробное число и возвращать строку, представляющую сумму в долларовом формате.

# Класс MoneyFmt использует внутренний атрибут amount для хранения денежной суммы и предоставляет методы для обновления суммы, возвращения ее как строки в долларовом формате и как исходного числового значения.
# Пример использования:
# # cash = MoneyFmt(12 345 678.021) 
# # print(cash) -- выводит "$12,345,678.02" 
# # cash.update(100 000.4567) 
# # print(cash) -- выводит "$100,000.46" 
# # cash.update(-0.3) 
# # print(cash) -- выводит "-$0.30" 
# # repr(cash) -- выводит -0.3 

# def dollarize(num = 12345678.021):
#     # return f'${num:,.2f}'
#     if isinstance(num, (float,int)):
#         num = str(num)
#         for i in num:
#             if i == '.':
#                 a = num[:num.index(i)]
#                 # print(f'${num}')
#                 b = a[::-1]
#                 # print(b)
#                 new_list = []
#                 step = 3
#                 for i in range(0, len(b), step):
#                     new_list.extend(b[i:i+step])
#                     new_list.append(',')
#                 c = new_list[-2::-1]
#                 joined = ''.join(c)
#         i = '.'
#         return f'${joined + num[num.index(i):]}'
#     else:
#         raise ValueError('This must be digits only!')

# print(dollarize())

# number = 123456789
# formatted_number = format(number, ",") # or f"{number:,}"
# print(formatted_number)


# class MoneyFmt:
#     def __init__(self, num) -> None:
#         self.num = num
#     def amount(self):
#         if isinstance(self.num, (float,int)):
#             self.num = str(self.num)
#             for i in self.num:
#                 if i == '.':
#                     a = self.num[:self.num.index(i)]
#                     # print(f'${num}')
#                     b = a[::-1]
#                     # print(b)
#                     new_list = []
#                     step = 3
#                     for i in range(0, len(b), step):
#                         new_list.extend(b[i:i+step])
#                         new_list.append(',')
#                     c = new_list[-2::-1]
#                     joined = ''.join(c)
#             i = '.'
#             return f'${joined + self.num[self.num.index(i):]}'
#         else:
#             raise ValueError('This must be digits only!')
        
#     def update(self, number):
#         self.number = number
#         return f'${self.number:,.2f}'
#     def __repr__(self):
#         return self.num
        
        
# cash = MoneyFmt(12345678.021) 
# print(cash.amount())
# print(cash.update(100000.4567))
# print(cash.update(-0.3))
# print(cash)

# Задача 2: "Велосипед"
# Цель: Реализовать класс Bike, моделирующий велосипед с различными атрибутами и методами управления.
# Описание:
# Класс должен содержать атрибуты для стоимости, производителя, модели, года выпуска, состояния, цены продажи и статуса продажи.
# Методы должны позволять 
# устанавливать цену продажи, учитывая минимальную прибыль, 
# обслуживать велосипед, изменяя его состояние и стоимость ремонта, 
# и продавать велосипед, изменяя его статус и рассчитывая прибыль.

# class Bike:
#     def __init__(self, min_price, producer, model, year, zustand, to_buy, status):
#         self.price = min_price
#         self.producer = producer
#         self.model = model
#         self.year = year
#         self.zustand = zustand
#         self.to_buy = to_buy
#         self.status = status
#     def set_price(self, min_prible):
#         self.min_prible = min_prible
#         return f'You can sell a bike at this price: ${self.price + self.min_prible}'
#     def repair(self):
#         self.zustand = 'Repaired'
#         self.price += 50
#         return(self.zustand)
#     def sell(self):
#         self.zustand = 'sold'
#         profit = self.to_buy - self.price
#         return(f'Bike is sold! Profit: {profit}')
    
    
        

# bycicle = Bike(12000, 'Yamaha', 'GT', 2018, 'broken', 13000, 'to sell')
# print(bycicle.set_price(50))
# print(bycicle.repair())
# print(bycicle.sell())





# Задача 3: "Герой"
# Цель: Разработать программу, имитирующую взаимодействие между солдатами и героями в контексте игры-стратегии.
# Описание:
# Необходимо создать классы для солдат и героев, каждый с уникальным номером и принадлежностью к команде.
# Солдаты могут "следовать" за героями своей команды, а герои могут повышать свой уровень.
# В программе должны генерироваться солдаты для двух команд, после чего сравнивается количество солдат в каждой команде, и у героя команды с большим числом солдат повышается уровень.

# import random

# class Soldier:
#     def __init__(self, number, team):
#         self.number = number
#         self.team = team
#         self.following = None
    
#     def follow(self, hero):
#         self.following = hero

# class Hero:
#     def __init__(self, name, team, level=1):
#         self.name = name
#         self.team = team
#         self.level = level

# def generate_soldiers(num_soldiers, team):
#     soldiers = []
#     for i in range(num_soldiers):
#         soldier = Soldier(i+1, team)
#         soldiers.append(soldier)
#     return soldiers

# def increase_hero_level(hero):
#     hero.level += 1
#     print(f"Hero {hero.name} of team {hero.team} leveled up to {hero.level}!")

# def compare_teams(team1_soldiers, team2_soldiers, team1_hero, team2_hero):
#     num_soldiers_team1 = len(team1_soldiers)
#     num_soldiers_team2 = len(team2_soldiers)
    
#     if num_soldiers_team1 > num_soldiers_team2:
#         increase_hero_level(team1_hero)
#     elif num_soldiers_team2 > num_soldiers_team1:
#         increase_hero_level(team2_hero)
#     else:
#         print("Teams have equal number of soldiers.")

# num_soldiers_team1 = random.randint(5, 15)
# num_soldiers_team2 = random.randint(5, 15)

# team1_soldiers = generate_soldiers(num_soldiers_team1, 1)
# team2_soldiers = generate_soldiers(num_soldiers_team2, 2)

# team1_hero = Hero('Spiderman', 1)
# team2_hero = Hero('Batman', 2)

# print(f"Team 1 has {num_soldiers_team1} soldiers.")
# print(f"Team 2 has {num_soldiers_team2} soldiers.")

# compare_teams(team1_soldiers, team2_soldiers, team1_hero, team2_hero)
