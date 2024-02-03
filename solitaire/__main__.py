import sys

from argparse import ArgumentParser, Namespace
from time import time

from solitaire.players.random import RandomPlayer


def parse_args() -> Namespace:
    parser = ArgumentParser("Solitaire simulator")
    parser.add_argument(
        "--print-moves",
        action="store_true",
        help="Print all moves as the game progresses."
    )
    parser.add_argument(
        "--no-print",
        action="store_true",
        help="Specify if you don't want any printing. Useful for large simulations."
    )
    parser.add_argument(
        "--num-games",
        type=int,
        default=1,
        help="How many times to run the simulation."
    )
    parser.add_argument(
        "--stop-on-win",
        action="store_true",
        help="Stop simulating if a win occurs."
    )
    args = parser.parse_args()
    if args.no_print and args.print_moves:
        raise ValueError("Can't use --no-print and --print-moves")
    return args


def main(args: Namespace):
    """
    Main runner for the program
    """
    start = time()
    for x in range(1, args.num_games+1):
        random_player = RandomPlayer(name=f"RandomPlayer game {x}")
        win = random_player.play(args.print_moves)
        if not args.no_print:
            print(str(random_player))
        if win:
            print(f"{random_player.name} was a winner!")
            if args.stop_on_win:
                break
    end = time()
    total_time = end - start
    avg = total_time / x
    print(f"Ran {x} simulations in {total_time:.3f}s, that's {avg:.3f}s per sim.")
    return 0

if __name__ == "__main__":
    sys.exit(main(parse_args()))
