from src.lexer import PokeBattleLexer
from src.parser import PokeBattleParser


def main():
    lexer = PokeBattleLexer()
    parser = PokeBattleParser()

    with open("programs/Test.poke", "r") as f:
        source = f.read()

    tokens = lexer.tokenize(source)

    for token in tokens:
        print(token)

    program = parser.parse(lexer.tokenize(source))

if __name__ == "__main__":
    main()
