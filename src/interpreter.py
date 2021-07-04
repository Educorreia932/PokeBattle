from typing import Dict

from plum import dispatch

from .models.pokemon import Pokemon
from .models.trainer import Trainer
from .statements.damage import Damage
from .statements.go_pokemon import GoPokemon
from .statements.heal import Heal
from .statements.input import Input
from .statements.leech import Leech
from .statements.math_damage import MathDamage
from .statements.ohko import OHKO
from .statements.output import Output
from .statements.program import Program
from .statements.status import Status
from .statements.switch import Switch
from .statements.sync import Sync
from .statements.turn import Turn


class PokeBattleInterpreter:
    pokemon: Dict[str, Pokemon]
    trainers: Dict[str, Trainer]

    @dispatch
    def interpret(self, program: Program):
        pokemon_lists = program.trainers.pokemon_lists

        player = Trainer(pokemon_lists[0].trainer, pokemon_lists[0].pokemon)
        adversary = Trainer(pokemon_lists[1].trainer, pokemon_lists[1].pokemon)

        player.opponent = adversary
        adversary.opponent = player

        self.trainers = {
            player.name: player,
            adversary.name: adversary
        }

        self.pokemon = {p.name: p for p in player.pokemon.values()}
        self.pokemon.update({p.name: p for p in adversary.pokemon.values()})

        for go_pokemon in program.battle.starter_pokemon:
            self.interpret(go_pokemon)

        for turn in program.battle.turns:
            self.interpret(turn)

    @dispatch
    def interpret(self, go_pokemon: GoPokemon):
        self.trainers[go_pokemon.trainer].active_pokemon = go_pokemon.pokemon

    @dispatch
    def interpret(self, turn: Turn):
        for command in turn.commands:
            self.interpret(command[1])

    @dispatch
    def interpret(self, damage: Damage):
        self.pokemon[damage.pokemon].deal_damage(damage.level)

    @dispatch
    def interpret(self, math_damage: MathDamage):
        self.pokemon[math_damage.pokemon].deal_math_damage()

    @dispatch
    def interpret(self, ohko: OHKO):
        self.pokemon[ohko.pokemon].knockout()

    @dispatch
    def interpret(self, heal: Heal):
        self.trainers[heal.trainer].active_pokemon.heal(heal.level)

    @dispatch
    def interpret(self, leech: Leech):
        self.pokemon[leech.pokemon].leech()

    @dispatch
    def interpret(self, sync: Sync):
        self.pokemon[sync.pokemon].sync()

    @dispatch
    def interpret(self, switch: Switch):
        self.trainers[switch.trainer].active_pokemon = switch.new_pokemon

    @dispatch
    def interpret(self, status: Status):
        pass

    @dispatch
    def interpret(self, output: Output):
        self.pokemon[output.pokemon].print(output.mode)

    @dispatch
    def interpret(self, input: Input):
        self.pokemon[input.pokemon].input(input.mode)
