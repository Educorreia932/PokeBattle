from src.lexer import PokeBattleLexer
from src.parser import PokeBattleParser


def main():
    lexer = PokeBattleLexer()
    parser = PokeBattleParser()

    with open("programs/HelloWorld.poke", "r") as f:
        source = f.read()

    tokens = lexer.tokenize(source)
    program = parser.parse(tokens)


if __name__ == "__main__":
    main()
