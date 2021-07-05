from sly import Lexer


class PokeBattleLexer(Lexer):
    tokens = {IDENTIFIER, INTEGER, DAMAGE_MOVE, MATH_DAMAGE_MOVE, KO_MOVE, ITEM, LEECH_MOVE, SYNC_MOVE, STATUS_MOVE,
              OUTPUT_MOVE,
              INPUT_MOVE, TRAINER_1, TRAINER_2, BATTLE_START, TURN, ZERO, GO, USES, EXCLAMATION, THINKS_ABOUT_TURN,
              THATS_ENOUGH,
              RUN_AWAY, FLINCHES, SPLASH, BATTLE_END, WINNER, NOT_VERY_EFFECTIVE, SUPER_EFFECTIVE}

    literals = {":", "!", "'", "."}

    ignore = " \t"

    TRAINER_1 = "Trainer 1:"
    TRAINER_2 = "Trainer 2:"
    BATTLE_START = "Battle Start!"
    TURN = "Turn"
    ZERO = "0"
    GO = "Go!"
    USES = "uses"
    EXCLAMATION = "!"
    THINKS_ABOUT_TURN = "thinks about turn"
    THATS_ENOUGH = "That\'s enough! Go"
    RUN_AWAY = "tried to run away! You can\'t run from a trainer battle!"
    FLINCHES = "flinches!"
    SPLASH = "Splash"
    BATTLE_END = "Battle End!"
    WINNER = "Winner:"
    NOT_VERY_EFFECTIVE = "It's not very effective."
    SUPER_EFFECTIVE = "It's super effective!"

    DAMAGE_MOVE = r"Tackle|Ember|Vine Whip|Water Gun|Thunder Shock|Rock Throw|Confusion|Mach Punch|Wing Attack|Powder " \
                  r"Snow|Body Slam|Flamethrower|Razor Leaf|Hydro Pump|Thunderbolt|Earthquake|Psychic|High Jump " \
                  r"Kick|Fly|Ice Beam "
    MATH_DAMAGE_MOVE = r"Hyper Beam|Dragon Rage"
    KO_MOVE = r"Fissure|Guillotine|Sheer Cold"
    ITEM = r"Potion|Super Potion|Hyper Potion|Max Potion"
    LEECH_MOVE = r"Absorb|Leech Life"
    SYNC_MOVE = r"Skill Swap|Heart Swap"
    STATUS_MOVE = r"Blizzard|Thunder Wave|Sing"
    OUTPUT_MOVE = r"Swords Dance|Barrier"
    INPUT_MOVE = r"Growl|Lear"

    IDENTIFIER = r"[a-zA-Z][a-zA-Z0-9]*"
    INTEGER = r"\d+"

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
