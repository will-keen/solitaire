import sys

from argparse import ArgumentParser, Namespace

from solitaire.players.random import RandomPlayer


def parse_args() -> Namespace:
    parser = ArgumentParser("Solitaire simulator")
    parser.add_argument(
        "--print-moves",
        action="store_true",
        help="Print all moves as the game progresses"
    )
    return parser.parse_args()


def main(args: Namespace):
    """
    Main runner for the program
    """
    random_player = RandomPlayer()
    random_player.play(args.print_moves)
    return 0

if __name__ == "__main__":
    sys.exit(main(parse_args()))
