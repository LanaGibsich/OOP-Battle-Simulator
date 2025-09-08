from enemy import Enemy
import random
class Boss(Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        self.health = 1000
        self.color = color
        self.attack_power = random.randint(50, 150)

    def take_damage(self, damage):
        print("I WILL ALWAYS WIN YOU LOSER!!!")
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")