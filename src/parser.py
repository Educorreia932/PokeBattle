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

    @_('BATTLE_START TURN "0" ":" IDENTIFIER GO IDENTIFIER ":" IDENTIFIER GO turns')
    def battle(self, p):
        pass

    @_('turn')
    def turns(self, p):
        t[0].append(t[1])

        return t[0]

    @_('TURN INTEGER ":" command command')
    def turn(self, p):
        pass

    @_('nothing', 'damage', 'math_damage', 'ohko', 'heal', 'leech', 'sync', 'switch', 'status', 'jump', 'output', 'input')
    def command(self, p):
        pass

    @_('IDENTIFIER RUN_AWAY',
       'IDENTIFIER FLINCHES',
       'IDENTIFIER SPLASH')
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

    @_('THATS_ENOUGH GO_ IDENTIFIER EXCLAMATION')
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
