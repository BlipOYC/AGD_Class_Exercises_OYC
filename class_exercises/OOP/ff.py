import random
from time import sleep
p = print

def print(txt, end="\n"):
    for char in txt:
        p(char, end='')
        sleep(0.025)
    p("", end=end)
    
print("Before we begin, on a scale from 0 to 10, how fast would you like the text speed to be: ", end="")
while True:
    try:
        choice = float(input())
        sleep_time = 0.1 - (0.01 * choice)
        def print(txt, end="\n"):
            for char in txt:
                p(char, end='')
                sleep(sleep_time)
            p("", end=end)
        print("Is this ok? (Y for yes, anything else for no) ", end="")
        if input().lower() == "y":
            print("Great\n\n")
            break
        else:
            print("How fast would you like the text speed to be? ", end="")
    except:
        print("Invalid option, please enter a numerical answer")


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

    def take_hit(self, damage=2, c=True):
        crit = False
        if isinstance(self, PlayerCharacter) and c:
            crit = random.randint(1, 100) <= self.luck
            print(f"{self.name} has been crit for double damage!")
            print(f"{self.name} now takes {damage} damage!")
        if crit:
            damage *= 2
        self.stamina = max(0, self.stamina-damage)

    def fight_round(self, other):
        self.find_score()
        other.find_score()
        match [self.score > other.score, self.score == other.score]:
            case [True, False]:
                other.take_hit()
                return "Win"
            case [False, True]:
                self.take_hit(1, c=False)
                other.take_hit(1, c=False)
                return "Draw"
            case [False, False]:
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

    def resolve_fight_round(self, flee):
        print("Would you like to flee? (Y for yes, anything else for no): ", end="")
        fleeing = input()
        if fleeing.lower() == "y":
            flee = True
            return f"You have fled the battle against {self.opponent.name}."
        self.round_result = self.player.fight_round(self.opponent)

    @staticmethod
    def return_character_status(character):
        name, skill, stamina = character.name, character.skill, character.stamina
        return f"{name} has skill {skill} and stamina {stamina}"

    def return_round_result(self, other, result):
        msg = self.player.return_roll_status() + "\n" + self.opponent.return_roll_status()
        if result == "Win":
            msg += f"{self.player.name} has scored a hit! {self.opponent.name} takes 2 damage!"
        if result == "Draw":
            msg += f"It is a draw! {self.player.name} and {self.opponent.name} both take 1 damage"
        if result == "lost":
            msg += f"{self.opponent.name} has scored a hit! {self.player.name} takes 2 damage!"
        return msg

class GameCLI:
    def __init__(self):
        self.game = Game()
        self.run_game()
        self.flee = False

    def run_game(self):
        print("Welcome to Fighting Fantasy. What is your name?\nName: ", end="")
        self.game.set_player(PlayerCharacter.generate_player_character(input()))
        print(f"Hello, esteemed {self.game.player.name}.")
        print(self.game.return_character_status(self.game.player))
        self.fight_battle()

    def fight_opponent(self):
        holder = self.game.resolve_fight_round(self.game.opponent)
        if holder:
            print(holder)
            self.game.opponent.is_dead(True)
            return
        print("Would you like to see the status of yourself, your opponent, or neither?")
        print("(Y for yourself, O for opponent, anything else for neither): ", end="")
        see_status = input()
        if see_status.lower() == "y":
            print(game.return_character_status(self.game.player))
        elif see_status.lower() == "o":
            print(game.return_character_status(self.game.opponent))
    
    def fight_battle(self):
        self.flee = False
        while True:
            self.game.choose_opponent()
            print(f"You will be fighting {self.game.opponent.name}.")
            print(self.game.return_character_status(self.game.opponent))
            while self.game.player.stamina > 0 and self.game.opponent.stamina > 0:
                print(self.game.return_round_result(self.fight_opponent()))
            if self.flee:
                continue
            else:
                print(f"You have defeated {game.opponent.name}!\n\n")
                self.game.player.stamina += 6
                print("You have regained some stamina!")


if __name__ == "__main__":
    GameCLI()

"""
while hero.stamina > 0 and dragon.stamina > 0:
    hero.fight_round(dragon)
winner = [hero, dragon][hero.stamina == 0].name
print(f"{winner} wins!")
print(f"Result\n{hero.name}: {hero.stamina}\n{dragon.name}: {dragon.stamina}")
"""
