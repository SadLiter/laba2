from abc import ABC, abstractmethod

class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass

class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

class GameObject:
    def __init__(self, obj_id, name, x, y):
        self._id = obj_id
        self._name = name
        self._x = x
        self._y = y
    
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

class Unit(GameObject):
    def __init__(self, obj_id, name, x, y, hp):
        super().__init__(obj_id, name, x, y)
        self._hp = hp
        self._alive = True

    def is_alive(self):
        return self._alive
    
    def get_hp(self):
        return self._hp
    
    def receive_damage(self, damage):
        if self._alive:
            self._hp -= damage
            if self._hp <= 0:
                self._alive = False

class Archer(Unit, Attacker, Moveable):
    def __init__(self, obj_id, name, x, y, hp, attack_power):
        super().__init__(obj_id, name, x, y, hp)
        self._attack_power = attack_power

    def attack(self, unit):
        if self.is_alive():
            print(f"{self.get_name()} attacks {unit.get_name()} for {self._attack_power} damage!")
            unit.receive_damage(self._attack_power)

    def move(self, dx, dy):
        self._x += dx
        self._y += dy
        print(f"{self.get_name()} moved to ({self.get_x()}, {self.get_y()})")

class Building(GameObject):
    def __init__(self, obj_id, name, x, y):
        super().__init__(obj_id, name, x, y)
        self._built = False

    def is_built(self):
        return self._built


class Fort(Building, Attacker):
    def __init__(self, obj_id, name, x, y, attack_power):
        super().__init__(obj_id, name, x, y)
        self._attack_power = attack_power

    def attack(self, unit):
        if self.is_built():
            print(f"{self.get_name()} fires at {unit.get_name()} for {self._attack_power} damage!")
            unit.receive_damage(self._attack_power)


class MobileHouse(Building, Moveable):
    def move(self, dx, dy):
        self._x += dx
        self._y += dy
        print(f"{self.get_name()} moved to ({self.get_x()}, {self.get_y()})")


# Пример использования
archer = Archer(1, "Arch", 5, 10, 25, 50)
enemy_unit = Unit(2, "Enemy", 5, 6, 50)

archer.attack(enemy_unit)
archer.move(10, 10)

fort = Fort(3, "Fort", 10, 10, 30)
fort.attack(enemy_unit)

mobile_house = MobileHouse(4, "Mobile House", 2, 5)
mobile_house.move(10, 10)