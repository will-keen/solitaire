"""
Base class for solitaire players.
"""
from solitaire.board import Board, Move


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

    def play(self, print_moves: bool=False) -> int:
        """
        Play the game to the end. Returns score (number of pieces left).
        A lower score is better, 1 being the best.

        args:
            print_moves:
                If True, print each move and its result as the game is played.
            strict:
                If True, check that result of `get_next_move` is valid.
                Slows down performance.
        return:
            The number of pieces remaining when there are no possible
            moves remaining.
        """
        while len(self.board.get_moves()) > 0:
            if print_moves:
                print(str(self))
            next_move = self.get_next_move()
            if print_moves:
                print(f"Next move: {next_move}\n")
            self.board.apply_move(next_move)
            self.turns += 1
        return self.board.num_pieces()

    def get_next_move(self) -> Move:
        """
        Method to override when creating players. Should return
        the next move according to the player's algorithm,
        based on the current board state (`self.board`).

        return:
            The next move to be made.
        """
        raise NotImplementedError("If inheriting from BasePlayer, must implement get_next_move")

    def __str__(self) -> str:
        """
        Return string representation.
        """
        as_str = f"{self.name} turn {self.turns}:\n\n"
        as_str += f"Board:\n{str(self.board)}\n\n"
        as_str += f"Pieces remaining: {self.board.num_pieces()}\n\n"
        possible_moves = self.board.get_moves()
        as_str += f"Possible moves ({len(possible_moves)}):\n"
        as_str += "\n".join([str(x) for x in possible_moves])
        return as_str + "\n"
