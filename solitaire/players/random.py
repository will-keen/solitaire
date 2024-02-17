import random

from solitaire.board import Move
from solitaire.players.base import BasePlayer


class RandomPlayer(BasePlayer):
    """
    Random solitaire player.

    Randomly traverses the state space.
    """

    def get_next_move(self) -> Move:
        return random.choice(self.board.get_moves())
