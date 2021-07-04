from src.models.mode import Mode


class Pokemon:
    def __init__(self, name, trainer):
        self.name = name
        self.trainer = trainer
        self.hp = 5

    @property
    def opposing_pokemon(self):
        return self.trainer.opponent.active_pokemon

    def deal_damage(self, level):
        self.opposing_pokemon.hp -= level

    def deal_math_damage(self):
        self.opposing_pokemon.hp -= self.hp

    def knockout(self):
        self.opposing_pokemon.hp = 0

    def heal(self, level):
        self.hp += level

    def leech(self):
        self.heal(self.opposing_pokemon.hp)

    def sync(self):
        self.hp = self.opposing_pokemon.hp

    def print(self, mode):
        if mode == Mode.ASCII:
            print(chr(self.hp), end="")

        elif mode == Mode.INTEGER:
            print(self.hp, end="")

    def input(self, mode):
        if mode == Mode.ASCII:
            self.hp = chr(int(input()))

        elif mode == Mode.INTEGER:
            self.hp = int(input())

    def __repr__(self):
        return f"<{self.name}: {self.hp}>"


