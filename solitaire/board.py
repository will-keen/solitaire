""" Classes to represent the solitaire game board. """

from dataclasses import dataclass
from enum import auto, Enum


BOARD_WIDTH = 7
MIN_VAL = 2
MAX_VAL = BOARD_WIDTH - 2


class Direction(Enum):
    LEFT = 0
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


@dataclass
class Move:
    x : int
    y : int
    jump_dir : Direction


def index_is_legal(x, y):
    return (((x >= MIN_VAL and x < MAX_VAL) and ((y >= MIN_VAL) or (y < MAX_VAL))) or
            ((y >= MIN_VAL and y < MAX_VAL) and ((x >= MIN_VAL) or (x < MAX_VAL))))


class Space:
    """ Represents one space on the game board. """

    def __init__(self, legal, occupied):
        """ Create a space - either it can
            accept a piece or not."""
        self.legal = legal
        self.occupied = occupied

    def as_string(self):
        """ Returns string representation of space. """
        space_str = " " if not self.legal else "o" if self.occupied else "."
        return space_str


class Board:
    """ Represents the game board, containing the spaces. """

    def __init__(self):
        """ Create the basic game board. """
        # Create a square of pieces for easy indexing.
        # Not all spaces are legal.
        self.spaces = [[None for x in range(BOARD_WIDTH)] for y in range(BOARD_WIDTH)]
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_WIDTH):
                is_legal = index_is_legal(x,y)
                self.spaces[x][y] = Space(is_legal, True)
        # Remove central piece.
        self.spaces[3][3].occupied = False

    def move_legal(self, move):
        """ For a given space, returns true if there is a
            legal move in that direction. """
        # No legal move if there's no piece in the space.
        x = move.x
        y = move.y
        jump_dir = move.jump_dir
        if not (self.spaces[x][y].legal and self.spaces[x][y].occupied):
            return False
        # Check each direction.
        if jump_dir == Direction.RIGHT:
            # Must be a piece in the space to the right.
            # Must be an unoccupied space to the right of that.
            return (
                index_is_legal(x+1, y) and
                self.spaces[x+1][y].occupied and
                index_is_legal(x+2, y) and
                not self.space[x+2][y].occupied
            )
        elif jump_dir == Direction.LEFT:
            # Must be a piece in the space to the left.
            # Must be an unoccupied space to the left of that.
            return (
                index_is_legal(x-1, y) and
                self.spaces[x-1][y].occupied and
                index_is_legal(x-2, y) and
                not self.space[x-2][y].occupied
            )
        elif jump_dir == Direction.UP:
            # Must be a piece in the space above.
            # Must be an unoccupied space above of that.
            return (
                index_is_legal(x, y+1) and
                self.spaces[x][y+1].occupied and
                index_is_legal(x, y+2) and
                not self.space[x][y+2].occupied
            )
        elif jump_dir == Direction.DOWN:
            # Must be a piece in the space above.
            # Must be an unoccupied space above of that.
            return (
                index_is_legal(x, y-1) and
                self.spaces[x][y-1].occupied and
                index_is_legal(x, y-2) and
                not self.space[x][y-2].occupied
            )

    def get_moves(self):
        """ Returns all currently legal moves, as a list of
            boards that represent legal next states. """
        legal_moves = []
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_WIDTH):
                for jump_dir in Direction:
                    move = Move(x, y, jump_dir)
                    if self.move_legal(move):
                        legal_moves.append(move)


    def as_string(self):
        """ Returns a string denoting the game board. """
        board_str = ""
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_WIDTH):
                board_str += self.spaces[x][y].as_string()
            board_str += "\n"
        return board_str[:-1]
