import random

def dice_sum(num_dice: int = 1, sides: int = 6):
    """returns the sum of num_dice dice, each with side sides"""
    return sum(random.randint(1, sides) for _ in range(num_dice))

class Character:

    def __init__(self, name : str, skill: int, stamina : int):
        self.name = name.title()
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None

    def __repr__(self):
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"

    def __str__(self):
        return self.name

    @property
    def is_dead(self):
        return self.stamina <= 0

    @is_dead.setter
    def is_dead(self, dead: bool):
        if dead:
            self.stamina = 0
        else:
            self.stamina = max(self.stamina, 1)

    def return_character_status(self):
        return f"{self.name} has skill {self.skill} and stamina {self.stamina}"

    def return_roll_status(self):
        return f"{self.name} rolled {self.roll} for a total score of {self.score}"

    def find_score(self):
        self.roll = dice_sum(2)
        self.score = self.roll + self.skill
        print(self.return_roll_status())
        return self.score

    def take_hit(self, damage=2):
        self.stamina = max(0, self.stamina-damage)

    def fight_round(self, other):
        self.find_score()
        other.find_score()
        match [self.score > other.score, self.score == other.score]:
            case [True, False]:
                print(f"{self.name} has scored a hit! {self.name} takes 2 damage!")
                other.take_hit()
                return "Win"
            case [False, True]:
                print(f"It is a draw! {self.name} and {other.name} both take 1 damage")
                self.take_hit(1)
                other.take_hit(1)
                return "Draw"
            case [False, False]:
                print(f"{other.name} has scored a hit! {self.name} takes 2 damage!")
                self.take_hit()
                return "lost"
        return None


class PlayerCharacter(Character):

    def __init__(self, name, skill, stamina, luck):
        super().__init__(name, skill, stamina)
        self.luck = luck

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', skill={self.skill}, stamina={self.stamina}, luck={self.luck})"

    def test_luck(self):
        self.luck -= 1
        self.roll = dice_sum(2)
        return self.roll <= self.luck+1

    @classmethod
    def generate_player_character(cls, name):
        skill = 6 + dice_sum()
        stamina = 12 + dice_sum(2)
        luck = 6 + dice_sum()
        return cls(name, skill, stamina, luck)

def NonPlayerCharacter(Character):
    pass

class Game:
    @classmethod
    def load_creatures(cls):
        creatures = [Character("Dragon", 10, 22),
                     Character("Orc", 7, 10),
                     Character("Skeleton", 5, 8),
                     Character("Giant Rat", 6, 6),
                     ]
        return creatures

    def __init__(self):
        self.opponent = None
        self.player = None
        self.round_result = None
        self.creatures = self.load_creatures()

    def choose_opponent(self):
        self.opponent = random.choice(self.creatures)
        self.creatures.remove(self.opponent)

    def set_player(self, player_character):
        self.player = player_character

    def resolve_fight_round(self):
        self.round_result = self.player.fight_round(self.opponent)

    def return_character_status(self, character):
        name, skill, stamina = character.name, character.skill, character.stamina
        return f"{name} has skill {skill} and stamina {stamina}"

hero = PlayerCharacter.generate_player_character("Hero")
dragon = Character("Dragon", 10, 10)

game = Game()
game.choose_opponent()

"""
while hero.stamina > 0 and dragon.stamina > 0:
    hero.fight_round(dragon)
winner = [hero, dragon][hero.stamina == 0].name
print(f"{winner} wins!")
print(f"Result\n{hero.name}: {hero.stamina}\n{dragon.name}: {dragon.stamina}")
"""
