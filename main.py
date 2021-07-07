import sys

from src.interpreter import PokeBattleInterpreter
from src.lexer import PokeBattleLexer
from src.parser import PokeBattleParser


def main():
    lexer = PokeBattleLexer()
    parser = PokeBattleParser()
    interpreter = PokeBattleInterpreter()

    with open(sys.argv[1], "r") as f:
        source = f.read()

    tokens = lexer.tokenize(source)
    program = parser.parse(tokens)
    interpreter.interpret(program)


if __name__ == "__main__":
    main()
