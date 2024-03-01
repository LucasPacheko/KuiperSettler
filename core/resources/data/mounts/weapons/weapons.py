class Turret:
    def __init__(self, name, size, rpm, damage, range_):
        self.name = name
        self.size = size
        self.rpm = rpm
        self.damage = damage
        self.range = range_

    def __str__(self):
        return f"{self.name} ({self.size})\nRPM: {self.rpm}\nDamage: {self.damage}\nRange: {self.range}m"

class Weapon:
    def __init__(self, name, size, dps, range_, draw):
        self.name = name
        self.size = size
        self.dps = dps
        self.range = range_
        self.draw = draw

    def __str__(self):
        return f"{self.name} ({self.size})\nDPS: {self.dps}\nRange: {self.range}m\nDraw: {self.draw}MW"

# Exemplo de uso
light_gravel_turret = Turret("Light Gravel Turret", "Small and large grid", 500, 10, 700)
heavy_gravel_turret = Turret("Heavy Gravel Turret", "Large grid", 10, 1500, 1000)
clg_autocannon = Turret("CLG Autocannon", "Large grid turret", 200, 150, 1000)
cannon_155mm = Turret("155mm Cannon", "Small grid turret and fixed-mount, large grid turret", 15, "5000 AP dmg, 7500 DUAP dmg, 5000 HE dmg", 2000)
cannon_305mm = Turret("305mm Cannon", "Small grid fixed-mount, large grid turret and twin turret", 15, "15000 AP dmg, 22500 DUAP dmg, 15000 HE dmg", 3500)
coilgun = Turret("Coilgun", "Large grid turret and fixed-mount", 8, "45000 AP dmg, 67500 DUAP dmg", 10000)
pd_laser = Weapon("PD Laser", "Large and small grid turret", 60, 500, "1MW draw")
light_laser = Weapon("Light Laser", "Large grid turret, small grid turret and fixed-mount", 1500, 1500, "15MW draw")
heavy_laser = Weapon("Heavy Laser", "Large grid turret and fixed-mount", "3600 dps (fixed), 7200 dps (turret)", 2500, "25MW draw (fixed), 50MW draw (turret)")

# Exibindo as informações das torretas e armas
print(light_gravel_turret)
print(heavy_gravel_turret)
print(clg_autocannon)
print(cannon_155mm)
print(cannon_305mm)
print(coilgun)
print(pd_laser)
print(light_laser)
print(heavy_laser)
