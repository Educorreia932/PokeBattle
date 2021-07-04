from .enums import Mode

class Output:
    def __init__(self, move):
        if move == "Swords Dance":
            self.mode = Mode.ASCII

        elif move == "Barrier":
            self.mode = Mode.INTEGER
