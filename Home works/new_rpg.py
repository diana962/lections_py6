from abc import ABC, abstractmethod
from random import choice, randint
from enum import Enum

class Element(Enum):
    FIRE = 1
    AIR = 2
    EARTH = 3
    WATER = 4

class Locations(Enum):
    HOME = 0
    VILLAGE = 1
    FROZEN = 2
    CASTLE = 3
    HALL = 4
    PARADISE = 5


class Weapons(Enum):
    SWORD = 1
    AXE = 2
    BOW = 3
    STAFF = 4
    DAGGER = 5
    POTION_HEAL = 6
    POTION_MANA = 7
    SHIELD = 8
    ARMOR = 9
    MAGIC_WAND = 10
    CROSSBOW = 11
    HAMMER = 12
    SPEAR = 13
    TRIDENT = 14
    FLAIL = 15
    GREATSWORD = 16
    THROWING_KNIVES = 17
    HOLY_WATER = 18
    FIREBALL_SCROLL = 19
    ICE_STAFF = 20
    LIGHTNING_ROD = 21
    POISON_DAGGER = 22
    MAGIC_ARMOR = 23
    TELEPORTATION_RING = 24
    INVISIBILITY_CLOAK = 25
    CHAINMAIL = 26
    WAND_OF_SUMMONING = 27
    AMULET_OF_PROTECTION = 28
    SCYTHE = 29
    WHIP = 30
    HEALING_STONE = 31
    SPELLBOOK = 32
    CURSED_RING = 33
    FROSTBITE_GAUNTLET = 34
    VAMPIRIC_DAGGER = 35
    THUNDER_HAMMER = 36
    SHADOW_CLOAK = 37
    RUNE_SWORD = 38
    DEMONIC_STAFF = 39
    DRAGONSCALE_ARMOR = 40
    TIME_WARP_ORB = 41
    PHOENIX_FEATHER = 42
    NECROMANCER_ROBE = 43
    ANGELIC_SHIELD = 44
    WIZARD_HAT = 45
    SCEPTER_OF_COMMAND = 46
    ETHEREAL_BLADE = 47
    BLOOD_SWORD = 48
    VOID_STAFF = 49
    SHATTERED_SHIELD = 50
    ELVEN_BOW = 51
    ANCIENT_TOME = 52
    LUNAR_SCEPTER = 53
    CORRUPTED_AMULET = 54
    SOUL_REAPER_SCYTHE = 55


class GameEntity:
    def __init__(self, name, health, damage):
        self.__health = health
        self.__name = name
        self.__damage = damage
    
    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health  
    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage
    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self) -> str:
        return f'name: {self.name}, health: {self.health}, damage: {self.damage}'

class Player(GameEntity):
    def __init__(self, name, health, damage, element):
        super().__init__(name, health, damage)
        self.element = [Element(element.value)]
        self.inventory = [Weapons.SWORD, Weapons.POTION_HEAL,Weapons.POTION_HEAL,Weapons.POTION_HEAL,Weapons.POTION_HEAL]  

    def use_item(self, item):
        if item in self.inventory:
            if item == Weapons.POTION_HEAL:
                self.health += 50  
                self.inventory.remove(item)
                print("Вы использовали зелье лечения и восстановили 50 здоровья.")
            elif item == Weapons.POTION_MANA:
                
                self.inventory.remove(item)
                print("Вы использовали зелье маны и восстановили ману.")
            else:
                print("Этот предмет нельзя использовать в бою.")
        else:
            print("У вас нет этого предмета.")

    def attack(self, monsters):
        for monster in monsters:
            if monster.health > 0:
                monster.health = monster.health - self.damage

    def add_elem(self, elem):
        self.element.append(elem)

    def add_weapon(self, weapon):
        self.inventory.append(weapon)

    def __str__(self) -> str:
        return super().__str__() + f', elements: FIRE'    


class Monster(GameEntity):
    def __init__(self, name, health, damage, weaknesses=None):
        super().__init__(name, health, damage)
        self.__weaknesses = weaknesses or []

    @property
    def weaknesses(self):
        return self.__weaknesses
    
    def attack(self, player):
        player.health -= self.damage


class Location:
    def __init__(self, name, location, is_open):
        self.__name = name
        self.__location = location
        self.__is_open = is_open
    
    @property
    def name(self):
        return self.__name
    
    @property
    def location(self):
        return self.__location
    
    @property
    def is_open(self):
        return self.__is_open
        
    def open_door(self, new_val):
        if new_val:
            self.__is_open = True

    def explore(self, player):
       
        event_chance = randint(1, 10)  
        if event_chance <= 3: 
            print("Вы нашли сундук с сокровищами!")
            
            item_found = choice(list(Weapons))
            player.inventory.append(item_found)
            print(f"Вы нашли {item_found} и добавили его в инвентарь.")
        elif event_chance <= 6: 
            print("Вы наткнулись на ловушку!")
            
            damage = randint(10, 30)
            player.health -= damage
            print(f"Вы потеряли {damage} здоровья.")
        else:
            print("Вы не нашли ничего особенного в этой локации.")
    

    def __str__(self):
        return f'Name: {self.name}'


def create_locations():
    village = Location('The StratHolm village', Locations.VILLAGE, True)
    frozen = Location('The Forest', Locations.FROZEN, False)
    castle = Location('The Anarbek Castle', Locations.CASTLE, False)
    hall = Location('HALL', Locations.HALL, False)
    paradise = Location('PARADISE', Locations.PARADISE, False)

    return [village, frozen, castle, hall, paradise]

def create_village_monsters():
    monsters = []
    healt = 5
    for _ in range(10):
        zombie = Monster('zomb', 50+ healt , 20, [Weapons.SWORD])
        monsters.append(zombie)
        healt += 5

    boss = Monster('Butcher', 500, 50, [Element.FIRE])
    monsters.append(boss)

    return monsters


def is_game_finished(monsters, player):
    if player.health <= 0:
        print('ПОБЕДА ПРОТИВНИКОВ!!!')
        print('Вас ОТЫМЕЛИ')
        return True
    
    all_monsters_dead = True
    for monster in monsters:
        if monster.health > 0:
            all_monsters_dead = False
            break
            
    if all_monsters_dead:
        print('ДЕРЕВНЯ ПРОЙДЕНА!!!')
        return True 
    
    return False


def choose_loc(locations, choose_location):
    for loc in locations:
        print(loc)
        if loc.location.value == choose_location and loc.is_open:
            print('Попедите вонючих нежитей которые напали на деревню!')
            print('я слышал они боятся огня \n надеюсь ты выбрал магию огня а то придется туго')
            print('не дай им себя отыметь')
            return loc
        else: 
            print('локация пока не открыта, пройдите прошлую локацию')


def choose_element(choose_magic):
    for elem in Element:
        if elem.value == choose_magic:
            return elem


round_number = 0
def print_statistics(player, enemies):
    global round_number
    round_number += 1
    print('_______________________'+ ' ROUND ' + str(round_number) + ' ________________________')
    print(player)
    for enemy in enemies:
        print(enemy)


def start():
    name = input('write your name: ')
    print("""
Приветствую, искатель приключений!

На континенте Этерналия раскинулись земли,
окутанные древней магией и обители, пронизанные тайнами. 
Здесь, под небом, пропитанным магическим светом, 
развернулась вечная борьба между светом и тьмой, 
где силы зла стремятся поглотить мир, а храбрые
души встают на защиту беспристрашно.

прими свой первый квест и спаси жену торговца Лизу
            """)

    choose_magic = int(input("""выбери магию:
1 - Огонь
2 - Вода
3 - Земля
4 - Вода
                          """))
    print('1 - choose location ')
    option = int(input('choose option: '))
    if option == 1:
        print('1 - VILLAGE')
        print('2 - Frozen')
        print('3 - CASTLE')
        print('4 - HALL')
        print('5 - PARADISE')
        choose_location = int(input('choose location: '))

    locations = create_locations()
    locating = choose_loc(locations, choose_location)
    
    player = Player(name, 500, 30, choose_element(choose_magic)) 
    if locating != Locations.VILLAGE:
        start_passing_village_location(player, locations)


def start_passing_village_location(player, on_loc):
    monsters = create_village_monsters()
    print_statistics(player, monsters)
    while not is_game_finished(monsters, player):
        print("Что вы хотите сделать?")
        print("1. Атаковать монстров")
        print("2. Использовать предмет")
        print("3. Исследовать локацию")
        choice = int(input("Выберите действие: "))

        if choice == 1:
            player.attack(monsters)
            for monster in monsters:
                monster.attack(player)
            print_statistics(player, monsters)
        elif choice == 2:
            print("Ваш инвентарь:", player.inventory)
            item_choice = int(input("Выберите предмет для использования (введите номер): "))
            if 1 <= item_choice <= len(player.inventory):
                player.use_item(player.inventory[item_choice - 1])
            else:
                print("Некорректный выбор.")
        elif choice == 3:
            on_loc.explore(player)
            print_statistics(player, monsters)


start()
