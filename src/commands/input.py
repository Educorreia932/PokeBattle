from .enums import IOType

def Input():
    def __init__(self, move):
        if move == "Growl":
            self.io_type = IOType.ASCII

        elif move == "Lear":
            self.io_type = IOType.INTEGER