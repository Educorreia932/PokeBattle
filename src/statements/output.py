from src.models.mode import Mode


class Output:
    def __init__(self, pokemon, move):
        self.pokemon = pokemon

        if move == "Swords Dance":
            self.mode = Mode.ASCII

        elif move == "Barrier":
            self.mode = Mode.INTEGER
