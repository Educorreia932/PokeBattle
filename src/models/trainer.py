from src.models.pokemon import Pokemon


class Trainer:
    _active_pokemon: Pokemon

    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = {p: Pokemon(p, self) for p in pokemon}
        
    @property
    def active_pokemon(self):
        return self._active_pokemon

    @active_pokemon.setter
    def active_pokemon(self, value):
        self._active_pokemon = self.pokemon[value]
