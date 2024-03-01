import random
class Entity:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.integrity = health
        self.attack_power = [weapon.damage for weapon in self.weapons.values()]

    def attack(self, target):
        damage = random.randint(0, self.attack_power)
        target.health -= damage
        print(f"{self.name} ataca {target.name} causando {damage} de dano.")
        if target.health <= 0:
            print(f"{target.name} foi derrotado!")

# Criando duas entidades para o combate
entity1 = Entity("Guerreiro 1", health=100, attack_power=20)
entity2 = Entity("Guerreiro 2", health=100, attack_power=20)

# Simulando o combate até que uma das entidades seja derrotada
rounds = 1
while entity1.health > 0 and entity2.health > 0:
    print(f"Rodada {rounds}:")
    entity1.attack(entity2)
    if entity2.health <= 0:
        break
    entity2.attack(entity1)
    rounds += 1
