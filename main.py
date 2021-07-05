from src.lexer import PokeBattleLexer
from src.parser import PokeBattleParser
from src.interpreter import PokeBattleInterpreter


def main():
    lexer = PokeBattleLexer()
    parser = PokeBattleParser()
    interpreter = PokeBattleInterpreter()

    with open("programs", "r") as f:
        source = f.read()

    tokens = lexer.tokenize(source)
    program = parser.parse(tokens)
    interpreter.interpret(program)


if __name__ == "__main__":
    main()
