import sys

from argparse import ArgumentParser, Namespace
from time import time

from solitaire.players.edges import EdgePlayer
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


def run_player(player: type, args: Namespace):
    start = time()
    total_score = 0
    player_name = player.__name__
    for x in range(1, args.num_games+1):
        random_player = player(name=f"{player_name} game {x}")
        score = random_player.play(args.print_moves)
        total_score += score
        if not args.no_print:
            print(str(random_player))
        if score == 1:
            print(f"{random_player.name} was a winner!")
            if args.stop_on_win:
                break
    end = time()
    total_time = end - start
    avg_time = total_time / x
    avg_score = total_score / x
    print(f"{player_name}: Average score was {avg_score}, or {total_score}/{x}")
    print(f"{player_name}: Ran {x} simulations in {total_time:.3f}s, that's {avg_time:.3f}s per sim.\n")


def main(args: Namespace):
    """
    Main runner for the program.
    """
    for player in [RandomPlayer, EdgePlayer]:
        run_player(player, args)
    return 0

if __name__ == "__main__":
    sys.exit(main(parse_args()))
