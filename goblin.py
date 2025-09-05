import random
from enemy import Enemy

class Goblin(Enemy):
    """
    This is our goblin blueprint 
    """
    def __init__(self, name, color):
        super()._init(name)
        self.color = color