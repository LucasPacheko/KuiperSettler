class Weapon:
    def __init__(self, name, damage, range_, fire_rate):
        self.name = name
        self.damage = damage
        self.range = range_
        self.fire_rate = fire_rate

    def __str__(self):
        return f"Weapon: {self.name}\nDamage: {self.damage}\nRange: {self.range}\nFire Rate: {self.fire_rate} shots per second"
# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma instância de Weapon
    rifle = Weapon("Rifle", damage=20, range_=100, fire_rate=5)

    # Exibindo os atributos da arma
    print(rifle)