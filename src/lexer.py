from sly import Lexer

class PokeBattleLexer(Lexer):
    tokens = {IDENTIFIER, INTEGER, DAMAGE_MOVE, MATH_DAMAGE_MOVE, KO_MOVE,
              ITEM, LEECH_MOVE, SYNC_MOVE, STATUS_MOVE, OUTPUT_MOVE, INPUT_MOVE}

    IDENTIFIER = r"[a-zA-Z][a-zA-Z0-9]*"
    INTEGER = r"\d+"
    DAMAGE_MOVE = r"Tackle | Ember | Vine Whip | Water Gun | Thunder Shock | Rock Throw | Confusion | Mach Punch | Wing Attack | Powder Snow | Body Slam | Flamethrower | Razor Leaf | Hydro Pump | Thunderbolt | Earthquake | Psychic | High Jump Kick | Fly | Ice Beam"
    MATH_DAMAGE_MOVE = r"Hyper Beam | Dragon Rage"
    KO_MOVE = r"Fissure | Guillotine | Sheer Cold"
    ITEM = r"Potion | Super Potion | Hyper Potion | Max Potion"
    LEECH_MOVE = r"Absorb | Leech Life"
    SYNC_MOVE = r"Skill Swap | Heart Swap"
    STATUS_MOVE = r"Blizzard | Thunder Wave | Sing"
    OUTPUT_MOVE = r"Swords Dance | Barrier"
    INPUT_MOVE = r"Growl | Lear"
