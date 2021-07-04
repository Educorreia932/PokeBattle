from src.models.mode import Mode


class Input:
    def __init__(self, pokemon, move):
        self.pokemon = pokemon

        if move == "Growl":
            self.mode = Mode.ASCII

        elif move == "Lear":
            self.mode = Mode.INTEGER
