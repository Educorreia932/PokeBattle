from .lexer import PokeBattleLexer
from sly import Parser

class PokeBattleParser(Parser):
    tokens = PokeBattleLexer.tokens

    @_('trainers battle')
    def program(self, p):
        pass

    @_('"Trainer 1:" IDENTIFIER pokemon_list "Trainer 2:" IDENTIFIER pokemon_list')
    def trainers(self, p):
        pass

    @_('IDENTIFIER IDENTIFIER IDENTIFIER IDENTIFIER IDENTIFIER IDENTIFIER')
    def pokemon_list(self, p):
        pass

    @_('"Battle Start!" "Turn 0:" IDENTIFIER ":" IDENTIFIER "Go!" IDENTIFIER ":" IDENTIFIER "Go!" ')
    def battle(self, p):
        pass

    @_('"Turn" INTEGER ":" command command')
    def turn(self, p):
        pass

    @_('nothing', 'damage', 'math_damage', 'ohko', 'heal', 'leech', 'sync', 'switch', 'status', 'jump', 'output', 'input')
    def command(self, p):
        pass

    @_('IDENTIFIER "tried to run away! You can\'t run from a trainer battle!"',
       'IDENTIFIER "flinches!"',
       'IDENTIFIER "uses Splash!"')
    def nothing(self, p):
        pass

    @_('IDENTIFIER "uses" DAMAGE_MOVE "!"')
    def damage(self, p):
        pass

    @_('IDENTIFIER "uses" MATH_ DAMAGE_MOVE "!"')
    def math_damage(self, p):
        pass

    @_('IDENTIFIER "uses" KO_MOVE "!"')
    def ohko(self, p):
        pass

    @_('IDENTIFIER "uses" ITEM "!"')
    def heal(self, p):
        pass

    @_('IDENTIFIER "uses" LEECH_MOVE "!"')
    def leech(self, p):
        pass

    @_('IDENTIFIER "uses" SYNC_MOVE "!"')
    def sync(self, p):
        pass

    @_('"That\'s enough!" "Go" IDENTIFIER "!"')
    def switch(self, p):
        pass

    @_('IDENTIFIER "uses" SYNC_MOVE "!"')
    def status(self, p):
        pass

    @_('IDENTIFIER "thinks about turn" INTEGER')
    def jump(self, p):
        pass

    @_('IDENTIFIER "thinks about turn" INTEGER')
    def output(self, p):
        pass

    @_('IDENTIFIER "thinks about turn" INTEGER')
    def input(self, p):
        pass