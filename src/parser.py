from .lexer import PokeBattleLexer
from sly import Parser


class PokeBattleParser(Parser):
    tokens = PokeBattleLexer.tokens

    @_('trainers battle')
    def program(self, p):
        pass

    @_('TRAINER_1 IDENTIFIER pokemon_list TRAINER_2 IDENTIFIER pokemon_list')
    def trainers(self, p):
        pass

    # TODO: Perhaps use regex, or string multiplication
    @_('IDENTIFIER IDENTIFIER IDENTIFIER IDENTIFIER IDENTIFIER IDENTIFIER')
    def pokemon_list(self, p):
        pass

    @_('BATTLE_START TURN ZERO ":" go_pokemon go_pokemon turns BATTLE_END WINNER IDENTIFIER')
    def battle(self, p):
        pass

    @_('IDENTIFIER ":" IDENTIFIER GO')
    def go_pokemon(self, p):
        pass

    @_('turns turn', '')
    def turns(self, p):
        pass

    @_('TURN INTEGER ":" command command')
    def turn(self, p):
        pass

    @_('nothing', 'damage', 'math_damage', 'ohko', 'heal', 'leech', 'sync', 'switch', 'status', 'jump', 'output', 'input')
    def command(self, p):
        pass

    @_('command effectiveness') # TODO: Only allow moves to have effectiveness
    def command(self, p):
        pass

    @_('NOT_VERY_EFFECTIVE', 'SUPER_EFFECTIVE', '')
    def effectiveness(self, p):
        pass

    @_('IDENTIFIER RUN_AWAY',
       'IDENTIFIER FLINCHES',
       'IDENTIFIER USES SPLASH EXCLAMATION')
    def nothing(self, p):
        pass

    @_('IDENTIFIER USES DAMAGE_MOVE EXCLAMATION')
    def damage(self, p):
        pass

    @_('IDENTIFIER USES MATH_DAMAGE_MOVE EXCLAMATION')
    def math_damage(self, p):
        pass

    @_('IDENTIFIER USES KO_MOVE EXCLAMATION')
    def ohko(self, p):
        pass

    @_('IDENTIFIER USES ITEM EXCLAMATION')
    def heal(self, p):
        pass

    @_('IDENTIFIER USES LEECH_MOVE EXCLAMATION')
    def leech(self, p):
        pass

    @_('IDENTIFIER USES SYNC_MOVE EXCLAMATION')
    def sync(self, p):
        pass

    @_('IDENTIFIER ":" THATS_ENOUGH IDENTIFIER EXCLAMATION')
    def switch(self, p):
        pass

    @_('IDENTIFIER USES STATUS_MOVE EXCLAMATION')
    def status(self, p):
        pass

    @_('IDENTIFIER THINKS_ABOUT_TURN INTEGER')
    def jump(self, p):
        pass

    @_('IDENTIFIER USES OUTPUT_MOVE EXCLAMATION')
    def output(self, p):
        pass

    @_('IDENTIFIER USES INPUT_MOVE EXCLAMATION')
    def input(self, p):
        pass
