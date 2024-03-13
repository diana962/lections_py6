class Account:
    def __init__(self, group, FIO, adress, amount_of_people, apartment_square, history):
        self.group = group
        self.FIO = FIO
        self.adress = adress
        self.amount_of_people = amount_of_people
        self.apartment_square = apartment_square
        self.history = history
    # def group_direction(self):


class Bishkek_Teploset:
    # Проблема: брать данные с лицевого счета. Нужно получить доступ к базе данных каждого из этих сфер.
    '''
    # Какие данные нам необходимо от них получить?
    0. Определить группы потребителей: Население (*), Промышленность(**), Бюджетные потребители(**), Прочие потребители(**)
    1. ФИО: Учугенова Б.
    2. Адрес: 7 мкр 37 д 56 кв # Отсюда можно определить район филиала, который собирает данные
    3. Колличество людей, прописанных в доме: 
    4. Площадь жилья: 
    5. История платежа (Наличие долгов + начисляемая пеня): 
    '''

    # не хватает добавить пени и долг, а также тарифы для разних предприятий

    '''Оплата за горячую воду и отопление'''
    measurement_unit_heating = 'Гкал' #гигакалория
    measurement_unit_hot_water = 'куб. м'
    limit_for_using_heating = 2.0790 # лимит 2 Гкал в использовании отопления по договору
    limit_for_using_hot_water = 24 # лимит 24 куб. м в использовании горячей воды по договору
    tariff_heating = 1248 #som
    tariff_hot_water = 72 #som по счетчику за литр

    tariff_service_heating = 1 # 1 som/ m2
    tariff_service_hot_water = 0.50 # 0.50 som/m2    

    '''Информация о площади квартиры должна определено хранится на лицевом счете.'''
    apartment_square = 71.50 # m2     !!!! 

    service_heating = tariff_service_heating * apartment_square
    service_hot_water = tariff_service_hot_water * apartment_square

    def metter_pay(self, fact_used_heating, fact_used_hot_water):
        '''Фактически затраченные ресурсы приходят с показанием счетчика'''
        '''Необходимо для этого встроить чип в умный счетчик, который в режиме реального времени будет показывать показания горячей воды. Что касается отопления: я без понятия!'''
        self.fact_used_heating = fact_used_heating
        self.fact_used_hot_water = fact_used_hot_water

        if self.fact_used_heating < Bishkek_Teploset.limit_for_using_heating:
            total_heating = round(self.fact_used_heating * Bishkek_Teploset.tariff_heating + Bishkek_Teploset.service_heating, 2)
        else:
            raise ValueError ('Вам заблокировали подачу отопления, так как вы превысили лимит, установленный в договоре.')


        if self.fact_used_hot_water < Bishkek_Teploset.limit_for_using_hot_water:
            total_hot_water = round(self.fact_used_hot_water * Bishkek_Teploset.tariff_hot_water + Bishkek_Teploset.service_hot_water, 2)
        else:
            raise ValueError ('Вам заблокировали подачу горячей воды, так как вы превысили лимит, установленный в договоре.')
        
        total_amount = round(total_heating + total_hot_water, 2)

        print(f'For Heating to pay: {total_heating}\nFor Hot Water to pay: {total_hot_water}\nTotal amount: {total_amount}.')
    


    def fixed_pay(self, count_of_people):
        tariff_hot_water_per_person = 345 #som
        hot_water_check = count_of_people *tariff_hot_water_per_person
        print (f'With fixed price for Hot Water to pay: {hot_water_check} som')

    

print('---------------------------------------')
obj = Bishkek_Teploset()
obj.metter_pay(1.6116, 2) # Примерно взятые данные за 2 человека
# fact_used_heating = 1.6116 # Гкал   !!!!
# fact_used_hot_water = 2 # куб. м    !!!!
print('---------------------------------------')
obj.fixed_pay(2)







print('---------------------------------------')
class Gasprom:
    tariff_gas = 19.93416 #som/m3
    history_old_value = 4320 # metter
    def __init__(self, new_value):
        self.new_value = new_value
    
    def to_pay(self):
        total = round((self.new_value - self.history_old_value) * self.tariff_gas, 2)
        return f'For gas to pay: {total} som'

gas = Gasprom(4323)
print(gas.to_pay())

print('---------------------------------------')

class BischkekVodoKanal:
    tariff_cold_water_per_person = 98.53
    cold_water_effluent = 32.53
    hot_water_effluent = 16.79
    service = 1.26 # на 1m2
    apartment_square = 60.80

    total = tariff_cold_water_per_person + cold_water_effluent + hot_water_effluent + (service * apartment_square)

    def __init__(self, amount_of_people):
        self.amount_of_people = amount_of_people
    
    def to_pay(self):
        total_to_pay = round(self.amount_of_people * BischkekVodoKanal.total, 2)
        return f'For Cold Water to pay: {total_to_pay} som.'
    
cold = BischkekVodoKanal(4)
print(cold.to_pay())

print('---------------------------------------')

class Tasalyk:
    tariff = 41
    def __init__(self):
        pass
    def to_pay(self, amount_of_people):
        self.amount_of_people = amount_of_people
        total = amount_of_people * Tasalyk.tariff
        return f'For Garbage-Removal to pay: {total} som.'
        
garbage = Tasalyk()
print(garbage.to_pay(2))

print('---------------------------------------')
class BischkekGorLift:
    tariff = 3.12 #som/m2
    def to_pay(self, apartment_square):
        self.apartment_square = apartment_square
        return f'For Lift to pay: {self.apartment_square * BischkekGorLift.tariff}'

lift = BischkekGorLift()
print(lift.to_pay(60.80))

print('---------------------------------------')

class Domofon:
    fix_price =  50
    print(f'For Domofon to pay: {fix_price} som')

domofon = Domofon()

print('---------------------------------------')

    



