import random

from solitaire.players.base import BasePlayer


class RandomPlayer(BasePlayer):
    """
    Random solitaire player.

    Randomly traverses the state space.
    """

    def make_move(self, print_move: bool) -> None:
        next_move = random.choice(self.board.get_moves())
        if print_move:
            print(f"Next move: {next_move}\n")
        self.board.apply_move(next_move)
