from plum import dispatch
from .commands.program import Program
from .commands.pokemon_list import PokemonList

class PokeBattleInterpreter:
    trainers_pokemon = {}

    @dispatch
    def interpret(self, program: Program):
        for pokemon_list in program.trainers.pokemon_lists:
            self.interpret(pokemon_list)

    @dispatch
    def interpret(self, pokemon_list: PokemonList):
        trainer_pokemon = []

        for pokemon in pokemon_list.pokemon:
            trainer_pokemon.append({pokemon: 5})

        print(trainer_pokemon)

        self.trainers_pokemon[pokemon_list.trainer] = trainer_pokemon
