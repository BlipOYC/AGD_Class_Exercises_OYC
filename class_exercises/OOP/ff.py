import random

def dice_sum(num_dice: int = 1, sides: int = 6):
    """returns the sum of num_dice dice, each with side sides"""
    return sum(random.randint(1, sides) for _ in range(num_dice))


class Character:

    def __init__(self, name : str, skill: int, stamina : int):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None

    def __repr__(self):
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"

    def find_score(self):
        self.roll = dice_sum(2)
        self.score = self.roll + self.skill
        return self.score

dragon = Character("Dragon", 10, 22)
print(dragon)