
import random
class Ship:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapons = {}
        self.mounting = {}
        self.cargo = {}
    def install_weapons(self, weapon):
        self.weapons[weapon.name] = weapon
        self.mounting[weapon.name] = 0
    def attack(self, target):
        
        damage = random.randint(0, self.attack_power)
        target.health -= damage
        print(f"{self.name} ataca {target.name} causando {damage} de dano.")
        if target.health <= 0:
            print(f"{target.name} foi derrotado!")