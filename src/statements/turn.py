class Turn:
    def __init__(self, turn_no, *commands):
        self.turn_no = turn_no
        self.commands = tuple(filter(lambda x: x[1] is not None, commands))
