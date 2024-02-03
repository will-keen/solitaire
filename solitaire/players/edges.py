import random

from solitaire.board import BOARD_WIDTH
from solitaire.players.base import BasePlayer


class EdgePlayer(BasePlayer):
    """
    Edge player. Aims to always move most extreme pieces.
    """

    def make_move(self, print_move: bool) -> None:
        all_moves = self.board.get_moves()
        random.shuffle(all_moves)
        best_move = None
        best_distance = None
        for move in all_moves:
            left_edge_distance = move.x
            right_edge_distance = (BOARD_WIDTH - 1) - move.x
            top_edge_distance = move.y
            bottom_edge_distance = (BOARD_WIDTH - 1) - move.y
            closest_distance = min((
                left_edge_distance,
                right_edge_distance,
                top_edge_distance,
                bottom_edge_distance
            ))
            if best_move is None:
                best_move = move
                best_distance = closest_distance
                continue
            elif closest_distance < best_distance:
                best_move = move
                best_distance = closest_distance
        if print_move:
            print(f"Next move: {best_move}\n")
        self.board.apply_move(best_move)
