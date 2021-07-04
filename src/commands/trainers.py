class Trainers:
    trainers = {}

    def __init__(self, trainer_1_name, trainer_1_pokemon, trainer_2_name, trainer_2_pokemon):
        self.trainers[trainer_1_name] = trainer_1_pokemon
        self.trainers[trainer_2_name] = trainer_2_pokemon
        