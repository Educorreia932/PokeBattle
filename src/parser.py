from sly import Parser
from .lexer import PokeBattleLexer
from .commands.program import Program
from .commands.trainers import Trainers
from .commands.pokemon_list import PokemonList
from .commands.battle import Battle
from .commands.go_pokemon import GoPokemon
from .commands.turn import Turn
from .commands.nothing import Nothing
from .commands.damage import Damage
from .commands.effectiveness import Effectiveness
from .commands.math_damage import MathDamage
from .commands.heal import Heal
from .commands.leech import Leech
from .commands.sync import Sync
from .commands.switch import Switch
from .commands.status import Status
from .commands.output import Output
from .commands.input import Input

class PokeBattleParser(Parser):
    tokens = PokeBattleLexer.tokens

    @_('trainers battle')
    def program(self, p):
        return Program(p[0], p[1])

    @_('TRAINER_1 pokemon_list TRAINER_2 pokemon_list')
    def trainers(self, p):
        return Trainers(p[1], p[3])

    @_('IDENTIFIER IDENTIFIER IDENTIFIER IDENTIFIER IDENTIFIER IDENTIFIER IDENTIFIER')
    def pokemon_list(self, p):
        return PokemonList(p[0], p[1], p[2], p[3], p[4], p[5], p[6])

    @_('BATTLE_START TURN ZERO ":" go_pokemon go_pokemon turns BATTLE_END WINNER IDENTIFIER')
    def battle(self, p):
        return Battle(p[5])

    @_('IDENTIFIER ":" IDENTIFIER GO')
    def go_pokemon(self, p):
        return GoPokemon()

    @_('turns turn')
    def turns(self, p):
        p[0].append(p[1])

        return p[0]

    @_('turn')
    def turns(self, p):
        return [p[0]]

    @_('TURN INTEGER ":" command command')
    def turn(self, p):
        return Turn(p[1], p[3], p[4])

    @_('nothing', 'damage', 'math_damage', 'ohko', 'heal', 'leech', 'sync', 'switch', 'status', 'jump', 'output', 'input')
    def command(self, p):
        pass

    @_('IDENTIFIER RUN_AWAY',
       'IDENTIFIER FLINCHES',
       'IDENTIFIER USES SPLASH EXCLAMATION')
    def nothing(self, p):
        return Nothing()

    @_('damage_ effectiveness', 'damage_')
    def damage(self, p):
        pass

    @_('IDENTIFIER USES DAMAGE_MOVE EXCLAMATION')
    def damage_(self, p):
        return Damage(p[2])

    @_('NOT_VERY_EFFECTIVE', 'SUPER_EFFECTIVE')
    def effectiveness(self, p):
        return Effectiveness()

    @_('IDENTIFIER USES MATH_DAMAGE_MOVE EXCLAMATION')
    def math_damage(self, p):
        return MathDamage()

    @_('IDENTIFIER USES KO_MOVE EXCLAMATION')
    def ohko(self, p):
        return OHKO()

    @_('IDENTIFIER USES ITEM EXCLAMATION')
    def heal(self, p):
        return Heal()

    @_('IDENTIFIER USES LEECH_MOVE EXCLAMATION')
    def leech(self, p):
        return Leech()

    @_('IDENTIFIER USES SYNC_MOVE EXCLAMATION')
    def sync(self, p):
        return Sync()

    @_('IDENTIFIER ":" THATS_ENOUGH IDENTIFIER EXCLAMATION')
    def switch(self, p):
        return Switch(p[3])

    @_('IDENTIFIER USES STATUS_MOVE EXCLAMATION')
    def status(self, p):
        return Status()

    @_('IDENTIFIER THINKS_ABOUT_TURN INTEGER')
    def jump(self, p):
        return Jump(p[2])

    @_('IDENTIFIER USES OUTPUT_MOVE EXCLAMATION')
    def output(self, p):
        return Output(p[2])

    @_('IDENTIFIER USES INPUT_MOVE EXCLAMATION')
    def input(self, p):
        return Input(p[2])
