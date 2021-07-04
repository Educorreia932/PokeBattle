from .enums import IOType

class Output:
    def __init__(self, move):
        if move == "Swords Dance":
            self.io_type = IOType.ASCII

        elif move == "Barrier":
            self.io_type = IOType.INTEGER
