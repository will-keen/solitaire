""" Classes to represent the solitaire game board. """

from dataclasses import dataclass
from enum import auto, Enum
from typing import List


BOARD_WIDTH = 7
MIN_VAL = 2
MAX_VAL = BOARD_WIDTH - 2


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


@dataclass
class Move:
    x : int
    y : int
    jump_dir : Direction


def space_exists(x: int, y: int) -> bool:
    '''
    Returns true if a space exists on the board, false otherwise.
    '''
    if x < 0 or y < 0 or x >= BOARD_WIDTH or y >= BOARD_WIDTH:
        return False
    return (((x >= MIN_VAL and x < MAX_VAL) and ((y >= MIN_VAL) or (y < MAX_VAL))) or
            ((y >= MIN_VAL and y < MAX_VAL) and ((x >= MIN_VAL) or (x < MAX_VAL))))

@dataclass
class Space:
    """
    Represents one space on the game board.

    A space either exists or doesn't (i.e. it's a real slot on
    the game board at this coordinate), and is either occupied
    or isn't.
    """
    exists: bool
    occupied: bool

    def __str__(self) -> str:
        """
        Returns string representation of space on the board.
        """
        space_str = " " if not self.exists else "o" if self.occupied else "."
        return space_str


class Board:
    """
    Represents the game board, containing the spaces.
    """

    def __init__(self):
        """
        Create the basic game board.
        """
        # Create a square of pieces for easy indexing.
        # Not all spaces on the grid exist on the board.
        # Top left is 0,0.
        self.spaces = [[None for x in range(BOARD_WIDTH)] for y in range(BOARD_WIDTH)]
        for y in range(BOARD_WIDTH):
            for x in range(BOARD_WIDTH):
                self.spaces[y][x] = Space(space_exists(x,y), True)
        # Remove central piece.
        self.spaces[3][3].occupied = False
        # For caching possible moves.
        self.changed = False
        self.cached_moves = None

    def move_legal(self, move: Move) -> bool:
        """
        For a given space, returns true if there is a
        legal move in that direction.
        """
        # No legal move if there's no piece in the space.
        x = move.x
        y = move.y
        jump_dir = move.jump_dir
        if not (self.spaces[y][x].exists and self.spaces[y][x].occupied):
            return False
        # Check each direction.
        if jump_dir == Direction.RIGHT:
            # Must be a piece in the space to the right.
            # Must be an unoccupied space to the right of that.
            return (
                space_exists(x+1, y) and
                self.spaces[y][x+1].occupied and
                space_exists(x+2, y) and
                not self.spaces[y][x+2].occupied
            )
        elif jump_dir == Direction.LEFT:
            # Must be a piece in the space to the left.
            # Must be an unoccupied space to the left of that.
            return (
                space_exists(x-1, y) and
                self.spaces[y][x-1].occupied and
                space_exists(x-2, y) and
                not self.spaces[y][x-2].occupied
            )
        elif jump_dir == Direction.UP:
            # Must be a piece in the space above.
            # Must be an unoccupied space above of that.
            return (
                space_exists(x, y-1) and
                self.spaces[y-1][x].occupied and
                space_exists(x, y-2) and
                not self.spaces[y-2][x].occupied
            )
        elif jump_dir == Direction.DOWN:
            # Must be a piece in the space above.
            # Must be an unoccupied space above of that.
            return (
                space_exists(x, y+1) and
                self.spaces[y+1][x].occupied and
                space_exists(x, y+2) and
                not self.spaces[y+2][x].occupied
            )

    def get_moves(self) -> List[Move]:
        """
        Returns all currently legal moves, as a list of
        moves that give legal next states.
        """
        legal_moves = []
        for y in range(BOARD_WIDTH):
            for x in range(BOARD_WIDTH):
                for jump_dir in Direction:
                    move = Move(x, y, jump_dir)
                    if self.move_legal(move):
                        legal_moves.append(move)
        return legal_moves

    def apply_move(self, move: Move) -> None:
        """
        Applies a move to the game board.
        """
        if not self.move_legal(move):
            raise RuntimeError(f"illegal move: {move} for board:\n{str(self)}")
        self.spaces[move.y][move.x].occupied = False
        if move.jump_dir == Direction.LEFT:
            self.spaces[move.y][move.x - 1].occupied = False
            self.spaces[move.y][move.x - 2].occupied = True
        elif move.jump_dir == Direction.RIGHT:
            self.spaces[move.y][move.x + 1].occupied = False
            self.spaces[move.y][move.x + 2].occupied = True
        elif move.jump_dir == Direction.UP:
            self.spaces[move.y - 1][move.x].occupied = False
            self.spaces[move.y - 2][move.x].occupied = True
        elif move.jump_dir == Direction.DOWN:
            self.spaces[move.y + 1][move.x].occupied = False
            self.spaces[move.y + 2][move.x].occupied = True

    def num_pieces(self) -> int:
        """
        Returns the number of pieces remaining on the board.
        """
        count = 0
        for y in range(BOARD_WIDTH):
            for x in range(BOARD_WIDTH):
                if self.spaces[y][x].exists and self.spaces[y][x].occupied:
                    count += 1
        return count

    def __str__(self) -> str:
        """
        Returns a string denoting the game board.
        """
        board_str = ""
        board_str += "  " + " ".join(str(x) for x in range(BOARD_WIDTH)) + "\n"
        for y in range(BOARD_WIDTH):
            board_str += f"{y} "
            for x in range(BOARD_WIDTH):
                board_str += str(self.spaces[y][x]) + " "
            board_str += "\n"
        return board_str[:-1]
