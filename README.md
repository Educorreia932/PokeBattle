<p align="center">
    <img src="logo.png" />
</p>

**PokéBattle** is an esoteric language designed so that the program looks like the transcript of a *Pokémon* battle.

The original inspiration and specification was taken from [Esolangs wiki](https://esolangs.org/wiki/Pok%C3%A9Battle).

## EBNF Grammar

```py
Identifier = (["A"-"Z", "a"-"z"](["0"-"9", "A"-"Z", "a"-"z"])*);
Integer = ["0"-"9"]+;

Program = Trainers, Battle;

Trainers = "Trainer 1:", Identifier, PokemonList, "Trainer 2:", Identifier, PokemonList;

PokemonList = Identifier, Identifier, Identifier, Identifier, Identifier, Identifier;

Battle = "Battle Start!", 
         "Turn 0:", 
         Identifier, ":", Identifier, "Go!",
         Identifier, ":", Identifier, "Go!"
         { Turn }-, 
         "Battle End!", 
         "Winner:", Identifier;

Turn = "Turn", Integer, ":", Command, Command;

Command = Nothing | Damage | MathDamage | OHKO | Heal | Leech | Sync | Switch | Status | Jump | Output | Input;

Nothing = Identifier, "tried to run away! You can't run from a trainer battle!",
        | Identifier, "flinches!",
        | Identifier, "uses Splash!";

Damage = Identifier, "uses", ("Tackle" | "Ember" | "Vine Whip" | "Water Gun" | "Thunder Shock" | "Rock Throw" | "Confusion" | "Mach Punch" | "Wing Attack" | "Powder Snow" | "Body Slam" | "Flamethrower" | "Razor Leaf" | "Hydro Pump" | "Thunderbolt" | "Earthquake" | "Psychic" | "High Jump Kick" | "Fly" | "Ice Beam"), "!",
         ["It's super effective!" | "It's not very effective."];

MathDamage = Identifier, "uses", ("Hyper Beam" | "Dragon Rage"), "!";

OHKO = Identifier, "uses", ("Fissure" | "Guillotine" | "Sheer Cold"), "!";

Heal = Identifier, "uses", ("Potion" | "Super Potion" | "Hyper Potion" | "Max Potion");

Leech = Identifier, "uses", ("Absorb" | "Leech Life"), "!";

Sync = Identifier, "uses", ("Skill Swap" | "Heart Swap"), "!";

Switch = "That's enough!", "Go", Identifier, "!";

Status = Identifier, "uses", ("Blizzard" | "Thunder Wave" | "Sing"), "!";

Jump = Identifier, "thinks about turn", Integer;

Output = Identifier, "uses", ("Swords Dance" | "Barrier"), "!";

Input = Identifier, "uses", ("Growl" | "Lear"), "!";
```