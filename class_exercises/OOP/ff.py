import random
def dice_sum(num_dice: int = 1, sides: int = 6):
    return sum(random.randint(1, sides) for _ in range(num_dice))
print(dice_sum(12))