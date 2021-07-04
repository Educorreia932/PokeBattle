from .enums import Mode

class Input:
    def __init__(self, move):
        if move == "Growl":
            self.mode = Mode.ASCII

        elif move == "Lear":
            self.mode = Mode.INTEGER