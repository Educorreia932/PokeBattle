class Turn:
    def __init__(self, turn_no, *commands):
        self.turn_no = turn_no
        self.commands = commands


    def __str__(self):
        return f"TURN {turn_no}"