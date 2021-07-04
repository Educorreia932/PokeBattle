from plum import dispatch
from .commands.enums import Mode
from .commands.program import Program
from .commands.pokemon_list import PokemonList
from .commands.go_pokemon import GoPokemon
from .commands.turn import Turn
from .commands.damage import Damage
from .commands.math_damage import MathDamage
from .commands.ohko import OHKO
from .commands.heal import Heal
from .commands.leech import Leech
from .commands.sync import Sync
from .commands.switch import Switch
from .commands.status import Status
from .commands.output import Output
from .commands.input import Input

class PokeBattleInterpreter:
    trainers_pokemon = {}
    active_pokemon = {}

    @dispatch
    def interpret(self, program: Program):
        self.player = program.trainers.pokemon_lists[0].trainer
        self.adversary = program.trainers.pokemon_lists[1].trainer

        for pokemon_list in program.trainers.pokemon_lists:
            self.interpret(pokemon_list)

        for go_pokemon in program.battle.starter_pokemon:
            self.interpret(go_pokemon)

        for turn in program.battle.turns:
            self.interpret(turn)

    @dispatch
    def interpret(self, pokemon_list: PokemonList):
        trainer_pokemon = {}

        for pokemon in pokemon_list.pokemon:
            trainer_pokemon[pokemon] = 5

        self.trainers_pokemon[pokemon_list.trainer] = trainer_pokemon

    @dispatch
    def interpret(self, go_pokemon: GoPokemon):
        self.active_pokemon[go_pokemon.trainer] = go_pokemon.pokemon

    @dispatch
    def interpret(self, turn: Turn):
        for command in turn.commands:
            self.interpret(command[1])

    @dispatch
    def interpret(self, damage: Damage):
        health = self.get_pokemon_health(self.player, self.active_pokemon[self.player]) - damage.level
        self.set_pokemon_health(self.player, self.active_pokemon[self.player], health)

    @dispatch
    def interpret(self, math_damage: MathDamage):
        player_health = self.get_pokemon_health(self.player, self.active_pokemon[self.player])
        adversary_health = self.get_pokemon_health(self.adversary, self.active_pokemon[self.adversary])
        health = adversary_health - player_health
        self.set_pokemon_health(self.adversary, self.active_pokemon[adversary], health)

    @dispatch
    def interpret(self, ohko: OHKO):
        self.set_pokemon_health(self.adversary, self.active_pokemon[adversary], 0)

    @dispatch
    def interpret(self, heal: Heal):
        self.trainers_pokemon[self.active_pokemon[self.player]] += heal.level

    @dispatch
    def interpret(self, leech: Leech):
        adversary_health = self.get_pokemon_health(self.adversary, self.active_pokemon[self.adversary])
        health = self.get_pokemon_health(self.player, self.active_pokemon[self.player]) + adversary_health
        self.set_pokemon_health(self.player, self.active_pokemon[self.player], health)

    @dispatch
    def interpret(self, sync: Sync):
        adversary_health = self.get_pokemon_health(self.adversary, self.active_pokemon[self.adversary])
        self.set_pokemon_health(self.player, self.active_pokemon[self.player], adversary_health)

    @dispatch
    def interpret(self, switch: Switch):
        self.active_pokemon[switch.trainer] = switch.new_pokemon

    @dispatch
    def interpret(self, status: Status):
        pass

    @dispatch
    def interpret(self, output: Output):
        if output.mode == Mode.ASCII:
            print(self.get_pokemon_health(self.player, self.active_pokemon[self.player]))

        elif output.mode == Mode.INTEGER:
            print(self.get_pokemon_health(self.player, self.active_pokemon[self.player]))

    @dispatch
    def interpret(self, input: Input):
        pass

    def set_pokemon_health(self, trainer, pokemon, health):
        self.trainers_pokemon[trainer][self.active_pokemon[trainer]] = health

    def get_pokemon_health(self, trainer, pokemon):
        return self.trainers_pokemon[trainer][self.active_pokemon[trainer]] 
    