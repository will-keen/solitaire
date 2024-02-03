"""
Base class for solitaire players.
"""
from solitaire.board import Board


class BasePlayer:

    def __init__(self, start_state=None, name=None) -> None:
        if name is None:
            self.name = self.__class__.__name__
        else:
            self.name = name
        if start_state is None:
            self.board = Board()
        else:
            self.board = start_state
        self.turns = 0

    def play(self, print_moves: bool=False) -> bool:
        """
        Play the game to the end. Returns true if it's a win.
        """
        while len(self.board.get_moves()) > 0:
            if print_moves:
                print(str(self))
            self.make_move(print_move=print_moves)
            self.turns += 1
        if self.board.num_pieces == 1:
            return True
        return False

    def make_move(self, print_move: bool) -> None:
        raise NotImplementedError("If inheriting from BasePlayer, must implement make_move")

    def __str__(self) -> str:
        as_str = f"{self.name} turn {self.turns}:\n\n"
        as_str += f"Board:\n{str(self.board)}\n\n"
        as_str += f"Pieces remaining: {self.board.num_pieces()}\n\n"
        possible_moves = self.board.get_moves()
        as_str += f"Possible moves ({len(possible_moves)}):\n"
        as_str += "\n".join([str(x) for x in possible_moves])
        return as_str + "\n"
