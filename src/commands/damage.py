class Damage:
    def __init__(self, move):
        if move in ["Tackle", "Ember", "Vine Whip", "Water Gun", "Thunder Shock", "Rock Throw", "Confusion", "Mach Punch", "Wing Attack", "Powder Snow"]:
            self.level = 2