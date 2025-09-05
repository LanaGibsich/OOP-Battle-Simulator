from enemy import Enemy

class baby_elf(Enemy):
    def cry():
        print("Wahh Wahh")

    def take_damage(self, damage):
        print("Why are you attacking a baby, YOU MONSTER!!!")
        return super().take_damge(damage)