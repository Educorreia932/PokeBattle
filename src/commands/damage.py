class Damage:
    def __init__(self, move, effectiveness = None):
        if move in ["Tackle", "Ember", "Vine Whip", "Water Gun", "Thunder Shock", "Rock Throw", "Confusion", "Mach Punch", "Wing Attack", "Powder Snow"]:
            self.level = 2

        elif move in ["Body Slam", "Flamethrower", "Razor Leaf", "Hydro Pump", "Thunderbolt", "Earthquake", "Psychic", "High Jump Kick", "Fly", "Ice Beam"]:
            self.level = 4

        if effectiveness is not None:
            self.level *= effectiveness.multiplier
        