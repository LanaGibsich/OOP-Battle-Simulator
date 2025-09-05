from enemy import Enemy
import random
class Boss(Enemy):
    def __init__(self, name, color):
        self.health = 1000
        self.color = color
        self.attack_power = random.randint(50, 150)
    def take_damage(self, damage):
        print("I WILL ALWAYS WIN YOU LOSER!!!")
        return super().take_damge(damage)